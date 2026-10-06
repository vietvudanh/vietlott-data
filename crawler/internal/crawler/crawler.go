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

// Sync downloads missing draws by scanning newest-first result pages and
// atomically appends successful results.
func Sync(ctx context.Context, repoRoot string, product model.Product, adapter ProductAdapter, maxDraws int) (SyncReport, error) {
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

	ids := MissingIDs(existing, product.MinID, latest, maxDraws)
	report.Missing = len(ids)
	if len(ids) == 0 {
		return report, nil
	}

	pages := product.MaxPages
	if pages < 1 {
		pages = 1
	}
	wanted := make(map[int]struct{}, len(ids))
	for _, id := range ids {
		wanted[id] = struct{}{}
	}
	// ids is ascending, so ids[0] is the oldest missing draw. Result pages
	// are newest-first, so once a page's highest ID falls below it, deeper
	// pages cannot contain anything we want.
	oldestWanted := ids[0]
	found := make(map[int]model.Draw, len(ids))
	var pageErr error
	var failedPage int
	canceled := false

pages:
	for page := 0; page < pages && len(found) < len(wanted); page++ {
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
			break pages
		}
		pageMax := -1
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
				}
			}
		}
		if pageMax >= 0 && pageMax < oldestWanted {
			break pages
		}
	}

	draws := make([]model.Draw, 0, len(found))
	for _, draw := range found {
		draws = append(draws, draw)
	}
	for _, id := range ids {
		if _, ok := found[id]; !ok {
			report.FailedIDs = append(report.FailedIDs, id)
		}
	}
	sort.Ints(report.FailedIDs)
	if len(draws) > 0 {
		if err := storage.AppendDrawsAtomic(path, draws); err != nil {
			return report, fmt.Errorf("write %s: %w", product.Name, err)
		}
		report.Written = len(draws)
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
