package crawler

import (
	"context"
	"errors"
	"fmt"
	"path/filepath"
	"sort"
	"strings"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
	"github.com/vietvudanh/vietlott-data/crawler/internal/storage"
)

// ProductAdapter retrieves the latest draw number and newest-first result
// pages. Pages start at 0; each page lists draws in no guaranteed order.
type ProductAdapter interface {
	Latest(context.Context) (int, error)
	FetchPage(context.Context, int) ([]model.Draw, error)
}

// SyncReport describes the result of synchronizing one product.
type SyncReport struct {
	Product   model.ProductName
	Existing  int
	Latest    int
	Missing   int
	Written   int
	FailedIDs []int
}

// MissingIDs returns missing draw IDs in ascending order, optionally limited
// to the first maxDraws IDs.
func MissingIDs(existing map[int]struct{}, minID, latestID, maxDraws int) []int {
	if latestID < minID {
		return nil
	}
	missing := make([]int, 0, latestID-minID+1)
	for id := minID; id <= latestID; id++ {
		if _, ok := existing[id]; !ok {
			missing = append(missing, id)
			if maxDraws > 0 && len(missing) == maxDraws {
				break
			}
		}
	}
	return missing
}

// TargetPages calculates the exact newest-first page numbers (0-indexed)
// needed to fetch the given missing draw IDs, based on latest draw ID and pageSize.
// If pageSize <= 0, sequential scanning is assumed.
func TargetPages(missingIDs []int, latestID, pageSize, maxPages int) []int {
	if len(missingIDs) == 0 {
		return nil
	}
	if pageSize <= 0 {
		pages := maxPages
		if pages < 1 {
			pages = 1
		}
		res := make([]int, pages)
		for i := 0; i < pages; i++ {
			res[i] = i
		}
		return res
	}

	pageSet := make(map[int]struct{})
	for _, id := range missingIDs {
		if id > latestID {
			continue
		}
		// Exact 0-indexed page where id is expected to be
		p := (latestID - id) / pageSize
		if p >= 0 && (maxPages <= 0 || p < maxPages) {
			pageSet[p] = struct{}{}
			// Also include adjacent page p+1 in case upstream skipped any draw numbers
			if maxPages <= 0 || p+1 < maxPages {
				pageSet[p+1] = struct{}{}
			}
		}
	}
	sorted := make([]int, 0, len(pageSet))
	for p := range pageSet {
		sorted = append(sorted, p)
	}
	sort.Ints(sorted)
	return sorted
}

// Progress reports crawling progress for long-running synchronization.
type Progress struct {
	Product   model.ProductName
	Page      int
	MaxPages  int
	Found     int
	Total     int
	BatchSize int // newly found draws in this page/batch
}

// ProgressFunc receives progress updates during synchronization.
type ProgressFunc func(Progress)

// SyncOptions configures synchronization behavior.
type SyncOptions struct {
	MaxDraws   int
	BatchSize  int // when > 0, flush discovered draws to disk in batches
	OnProgress ProgressFunc
}

// Sync downloads missing draws by scanning newest-first result pages and
// atomically appends successful results.
func Sync(ctx context.Context, repoRoot string, product model.Product, adapter ProductAdapter, maxDraws int) (SyncReport, error) {
	return SyncWithOptions(ctx, repoRoot, product, adapter, SyncOptions{MaxDraws: maxDraws})
}

// SyncWithOptions downloads missing draws with progress reporting and optional batching.
func SyncWithOptions(ctx context.Context, repoRoot string, product model.Product, adapter ProductAdapter, opts SyncOptions) (SyncReport, error) {
	report := SyncReport{Product: product.Name}
	if adapter == nil {
		return report, errors.New("product adapter is nil")
	}
	if err := ctx.Err(); err != nil {
		return report, err
	}

	path, err := productDataPath(repoRoot, product.FileName)
	if err != nil {
		return report, err
	}
	existing, _, _, err := storage.LoadExistingDrawIDs(path)
	if err != nil {
		return report, fmt.Errorf("load %s: %w", product.Name, err)
	}
	report.Existing = len(existing)

	latest, err := adapter.Latest(ctx)
	if err != nil {
		return report, fmt.Errorf("latest %s: %w", product.Name, err)
	}
	report.Latest = latest
	if latest < product.MinID {
		return report, fmt.Errorf("latest draw %d is before minimum ID %d", latest, product.MinID)
	}

	pages := product.MaxPages
	if pages < 1 {
		pages = 1
	}

	pageSize := product.PageSize
	if pageSize <= 0 {
		pageSize = 20
	}

	minID := product.MinID
	if reachable := latest - pages*pageSize; reachable > minID {
		minID = reachable
	}

	allMissing := MissingIDs(existing, minID, latest, 0)
	if opts.MaxDraws > 0 && len(allMissing) > opts.MaxDraws {
		allMissing = allMissing[len(allMissing)-opts.MaxDraws:]
	}
	ids := allMissing
	report.Missing = len(ids)
	if len(ids) == 0 {
		return report, nil
	}
	wanted := make(map[int]struct{}, len(ids))
	for _, id := range ids {
		wanted[id] = struct{}{}
	}
	oldestWanted := ids[0]
	// Calculate the exact target pages to fetch
	targetPages := TargetPages(ids, latest, product.PageSize, pages)
	found := make(map[int]model.Draw, len(ids))
	unflushed := make([]model.Draw, 0)
	var pageErr error
	var failedPage int
	canceled := false

	flushBatch := func() error {
		if len(unflushed) == 0 {
			return nil
		}
		if err := storage.AppendDrawsAtomic(path, unflushed); err != nil {
			return fmt.Errorf("write %s batch: %w", product.Name, err)
		}
		report.Written += len(unflushed)
		unflushed = unflushed[:0]
		return nil
	}

pages:
	for pageIdx, page := range targetPages {
		if len(found) >= len(wanted) {
			break pages
		}
		if ctx.Err() != nil {
			canceled = true
			break pages
		}
		draws, err := adapter.FetchPage(ctx, page)
		if err != nil {
			if ctx.Err() != nil {
				canceled = true
				break pages
			}
			pageErr = err
			failedPage = page
			break pages
		}
		if len(draws) == 0 {
			continue
		}
		pageMax := -1
		pageNewFound := 0
		for _, draw := range draws {
			if draw == nil {
				continue
			}
			id, err := model.NormalizeID(draw.GetID())
			if err != nil {
				pageErr = fmt.Errorf("page %d %s: %w", page, product.Name, err)
				failedPage = page
				break pages
			}
			if id.Number > pageMax {
				pageMax = id.Number
			}
			if _, ok := wanted[id.Number]; ok {
				if _, dup := found[id.Number]; !dup {
					found[id.Number] = draw
					unflushed = append(unflushed, draw)
					pageNewFound++
				}
			}
		}

		if opts.OnProgress != nil {
			opts.OnProgress(Progress{
				Product:   product.Name,
				Page:      pageIdx + 1,
				MaxPages:  len(targetPages),
				Found:     len(found),
				Total:     len(wanted),
				BatchSize: pageNewFound,
			})
		}

		if opts.BatchSize > 0 && len(unflushed) >= opts.BatchSize {
			if err := flushBatch(); err != nil {
				return report, err
			}
		}

		if product.PageSize <= 0 && pageMax >= 0 && pageMax < oldestWanted {
			break pages
		}
	}

	for _, id := range ids {
		if _, ok := found[id]; !ok {
			report.FailedIDs = append(report.FailedIDs, id)
		}
	}
	sort.Ints(report.FailedIDs)

	if len(unflushed) > 0 {
		if err := flushBatch(); err != nil {
			return report, err
		}
	}

	if canceled {
		return report, ctx.Err()
	}
	if pageErr != nil {
		return report, fmt.Errorf("%s page %d: %w", product.Name, failedPage, pageErr)
	}
	if len(report.FailedIDs) > 0 {
		return report, fmt.Errorf("%s: failed to fetch draw IDs %v", product.Name, report.FailedIDs)
	}
	return report, nil
}

func productDataPath(repoRoot, fileName string) (string, error) {
	if fileName == "" || filepath.IsAbs(fileName) || strings.ContainsAny(fileName, `/\`) ||
		fileName == "." || fileName == ".." {
		return "", fmt.Errorf("invalid product file name %q", fileName)
	}
	dataDir := filepath.Clean(filepath.Join(repoRoot, "data"))
	path := filepath.Clean(filepath.Join(dataDir, fileName))
	relative, err := filepath.Rel(dataDir, path)
	if err != nil || relative == ".." || strings.HasPrefix(relative, ".."+string(filepath.Separator)) {
		return "", fmt.Errorf("invalid product file name %q: path escapes data directory", fileName)
	}
	return path, nil
}
