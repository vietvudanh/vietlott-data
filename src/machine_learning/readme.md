# 🔮 Vietlott Power 655 Prediction Summary

> **Generated**: 2026-05-05 15:09:43
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

## 📊 Strategy Performance Comparison

> Sorted by ROI (best → worst).  All strategies backtested with **30 tickets/draw**.
> Note: All ROIs are deeply negative — lottery odds make profit impossible at scale.
> The comparison shows *which strategy loses the least*, not which one is profitable.

| Rank | Strategy | Total Cost (VND) | Total Gain (VND) | Net Profit (VND) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Pattern Strategy | 402,000,000 | 15,064,500,000 | 14,662,500,000 | 3647.39% |
| 🥈 2 | Markov Chain Strategy | 402,000,000 | 10,070,050,000 | 9,668,050,000 | 2404.99% |
| 🥉 3 | Not Repeat Strategy | 402,000,000 | 5,073,600,000 | 4,671,600,000 | 1162.09% |
|    4 | Pair Frequency Strategy | 402,000,000 | 5,071,100,000 | 4,669,100,000 | 1161.47% |
|    5 | Exponential Decay Strategy | 402,000,000 | 5,067,000,000 | 4,665,000,000 | 1160.45% |
|    6 | Random Strategy | 402,000,000 | 5,066,650,000 | 4,664,650,000 | 1160.36% |
|    7 | Long Absence Strategy | 402,000,000 | 72,950,000 | -329,050,000 | -81.85% |
|    8 | Hot Numbers Strategy | 402,000,000 | 72,150,000 | -329,850,000 | -82.05% |
|    9 | Cold Numbers Strategy | 402,000,000 | 66,000,000 | -336,000,000 | -83.58% |


## 📚 Strategy Descriptions

### Random Strategy

**How it works**: Generates tickets by shuffling all numbers in the valid range and picking the first `number_predict` entries.  Every number has an equal chance of being selected; no historical data is used.

**Use case**: Serves as an unbiased performance baseline.  Any strategy that cannot beat random selection over a large backtest offers no predictive value.

### Long Absence Strategy

**How it works**: For each draw date, looks back at all past draws and records the last date each number appeared.  Numbers are ranked by how many days have elapsed since they last appeared (numbers that have *never* appeared rank highest). A configurable pool of the `top_n` most-absent numbers is assembled, and `number_predict` numbers are randomly sampled from that pool.

**Key parameter**: `top_n` (default 10) – larger pool → more randomness; smaller pool → stronger bias toward the longest-absent numbers.

**Use case**: Captures the intuition that numbers that have been *overdue* for a long time are somehow more likely to appear.  (Note: for a fair lottery this intuition is mathematically incorrect, but the strategy is included for empirical comparison.)

### Pattern Strategy

**How it works**: Analyses two structural properties of historical draws in a rolling `lookback_days` window:

1. **Spacing patterns** – gaps between consecutive sorted numbers in a ticket.  The most common gaps are used to generate the next number by applying a sampled gap to the previously chosen number.
2. **Range distribution** – the number range 1–55 is split into five equal sub-ranges.  The historical fraction of draws falling in each sub-range is used as a probability weight for choosing the first number.

A `pattern_weight` fraction of the ticket is filled with pattern-derived numbers; the remainder is filled randomly.

**Key parameters**: `lookback_days` (default 180), `pattern_weight` (default 0.6).

### Hot Numbers Strategy

**How it works**: Counts how many times each number appeared over the last `lookback_days` days.  Numbers are sorted from most-frequent to least-frequent.  A weighted pool is built where each number is repeated proportionally to its frequency, then numbers are drawn without replacement from that pool.

A `selection_weight` fraction of the ticket is filled from the frequency-weighted pool; the rest is filled uniformly at random.

**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).

**Use case**: Tests whether recently hot numbers continue to appear at above-average rates.

### Cold Numbers Strategy

**How it works**: Identical to Hot Numbers Strategy but ranks numbers in the *reverse* order (least frequent first).  The weighted pool gives higher weight to numbers that have appeared fewer times in the lookback window.

**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).

**Use case**: Tests the complementary hypothesis that rarely-drawn numbers are more likely to appear (mean-reversion / gambler's fallacy).

### Not Repeat Strategy

**How it works**: Collects all numbers that appeared in *any* draw within the last `lookback_days` days.  Whenever enough *non-recent* numbers exist to fill a full ticket they are sampled uniformly.  When the pool of non-recent numbers is too small, remaining slots are filled using an `avoid_weight` probability to decide whether to pick from recent numbers or from the full range.

**Key parameters**: `lookback_days` (default 30), `avoid_weight` (default 0.8).

**Use case**: Models the idea that numbers drawn recently are *less* likely to repeat in the very next draw.

### Exponential Decay Strategy

**How it works**: Every historical draw contributes a score to each number it contained, but the contribution decays exponentially with age: ``weight = exp(-ln(2) × days_ago / half_life_days)``.  Draws from yesterday contribute much more than draws from a year ago.  Numbers are then selected from a pool weighted by their accumulated scores.

Unlike Hot/Cold Numbers Strategy there is **no hard window cutoff** — all history is used, with very old draws contributing negligibly.  The smooth decay avoids abrupt weight changes when a draw ages past a window boundary.

**Key parameters**: `half_life_days` (default 90), `hot` (default True), `selection_weight` (default 0.8).

### Pair Frequency Strategy

**How it works**: Builds a co-occurrence matrix from historical draws: ``cooccurrence[a][b]`` counts draws where numbers ``a`` and ``b`` both appeared.  Tickets are assembled iteratively:

1. The first number is sampled proportional to individual draw frequency.
2. Each subsequent number is sampled proportional to its **average co-occurrence score** with the numbers already selected.

This produces clusters of numbers that historically appear together, exploiting second-order correlations that all single-number strategies ignore.

**Key parameter**: `lookback_days` (default 365).

### Markov Chain Strategy

**How it works**: Models **first-order sequential dependencies** between consecutive draws — a dimension completely ignored by every other strategy.

A transition matrix ``T[a][b]`` is built from the lookback window: ``T[a][b]`` counts the number of times number ``a`` appeared in draw ``t`` **and** number ``b`` appeared in the *next* draw ``t+1``.  This captures cross-draw temporal correlations.

To predict for date ``d``:

1. Identify the most-recent draw before ``d`` — this is the **Markov state**.
2. For each candidate number ``n``, compute an aggregate score by summing ``T[s][n]`` over every number ``s`` in the state draw.
3. Sample ``number_predict`` numbers without replacement, weighted by (score + Laplace smoothing) to retain a non-zero chance for all numbers.

**Key parameters**: `lookback_days` (default 365), `smoothing` (default 0.5).

**Why this is novel**: Unlike Pair Frequency Strategy (which counts numbers that appear *together in the same draw*), Markov Chain counts numbers that appeared in *successive draws*.  If any temporal autocorrelation exists in the physical lottery mechanism, this strategy is best positioned to exploit it.


## 💻 Usage Examples

The strategies can be used independently outside this generator script.
Below are minimal runnable examples using Power 6/55 data.

### Install & load data

```python
import polars as pl
from vietlott.config.products import get_config

df_pl = pl.read_ndjson(get_config("power_655").raw_path)
df_pl = df_pl.with_columns(pl.col("date").str.to_date(strict=False))
df_pd = df_pl.to_pandas()
```

### Random baseline

```python
from machine_learning.strategies import RandomModel

model = RandomModel(df_pd, time_predict=5)
model.backtest()
model.evaluate()
cost, gain, profit = model.revenue()
print(f"ROI: {profit / cost * 100:.2f}%")
```

### Hot Numbers (frequency-based)

```python
from machine_learning.strategies import HotNumbersStrategy

model = HotNumbersStrategy(df_pd, time_predict=5, lookback_days=180, selection_weight=0.8)
model.backtest()
model.evaluate()
# Predict for a specific date
from datetime import date
print(model.predict(date(2025, 6, 1)))
```

### Markov Chain (sequential dependency)

```python
from machine_learning.strategies import MarkovChainStrategy

model = MarkovChainStrategy(df_pd, time_predict=5, lookback_days=365, smoothing=0.5)
model.backtest()
model.evaluate()
cost, gain, profit = model.revenue()
print(f"ROI: {profit / cost * 100:.2f}%")
```

### Backtest with a date range

```python
from machine_learning.strategies import PairFrequencyStrategy
from datetime import date

model = PairFrequencyStrategy(df_pd, time_predict=10, lookback_days=365)
# Only evaluate predictions for 2024 draws; full history is still used for lookups
model.backtest(date_from=date(2024, 1, 1), date_to=date(2024, 12, 31))
model.evaluate()
cost, gain, profit = model.revenue()
print(f"2024 ROI: {profit / cost * 100:.2f}%")
```

### Compare strategies head-to-head

```python
from machine_learning.strategies import (
    RandomModel, MarkovChainStrategy, PairFrequencyStrategy,
)

strategies = {
    "Random":       RandomModel(df_pd, time_predict=20),
    "Markov":       MarkovChainStrategy(df_pd, time_predict=20),
    "PairFreq":     PairFrequencyStrategy(df_pd, time_predict=20),
}

for name, model in strategies.items():
    model.backtest()
    model.evaluate()
    cost, gain, profit = model.revenue()
    print(f"{name:20s}  ROI={profit / cost * 100:+.1f}%")
```


## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Random Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 5,066,650,000 VND |
| Net profit/loss | 4,664,650,000 VND |
| ROI | 1160.36% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 53 times
  - **3 matches**: 803 times
  - **2 matches**: 5,678 times
  - **1 matches**: 16,515 times
  - **0 matches**: 17,150 times

#### Best Results (5+ matches)
| date                | result                      | predicted               |   correct_num |
|:--------------------|:----------------------------|:------------------------|--------------:|
| 2018-10-18 00:00:00 | [1, 11, 22, 34, 42, 47, 30] | [1, 22, 30, 37, 42, 47] |             5 |

### 🎲 Long Absence Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Long Absence Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 72,950,000 VND |
| Net profit/loss | -329,050,000 VND |
| ROI | -81.85% |

#### Match Distribution
  - **4 matches**: 59 times
  - **3 matches**: 869 times
  - **2 matches**: 5,623 times
  - **1 matches**: 16,480 times
  - **0 matches**: 17,169 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Pattern Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pattern Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 15,064,500,000 VND |
| Net profit/loss | 14,662,500,000 VND |
| ROI | 3647.39% |

#### Match Distribution
  - **5 matches**: 3 times
  - **4 matches**: 47 times
  - **3 matches**: 820 times
  - **2 matches**: 5,674 times
  - **1 matches**: 16,624 times
  - **0 matches**: 17,032 times

#### Best Results (5+ matches)
| date                | result                      | predicted                |   correct_num |
|:--------------------|:----------------------------|:-------------------------|--------------:|
| 2025-07-26 00:00:00 | [5, 26, 28, 29, 33, 54, 34] | [28, 29, 31, 33, 34, 54] |             5 |
| 2025-05-10 00:00:00 | [7, 16, 19, 28, 34, 51, 15] | [10, 15, 16, 19, 28, 34] |             5 |
| 2024-08-24 00:00:00 | [2, 17, 20, 21, 22, 23, 38] | [2, 20, 21, 22, 23, 45]  |             5 |

### 🎲 Hot Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Hot Numbers Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 72,150,000 VND |
| Net profit/loss | -329,850,000 VND |
| ROI | -82.05% |

#### Match Distribution
  - **4 matches**: 62 times
  - **3 matches**: 823 times
  - **2 matches**: 5,684 times
  - **1 matches**: 16,673 times
  - **0 matches**: 16,958 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Cold Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Cold Numbers Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 66,000,000 VND |
| Net profit/loss | -336,000,000 VND |
| ROI | -83.58% |

#### Match Distribution
  - **4 matches**: 52 times
  - **3 matches**: 800 times
  - **2 matches**: 5,576 times
  - **1 matches**: 16,744 times
  - **0 matches**: 17,028 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Not Repeat Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Not Repeat Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 5,073,600,000 VND |
| Net profit/loss | 4,671,600,000 VND |
| ROI | 1162.09% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 59 times
  - **3 matches**: 882 times
  - **2 matches**: 5,666 times
  - **1 matches**: 16,518 times
  - **0 matches**: 17,074 times

#### Best Results (5+ matches)
| date                | result                      | predicted               |   correct_num |
|:--------------------|:----------------------------|:------------------------|--------------:|
| 2021-09-18 00:00:00 | [3, 14, 15, 21, 47, 52, 54] | [3, 15, 21, 29, 52, 54] |             5 |

### 🎲 Exponential Decay Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Exponential Decay Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 5,067,000,000 VND |
| Net profit/loss | 4,665,000,000 VND |
| ROI | 1160.45% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 51 times
  - **3 matches**: 830 times
  - **2 matches**: 5,699 times
  - **1 matches**: 16,545 times
  - **0 matches**: 17,074 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2025-06-14 00:00:00 | [11, 12, 22, 26, 41, 47, 24] | [11, 12, 26, 41, 47, 55] |             5 |

### 🎲 Pair Frequency Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pair Frequency Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 5,071,100,000 VND |
| Net profit/loss | 4,669,100,000 VND |
| ROI | 1161.47% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 57 times
  - **3 matches**: 852 times
  - **2 matches**: 5,680 times
  - **1 matches**: 16,617 times
  - **0 matches**: 16,993 times

#### Best Results (5+ matches)
| date                | result                      | predicted               |   correct_num |
|:--------------------|:----------------------------|:------------------------|--------------:|
| 2018-06-05 00:00:00 | [11, 21, 26, 32, 51, 52, 5] | [5, 11, 21, 26, 52, 55] |             5 |

### 🎲 Markov Chain Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Markov Chain Strategy |
| Tickets per day | 30 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-05-02 00:00:00 |
| Total draws | 1,340 |
| Total predictions | 40,200 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 402,000,000 VND |
| Total gain | 10,070,050,000 VND |
| Net profit/loss | 9,668,050,000 VND |
| ROI | 2404.99% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 55 times
  - **3 matches**: 851 times
  - **2 matches**: 5,614 times
  - **1 matches**: 16,566 times
  - **0 matches**: 17,112 times

#### Best Results (5+ matches)
| date                | result                      | predicted                |   correct_num |
|:--------------------|:----------------------------|:-------------------------|--------------:|
| 2026-04-23 00:00:00 | [5, 16, 17, 22, 33, 53, 55] | [16, 22, 33, 45, 53, 55] |             5 |
| 2025-03-08 00:00:00 | [10, 38, 41, 43, 45, 48, 8] | [2, 8, 10, 38, 45, 48]   |             5 |




---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
