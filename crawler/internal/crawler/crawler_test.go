package crawler

import (
	"context"
	"errors"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
	"github.com/vietvudanh/vietlott-data/crawler/internal/storage"
)

type fakeAdapter struct {
	latest int
	draws  map[int]model.Draw
	errs   map[int]error
}

func (f *fakeAdapter) Latest(context.Context) (int, error) { return f.latest, nil }

func (f *fakeAdapter) Fetch(_ context.Context, id int) (model.Draw, error) {
	if err := f.errs[id]; err != nil {
		return nil, err
	}
	return f.draws[id], nil
}

func testDraw(id string) model.Draw {
	draw, err := model.DecodeDraw(model.Power655, []byte(`{"id":"`+id+`","date":"2026-01-01","result":[1]}`))
	if err != nil {
		panic(err)
	}
	return draw
}

func TestMissingIDsReturnsOnlyGapsThroughLatest(t *testing.T) {
	got := MissingIDs(map[int]struct{}{2: {}, 4: {}}, 1, 5, 0)
	want := []int{1, 3, 5}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("MissingIDs() = %v, want %v", got, want)
	}
}

func TestMissingIDsHonorsMaxDraws(t *testing.T) {
	got := MissingIDs(nil, 1, 5, 2)
	want := []int{1, 2}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("MissingIDs() = %v, want %v", got, want)
	}
}

func TestSyncWritesSuccessfulDrawsAndReturnsFailures(t *testing.T) {
	root := t.TempDir()
	dataDir := filepath.Join(root, "data")
	if err := os.Mkdir(dataDir, 0o755); err != nil {
		t.Fatal(err)
	}
	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1}
	if err := os.WriteFile(filepath.Join(dataDir, product.FileName), []byte(`{"id":"1","date":"2026-01-01","result":[1]}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	adapter := &fakeAdapter{
		latest: 4,
		draws:  map[int]model.Draw{2: testDraw("2"), 4: testDraw("4")},
		errs:   map[int]error{3: errors.New("unavailable")},
	}

	report, err := Sync(context.Background(), root, product, adapter, 0)
	if err == nil {
		t.Fatal("Sync() error = nil, want fetch failure")
	}
	if !reflect.DeepEqual(report.FailedIDs, []int{3}) {
		t.Fatalf("FailedIDs = %v, want [3]", report.FailedIDs)
	}
	if report.Written != 2 || report.Missing != 3 {
		t.Fatalf("report = %#v, want two writes and three missing", report)
	}
	ids, _, rows, err := storage.LoadExistingDrawIDs(filepath.Join(dataDir, product.FileName))
	if err != nil {
		t.Fatal(err)
	}
	if rows != 3 || !reflect.DeepEqual(ids, map[int]struct{}{1: {}, 2: {}, 4: {}}) {
		t.Fatalf("stored IDs = %v, rows = %d", ids, rows)
	}
}

func TestSyncNoOpWhenThereAreNoGaps(t *testing.T) {
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}

	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1}
	if err := os.WriteFile(filepath.Join(root, "data", product.FileName), []byte(`{"id":"1","date":"2026-01-01","result":[1]}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	report, err := Sync(context.Background(), root, product, &fakeAdapter{latest: 1}, 0)
	if err != nil {
		t.Fatal(err)
	}
	if report.Written != 0 || report.Missing != 0 {
		t.Fatalf("report = %#v, want no-op", report)
	}
}

func TestSyncRejectsProductFilePathTraversal(t *testing.T) {
	root := t.TempDir()
	product := model.Product{Name: model.Power655, FileName: "../outside.jsonl", MinID: 1}

	_, err := Sync(context.Background(), root, product, &fakeAdapter{latest: 1}, 0)
	if err == nil {
		t.Fatal("Sync() error = nil, want invalid product file path error")
	}
	if !strings.Contains(err.Error(), "invalid product file name") {
		t.Fatalf("Sync() error = %q, want explicit file name validation error", err)
	}
	if _, statErr := os.Stat(filepath.Join(root, "outside.jsonl")); !os.IsNotExist(statErr) {
		t.Fatal("Sync() created a file outside the data directory")
	}
}
