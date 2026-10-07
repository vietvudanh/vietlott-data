package main

import (
	"context"
	"encoding/json"
	"errors"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"testing"

	"github.com/vietvudanh/vietlott-data/crawler/internal/crawler"
	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
)

func TestParseArgsValidatesSelectionAndMaxDraws(t *testing.T) {
	tests := []struct {
		name string
		args []string
		want string
	}{
		{"missing product", []string{"missing"}, "product is required"},
		{"sync selection", []string{"sync"}, "exactly one of --product or --all is required"},
		{"both selections", []string{"sync", "--product", "keno", "--all"}, "exactly one of --product or --all is required"},
		{"negative max", []string{"sync", "--product", "keno", "--max-draws", "-1"}, "max-draws must be nonnegative"},
		{"unknown product", []string{"missing", "--product", "nope"}, `unknown product "nope"`},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if _, err := parseArgs(tt.args); err == nil || !strings.Contains(err.Error(), tt.want) {
				t.Fatalf("parseArgs(%v) error = %v, want %q", tt.args, err, tt.want)
			}
		})
	}
	for _, args := range [][]string{
		{"--root=/custom/root", "status"},
		{"--root", "/custom/root", "status"},
	} {
		opts, err := parseArgs(args)
		if err != nil || opts.root != strings.TrimPrefix(args[0], "--root=") {
			if args[0] == "--root" {
				if err != nil || opts.root != args[1] {
					t.Fatalf("parseArgs(%v) = %#v, %v", args, opts, err)
				}
			} else {
				t.Fatalf("parseArgs(%v) = %#v, %v", args, opts, err)
			}
		}
	}
}

func TestMissingProductDispatchesInjectedAdapter(t *testing.T) {
	root := testRoot(t)
	product, _ := model.Lookup("keno")
	var calls []model.ProductName
	var out strings.Builder
	code := run(context.Background(), []string{"--root=" + root, "missing", "--product", "keno"}, &out, &out,
		func(name model.ProductName) (crawler.ProductAdapter, error) {
			calls = append(calls, name)
			return fakeAdapter{latest: product.MinID + 1}, nil
		})
	if code != 0 || len(calls) != 1 || !strings.Contains(out.String(), "keno existing=0") {
		t.Fatalf("code=%d calls=%v output=%q", code, calls, out.String())
	}
}

func TestSyncProductHonorsMaxDraws(t *testing.T) {
	root := testRoot(t)
	product, _ := model.Lookup("power655")
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "sync", "--product", "power655", "--max-draws", "1"},
		&out, &out, func(model.ProductName) (crawler.ProductAdapter, error) {
			return fakeAdapter{latest: product.MinID + 1}, nil
		})
	if code != 0 || !strings.Contains(out.String(), "power655 existing=0 latest=2 missing=1 written=1 failed=0") {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
}

func TestSyncAllDispatchesAllSevenRegistrations(t *testing.T) {
	root := testRoot(t)
	var calls []model.ProductName
	var out strings.Builder
	code := run(context.Background(), []string{"--root=" + root, "sync", "--all", "--max-draws", "1"},
		&out, &out, func(name model.ProductName) (crawler.ProductAdapter, error) {
			calls = append(calls, name)
			product, _ := model.Lookup(string(name))
			return fakeAdapter{latest: product.MinID}, nil
		})
	if code != 0 || len(calls) != len(allProducts) {
		t.Fatalf("code=%d calls=%v output=%q", code, calls, out.String())
	}
	for _, name := range allProducts {
		if !strings.Contains(out.String(), string(name)+" existing=0") {
			t.Fatalf("missing %s in output %q", name, out.String())
		}
	}
}

func TestSyncReturnsNonzeroForAdapterFailure(t *testing.T) {
	root := testRoot(t)
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "sync", "--product", "keno"},
		&out, &out, func(model.ProductName) (crawler.ProductAdapter, error) {
			return nil, errors.New("injected failure")
		})
	if code == 0 || !strings.Contains(out.String(), "injected failure") {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
}

func testRoot(t *testing.T) string {
	t.Helper()
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.Mkdir(filepath.Join(root, "crawler"), 0o755); err != nil {
		t.Fatal(err)
	}
	return root
}

func TestStatusQueriesAllAdaptersAndReportsStaleData(t *testing.T) {
	root := testRoot(t)
	product, _ := model.Lookup("power655")
	if err := os.WriteFile(filepath.Join(root, "data", product.FileName),
		[]byte(`{"id":"`+strconv.Itoa(product.MinID)+`"}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	var calls []model.ProductName
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "status"}, &out, &out, func(name model.ProductName) (crawler.ProductAdapter, error) {
		calls = append(calls, name)
		product, _ := model.Lookup(string(name))
		return fakeAdapter{latest: product.MinID}, nil
	})
	if code != 0 || len(calls) != len(allProducts) {
		t.Fatalf("run status exit code = %d, calls=%v, output: %s", code, calls, out.String())
	}
	if !strings.Contains(out.String(), "power655 existing=1 latest=1 missing=0 written=0 failed=0") {
		t.Fatalf("status output = %q", out.String())
	}
	if _, err := os.Stat(filepath.Join(root, "data", "power655.jsonl")); err != nil {
		t.Fatalf("status changed data: %v", err)
	}
}

func TestStatusReportsStaleDataFromUpstreamLatest(t *testing.T) {
	root := testRoot(t)
	product, _ := model.Lookup("power655")
	if err := os.WriteFile(filepath.Join(root, "data", product.FileName),
		[]byte(`{"id":"`+strconv.Itoa(product.MinID)+`"}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "status"}, &out, &out,
		func(name model.ProductName) (crawler.ProductAdapter, error) {
			product, _ := model.Lookup(string(name))
			if name == model.Power655 {
				return fakeAdapter{latest: product.MinID + 2}, nil
			}
			return fakeAdapter{latest: product.MinID}, nil
		})
	if code != 0 || !strings.Contains(out.String(), "power655 existing=1 latest=3 missing=2 written=0 failed=0") {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
}

func TestStatusReturnsNonzeroForAdapterFailure(t *testing.T) {
	root := testRoot(t)
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "status"}, &out, &out,
		func(name model.ProductName) (crawler.ProductAdapter, error) {
			if name == model.Keno {
				return nil, errors.New("injected status failure")
			}
			product, _ := model.Lookup(string(name))
			return fakeAdapter{latest: product.MinID}, nil
		})
	if code == 0 || !strings.Contains(out.String(), "injected status failure") ||
		!strings.Contains(out.String(), "keno existing=0 latest=0 missing=0 written=0 failed=1") {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
}

type fakeAdapter struct {
	latest int
}

func (f fakeAdapter) Latest(context.Context) (int, error) { return f.latest, nil }
func (f fakeAdapter) FetchPage(_ context.Context, page int) ([]model.Draw, error) {
	if page > 0 {
		return nil, nil
	}
	return []model.Draw{fakeDraw{ID: strconv.Itoa(f.latest - 1)}, fakeDraw{ID: strconv.Itoa(f.latest)}}, nil
}

type fakeDraw struct {
	ID string `json:"id"`
}

func (d fakeDraw) GetID() string                  { return d.ID }
func (d fakeDraw) GetDate() string                { return "" }
func (d fakeDraw) ProductName() model.ProductName { return model.Power655 }
func (d fakeDraw) MarshalJSON() ([]byte, error)   { type plain fakeDraw; return json.Marshal(plain(d)) }

func TestRenderReadmeWritesFile(t *testing.T) {
	root := testRoot(t)
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "render-readme"}, &out, &out, nil)
	if code != 0 {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
	raw, err := os.ReadFile(filepath.Join(root, "readme.md"))
	if err != nil {
		t.Fatal(err)
	}
	for _, want := range []string{"# Vietlott Data", "No data available"} {
		if !strings.Contains(string(raw), want) {
			t.Fatalf("readme.md missing %q", want)
		}
	}
}

func TestRenderDocsUpdatesHTML(t *testing.T) {
	root := testRoot(t)
	if err := os.Mkdir(filepath.Join(root, "docs"), 0o755); err != nil {
		t.Fatal(err)
	}
	html := `<html><body><table><tbody><tr><td>old</td></tr></tbody></table><!-- BEGIN_DAYS_SINCE_SECTION -->old<!-- END_DAYS_SINCE_SECTION --></body></html>`
	if err := os.WriteFile(filepath.Join(root, "docs", "index.html"), []byte(html), 0o644); err != nil {
		t.Fatal(err)
	}
	var out strings.Builder
	code := run(context.Background(), []string{"--root", root, "render-docs"}, &out, &out, nil)
	if code != 0 {
		t.Fatalf("code=%d output=%q", code, out.String())
	}
	raw, err := os.ReadFile(filepath.Join(root, "docs", "index.html"))
	if err != nil {
		t.Fatal(err)
	}
	if strings.Contains(string(raw), "<td>old</td>") {
		t.Fatalf("tbody not replaced: %s", raw)
	}
}
