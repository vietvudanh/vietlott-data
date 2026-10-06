# Go Downloader Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Go CLI under `crawler/` that detects and downloads missing Vietlott draws for all seven existing JSONL products without changing their on-disk schemas, and add a Raspberry Pi ARM64 Makefile target.

**Architecture:** Use a typed product registry and shared HTTP transport, with product-specific HTML parsers behind a common client interface. Stream existing JSONL IDs, normalize only for numeric comparisons, fetch missing IDs through bounded workers, and atomically rewrite deduplicated JSONL files. Keep the Go module independent from the Python package and resolve data paths from the repository root.

**Tech Stack:** Go standard library (`net/http`, `encoding/json`, `html` parsing helpers, `bufio`, `os`, `sync`), `golang.org/x/net/html` only if required by parser implementation, existing Vietlott AJAX endpoints, Make.

---

## File map

Create:

- `crawler/go.mod` and `crawler/go.sum`: standalone module metadata.
- `crawler/cmd/vietlott/main.go`: flag-based CLI entrypoint and command dispatch.
- `crawler/internal/model/product.go`: product registry, aliases, file names, endpoint metadata, and ID normalization.
- `crawler/internal/model/draw.go`: typed draw records and compact JSON encoding.
- `crawler/internal/model/product_test.go`: registry and ID normalization tests.
- `crawler/internal/model/draw_test.go`: seven product schema round-trip tests.
- `crawler/internal/storage/jsonl.go`: streaming reads and atomic writes.
- `crawler/internal/storage/jsonl_test.go`: storage behavior tests.
- `crawler/internal/client/client.go`: HTTP transport, headers, retries, and rate limiting.
- `crawler/internal/client/client_test.go`: mocked transport tests.
- `crawler/internal/client/products.go`: product request builders, HTML parsers, and latest-ID extraction.
- `crawler/internal/client/products_test.go`: parser fixture tests for all product layouts.
- `crawler/internal/crawler/crawler.go`: gap calculation, worker pool, and sync/status operations.
- `crawler/internal/crawler/crawler_test.go`: orchestration and partial-failure tests.

Modify:

- `Makefile`: add `build-crawler` and `build-arm-pi` targets.

Do not modify:

- `src/machine_learning/`
- `nb/`
- existing `data/*.jsonl` rows
- Python crawler behavior

## Task 1: Scaffold the Go module and product/ID model

**Files:**
- Create: `crawler/go.mod`
- Create: `crawler/internal/model/product.go`
- Create: `crawler/internal/model/product_test.go`

- [ ] **Step 1: Write failing registry and normalization tests**

Add tests covering all seven names, file stems, exact ID preservation, and Keno’s `#` prefix:

```go
func TestLookupProductUsesDataStem(t *testing.T) {
    p, err := Lookup("3d_pro")
    if err != nil || p.Name != "3d_pro" || p.FileName != "3d_pro.jsonl" {
        t.Fatalf("unexpected product: %#v, %v", p, err)
    }
}

func TestNormalizeIDPreservesRawAndParsesNumericValue(t *testing.T) {
    got, err := NormalizeID("#0000123")
    if err != nil || got.Raw != "#0000123" || got.Number != 123 {
        t.Fatalf("unexpected normalized ID: %#v, %v", got, err)
    }
}
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
cd crawler && go test ./internal/model
```

Expected: failure because the module and model package do not yet exist.

- [ ] **Step 3: Initialize the module and implement the registry**

Create `crawler/go.mod` with:

```go
module github.com/vietvudanh/vietlott-data/crawler

go 1.22
```

Implement:

```go
type ProductName string

const (
    Power655 ProductName = "power655"
    Power645 ProductName = "power645"
    Power535 ProductName = "power535"
    Keno     ProductName = "keno"
    Bingo18  ProductName = "bingo18"
    Max3D    ProductName = "3d"
    Max3DPro ProductName = "3d_pro"
)

type Product struct {
    Name       ProductName
    FileName   string
    Endpoint   string
    IDWidth    int
    IDPrefix   string
    MinID      int
    ResultKind string
}

type NormalizedID struct {
    Raw    string
    Number int
}

func NormalizeID(raw string) (NormalizedID, error) {
    trimmed := strings.TrimSpace(raw)
    if trimmed == "" {
        return NormalizedID{}, errors.New("draw ID is empty")
    }
    numeric := strings.TrimPrefix(trimmed, "#")
    number, err := strconv.Atoi(numeric)
    if err != nil || number < 0 {
        return NormalizedID{}, fmt.Errorf("invalid draw ID %q", raw)
    }
    return NormalizedID{Raw: trimmed, Number: number}, nil
}
```

Populate a map for all seven products using the endpoint names and ID widths
already extracted from the Python product classes. `Lookup` must reject unknown
names with an explicit error.

- [ ] **Step 4: Run model tests and commit**

Run:

```bash
cd crawler && go test ./internal/model
```

Expected: PASS.

Commit:

```bash
git add crawler/go.mod crawler/internal/model/product.go crawler/internal/model/product_test.go
git commit -m "feat(crawler): add Go product registry"
```

## Task 2: Add typed draw contracts

**Files:**
- Create: `crawler/internal/model/draw.go`
- Create: `crawler/internal/model/draw_test.go`

- [ ] **Step 1: Add one representative JSON fixture test per product**

Each test must unmarshal a line copied from the corresponding `data/*.jsonl`,
call `Draw.GetID()` and `Draw.GetDate()`, marshal it again, unmarshal into
`map[string]any`, and compare the key set and value types. Assert that IDs such
as `"00001"` and `"#0110271"` remain strings.

- [ ] **Step 2: Run the tests to verify the missing types fail**

Run:

```bash
cd crawler && go test ./internal/model -run Draw
```

Expected: compile failure because draw types are not defined.

- [ ] **Step 3: Implement the draw types and common interface**

Define:

```go
type Draw interface {
    GetID() string
    GetDate() string
    ProductName() ProductName
    MarshalJSON() ([]byte, error)
}

type NumberDraw struct {
    Date        string `json:"date"`
    ID          string `json:"id"`
    Result      []int  `json:"result"`
    ProcessTime string `json:"process_time"`
}

type KenoDraw struct {
    Date     string `json:"date"`
    ID       string `json:"id"`
    Result   []int  `json:"result"`
    BigSmall string `json:"big_small"`
    OddEven  string `json:"odd_even"`
}

type Bingo18Draw struct {
    Date        string `json:"date"`
    ID          string `json:"id"`
    Result      []int  `json:"result"`
    Total       int    `json:"total"`
    LargeSmall  string `json:"large_small"`
    ProcessTime string `json:"process_time"`
}

type ThreeDDraw struct {
    Date   string              `json:"date"`
    ID     string              `json:"id"`
    Result map[string][]string `json:"result"`
}
```

Use product-specific wrappers or aliases for Power 6/55, Power 6/45, and
Power 5/35 so the encoder emits the exact existing keys. Do not emit
`process_time` for Keno or either 3D product.

- [ ] **Step 4: Run schema tests and commit**

Run:

```bash
cd crawler && go test ./internal/model
```

Expected: PASS for all seven product fixtures.

Commit:

```bash
git add crawler/internal/model/draw.go crawler/internal/model/draw_test.go
git commit -m "feat(crawler): model existing draw schemas"
```

## Task 3: Implement streaming and atomic JSONL storage

**Files:**
- Create: `crawler/internal/storage/jsonl.go`
- Create: `crawler/internal/storage/jsonl_test.go`

- [ ] **Step 1: Write storage tests**

Cover:

```go
func TestLoadExistingDrawIDsStreamsAndFindsHighestID(t *testing.T) {}
func TestAppendDrawsAtomicDeduplicatesByNormalizedID(t *testing.T) {}
func TestAppendDrawsAtomicEmptyInputLeavesFileUnchanged(t *testing.T) {}
func TestAppendDrawsAtomicFailureLeavesOriginalFile(t *testing.T) {}
```

Use `t.TempDir()`, include leading-zero IDs and a Keno `#` ID, and assert each
output record ends with one newline and remains valid JSON.

- [ ] **Step 2: Run storage tests and verify they fail**

Run:

```bash
cd crawler && go test ./internal/storage
```

Expected: compile failure because storage functions are absent.

- [ ] **Step 3: Implement the streaming reader**

Use a `bufio.Scanner` with an increased buffer, unmarshal only:

```go
type idRecord struct {
    ID string `json:"id"`
}
```

Implement:

```go
func LoadExistingDrawIDs(path string) (map[int]struct{}, int, int, error)
```

Return the normalized-ID set, highest numeric ID, and valid-row count. Return
line-numbered errors for malformed JSON or invalid IDs; do not silently skip
bad input.

- [ ] **Step 4: Implement atomic deduplicating writes**

Implement:

```go
func AppendDrawsAtomic(path string, draws []model.Draw) error
```

Read existing lines into a temporary output stream while tracking normalized
IDs, skip duplicate new draws, sort new draws by numeric ID, encode each with
`json.Encoder` configured for compact output, call `Sync`, close, and rename
the temporary sibling file over the target. Remove only the specifically
created temporary path on failure.

- [ ] **Step 5: Run storage tests and commit**

Run:

```bash
cd crawler && go test ./internal/storage
```

Expected: PASS.

Commit:

```bash
git add crawler/internal/storage
git commit -m "feat(crawler): add atomic JSONL storage"
```

## Task 4: Build the shared HTTP client and product parsers

**Files:**
- Create: `crawler/internal/client/client.go`
- Create: `crawler/internal/client/client_test.go`
- Create: `crawler/internal/client/products.go`
- Create: `crawler/internal/client/products_test.go`

- [ ] **Step 1: Add mocked transport tests**

Use `httptest.Server` or a custom `http.RoundTripper` to assert:

```go
func TestClientRetriesTransientResponses(t *testing.T) {}
func TestClientStopsAfterThreeAttempts(t *testing.T) {}
func TestClientAddsVietlottHeaders(t *testing.T) {}
```

Test that a 500, then 200 response succeeds and that three failures return an
error containing the URL and status.

- [ ] **Step 2: Implement transport, retry, and rate limiting**

Define:

```go
type Client struct {
    HTTP       *http.Client
    limiter    *rateLimiter
    maxRetries int
}

func New(httpClient *http.Client) *Client
func (c *Client) PostJSON(ctx context.Context, url string, body []byte) ([]byte, error)
```

Use a ten-second timeout by default, persistent connections, the headers from
`src/vietlott/crawler/requests_helper/config.py`, three attempts, and
exponential delays of 250ms and 500ms. The limiter must serialize token
acquisition at no more than five requests per second.

- [ ] **Step 3: Create parser fixtures for all seven products**

Store small HTML strings in `products_test.go` that match the table layouts
used by the Python classes. Assert exact IDs, ISO dates, result arrays, prize
keys, and Bingo18 metadata.

- [ ] **Step 4: Implement request builders and parsers**

Define a common product adapter:

```go
type ProductAdapter interface {
    Latest(ctx context.Context) (int, error)
    Fetch(ctx context.Context, numericID int) (model.Draw, error)
}
```

Implement one adapter per product using the existing AJAX endpoint and request
body fields from the Python request schemas. Parse HTML with
`golang.org/x/net/html`, validate required cells and result counts, preserve
three-digit strings with leading zeros, and return errors with product and
draw-ID context. `Latest` must identify the highest parsed ID rather than
assuming the first table row is valid.

- [ ] **Step 5: Run client tests and commit**

Run:

```bash
cd crawler && go test ./internal/client
```

Expected: PASS.

Commit:

```bash
git add crawler/internal/client crawler/go.mod crawler/go.sum
git commit -m "feat(crawler): add Vietlott HTTP adapters"
```

## Task 5: Add gap calculation and sync orchestration

**Files:**
- Create: `crawler/internal/crawler/crawler.go`
- Create: `crawler/internal/crawler/crawler_test.go`

- [ ] **Step 1: Write deterministic gap and partial-success tests**

Test:

```go
func TestMissingIDsReturnsOnlyGapsThroughLatest(t *testing.T) {}
func TestMissingIDsHonorsMaxDraws(t *testing.T) {}
func TestSyncWritesSuccessfulDrawsAndReturnsFailures(t *testing.T) {}
```

Use a fake `ProductAdapter` that returns two draws and one error, then assert
that two valid draws are written and the result reports one failure.

- [ ] **Step 2: Implement gap calculation**

Define:

```go
func MissingIDs(existing map[int]struct{}, minID, latestID, maxDraws int) []int
```

Return ascending IDs from `minID` through `latestID`, exclude present IDs, and
apply `maxDraws > 0` after sorting. Reject `latestID < minID` in the caller
with an explicit error.

- [ ] **Step 3: Implement bounded worker orchestration**

Define:

```go
type SyncReport struct {
    Product      model.ProductName
    Existing     int
    Latest       int
    Missing      int
    Written      int
    FailedIDs    []int
}

func Sync(ctx context.Context, repoRoot string, product model.Product, adapter ProductAdapter, maxDraws int) (SyncReport, error)
```

Use two to four workers, a jobs channel, a results channel, context
cancellation, and deterministic sorting of `FailedIDs`. Write successful draws
only after all workers finish. Return a non-nil error when any ID failed,
while preserving the successful writes.

- [ ] **Step 4: Run crawler tests and commit**

Run:

```bash
cd crawler && go test ./internal/crawler
```

Expected: PASS.

Commit:

```bash
git add crawler/internal/crawler
git commit -m "feat(crawler): add missing-draw orchestration"
```

## Task 6: Implement the CLI

**Files:**
- Create: `crawler/cmd/vietlott/main.go`
- Create: `crawler/cmd/vietlott/main_test.go`

- [ ] **Step 1: Add CLI behavior tests**

Test argument parsing and command validation for:

```text
vietlott status
vietlott missing --product power655
vietlott sync --product power655 --max-draws 1
vietlott sync --all
```

Assert unknown products, missing `--product`/`--all`, and negative
`--max-draws` return non-zero errors with useful messages.

- [ ] **Step 2: Implement repository-root resolution and dispatch**

Use an optional `--root` flag for tests and otherwise walk upward from the
executable/current directory until both `data/` and `crawler/` exist. Register
all seven adapters and dispatch commands to `crawler.Sync`.

Print stable one-line summaries such as:

```text
power655 existing=1406 latest=1406 missing=0 written=0 failed=0
```

Exit with status 1 when any product has failures.

- [ ] **Step 3: Run CLI tests, build, and commit**

Run:

```bash
cd crawler && go test ./cmd/vietlott
go build -o ../bin/vietlott-crawler ./cmd/vietlott
```

Expected: tests pass and `bin/vietlott-crawler` is created.

Commit:

```bash
git add crawler/cmd/vietlott
git commit -m "feat(crawler): add downloader CLI"
```

## Task 7: Add Makefile targets for local and Raspberry Pi builds

**Files:**
- Modify: `Makefile`

- [ ] **Step 1: Add build targets**

Add `.PHONY` entries and targets:

```make
.PHONY: build-crawler build-arm-pi

build-crawler:
	cd crawler && go build -o ../bin/vietlott-crawler ./cmd/vietlott

build-arm-pi:
	cd crawler && GOOS=linux GOARCH=arm64 GOARM=7 go build -ldflags="-s -w" -o ../bin/vietlott-crawler-arm64 ./cmd/vietlott
```

Keep `GOARM=7` exactly as requested even though it is ignored by Go for
`arm64`; retaining it makes the build configuration explicit and compatible
with the deployment environment.

- [ ] **Step 2: Verify both targets**

Run:

```bash
make build-crawler
make build-arm-pi
file bin/vietlott-crawler bin/vietlott-crawler-arm64
```

Expected: the first binary targets the local machine and the second reports an
`ELF 64-bit LSB executable, ARM aarch64` target.

- [ ] **Step 3: Commit the Makefile change**

```bash
git add Makefile
git commit -m "build: add Raspberry Pi ARM64 crawler target"
```

## Task 8: Run full verification and compatibility checks

**Files:**
- No source changes expected.

- [ ] **Step 1: Run all Go tests**

Run:

```bash
cd crawler && go test ./...
```

Expected: PASS for model, storage, client, crawler, and CLI packages.

- [ ] **Step 2: Exercise read-only CLI commands**

Run:

```bash
./bin/vietlott-crawler status
./bin/vietlott-crawler missing --product power655
```

Expected: summaries are printed and no `data/*.jsonl` file changes.

- [ ] **Step 3: Run a bounded sync against one product**

Run:

```bash
./bin/vietlott-crawler sync --product power655 --max-draws 1
```

Expected: at most one missing draw is fetched, successful output is
deduplicated, and any upstream failure produces a non-zero exit code with the
failed draw ID.

- [ ] **Step 4: Verify every dataset remains readable by Polars**

Run:

```bash
uv run python - <<'PY'
import polars as pl
from pathlib import Path

for path in sorted(Path("data").glob("*.jsonl")):
    frame = pl.read_ndjson(path)
    print(f"{path}: {len(frame)} rows, schema OK")
PY
```

Expected: all seven files load successfully.

- [ ] **Step 5: Inspect the final diff**

Run:

```bash
git diff --check HEAD~8..HEAD
git status --short
```

Expected: no whitespace errors, no changes under `src/machine_learning/` or
`nb/`, and only the planned Go module, tests, Makefile, and generated binary
artifacts (with binaries removed or ignored before completion).
