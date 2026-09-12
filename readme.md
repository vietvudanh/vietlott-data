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
| Power 655 | 1397 | 2017-08-01 | 2026-09-12 | 1397 | 00001 | 01397 |
| Power 645 | 1364 | 2017-10-25 | 2026-09-11 | 1364 | 00198 | 01561 |
| Power 535 | 405 | 2025-06-29 | 2026-09-12 | 808 | 00001 | 00882 |
| Keno | 673 | 2022-12-04 | 2026-09-12 | 84280 | #0110271 | #0295498 |
| 3D | 1127 | 2019-04-22 | 2026-09-11 | 1127 | 00001 | 01131 |
| 3D Pro | 774 | 2021-09-14 | 2026-09-12 | 774 | 00001 | 00778 |
| Bingo18 | 647 | 2024-12-03 | 2026-09-12 | 90275 | 0083123 | 0186198 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-12 | 01397 | [7, 24, 31, 43, 47, 54, 22] | 2026-09-13T00:01:08.403983 |
| 2026-09-10 | 01396 | [2, 5, 28, 32, 51, 53, 50] | 2026-09-12T12:01:58.169601 |
| 2026-09-08 | 01395 | [8, 11, 14, 23, 25, 54, 17] | 2026-09-09T00:01:06.966495 |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24] | 2026-09-05T07:32:08.579054 |
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10] | 2026-08-28T00:01:17.809418 |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 188 | 1.92 |  | 21 | 175 | 1.79 |  | 41 | 206 | 2.11 |
| 2 | 162 | 1.66 |  | 22 | 207 | 2.12 |  | 42 | 181 | 1.85 |
| 3 | 189 | 1.93 |  | 23 | 188 | 1.92 |  | 43 | 199 | 2.04 |
| 4 | 144 | 1.47 |  | 24 | 179 | 1.83 |  | 44 | 182 | 1.86 |
| 5 | 183 | 1.87 |  | 25 | 160 | 1.64 |  | 45 | 181 | 1.85 |
| 6 | 143 | 1.46 |  | 26 | 166 | 1.7 |  | 46 | 182 | 1.86 |
| 7 | 158 | 1.62 |  | 27 | 162 | 1.66 |  | 47 | 179 | 1.83 |
| 8 | 196 | 2.0 |  | 28 | 159 | 1.63 |  | 48 | 190 | 1.94 |
| 9 | 195 | 1.99 |  | 29 | 191 | 1.95 |  | 49 | 174 | 1.78 |
| 10 | 166 | 1.7 |  | 30 | 162 | 1.66 |  | 50 | 178 | 1.82 |
| 11 | 183 | 1.87 |  | 31 | 188 | 1.92 |  | 51 | 198 | 2.02 |
| 12 | 180 | 1.84 |  | 32 | 187 | 1.91 |  | 52 | 177 | 1.81 |
| 13 | 173 | 1.77 |  | 33 | 180 | 1.84 |  | 53 | 188 | 1.92 |
| 14 | 179 | 1.83 |  | 34 | 196 | 2.0 |  | 54 | 169 | 1.73 |
| 15 | 166 | 1.7 |  | 35 | 170 | 1.74 |  | 55 | 179 | 1.83 |
| 16 | 175 | 1.79 |  | 36 | 167 | 1.71 |  |  |  |  |
| 17 | 161 | 1.65 |  | 37 | 158 | 1.62 |  |  |  |  |
| 18 | 178 | 1.82 |  | 38 | 172 | 1.76 |  |  |  |  |
| 19 | 174 | 1.78 |  | 39 | 172 | 1.76 |  |  |  |  |
| 20 | 189 | 1.93 |  | 40 | 194 | 1.98 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 24 | 3 | 3.3 |  | 46 | 1 | 1.1 |
| 2 | 3 | 3.3 |  | 25 | 3 | 3.3 |  | 47 | 4 | 4.4 |
| 3 | 2 | 2.2 |  | 26 | 1 | 1.1 |  | 48 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 27 | 1 | 1.1 |  | 49 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 28 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 8 | 4 | 4.4 |  | 29 | 2 | 2.2 |  | 51 | 2 | 2.2 |
| 9 | 3 | 3.3 |  | 30 | 2 | 2.2 |  | 53 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 54 | 2 | 2.2 |
| 11 | 4 | 4.4 |  | 32 | 1 | 1.1 |  | 55 | 1 | 1.1 |
| 13 | 1 | 1.1 |  | 33 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 17 | 2 | 2.2 |  | 39 | 1 | 1.1 |  |  |  |  |
| 18 | 3 | 3.3 |  | 40 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 20 | 1 | 1.1 |  | 42 | 1 | 1.1 |  |  |  |  |
| 21 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 44 | 2 | 2.2 |  |  |  |  |
| 23 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 23 | 3 | 1.65 |  | 43 | 2 | 1.1 |
| 2 | 5 | 2.75 |  | 24 | 5 | 2.75 |  | 44 | 4 | 2.2 |
| 3 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 45 | 6 | 3.3 |
| 5 | 6 | 3.3 |  | 26 | 1 | 0.55 |  | 46 | 2 | 1.1 |
| 7 | 4 | 2.2 |  | 27 | 4 | 2.2 |  | 47 | 5 | 2.75 |
| 8 | 6 | 3.3 |  | 28 | 2 | 1.1 |  | 48 | 5 | 2.75 |
| 9 | 5 | 2.75 |  | 29 | 4 | 2.2 |  | 49 | 3 | 1.65 |
| 10 | 2 | 1.1 |  | 30 | 2 | 1.1 |  | 50 | 4 | 2.2 |
| 11 | 6 | 3.3 |  | 31 | 5 | 2.75 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 53 | 2 | 1.1 |
| 13 | 2 | 1.1 |  | 33 | 4 | 2.2 |  | 54 | 4 | 2.2 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 55 | 5 | 2.75 |
| 15 | 2 | 1.1 |  | 35 | 1 | 0.55 |  |  |  |  |
| 16 | 4 | 2.2 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 4 | 2.2 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 3 | 1.65 |  | 40 | 4 | 2.2 |  |  |  |  |
| 21 | 4 | 2.2 |  | 41 | 4 | 2.2 |  |  |  |  |
| 22 | 4 | 2.2 |  | 42 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.56 |  | 21 | 5 | 1.83 |  | 41 | 7 | 2.56 |
| 2 | 7 | 2.56 |  | 22 | 5 | 1.83 |  | 42 | 5 | 1.83 |
| 3 | 4 | 1.47 |  | 23 | 7 | 2.56 |  | 43 | 4 | 1.47 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 6 | 2.2 |
| 5 | 10 | 3.66 |  | 25 | 4 | 1.47 |  | 45 | 8 | 2.93 |
| 6 | 1 | 0.37 |  | 26 | 2 | 0.73 |  | 46 | 5 | 1.83 |
| 7 | 6 | 2.2 |  | 27 | 4 | 1.47 |  | 47 | 6 | 2.2 |
| 8 | 8 | 2.93 |  | 28 | 5 | 1.83 |  | 48 | 5 | 1.83 |
| 9 | 7 | 2.56 |  | 29 | 4 | 1.47 |  | 49 | 6 | 2.2 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 4 | 1.47 |
| 11 | 7 | 2.56 |  | 31 | 7 | 2.56 |  | 51 | 5 | 1.83 |
| 12 | 1 | 0.37 |  | 32 | 3 | 1.1 |  | 52 | 2 | 0.73 |
| 13 | 5 | 1.83 |  | 33 | 7 | 2.56 |  | 53 | 3 | 1.1 |
| 14 | 8 | 2.93 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 6 | 2.2 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 2 | 0.73 |  |  |  |  |
| 18 | 6 | 2.2 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 7 | 2.56 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-06-27 | 77 |
| 6 | 2026-07-07 | 67 |
| 4 | 2026-07-07 | 67 |
| 12 | 2026-07-30 | 44 |
| 35 | 2026-08-06 | 37 |
| 37 | 2026-08-08 | 35 |
| 27 | 2026-08-15 | 28 |
| 20 | 2026-08-15 | 28 |
| 30 | 2026-08-18 | 25 |
| 48 | 2026-08-18 | 25 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-01 | 11 |
| 2 | 2026-09-10 | 2 |
| 3 | 2026-08-27 | 16 |
| 4 | 2026-07-07 | 67 |
| 5 | 2026-09-10 | 2 |
| 6 | 2026-07-07 | 67 |
| 7 | 2026-09-12 | 0 |
| 8 | 2026-09-08 | 4 |
| 9 | 2026-09-05 | 7 |
| 10 | 2026-08-29 | 14 |
| 11 | 2026-09-08 | 4 |
| 12 | 2026-07-30 | 44 |
| 13 | 2026-08-25 | 18 |
| 14 | 2026-09-08 | 4 |
| 15 | 2026-08-29 | 14 |
| 16 | 2026-09-03 | 9 |
| 17 | 2026-09-08 | 4 |
| 18 | 2026-08-25 | 18 |
| 19 | 2026-08-22 | 21 |
| 20 | 2026-08-15 | 28 |
| 21 | 2026-09-05 | 7 |
| 22 | 2026-09-12 | 0 |
| 23 | 2026-09-08 | 4 |
| 24 | 2026-09-12 | 0 |
| 25 | 2026-09-08 | 4 |
| 26 | 2026-08-27 | 16 |
| 27 | 2026-08-15 | 28 |
| 28 | 2026-09-10 | 2 |
| 29 | 2026-08-29 | 14 |
| 30 | 2026-08-18 | 25 |
| 31 | 2026-09-12 | 0 |
| 32 | 2026-09-10 | 2 |
| 33 | 2026-09-05 | 7 |
| 34 | 2026-08-29 | 14 |
| 35 | 2026-08-06 | 37 |
| 36 | 2026-08-22 | 21 |
| 37 | 2026-08-08 | 35 |
| 38 | 2026-08-20 | 23 |
| 39 | 2026-08-20 | 23 |
| 40 | 2026-08-25 | 18 |
| 41 | 2026-09-01 | 11 |
| 42 | 2026-09-03 | 9 |
| 43 | 2026-09-12 | 0 |
| 44 | 2026-09-01 | 11 |
| 45 | 2026-09-01 | 11 |
| 46 | 2026-09-03 | 9 |
| 47 | 2026-09-12 | 0 |
| 48 | 2026-08-18 | 25 |
| 49 | 2026-09-01 | 11 |
| 50 | 2026-09-10 | 2 |
| 51 | 2026-09-10 | 2 |
| 52 | 2026-06-27 | 77 |
| 53 | 2026-09-10 | 2 |
| 54 | 2026-09-12 | 0 |
| 55 | 2026-09-01 | 11 |



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

