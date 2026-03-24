# 🔮 Vietlott Power 655 Prediction Summary

> **Generated**: 2026-03-23 08:42:09
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

## 📊 Strategy Performance Comparison

> Sorted by ROI (best → worst).  All strategies backtested with **20 tickets/draw**.
> Note: All ROIs are deeply negative — lottery odds make profit impossible at scale.
> The comparison shows *which strategy loses the least*, not which one is profitable.

| Rank | Strategy | Total Cost (VND) | Total Gain (VND) | Net Profit (VND) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Not Repeat Strategy | 264,400,000 | 10,053,250,000 | 9,788,850,000 | 3702.29% |
| 🥈 2 | Pair Frequency Strategy | 264,400,000 | 10,043,100,000 | 9,778,700,000 | 3698.45% |
| 🥉 3 | Exponential Decay Strategy | 264,400,000 | 5,053,050,000 | 4,788,650,000 | 1811.14% |
|    4 | Hot Numbers Strategy | 264,400,000 | 5,045,350,000 | 4,780,950,000 | 1808.23% |
|    5 | Cold Numbers Strategy | 264,400,000 | 5,044,350,000 | 4,779,950,000 | 1807.85% |
|    6 | Pattern Strategy | 264,400,000 | 5,041,900,000 | 4,777,500,000 | 1806.92% |
|    7 | Random Strategy | 264,400,000 | 5,041,550,000 | 4,777,150,000 | 1806.79% |
|    8 | Long Absence Strategy | 264,400,000 | 49,150,000 | -215,250,000 | -81.41% |


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


## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Random Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 5,041,550,000 VND |
| Net profit/loss | 4,777,150,000 VND |
| ROI | 1806.79% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 27 times
  - **3 matches**: 561 times
  - **2 matches**: 3,677 times
  - **1 matches**: 11,062 times
  - **0 matches**: 11,112 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2024-03-05 00:00:00 | [12, 19, 21, 23, 28, 54, 31] | [35, 23, 28, 54, 19, 21] |             5 |

### 🎲 Long Absence Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Long Absence Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 49,150,000 VND |
| Net profit/loss | -215,250,000 VND |
| ROI | -81.41% |

#### Match Distribution
  - **4 matches**: 41 times
  - **3 matches**: 573 times
  - **2 matches**: 3,729 times
  - **1 matches**: 10,691 times
  - **0 matches**: 11,406 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Pattern Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pattern Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 5,041,900,000 VND |
| Net profit/loss | 4,777,500,000 VND |
| ROI | 1806.92% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 25 times
  - **3 matches**: 588 times
  - **2 matches**: 3,695 times
  - **1 matches**: 10,948 times
  - **0 matches**: 11,183 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2025-05-20 00:00:00 | [19, 27, 44, 45, 47, 52, 15] | [15, 19, 44, 45, 47, 53] |             5 |

### 🎲 Hot Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Hot Numbers Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 5,045,350,000 VND |
| Net profit/loss | 4,780,950,000 VND |
| ROI | 1808.23% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 35 times
  - **3 matches**: 557 times
  - **2 matches**: 3,650 times
  - **1 matches**: 11,057 times
  - **0 matches**: 11,140 times

#### Best Results (5+ matches)
| date                | result                     | predicted              |   correct_num |
|:--------------------|:---------------------------|:-----------------------|--------------:|
| 2019-02-16 00:00:00 | [5, 8, 14, 28, 37, 40, 41] | [5, 8, 12, 28, 37, 40] |             5 |

### 🎲 Cold Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Cold Numbers Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 5,044,350,000 VND |
| Net profit/loss | 4,779,950,000 VND |
| ROI | 1807.85% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 36 times
  - **3 matches**: 527 times
  - **2 matches**: 3,801 times
  - **1 matches**: 10,790 times
  - **0 matches**: 11,285 times

#### Best Results (5+ matches)
| date                | result                      | predicted               |   correct_num |
|:--------------------|:----------------------------|:------------------------|--------------:|
| 2023-06-27 00:00:00 | [2, 12, 15, 16, 27, 28, 47] | [2, 12, 26, 27, 28, 47] |             5 |

### 🎲 Not Repeat Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Not Repeat Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 10,053,250,000 VND |
| Net profit/loss | 9,788,850,000 VND |
| ROI | 3702.29% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 51 times
  - **3 matches**: 555 times
  - **2 matches**: 3,674 times
  - **1 matches**: 10,823 times
  - **0 matches**: 11,335 times

#### Best Results (5+ matches)
| date                | result                      | predicted               |   correct_num |
|:--------------------|:----------------------------|:------------------------|--------------:|
| 2021-09-18 00:00:00 | [3, 14, 15, 21, 47, 52, 54] | [3, 15, 21, 29, 52, 54] |             5 |
| 2021-09-18 00:00:00 | [3, 14, 15, 21, 47, 52, 54] | [3, 15, 21, 25, 52, 54] |             5 |

### 🎲 Exponential Decay Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Exponential Decay Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 5,053,050,000 VND |
| Net profit/loss | 4,788,650,000 VND |
| ROI | 1811.14% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 49 times
  - **3 matches**: 571 times
  - **2 matches**: 3,826 times
  - **1 matches**: 10,907 times
  - **0 matches**: 11,086 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2022-02-08 00:00:00 | [12, 15, 21, 28, 32, 40, 43] | [12, 15, 21, 23, 28, 32] |             5 |

### 🎲 Pair Frequency Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pair Frequency Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 55 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2017-08-01 00:00:00 |
| End date | 2026-03-21 00:00:00 |
| Total draws | 1,322 |
| Total predictions | 26,440 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 264,400,000 VND |
| Total gain | 10,043,100,000 VND |
| Net profit/loss | 9,778,700,000 VND |
| ROI | 3698.45% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 31 times
  - **3 matches**: 552 times
  - **2 matches**: 3,722 times
  - **1 matches**: 10,869 times
  - **0 matches**: 11,264 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2024-08-10 00:00:00 | [10, 23, 32, 37, 48, 55, 14] | [14, 32, 36, 37, 48, 55] |             5 |
| 2017-12-28 00:00:00 | [7, 18, 26, 29, 31, 35, 34]  | [7, 26, 29, 31, 34, 50]  |             5 |




---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
