# ML Multi-Run Prediction Stability Design

## Problem

Current ML prediction reporting runs once and produces a single summary snapshot. This does not show whether strategy ranking is stable across repeated stochastic executions.

We need a multi-run mode (default 10 runs) that:

1. Runs the prediction/backtest flow repeatedly.
2. Stores per-run logs.
3. Produces an aggregated report focused on strategy ranking stability over time.

## Scope

In scope:

- Extend `src/machine_learning/render_prediction.py`.
- Add CLI arguments for multi-run execution and output locations.
- Append per-run structured logs.
- Generate one aggregated markdown report with ranking stability metrics.

Out of scope:

- Refactoring the ML module into new package boundaries.
- Introducing new strategy algorithms.
- Replacing existing single-run logic.

## Goals and Non-Goals

### Goals

- Default behavior supports repeated runs (`runs=10`).
- Measure whether top strategies remain top across repeated runs.
- Keep current strategy evaluation logic and output semantics.
- Preserve reproducibility with deterministic per-run seeds.

### Non-Goals

- Profitability claims or gambling optimization.
- UI/dashboard development.
- Full experiment tracking platform.

## User Interface and CLI

`render_prediction.py` will support:

- `--runs` (int, default `10`)
- `--log-path` (path, default `src/machine_learning/reports/prediction_runs.log.jsonl`)
- `--report-path` (path, default `src/machine_learning/reports/prediction_runs_report.md`)
- `--base-seed` (optional int)
- existing date filters remain supported (`date_from`, `date_to` behavior unchanged)

Behavior:

- Runs loop from `run_index=1..N`.
- Seed per run = `effective_base_seed + (run_index - 1)`.
- If `--base-seed` is omitted, generate one base seed once and log it.

## Architecture

Keep `PredictionSummaryGenerator` as the core orchestration class and add a multi-run orchestration layer in the same file:

1. **Single-run executor**  
   Reuse current flow for loading data, building/running strategies, and extracting per-strategy metrics.

2. **Multi-run orchestrator**  
   Loop N runs, set deterministic seeds for Python and NumPy each run, collect run summaries.

3. **Log writer (JSONL append-only)**  
   Append one record per run.

4. **Aggregated report builder**  
   Compute ranking stability metrics from all run records and write one markdown report.

This keeps implementation local and low-risk while enabling future extraction if needed.

## Data Flow

1. Load `power_655` data once.
2. For each run:
   - Apply run seed.
   - Execute all strategies (`backtest` + `evaluate`).
   - Compute metrics per strategy (`roi`, `win_rate`, `avg_matches`, `net_profit`, `total_predictions`).
   - Build ranking list by ROI.
   - Append run record to JSONL.
3. After loop:
   - Aggregate rankings across runs.
   - Build stability report.
   - Write markdown report.

## Log Schema (JSONL)

One JSON object per line:

- `run_id` (string)
- `run_index` (int)
- `timestamp` (ISO string)
- `seed` (int)
- `tickets_per_day` (int)
- `date_from` (nullable string)
- `date_to` (nullable string)
- `strategy_results` (array of objects):
  - `strategy_name` (string)
  - `roi` (float)
  - `win_rate` (float)
  - `avg_matches` (float)
  - `net_profit` (float/int)
  - `total_predictions` (int)
  - `rank` (int)
- `ranking` (array of strategy names ordered best->worst)

## Aggregated Report Content

`prediction_runs_report.md` will include:

1. Run configuration summary (N, base seed, date range, output paths).
2. Ranking stability table per strategy:
   - average rank
   - rank stddev
   - times ranked #1
   - min rank
   - max rank
3. Per-run ranking history table.
4. Consensus ranking (sorted by average rank).
5. Interpretation notes on stochastic variability.

## Error Handling

- Global setup failures (data load, invalid config) abort command with explicit error.
- Per-run failures are logged with `error_type` and `error_message`; remaining runs continue.
- Ensure output directories exist before writing.
- JSONL append failures and report write failures are surfaced explicitly.

## Compatibility and Defaults

- Existing single-run semantics remain available via `--runs 1`.
- New default `--runs 10` is intentional for stability analysis.
- Existing strategy definitions and backtest math are unchanged.

## Testing Strategy

1. **Unit tests (aggregation):**
   - average rank, stddev, #1 counts, min/max rank.
2. **Unit tests (seed behavior):**
   - deterministic per-run seeds from base seed.
3. **Integration-style test (output generation):**
   - generate multiple runs on small synthetic data and validate:
     - JSONL record count equals N.
     - report contains stability table and per-run rankings.
4. **CLI parsing tests:**
   - default values and custom path/seed overrides.

## Risks and Mitigations

- **Risk:** random-heavy strategies produce high run-to-run variance.  
  **Mitigation:** explicit stability metrics and full per-run rankings.

- **Risk:** accidental behavioral drift in existing summary generation.  
  **Mitigation:** retain current strategy execution path and add focused tests.

- **Risk:** large logs over time.  
  **Mitigation:** append-only JSONL with user-configurable path and easy rotation outside command.

