# 🔮 Vietlott Power 655 Prediction Summary

> **Generated**: 2026-03-04 23:18:49
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

## 📊 Strategy Performance Comparison

> Sorted by ROI (best → worst).  All strategies backtested with **20 tickets/draw**.
> Note: All ROIs are deeply negative — lottery odds make profit impossible at scale.
> The comparison shows *which strategy loses the least*, not which one is profitable.

| Rank | Strategy | Total Cost (VND) | Total Gain (VND) | Net Profit (VND) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Hot Numbers Strategy | 262,800,000 | 10,046,450,000 | 9,783,650,000 | 3722.85% |
| 🥈 2 | Exponential Decay Strategy | 262,800,000 | 10,044,800,000 | 9,782,000,000 | 3722.22% |
| 🥉 3 | Pair Frequency Strategy | 262,800,000 | 10,042,000,000 | 9,779,200,000 | 3721.16% |
|    4 | Not Repeat Strategy | 262,800,000 | 5,047,500,000 | 4,784,700,000 | 1820.66% |
|    5 | Cold Numbers Strategy | 262,800,000 | 5,047,100,000 | 4,784,300,000 | 1820.51% |
|    6 | Random Strategy | 262,800,000 | 5,045,550,000 | 4,782,750,000 | 1819.92% |
|    7 | Pattern Strategy | 262,800,000 | 48,150,000 | -214,650,000 | -81.68% |
|    8 | Long Absence Strategy | 262,800,000 | 44,100,000 | -218,700,000 | -83.22% |


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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 5,045,550,000 VND |
| Net profit/loss | 4,782,750,000 VND |
| ROI | 1819.92% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 36 times
  - **3 matches**: 551 times
  - **2 matches**: 3,670 times
  - **1 matches**: 10,883 times
  - **0 matches**: 11,139 times

#### Best Results (5+ matches)
| date                | result                     | predicted              |   correct_num |
|:--------------------|:---------------------------|:-----------------------|--------------:|
| 2017-08-05 00:00:00 | [1, 5, 11, 32, 40, 45, 43] | [1, 32, 29, 5, 11, 45] |             5 |

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 44,100,000 VND |
| Net profit/loss | -218,700,000 VND |
| ROI | -83.22% |

#### Match Distribution
  - **4 matches**: 30 times
  - **3 matches**: 582 times
  - **2 matches**: 3,709 times
  - **1 matches**: 10,656 times
  - **0 matches**: 11,303 times

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 48,150,000 VND |
| Net profit/loss | -214,650,000 VND |
| ROI | -81.68% |

#### Match Distribution
  - **4 matches**: 40 times
  - **3 matches**: 563 times
  - **2 matches**: 3,711 times
  - **1 matches**: 10,869 times
  - **0 matches**: 11,097 times

#### Best Results (5+ matches)
No results with 5+ matches found.

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 10,046,450,000 VND |
| Net profit/loss | 9,783,650,000 VND |
| ROI | 3722.85% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 36 times
  - **3 matches**: 569 times
  - **2 matches**: 3,722 times
  - **1 matches**: 10,830 times
  - **0 matches**: 11,121 times

#### Best Results (5+ matches)
| date                | result                      | predicted                |   correct_num |
|:--------------------|:----------------------------|:-------------------------|--------------:|
| 2019-08-13 00:00:00 | [4, 8, 16, 27, 32, 40, 23]  | [4, 8, 16, 18, 23, 40]   |             5 |
| 2017-12-16 00:00:00 | [5, 23, 37, 41, 43, 53, 25] | [13, 25, 37, 41, 43, 53] |             5 |

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 5,047,100,000 VND |
| Net profit/loss | 4,784,300,000 VND |
| ROI | 1820.51% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 36 times
  - **3 matches**: 582 times
  - **2 matches**: 3,722 times
  - **1 matches**: 10,886 times
  - **0 matches**: 11,053 times

#### Best Results (5+ matches)
| date                | result                      | predicted                |   correct_num |
|:--------------------|:----------------------------|:-------------------------|--------------:|
| 2017-11-30 00:00:00 | [5, 13, 26, 37, 53, 55, 28] | [13, 26, 37, 49, 53, 55] |             5 |

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 5,047,500,000 VND |
| Net profit/loss | 4,784,700,000 VND |
| ROI | 1820.66% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 42 times
  - **3 matches**: 530 times
  - **2 matches**: 3,679 times
  - **1 matches**: 10,852 times
  - **0 matches**: 11,176 times

#### Best Results (5+ matches)
| date                | result                    | predicted              |   correct_num |
|:--------------------|:--------------------------|:-----------------------|--------------:|
| 2021-01-05 00:00:00 | [5, 7, 9, 22, 42, 54, 47] | [5, 9, 22, 39, 42, 47] |             5 |

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 10,044,800,000 VND |
| Net profit/loss | 9,782,000,000 VND |
| ROI | 3722.22% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 36 times
  - **3 matches**: 536 times
  - **2 matches**: 3,709 times
  - **1 matches**: 10,821 times
  - **0 matches**: 11,176 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2023-12-26 00:00:00 | [10, 14, 17, 27, 29, 40, 25] | [14, 17, 25, 29, 40, 44] |             5 |
| 2018-10-16 00:00:00 | [5, 28, 29, 34, 42, 46, 17]  | [12, 17, 28, 29, 42, 46] |             5 |

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
| End date | 2026-03-03 00:00:00 |
| Total draws | 1,314 |
| Total predictions | 26,280 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 262,800,000 VND |
| Total gain | 10,042,000,000 VND |
| Net profit/loss | 9,779,200,000 VND |
| ROI | 3721.16% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 29 times
  - **3 matches**: 550 times
  - **2 matches**: 3,596 times
  - **1 matches**: 10,872 times
  - **0 matches**: 11,231 times

#### Best Results (5+ matches)
| date                | result                       | predicted                |   correct_num |
|:--------------------|:-----------------------------|:-------------------------|--------------:|
| 2022-09-15 00:00:00 | [3, 8, 19, 30, 41, 52, 9]    | [3, 8, 9, 19, 35, 41]    |             5 |
| 2019-09-14 00:00:00 | [10, 36, 42, 44, 45, 54, 14] | [10, 14, 38, 42, 44, 54] |             5 |




---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
