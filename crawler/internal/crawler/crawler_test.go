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
	latest   int
	pages    map[int][]model.Draw
	pageErrs map[int]error
	calls    *[]int
}

func (f *fakeAdapter) Latest(context.Context) (int, error) { return f.latest, nil }

func (f *fakeAdapter) FetchPage(_ context.Context, page int) ([]model.Draw, error) {
	if f.calls != nil {
		*f.calls = append(*f.calls, page)
	}
	if err := f.pageErrs[page]; err != nil {
		return nil, err
	}
	return f.pages[page], nil
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
	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1, MaxPages: 3}
	if err := os.WriteFile(filepath.Join(dataDir, product.FileName), []byte(`{"id":"1","date":"2026-01-01","result":[1]}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	adapter := &fakeAdapter{
		latest: 4,
		pages: map[int][]model.Draw{
			0: {testDraw("4"), testDraw("2")},
			1: {testDraw("2")},
		},
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

func TestSyncStopsPagingOnceAllMissingAreFound(t *testing.T) {
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1, MaxPages: 5}
	var calls []int
	adapter := &fakeAdapter{
		latest: 2,
		pages:  map[int][]model.Draw{0: {testDraw("1"), testDraw("2")}},
		calls:  &calls,
	}
	report, err := Sync(context.Background(), root, product, adapter, 0)
	if err != nil {
		t.Fatal(err)
	}
	if report.Written != 2 || len(report.FailedIDs) != 0 {
		t.Fatalf("report = %#v, want two writes and no failures", report)
	}
	if !reflect.DeepEqual(calls, []int{0}) {
		t.Fatalf("page calls = %v, want only page 0", calls)
	}
}

func TestSyncStopsWhenPagesPassOldestWanted(t *testing.T) {
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1, MaxPages: 10}
	var existing strings.Builder
	for _, id := range []string{"1", "2", "3", "4", "6", "7", "8", "9", "10"} {
		existing.WriteString(`{"id":"` + id + `","date":"2026-01-01","result":[1]}` + "\n")
	}
	if err := os.WriteFile(filepath.Join(root, "data", product.FileName), []byte(existing.String()), 0o644); err != nil {
		t.Fatal(err)
	}
	var calls []int
	adapter := &fakeAdapter{
		latest: 10,
		pages: map[int][]model.Draw{
			0: {testDraw("10"), testDraw("9")},
			1: {testDraw("8"), testDraw("7")},
			2: {testDraw("4"), testDraw("3")},
		},
		calls: &calls,
	}
	report, err := Sync(context.Background(), root, product, adapter, 0)
	if err == nil || !strings.Contains(err.Error(), "[5]") {
		t.Fatalf("Sync() error = %v, want failure listing ID 5", err)
	}
	if !reflect.DeepEqual(report.FailedIDs, []int{5}) {
		t.Fatalf("FailedIDs = %v, want [5]", report.FailedIDs)
	}
	if !reflect.DeepEqual(calls, []int{0, 1, 2}) {
		t.Fatalf("page calls = %v, want stop after paging past ID 5", calls)
	}
}

func TestSyncReturnsPageErrorAfterWritingPartialResults(t *testing.T) {
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	product := model.Product{Name: model.Power655, FileName: "power655.jsonl", MinID: 1, MaxPages: 3}
	adapter := &fakeAdapter{
		latest:   3,
		pages:    map[int][]model.Draw{0: {testDraw("1"), testDraw("2")}},
		pageErrs: map[int]error{1: errors.New("upstream unavailable")},
	}
	report, err := Sync(context.Background(), root, product, adapter, 0)
	if err == nil || !strings.Contains(err.Error(), "upstream unavailable") {
		t.Fatalf("Sync() error = %v, want page failure", err)
	}
	if report.Written != 2 || !reflect.DeepEqual(report.FailedIDs, []int{3}) {
		t.Fatalf("report = %#v, want two writes and ID 3 failed", report)
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
