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
| Power 655 | 1400 | 2017-08-01 | 2026-09-19 | 1400 | 00001 | 01400 |
| Power 645 | 1368 | 2017-10-25 | 2026-09-20 | 1368 | 00198 | 01565 |
| Power 535 | 414 | 2025-06-29 | 2026-09-21 | 826 | 00001 | 00900 |
| Keno | 683 | 2022-12-04 | 2026-09-21 | 85514 | #0110271 | #0296569 |
| 3D | 1131 | 2019-04-22 | 2026-09-21 | 1131 | 00001 | 01135 |
| 3D Pro | 777 | 2021-09-14 | 2026-09-19 | 777 | 00001 | 00781 |
| Bingo18 | 656 | 2024-12-03 | 2026-09-21 | 91706 | 0083123 | 0187629 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-19 | 01400 | [4, 7, 11, 18, 22, 25, 50] | 2026-09-20T00:01:07.511406 |
| 2026-09-17 | 01399 | [6, 11, 25, 27, 37, 45, 15] | 2026-09-18T00:01:15.250052 |
| 2026-09-15 | 01398 | [24, 27, 32, 36, 38, 47, 52] | 2026-09-16T00:01:46.289586 |
| 2026-09-12 | 01397 | [7, 24, 31, 43, 47, 54, 22] | 2026-09-13T00:01:08.403983 |
| 2026-09-10 | 01396 | [2, 5, 28, 32, 51, 53, 50] | 2026-09-12T12:01:58.169601 |
| 2026-09-08 | 01395 | [8, 11, 14, 23, 25, 54, 17] | 2026-09-09T00:01:06.966495 |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24] | 2026-09-05T07:32:08.579054 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 188 | 1.92 |  | 21 | 175 | 1.79 |  | 41 | 206 | 2.1 |
| 2 | 162 | 1.65 |  | 22 | 208 | 2.12 |  | 42 | 181 | 1.85 |
| 3 | 189 | 1.93 |  | 23 | 188 | 1.92 |  | 43 | 199 | 2.03 |
| 4 | 145 | 1.48 |  | 24 | 180 | 1.84 |  | 44 | 182 | 1.86 |
| 5 | 183 | 1.87 |  | 25 | 162 | 1.65 |  | 45 | 182 | 1.86 |
| 6 | 144 | 1.47 |  | 26 | 166 | 1.69 |  | 46 | 182 | 1.86 |
| 7 | 159 | 1.62 |  | 27 | 164 | 1.67 |  | 47 | 180 | 1.84 |
| 8 | 196 | 2.0 |  | 28 | 159 | 1.62 |  | 48 | 190 | 1.94 |
| 9 | 195 | 1.99 |  | 29 | 191 | 1.95 |  | 49 | 174 | 1.78 |
| 10 | 166 | 1.69 |  | 30 | 162 | 1.65 |  | 50 | 179 | 1.83 |
| 11 | 185 | 1.89 |  | 31 | 188 | 1.92 |  | 51 | 198 | 2.02 |
| 12 | 180 | 1.84 |  | 32 | 188 | 1.92 |  | 52 | 178 | 1.82 |
| 13 | 173 | 1.77 |  | 33 | 180 | 1.84 |  | 53 | 188 | 1.92 |
| 14 | 179 | 1.83 |  | 34 | 196 | 2.0 |  | 54 | 169 | 1.72 |
| 15 | 167 | 1.7 |  | 35 | 170 | 1.73 |  | 55 | 179 | 1.83 |
| 16 | 175 | 1.79 |  | 36 | 168 | 1.71 |  |  |  |  |
| 17 | 161 | 1.64 |  | 37 | 159 | 1.62 |  |  |  |  |
| 18 | 179 | 1.83 |  | 38 | 173 | 1.77 |  |  |  |  |
| 19 | 174 | 1.78 |  | 39 | 172 | 1.76 |  |  |  |  |
| 20 | 189 | 1.93 |  | 40 | 194 | 1.98 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 24 | 4 | 4.76 |  | 47 | 4 | 4.76 |
| 2 | 1 | 1.19 |  | 25 | 3 | 3.57 |  | 49 | 1 | 1.19 |
| 3 | 1 | 1.19 |  | 26 | 1 | 1.19 |  | 50 | 2 | 2.38 |
| 4 | 1 | 1.19 |  | 27 | 2 | 2.38 |  | 51 | 1 | 1.19 |
| 5 | 3 | 3.57 |  | 28 | 1 | 1.19 |  | 52 | 1 | 1.19 |
| 6 | 1 | 1.19 |  | 29 | 1 | 1.19 |  | 53 | 1 | 1.19 |
| 7 | 3 | 3.57 |  | 31 | 3 | 3.57 |  | 54 | 2 | 2.38 |
| 8 | 2 | 2.38 |  | 32 | 2 | 2.38 |  | 55 | 1 | 1.19 |
| 9 | 2 | 2.38 |  | 33 | 1 | 1.19 |  |  |  |  |
| 10 | 2 | 2.38 |  | 34 | 1 | 1.19 |  |  |  |  |
| 11 | 6 | 7.14 |  | 36 | 1 | 1.19 |  |  |  |  |
| 13 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 14 | 2 | 2.38 |  | 38 | 1 | 1.19 |  |  |  |  |
| 15 | 2 | 2.38 |  | 40 | 1 | 1.19 |  |  |  |  |
| 16 | 1 | 1.19 |  | 41 | 1 | 1.19 |  |  |  |  |
| 17 | 2 | 2.38 |  | 42 | 1 | 1.19 |  |  |  |  |
| 18 | 2 | 2.38 |  | 43 | 1 | 1.19 |  |  |  |  |
| 21 | 2 | 2.38 |  | 44 | 2 | 2.38 |  |  |  |  |
| 22 | 2 | 2.38 |  | 45 | 3 | 3.57 |  |  |  |  |
| 23 | 1 | 1.19 |  | 46 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.71 |  | 21 | 3 | 1.71 |  | 41 | 3 | 1.71 |
| 2 | 5 | 2.86 |  | 22 | 3 | 1.71 |  | 42 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 23 | 3 | 1.71 |  | 43 | 2 | 1.14 |
| 4 | 1 | 0.57 |  | 24 | 5 | 2.86 |  | 44 | 4 | 2.29 |
| 5 | 6 | 3.43 |  | 25 | 5 | 2.86 |  | 45 | 5 | 2.86 |
| 6 | 1 | 0.57 |  | 26 | 1 | 0.57 |  | 46 | 2 | 1.14 |
| 7 | 5 | 2.86 |  | 27 | 6 | 3.43 |  | 47 | 6 | 3.43 |
| 8 | 4 | 2.29 |  | 28 | 2 | 1.14 |  | 48 | 3 | 1.71 |
| 9 | 5 | 2.86 |  | 29 | 4 | 2.29 |  | 49 | 3 | 1.71 |
| 10 | 2 | 1.14 |  | 30 | 2 | 1.14 |  | 50 | 5 | 2.86 |
| 11 | 7 | 4.0 |  | 31 | 5 | 2.86 |  | 51 | 4 | 2.29 |
| 12 | 1 | 0.57 |  | 32 | 2 | 1.14 |  | 52 | 1 | 0.57 |
| 13 | 1 | 0.57 |  | 33 | 3 | 1.71 |  | 53 | 1 | 0.57 |
| 14 | 5 | 2.86 |  | 34 | 1 | 0.57 |  | 54 | 3 | 1.71 |
| 15 | 3 | 1.71 |  | 35 | 1 | 0.57 |  | 55 | 3 | 1.71 |
| 16 | 3 | 1.71 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 2 | 1.14 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 5 | 2.86 |  | 38 | 4 | 2.29 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 4 | 2.29 |  |  |  |  |
| 20 | 2 | 1.14 |  | 40 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 1.88 |  | 21 | 5 | 1.88 |  | 41 | 7 | 2.63 |
| 2 | 6 | 2.26 |  | 22 | 6 | 2.26 |  | 42 | 5 | 1.88 |
| 3 | 4 | 1.5 |  | 23 | 6 | 2.26 |  | 43 | 4 | 1.5 |
| 4 | 2 | 0.75 |  | 24 | 7 | 2.63 |  | 44 | 6 | 2.26 |
| 5 | 8 | 3.01 |  | 25 | 6 | 2.26 |  | 45 | 9 | 3.38 |
| 6 | 2 | 0.75 |  | 26 | 1 | 0.38 |  | 46 | 2 | 0.75 |
| 7 | 6 | 2.26 |  | 27 | 6 | 2.26 |  | 47 | 7 | 2.63 |
| 8 | 8 | 3.01 |  | 28 | 4 | 1.5 |  | 48 | 5 | 1.88 |
| 9 | 7 | 2.63 |  | 29 | 4 | 1.5 |  | 49 | 5 | 1.88 |
| 10 | 4 | 1.5 |  | 30 | 3 | 1.13 |  | 50 | 5 | 1.88 |
| 11 | 9 | 3.38 |  | 31 | 6 | 2.26 |  | 51 | 5 | 1.88 |
| 12 | 1 | 0.38 |  | 32 | 4 | 1.5 |  | 52 | 2 | 0.75 |
| 13 | 4 | 1.5 |  | 33 | 7 | 2.63 |  | 53 | 2 | 0.75 |
| 14 | 6 | 2.26 |  | 34 | 2 | 0.75 |  | 54 | 5 | 1.88 |
| 15 | 5 | 1.88 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 5 | 1.88 |  | 36 | 3 | 1.13 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 7 | 2.63 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 5 | 1.88 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 5 | 1.88 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-07-30 | 51 |
| 35 | 2026-08-06 | 44 |
| 20 | 2026-08-15 | 35 |
| 30 | 2026-08-18 | 32 |
| 48 | 2026-08-18 | 32 |
| 39 | 2026-08-20 | 30 |
| 19 | 2026-08-22 | 28 |
| 13 | 2026-08-25 | 25 |
| 40 | 2026-08-25 | 25 |
| 3 | 2026-08-27 | 23 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-01 | 18 |
| 2 | 2026-09-10 | 9 |
| 3 | 2026-08-27 | 23 |
| 4 | 2026-09-19 | 0 |
| 5 | 2026-09-10 | 9 |
| 6 | 2026-09-17 | 2 |
| 7 | 2026-09-19 | 0 |
| 8 | 2026-09-08 | 11 |
| 9 | 2026-09-05 | 14 |
| 10 | 2026-08-29 | 21 |
| 11 | 2026-09-19 | 0 |
| 12 | 2026-07-30 | 51 |
| 13 | 2026-08-25 | 25 |
| 14 | 2026-09-08 | 11 |
| 15 | 2026-09-17 | 2 |
| 16 | 2026-09-03 | 16 |
| 17 | 2026-09-08 | 11 |
| 18 | 2026-09-19 | 0 |
| 19 | 2026-08-22 | 28 |
| 20 | 2026-08-15 | 35 |
| 21 | 2026-09-05 | 14 |
| 22 | 2026-09-19 | 0 |
| 23 | 2026-09-08 | 11 |
| 24 | 2026-09-15 | 4 |
| 25 | 2026-09-19 | 0 |
| 26 | 2026-08-27 | 23 |
| 27 | 2026-09-17 | 2 |
| 28 | 2026-09-10 | 9 |
| 29 | 2026-08-29 | 21 |
| 30 | 2026-08-18 | 32 |
| 31 | 2026-09-12 | 7 |
| 32 | 2026-09-15 | 4 |
| 33 | 2026-09-05 | 14 |
| 34 | 2026-08-29 | 21 |
| 35 | 2026-08-06 | 44 |
| 36 | 2026-09-15 | 4 |
| 37 | 2026-09-17 | 2 |
| 38 | 2026-09-15 | 4 |
| 39 | 2026-08-20 | 30 |
| 40 | 2026-08-25 | 25 |
| 41 | 2026-09-01 | 18 |
| 42 | 2026-09-03 | 16 |
| 43 | 2026-09-12 | 7 |
| 44 | 2026-09-01 | 18 |
| 45 | 2026-09-17 | 2 |
| 46 | 2026-09-03 | 16 |
| 47 | 2026-09-15 | 4 |
| 48 | 2026-08-18 | 32 |
| 49 | 2026-09-01 | 18 |
| 50 | 2026-09-19 | 0 |
| 51 | 2026-09-10 | 9 |
| 52 | 2026-09-15 | 4 |
| 53 | 2026-09-10 | 9 |
| 54 | 2026-09-12 | 7 |
| 55 | 2026-09-01 | 18 |



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

