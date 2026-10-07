package storage

import (
	"errors"
	"os"
	"path/filepath"
	"testing"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
)

type testDraw struct {
	ID string `json:"id"`
}

func (d testDraw) GetID() string                { return d.ID }
func (testDraw) GetDate() string                { return "" }
func (testDraw) ProductName() model.ProductName { return model.Power655 }
func (d testDraw) MarshalJSON() ([]byte, error) { return []byte(`{"id":"` + d.ID + `"}`), nil }

type failingDraw struct{}

func (failingDraw) GetID() string                  { return "2" }
func (failingDraw) GetDate() string                { return "" }
func (failingDraw) ProductName() model.ProductName { return model.Power655 }
func (failingDraw) MarshalJSON() ([]byte, error)   { return nil, errors.New("boom") }

func TestLoadExistingDrawIDs(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	if err := os.WriteFile(path, []byte(`{"id":"0002"}
{"id":"#00001"}
`), 0o644); err != nil {
		t.Fatal(err)
	}
	ids, highest, validRows, err := LoadExistingDrawIDs(path)
	if err != nil {
		t.Fatal(err)
	}
	if len(ids) != 2 || highest != 2 || validRows != 2 {
		t.Fatalf("got ids=%v highest=%d validRows=%d", ids, highest, validRows)
	}
}

func TestAppendDrawsAtomicDeduplicatesAndSorts(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	if err := os.WriteFile(path, []byte(`{"id":"0002"}
`), 0o644); err != nil {
		t.Fatal(err)
	}
	draws := []model.Draw{testDraw{ID: "0003"}, testDraw{ID: "#00001"}, testDraw{ID: "3"}}
	if err := AppendDrawsAtomic(path, draws); err != nil {
		t.Fatal(err)
	}
	got, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}
	want := "{\"id\":\"0002\"}\n{\"id\":\"#00001\"}\n{\"id\":\"0003\"}\n"
	if string(got) != want {
		t.Fatalf("got %q, want %q", got, want)
	}
}

func TestAppendDrawsAtomicPreservesExistingMode(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	if err := os.WriteFile(path, []byte("{\"id\":\"1\"}\n"), 0o600); err != nil {
		t.Fatal(err)
	}
	if err := AppendDrawsAtomic(path, []model.Draw{testDraw{ID: "2"}}); err != nil {
		t.Fatal(err)
	}
	info, err := os.Stat(path)
	if err != nil {
		t.Fatal(err)
	}
	if got := info.Mode().Perm(); got != 0o600 {
		t.Fatalf("mode = %o, want 600", got)
	}
}

func TestAppendDrawsAtomicExistingIDWinsIncomingCollision(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	existing := "{\"id\":\"0002\",\"value\":1}\n{\"id\":\"0004\"}\n"
	if err := os.WriteFile(path, []byte(existing), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := AppendDrawsAtomic(path, []model.Draw{
		testDraw{ID: "2"},
		testDraw{ID: "3"},
	}); err != nil {
		t.Fatal(err)
	}
	got, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}
	want := "{\"id\":\"0002\",\"value\":1}\n{\"id\":\"0004\"}\n{\"id\":\"3\"}\n"
	if string(got) != want {
		t.Fatalf("got %q, want %q", got, want)
	}
}

func TestAppendDrawsAtomicPreservesExistingRowBytes(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	existing := "  {\"id\":\"0002\",\"value\":1}  \r\n"
	if err := os.WriteFile(path, []byte(existing), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := AppendDrawsAtomic(path, []model.Draw{testDraw{ID: "3"}}); err != nil {
		t.Fatal(err)
	}
	got, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}
	want := existing + "{\"id\":\"3\"}\n"
	if string(got) != want {
		t.Fatalf("got %q, want %q", got, want)
	}
}

func TestAppendDrawsAtomicEmptyInput(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	original := []byte("original\n")
	if err := os.WriteFile(path, original, 0o644); err != nil {
		t.Fatal(err)
	}
	if err := AppendDrawsAtomic(path, nil); err != nil {
		t.Fatal(err)
	}
	got, _ := os.ReadFile(path)
	if string(got) != string(original) {
		t.Fatalf("file changed: %q", got)
	}
}

func TestAppendDrawsAtomicMalformedInputPreservesOriginal(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	original := []byte("{\"id\":\"1\"}\n")
	if err := os.WriteFile(path, original, 0o644); err != nil {
		t.Fatal(err)
	}
	if err := AppendDrawsAtomic(path, []model.Draw{failingDraw{}}); err == nil {
		t.Fatal("expected marshal error")
	}
	got, _ := os.ReadFile(path)
	if string(got) != string(original) {
		t.Fatalf("file changed: %q", got)
	}
}

func TestLoadExistingDrawIDsMalformed(t *testing.T) {
	path := filepath.Join(t.TempDir(), "draws.jsonl")
	if err := os.WriteFile(path, []byte(`{"id":"not-a-number"}`), 0o644); err != nil {
		t.Fatal(err)
	}
	if _, _, _, err := LoadExistingDrawIDs(path); err == nil {
		t.Fatal("expected malformed ID error")
	}
}
