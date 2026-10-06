package crawler

import (
	"context"
	"errors"
	"fmt"
	"path/filepath"
	"sort"
	"strings"
	"sync"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
	"github.com/vietvudanh/vietlott-data/crawler/internal/storage"
)

// ProductAdapter retrieves the latest draw number and individual draws.
type ProductAdapter interface {
	Latest(context.Context) (int, error)
	Fetch(context.Context, int) (model.Draw, error)
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

type fetchResult struct {
	id   int
	draw model.Draw
	err  error
}

// Sync downloads missing draws and atomically appends successful results.
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

	workerCount := len(ids)
	if workerCount > 4 {
		workerCount = 4
	}
	if workerCount < 2 {
		workerCount = 2
	}
	workerCtx, cancel := context.WithCancel(ctx)
	defer cancel()
	jobs := make(chan int)
	results := make(chan fetchResult, len(ids))
	var workers sync.WaitGroup
	for i := 0; i < workerCount; i++ {
		workers.Add(1)
		go func() {
			defer workers.Done()
			for {
				select {
				case <-workerCtx.Done():
					return
				case id, ok := <-jobs:
					if !ok {
						return
					}
					draw, fetchErr := adapter.Fetch(workerCtx, id)
					if fetchErr == nil && draw == nil {
						fetchErr = errors.New("adapter returned nil draw")
					}
					results <- fetchResult{id: id, draw: draw, err: fetchErr}
				}
			}
		}()
	}

send:
	for _, id := range ids {
		select {
		case <-workerCtx.Done():
			break send
		case jobs <- id:
		}
	}
	close(jobs)
	workers.Wait()
	close(results)

	draws := make([]model.Draw, 0, len(ids))
	for result := range results {
		if result.err != nil {
			report.FailedIDs = append(report.FailedIDs, result.id)
			continue
		}
		draws = append(draws, result.draw)
	}
	sort.Ints(report.FailedIDs)
	if err := ctx.Err(); err != nil {
		if len(draws) > 0 {
			if writeErr := storage.AppendDrawsAtomic(path, draws); writeErr != nil {
				return report, fmt.Errorf("write %s: %w (context canceled: %v)", product.Name, writeErr, err)
			}
			report.Written = len(draws)
		}
		return report, err
	}
	if len(draws) > 0 {
		if err := storage.AppendDrawsAtomic(path, draws); err != nil {
			return report, fmt.Errorf("write %s: %w", product.Name, err)
		}
		report.Written = len(draws)
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
