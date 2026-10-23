# Go Downloader Design

## Goal

Add a standalone Go CLI under `crawler/` that can inspect and backfill the
seven existing Vietlott JSONL datasets without changing their schema or
touching `src/machine_learning/` and `nb/`.

The first deliverable is the core downloader. Raspberry Pi cross-compilation
and the `bin/pi_sync.sh` automation remain a follow-up after the downloader is
verified locally.

## Existing contracts

The on-disk identifier is always a JSON string and must remain unchanged:

| Product | File | Identifier | Result shape |
| --- | --- | --- | --- |
| Power 6/55 | `data/power655.jsonl` | five-digit string | six main numbers plus bonus |
| Power 6/45 | `data/power645.jsonl` | five-digit string | six numbers |
| Power 5/35 | `data/power535.jsonl` | five-digit string | five numbers plus bonus |
| Keno | `data/keno.jsonl` | `#` plus seven-digit string | twenty numbers and `big_small`/`odd_even` |
| Bingo18 | `data/bingo18.jsonl` | seven-digit string | three numbers, `total`, `large_small`, `process_time` |
| Max 3D | `data/3d.jsonl` | five-digit string | prize-tier map of three-digit strings |
| Max 3D Pro | `data/3d_pro.jsonl` | five-digit string | prize-tier map of three-digit strings |

Dates are ISO calendar strings. Existing rows are retained byte-for-byte where
possible; newly fetched rows use the same field names and JSON-compatible
types, without adding metadata fields to products that do not already have
them. IDs are normalized only in memory for numeric range and gap operations.

## Architecture

`crawler/` is an independent Go module:

```text
crawler/
  cmd/vietlott/main.go
  internal/
    client/       shared HTTP transport, request templates, parsers
    crawler/      sync orchestration and gap calculation
    model/        product registry, typed draws, ID normalization
    storage/      streaming JSONL and atomic writes
  go.mod
```

The product registry is the source of truth for product names, file names,
request URLs, request templates, ID formatting, latest-draw discovery, and
parsers. A shared client owns common Vietlott headers, a ten-second timeout,
connection reuse, three-attempt exponential retry, and a 3–5 requests/second
rate limit. Product parsers remain separate because the upstream HTML layouts
and result fields differ.

## Data flow

For `missing --product` and `sync --product`:

1. Resolve the repository root and product registry entry.
2. Stream the product JSONL file and collect normalized IDs plus the highest ID.
3. Query the product’s latest page/metadata through the shared client.
4. Calculate missing IDs in the configured numeric interval.
5. Apply `--max-draws` as a limit to the missing-ID work list.
6. Fetch missing IDs through a bounded worker pool (two to four workers).
7. Parse and validate each result against the product’s typed contract.
8. Deduplicate by normalized ID, sort newly fetched rows by numeric ID, and
   append/rewrite through the storage layer.
9. Print a summary containing written rows, already-present rows, and failures.

`status` performs steps 1–3 and reports existing count, latest count, and gap
count without modifying data.

## Storage and atomicity

`LoadExistingDrawIDs` uses a buffered scanner and parses only the fields needed
for ID/date analysis. It returns normalized IDs and the highest numeric ID
without loading the full dataset into memory.

Writes are idempotent. Empty writes return immediately. When new rows exist,
the storage layer writes a temporary sibling file containing existing rows plus
deduplicated new rows, flushes and closes it, then atomically renames it over
the target. A failed write leaves the original file untouched. Every record is
one compact JSON object followed by exactly one newline.

## Error handling

HTTP status failures, exhausted retries, malformed HTML, missing required
fields, and ID mismatches are reported with product and draw-ID context.
Successful draws are retained even if other requested IDs fail. The command
exits non-zero when any requested draw fails, so unattended runners can detect
an incomplete sync. No broad catch or success-shaped fallback is used.

## CLI

The binary supports:

```text
vietlott status
vietlott missing --product <name>
vietlott sync --product <name> [--max-draws <n>]
vietlott sync --all [--max-draws <n>]
```

Product names match the data file stems (`power655`, `power645`, `power535`,
`keno`, `bingo18`, `3d`, and `3d_pro`). Invalid combinations and unknown
products produce explicit usage errors.

## Testing

Unit tests will cover:

- deserialization and compact re-serialization for representative rows from
  all seven datasets;
- exact ID preservation and normalized numeric comparisons;
- gap calculation, including prefixes and leading zeros;
- streaming reads, duplicate suppression, empty writes, and atomic replacement;
- mocked HTTP retry/rate-limit behavior and product parser fixtures;
- CLI status, missing, max-draw limits, and partial-failure exit codes.

Verification will run `go test ./...`, build the CLI, exercise local
`status`/`missing`, and read every resulting JSONL file with Polars. Existing
Python source, notebooks, and dataset schema are outside the change scope.
