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
| Power 655 | 1394 | 2017-08-01 | 2026-09-05 | 1394 | 00001 | 01394 |
| Power 645 | 1361 | 2017-10-25 | 2026-09-04 | 1361 | 00198 | 01558 |
| Power 535 | 398 | 2025-06-29 | 2026-09-05 | 794 | 00001 | 00868 |
| Keno | 668 | 2022-12-04 | 2026-09-06 | 83698 | #0110271 | #0294709 |
| 3D | 1124 | 2019-04-22 | 2026-09-04 | 1124 | 00001 | 01128 |
| 3D Pro | 771 | 2021-09-14 | 2026-09-05 | 771 | 00001 | 00775 |
| Bingo18 | 641 | 2024-12-03 | 2026-09-06 | 89261 | 0083123 | 0185145 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24] | 2026-09-05T07:32:08.579054 |
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10] | 2026-08-28T00:01:17.809418 |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 188 | 1.93 |  | 21 | 175 | 1.79 |  | 41 | 206 | 2.11 |
| 2 | 161 | 1.65 |  | 22 | 206 | 2.11 |  | 42 | 181 | 1.86 |
| 3 | 189 | 1.94 |  | 23 | 187 | 1.92 |  | 43 | 198 | 2.03 |
| 4 | 144 | 1.48 |  | 24 | 178 | 1.82 |  | 44 | 182 | 1.87 |
| 5 | 182 | 1.87 |  | 25 | 159 | 1.63 |  | 45 | 181 | 1.86 |
| 6 | 143 | 1.47 |  | 26 | 166 | 1.7 |  | 46 | 182 | 1.87 |
| 7 | 157 | 1.61 |  | 27 | 162 | 1.66 |  | 47 | 178 | 1.82 |
| 8 | 195 | 2.0 |  | 28 | 158 | 1.62 |  | 48 | 190 | 1.95 |
| 9 | 195 | 2.0 |  | 29 | 191 | 1.96 |  | 49 | 174 | 1.78 |
| 10 | 166 | 1.7 |  | 30 | 162 | 1.66 |  | 50 | 177 | 1.81 |
| 11 | 182 | 1.87 |  | 31 | 187 | 1.92 |  | 51 | 197 | 2.02 |
| 12 | 180 | 1.84 |  | 32 | 186 | 1.91 |  | 52 | 177 | 1.81 |
| 13 | 173 | 1.77 |  | 33 | 180 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 178 | 1.82 |  | 34 | 196 | 2.01 |  | 54 | 167 | 1.71 |
| 15 | 166 | 1.7 |  | 35 | 170 | 1.74 |  | 55 | 179 | 1.83 |
| 16 | 175 | 1.79 |  | 36 | 167 | 1.71 |  |  |  |  |
| 17 | 160 | 1.64 |  | 37 | 158 | 1.62 |  |  |  |  |
| 18 | 178 | 1.82 |  | 38 | 172 | 1.76 |  |  |  |  |
| 19 | 174 | 1.78 |  | 39 | 172 | 1.76 |  |  |  |  |
| 20 | 189 | 1.94 |  | 40 | 194 | 1.99 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 26 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 2 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 29 | 4 | 4.4 |  | 55 | 1 | 1.1 |
| 5 | 4 | 4.4 |  | 30 | 2 | 2.2 |  |  |  |  |
| 7 | 2 | 2.2 |  | 31 | 3 | 3.3 |  |  |  |  |
| 8 | 3 | 3.3 |  | 33 | 2 | 2.2 |  |  |  |  |
| 9 | 4 | 4.4 |  | 34 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 11 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 38 | 3 | 3.3 |  |  |  |  |
| 14 | 1 | 1.1 |  | 39 | 2 | 2.2 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 18 | 3 | 3.3 |  | 44 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 45 | 4 | 4.4 |  |  |  |  |
| 20 | 2 | 2.2 |  | 46 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 47 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 48 | 1 | 1.1 |  |  |  |  |
| 25 | 2 | 2.2 |  | 49 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 23 | 2 | 1.1 |  | 43 | 1 | 0.55 |
| 2 | 5 | 2.75 |  | 24 | 5 | 2.75 |  | 44 | 4 | 2.2 |
| 3 | 3 | 1.65 |  | 25 | 2 | 1.1 |  | 45 | 8 | 4.4 |
| 5 | 5 | 2.75 |  | 26 | 1 | 0.55 |  | 46 | 2 | 1.1 |
| 7 | 3 | 1.65 |  | 27 | 4 | 2.2 |  | 47 | 4 | 2.2 |
| 8 | 5 | 2.75 |  | 28 | 1 | 0.55 |  | 48 | 5 | 2.75 |
| 9 | 7 | 3.85 |  | 29 | 4 | 2.2 |  | 49 | 4 | 2.2 |
| 10 | 4 | 2.2 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 11 | 5 | 2.75 |  | 31 | 4 | 2.2 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 1 | 0.55 |  | 53 | 1 | 0.55 |
| 13 | 2 | 1.1 |  | 33 | 6 | 3.3 |  | 54 | 2 | 1.1 |
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
| 3 | 4 | 1.47 |  | 23 | 6 | 2.2 |  | 43 | 3 | 1.1 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 6 | 2.2 |
| 5 | 9 | 3.3 |  | 25 | 3 | 1.1 |  | 45 | 8 | 2.93 |
| 6 | 2 | 0.73 |  | 26 | 2 | 0.73 |  | 46 | 6 | 2.2 |
| 7 | 5 | 1.83 |  | 27 | 5 | 1.83 |  | 47 | 6 | 2.2 |
| 8 | 10 | 3.66 |  | 28 | 4 | 1.47 |  | 48 | 6 | 2.2 |
| 9 | 7 | 2.56 |  | 29 | 4 | 1.47 |  | 49 | 6 | 2.2 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 3 | 1.1 |
| 11 | 6 | 2.2 |  | 31 | 6 | 2.2 |  | 51 | 4 | 1.47 |
| 12 | 1 | 0.37 |  | 32 | 3 | 1.1 |  | 52 | 2 | 0.73 |
| 13 | 5 | 1.83 |  | 33 | 8 | 2.93 |  | 53 | 2 | 0.73 |
| 14 | 7 | 2.56 |  | 34 | 3 | 1.1 |  | 54 | 3 | 1.1 |
| 15 | 4 | 1.47 |  | 35 | 4 | 1.47 |  | 55 | 6 | 2.2 |
| 16 | 6 | 2.2 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 2 | 0.73 |  |  |  |  |
| 18 | 7 | 2.56 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 8 | 2.93 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-06-27 | 70 |
| 6 | 2026-07-07 | 60 |
| 4 | 2026-07-07 | 60 |
| 53 | 2026-07-16 | 51 |
| 32 | 2026-07-21 | 46 |
| 22 | 2026-07-28 | 39 |
| 12 | 2026-07-30 | 37 |
| 43 | 2026-07-30 | 37 |
| 28 | 2026-07-30 | 37 |
| 54 | 2026-08-04 | 32 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-01 | 4 |
| 2 | 2026-08-20 | 16 |
| 3 | 2026-08-27 | 9 |
| 4 | 2026-07-07 | 60 |
| 5 | 2026-08-29 | 7 |
| 6 | 2026-07-07 | 60 |
| 7 | 2026-08-25 | 11 |
| 8 | 2026-09-03 | 2 |
| 9 | 2026-09-05 | 0 |
| 10 | 2026-08-29 | 7 |
| 11 | 2026-09-05 | 0 |
| 12 | 2026-07-30 | 37 |
| 13 | 2026-08-25 | 11 |
| 14 | 2026-08-25 | 11 |
| 15 | 2026-08-29 | 7 |
| 16 | 2026-09-03 | 2 |
| 17 | 2026-09-01 | 4 |
| 18 | 2026-08-25 | 11 |
| 19 | 2026-08-22 | 14 |
| 20 | 2026-08-15 | 21 |
| 21 | 2026-09-05 | 0 |
| 22 | 2026-07-28 | 39 |
| 23 | 2026-08-06 | 30 |
| 24 | 2026-09-05 | 0 |
| 25 | 2026-08-22 | 14 |
| 26 | 2026-08-27 | 9 |
| 27 | 2026-08-15 | 21 |
| 28 | 2026-07-30 | 37 |
| 29 | 2026-08-29 | 7 |
| 30 | 2026-08-18 | 18 |
| 31 | 2026-09-05 | 0 |
| 32 | 2026-07-21 | 46 |
| 33 | 2026-09-05 | 0 |
| 34 | 2026-08-29 | 7 |
| 35 | 2026-08-06 | 30 |
| 36 | 2026-08-22 | 14 |
| 37 | 2026-08-08 | 28 |
| 38 | 2026-08-20 | 16 |
| 39 | 2026-08-20 | 16 |
| 40 | 2026-08-25 | 11 |
| 41 | 2026-09-01 | 4 |
| 42 | 2026-09-03 | 2 |
| 43 | 2026-07-30 | 37 |
| 44 | 2026-09-01 | 4 |
| 45 | 2026-09-01 | 4 |
| 46 | 2026-09-03 | 2 |
| 47 | 2026-09-05 | 0 |
| 48 | 2026-08-18 | 18 |
| 49 | 2026-09-01 | 4 |
| 50 | 2026-08-15 | 21 |
| 51 | 2026-08-20 | 16 |
| 52 | 2026-06-27 | 70 |
| 53 | 2026-07-16 | 51 |
| 54 | 2026-08-04 | 32 |
| 55 | 2026-09-01 | 4 |



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

