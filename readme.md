# Vietlott Data

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing statistics and insights for all major lottery products.

## Links

- [Website](https://vietvudanh.github.io/vietlott-data/) - Interactive data visualization
- [Blog Post](https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the) - About this project

## Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Power 5/35** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535) | Choose 5 numbers from 1-35 |
| **Keno** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |
| **Bingo18** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game |


## Table of Contents

- [Links](#links)
- [Supported Lottery Products](#supported-lottery-products)
- [Predictions](#predictions)
- [Data Statistics](#data-statistics)
- [Power 6/55 Analysis](#power-655-analysis)
  - [Recent Results](#recent-results-last-10-draws)
  - [Number Frequency (All Time)](#number-frequency-all-time)
  - [Frequency Analysis by Period](#frequency-analysis-by-period)
  - [Top 10 Numbers by Days Since Last Appearance](#top-10-numbers-by-days-since-last-appearance)
  - [Days Since Last Appearance - All Numbers](#days-since-last-appearance---all-numbers)
- [How It Works](#how-it-works)
- [Installation & Usage](#installation--usage)
- [License](#license)


## Predictions

Prediction models are at [/src/machine_learning](./src/machine_learning/).

For background on these models, see the [Machine Learning README](./src/machine_learning/).

## Data Statistics

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 1395 | 2017-08-01 | 2026-09-08 | 1395 | 00001 | 01395 |
| Power 645 | 1362 | 2017-10-25 | 2026-09-06 | 1362 | 00198 | 01559 |
| Power 535 | 401 | 2025-06-29 | 2026-09-08 | 800 | 00001 | 00874 |
| Keno | 670 | 2022-12-04 | 2026-09-08 | 84011 | #0110271 | #0295022 |
| 3D | 1125 | 2019-04-22 | 2026-09-07 | 1125 | 00001 | 01129 |
| 3D Pro | 772 | 2021-09-14 | 2026-09-08 | 772 | 00001 | 00776 |
| Bingo18 | 643 | 2024-12-03 | 2026-09-08 | 89639 | 0083123 | 0185562 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-08 | 01395 | [8, 11, 14, 23, 25, 54, 17] | 2026-09-09T00:01:06.966495 |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24] | 2026-09-05T07:32:08.579054 |
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10] | 2026-08-28T00:01:17.809418 |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 188 | 1.93 |  | 21 | 175 | 1.79 |  | 41 | 206 | 2.11 |
| 2 | 161 | 1.65 |  | 22 | 206 | 2.11 |  | 42 | 181 | 1.85 |
| 3 | 189 | 1.94 |  | 23 | 188 | 1.93 |  | 43 | 198 | 2.03 |
| 4 | 144 | 1.47 |  | 24 | 178 | 1.82 |  | 44 | 182 | 1.86 |
| 5 | 182 | 1.86 |  | 25 | 160 | 1.64 |  | 45 | 181 | 1.85 |
| 6 | 143 | 1.46 |  | 26 | 166 | 1.7 |  | 46 | 182 | 1.86 |
| 7 | 157 | 1.61 |  | 27 | 162 | 1.66 |  | 47 | 178 | 1.82 |
| 8 | 196 | 2.01 |  | 28 | 158 | 1.62 |  | 48 | 190 | 1.95 |
| 9 | 195 | 2.0 |  | 29 | 191 | 1.96 |  | 49 | 174 | 1.78 |
| 10 | 166 | 1.7 |  | 30 | 162 | 1.66 |  | 50 | 177 | 1.81 |
| 11 | 183 | 1.87 |  | 31 | 187 | 1.92 |  | 51 | 197 | 2.02 |
| 12 | 180 | 1.84 |  | 32 | 186 | 1.9 |  | 52 | 177 | 1.81 |
| 13 | 173 | 1.77 |  | 33 | 180 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 179 | 1.83 |  | 34 | 196 | 2.01 |  | 54 | 168 | 1.72 |
| 15 | 166 | 1.7 |  | 35 | 170 | 1.74 |  | 55 | 179 | 1.83 |
| 16 | 175 | 1.79 |  | 36 | 167 | 1.71 |  |  |  |  |
| 17 | 161 | 1.65 |  | 37 | 158 | 1.62 |  |  |  |  |
| 18 | 178 | 1.82 |  | 38 | 172 | 1.76 |  |  |  |  |
| 19 | 174 | 1.78 |  | 39 | 172 | 1.76 |  |  |  |  |
| 20 | 189 | 1.94 |  | 40 | 194 | 1.99 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 25 | 3 | 3.3 |  | 50 | 2 | 2.2 |
| 2 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 27 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 29 | 3 | 3.3 |  | 55 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 30 | 2 | 2.2 |  |  |  |  |
| 8 | 4 | 4.4 |  | 31 | 3 | 3.3 |  |  |  |  |
| 9 | 4 | 4.4 |  | 33 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 4 | 4.4 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 38 | 2 | 2.2 |  |  |  |  |
| 14 | 2 | 2.2 |  | 39 | 2 | 2.2 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 18 | 3 | 3.3 |  | 44 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |
| 20 | 2 | 2.2 |  | 46 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 47 | 3 | 3.3 |  |  |  |  |
| 23 | 1 | 1.1 |  | 48 | 1 | 1.1 |  |  |  |  |
| 24 | 2 | 2.2 |  | 49 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 23 | 3 | 1.65 |  | 43 | 1 | 0.55 |
| 2 | 4 | 2.2 |  | 24 | 5 | 2.75 |  | 44 | 4 | 2.2 |
| 3 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 45 | 7 | 3.85 |
| 5 | 5 | 2.75 |  | 26 | 1 | 0.55 |  | 46 | 2 | 1.1 |
| 7 | 3 | 1.65 |  | 27 | 4 | 2.2 |  | 47 | 4 | 2.2 |
| 8 | 6 | 3.3 |  | 28 | 1 | 0.55 |  | 48 | 5 | 2.75 |
| 9 | 6 | 3.3 |  | 29 | 4 | 2.2 |  | 49 | 3 | 1.65 |
| 10 | 3 | 1.65 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 11 | 6 | 3.3 |  | 31 | 4 | 2.2 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 1 | 0.55 |  | 53 | 1 | 0.55 |
| 13 | 2 | 1.1 |  | 33 | 6 | 3.3 |  | 54 | 3 | 1.65 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 55 | 5 | 2.75 |
| 15 | 2 | 1.1 |  | 35 | 2 | 1.1 |  |  |  |  |
| 16 | 4 | 2.2 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 4 | 2.2 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 5 | 2.75 |  |  |  |  |
| 21 | 4 | 2.2 |  | 41 | 5 | 2.75 |  |  |  |  |
| 22 | 3 | 1.65 |  | 42 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 5 | 1.83 |  | 41 | 7 | 2.56 |
| 2 | 7 | 2.56 |  | 22 | 4 | 1.47 |  | 42 | 6 | 2.2 |
| 3 | 4 | 1.47 |  | 23 | 7 | 2.56 |  | 43 | 3 | 1.1 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 6 | 2.2 |
| 5 | 9 | 3.3 |  | 25 | 4 | 1.47 |  | 45 | 8 | 2.93 |
| 6 | 1 | 0.37 |  | 26 | 2 | 0.73 |  | 46 | 6 | 2.2 |
| 7 | 5 | 1.83 |  | 27 | 4 | 1.47 |  | 47 | 6 | 2.2 |
| 8 | 10 | 3.66 |  | 28 | 4 | 1.47 |  | 48 | 6 | 2.2 |
| 9 | 7 | 2.56 |  | 29 | 4 | 1.47 |  | 49 | 6 | 2.2 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 3 | 1.1 |
| 11 | 7 | 2.56 |  | 31 | 6 | 2.2 |  | 51 | 4 | 1.47 |
| 12 | 1 | 0.37 |  | 32 | 2 | 0.73 |  | 52 | 2 | 0.73 |
| 13 | 5 | 1.83 |  | 33 | 8 | 2.93 |  | 53 | 2 | 0.73 |
| 14 | 8 | 2.93 |  | 34 | 2 | 0.73 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 6 | 2.2 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 2 | 0.73 |  |  |  |  |
| 18 | 6 | 2.2 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 8 | 2.93 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-06-27 | 73 |
| 6 | 2026-07-07 | 63 |
| 4 | 2026-07-07 | 63 |
| 53 | 2026-07-16 | 54 |
| 32 | 2026-07-21 | 49 |
| 22 | 2026-07-28 | 42 |
| 12 | 2026-07-30 | 40 |
| 28 | 2026-07-30 | 40 |
| 43 | 2026-07-30 | 40 |
| 35 | 2026-08-06 | 33 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-01 | 7 |
| 2 | 2026-08-20 | 19 |
| 3 | 2026-08-27 | 12 |
| 4 | 2026-07-07 | 63 |
| 5 | 2026-08-29 | 10 |
| 6 | 2026-07-07 | 63 |
| 7 | 2026-08-25 | 14 |
| 8 | 2026-09-08 | 0 |
| 9 | 2026-09-05 | 3 |
| 10 | 2026-08-29 | 10 |
| 11 | 2026-09-08 | 0 |
| 12 | 2026-07-30 | 40 |
| 13 | 2026-08-25 | 14 |
| 14 | 2026-09-08 | 0 |
| 15 | 2026-08-29 | 10 |
| 16 | 2026-09-03 | 5 |
| 17 | 2026-09-08 | 0 |
| 18 | 2026-08-25 | 14 |
| 19 | 2026-08-22 | 17 |
| 20 | 2026-08-15 | 24 |
| 21 | 2026-09-05 | 3 |
| 22 | 2026-07-28 | 42 |
| 23 | 2026-09-08 | 0 |
| 24 | 2026-09-05 | 3 |
| 25 | 2026-09-08 | 0 |
| 26 | 2026-08-27 | 12 |
| 27 | 2026-08-15 | 24 |
| 28 | 2026-07-30 | 40 |
| 29 | 2026-08-29 | 10 |
| 30 | 2026-08-18 | 21 |
| 31 | 2026-09-05 | 3 |
| 32 | 2026-07-21 | 49 |
| 33 | 2026-09-05 | 3 |
| 34 | 2026-08-29 | 10 |
| 35 | 2026-08-06 | 33 |
| 36 | 2026-08-22 | 17 |
| 37 | 2026-08-08 | 31 |
| 38 | 2026-08-20 | 19 |
| 39 | 2026-08-20 | 19 |
| 40 | 2026-08-25 | 14 |
| 41 | 2026-09-01 | 7 |
| 42 | 2026-09-03 | 5 |
| 43 | 2026-07-30 | 40 |
| 44 | 2026-09-01 | 7 |
| 45 | 2026-09-01 | 7 |
| 46 | 2026-09-03 | 5 |
| 47 | 2026-09-05 | 3 |
| 48 | 2026-08-18 | 21 |
| 49 | 2026-09-01 | 7 |
| 50 | 2026-08-15 | 24 |
| 51 | 2026-08-20 | 19 |
| 52 | 2026-06-27 | 73 |
| 53 | 2026-07-16 | 54 |
| 54 | 2026-09-08 | 0 |
| 55 | 2026-09-01 | 7 |



## How It Works

Vietlott blocks non-Vietnam IPs ([issue #13](https://github.com/vietvudanh/vietlott-data/issues/13)), so crawling runs on a scheduled local runner (`bin/github_data.sh`) and commits updated data back to GitHub.

For architecture and runner setup, see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).


## Installation & Usage

### CLI Usage (using uv)

```bash
# Crawl latest data
uv run vietlott-crawl keno

# Backfill missing data
uv run vietlott-missing power_655

# Available products: power_655, power_645, power_535, keno, 3d, 3d_pro, bingo18
```

### Development Setup

```bash
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data
uv sync --dev
uv run pytest
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE).

---

<div align="center">
  <strong>If you find this project useful, please consider giving it a star!</strong>
</div>

