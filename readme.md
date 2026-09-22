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
| Power 655 | 1401 | 2017-08-01 | 2026-09-22 | 1401 | 00001 | 01401 |
| Power 645 | 1368 | 2017-10-25 | 2026-09-20 | 1368 | 00198 | 01565 |
| Power 535 | 415 | 2025-06-29 | 2026-09-22 | 828 | 00001 | 00902 |
| Keno | 684 | 2022-12-04 | 2026-09-22 | 85633 | #0110271 | #0296688 |
| 3D | 1131 | 2019-04-22 | 2026-09-21 | 1131 | 00001 | 01135 |
| 3D Pro | 778 | 2021-09-14 | 2026-09-22 | 778 | 00001 | 00782 |
| Bingo18 | 657 | 2024-12-03 | 2026-09-22 | 91865 | 0083123 | 0187788 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-22 | 01401 | [1, 3, 9, 11, 41, 46, 10] | 2026-09-23T00:01:18.071623 |
| 2026-09-19 | 01400 | [4, 7, 11, 18, 22, 25, 50] | 2026-09-20T00:01:07.511406 |
| 2026-09-17 | 01399 | [6, 11, 25, 27, 37, 45, 15] | 2026-09-18T00:01:15.250052 |
| 2026-09-15 | 01398 | [24, 27, 32, 36, 38, 47, 52] | 2026-09-16T00:01:46.289586 |
| 2026-09-12 | 01397 | [7, 24, 31, 43, 47, 54, 22] | 2026-09-13T00:01:08.403983 |
| 2026-09-10 | 01396 | [2, 5, 28, 32, 51, 53, 50] | 2026-09-12T12:01:58.169601 |
| 2026-09-08 | 01395 | [8, 11, 14, 23, 25, 54, 17] | 2026-09-09T00:01:06.966495 |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 189 | 1.93 |  | 21 | 175 | 1.78 |  | 41 | 207 | 2.11 |
| 2 | 162 | 1.65 |  | 22 | 208 | 2.12 |  | 42 | 181 | 1.85 |
| 3 | 190 | 1.94 |  | 23 | 188 | 1.92 |  | 43 | 199 | 2.03 |
| 4 | 145 | 1.48 |  | 24 | 180 | 1.84 |  | 44 | 182 | 1.86 |
| 5 | 183 | 1.87 |  | 25 | 162 | 1.65 |  | 45 | 182 | 1.86 |
| 6 | 144 | 1.47 |  | 26 | 166 | 1.69 |  | 46 | 183 | 1.87 |
| 7 | 159 | 1.62 |  | 27 | 164 | 1.67 |  | 47 | 180 | 1.84 |
| 8 | 196 | 2.0 |  | 28 | 159 | 1.62 |  | 48 | 190 | 1.94 |
| 9 | 196 | 2.0 |  | 29 | 191 | 1.95 |  | 49 | 174 | 1.77 |
| 10 | 167 | 1.7 |  | 30 | 162 | 1.65 |  | 50 | 179 | 1.83 |
| 11 | 186 | 1.9 |  | 31 | 188 | 1.92 |  | 51 | 198 | 2.02 |
| 12 | 180 | 1.84 |  | 32 | 188 | 1.92 |  | 52 | 178 | 1.82 |
| 13 | 173 | 1.76 |  | 33 | 180 | 1.84 |  | 53 | 188 | 1.92 |
| 14 | 179 | 1.83 |  | 34 | 196 | 2.0 |  | 54 | 169 | 1.72 |
| 15 | 167 | 1.7 |  | 35 | 170 | 1.73 |  | 55 | 179 | 1.83 |
| 16 | 175 | 1.78 |  | 36 | 168 | 1.71 |  |  |  |  |
| 17 | 161 | 1.64 |  | 37 | 159 | 1.62 |  |  |  |  |
| 18 | 179 | 1.83 |  | 38 | 173 | 1.76 |  |  |  |  |
| 19 | 174 | 1.77 |  | 39 | 172 | 1.75 |  |  |  |  |
| 20 | 189 | 1.93 |  | 40 | 194 | 1.98 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 24 | 4 | 4.4 |  | 47 | 4 | 4.4 |
| 2 | 1 | 1.1 |  | 25 | 3 | 3.3 |  | 49 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 26 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 4 | 1 | 1.1 |  | 27 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 52 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 29 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 7 | 3 | 3.3 |  | 31 | 3 | 3.3 |  | 54 | 2 | 2.2 |
| 8 | 2 | 2.2 |  | 32 | 2 | 2.2 |  | 55 | 1 | 1.1 |
| 9 | 3 | 3.3 |  | 33 | 1 | 1.1 |  |  |  |  |
| 10 | 3 | 3.3 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 7 | 7.69 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 38 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 1 | 1.1 |  |  |  |  |
| 16 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 22 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |
| 23 | 1 | 1.1 |  | 46 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 21 | 3 | 1.65 |  | 41 | 4 | 2.2 |
| 2 | 5 | 2.75 |  | 22 | 3 | 1.65 |  | 42 | 3 | 1.65 |
| 3 | 3 | 1.65 |  | 23 | 3 | 1.65 |  | 43 | 2 | 1.1 |
| 4 | 1 | 0.55 |  | 24 | 5 | 2.75 |  | 44 | 4 | 2.2 |
| 5 | 6 | 3.3 |  | 25 | 5 | 2.75 |  | 45 | 5 | 2.75 |
| 6 | 1 | 0.55 |  | 26 | 1 | 0.55 |  | 46 | 3 | 1.65 |
| 7 | 5 | 2.75 |  | 27 | 6 | 3.3 |  | 47 | 6 | 3.3 |
| 8 | 4 | 2.2 |  | 28 | 2 | 1.1 |  | 48 | 3 | 1.65 |
| 9 | 6 | 3.3 |  | 29 | 4 | 2.2 |  | 49 | 3 | 1.65 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 5 | 2.75 |
| 11 | 8 | 4.4 |  | 31 | 5 | 2.75 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 52 | 1 | 0.55 |
| 13 | 1 | 0.55 |  | 33 | 3 | 1.65 |  | 53 | 1 | 0.55 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 54 | 3 | 1.65 |
| 15 | 3 | 1.65 |  | 35 | 1 | 0.55 |  | 55 | 3 | 1.65 |
| 16 | 3 | 1.65 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 5 | 2.75 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 4 | 2.2 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.2 |  | 21 | 5 | 1.83 |  | 41 | 8 | 2.93 |
| 2 | 6 | 2.2 |  | 22 | 6 | 2.2 |  | 42 | 5 | 1.83 |
| 3 | 5 | 1.83 |  | 23 | 6 | 2.2 |  | 43 | 4 | 1.47 |
| 4 | 2 | 0.73 |  | 24 | 7 | 2.56 |  | 44 | 6 | 2.2 |
| 5 | 8 | 2.93 |  | 25 | 6 | 2.2 |  | 45 | 9 | 3.3 |
| 6 | 2 | 0.73 |  | 26 | 1 | 0.37 |  | 46 | 3 | 1.1 |
| 7 | 6 | 2.2 |  | 27 | 6 | 2.2 |  | 47 | 7 | 2.56 |
| 8 | 8 | 2.93 |  | 28 | 4 | 1.47 |  | 48 | 5 | 1.83 |
| 9 | 8 | 2.93 |  | 29 | 4 | 1.47 |  | 49 | 5 | 1.83 |
| 10 | 5 | 1.83 |  | 30 | 3 | 1.1 |  | 50 | 5 | 1.83 |
| 11 | 10 | 3.66 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 1 | 0.37 |  | 32 | 4 | 1.47 |  | 52 | 2 | 0.73 |
| 13 | 4 | 1.47 |  | 33 | 7 | 2.56 |  | 53 | 2 | 0.73 |
| 14 | 6 | 2.2 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 15 | 5 | 1.83 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 5 | 1.83 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 7 | 2.56 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-07-30 | 54 |
| 35 | 2026-08-06 | 47 |
| 20 | 2026-08-15 | 38 |
| 48 | 2026-08-18 | 35 |
| 30 | 2026-08-18 | 35 |
| 39 | 2026-08-20 | 33 |
| 19 | 2026-08-22 | 31 |
| 40 | 2026-08-25 | 28 |
| 13 | 2026-08-25 | 28 |
| 26 | 2026-08-27 | 26 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-22 | 0 |
| 2 | 2026-09-10 | 12 |
| 3 | 2026-09-22 | 0 |
| 4 | 2026-09-19 | 3 |
| 5 | 2026-09-10 | 12 |
| 6 | 2026-09-17 | 5 |
| 7 | 2026-09-19 | 3 |
| 8 | 2026-09-08 | 14 |
| 9 | 2026-09-22 | 0 |
| 10 | 2026-09-22 | 0 |
| 11 | 2026-09-22 | 0 |
| 12 | 2026-07-30 | 54 |
| 13 | 2026-08-25 | 28 |
| 14 | 2026-09-08 | 14 |
| 15 | 2026-09-17 | 5 |
| 16 | 2026-09-03 | 19 |
| 17 | 2026-09-08 | 14 |
| 18 | 2026-09-19 | 3 |
| 19 | 2026-08-22 | 31 |
| 20 | 2026-08-15 | 38 |
| 21 | 2026-09-05 | 17 |
| 22 | 2026-09-19 | 3 |
| 23 | 2026-09-08 | 14 |
| 24 | 2026-09-15 | 7 |
| 25 | 2026-09-19 | 3 |
| 26 | 2026-08-27 | 26 |
| 27 | 2026-09-17 | 5 |
| 28 | 2026-09-10 | 12 |
| 29 | 2026-08-29 | 24 |
| 30 | 2026-08-18 | 35 |
| 31 | 2026-09-12 | 10 |
| 32 | 2026-09-15 | 7 |
| 33 | 2026-09-05 | 17 |
| 34 | 2026-08-29 | 24 |
| 35 | 2026-08-06 | 47 |
| 36 | 2026-09-15 | 7 |
| 37 | 2026-09-17 | 5 |
| 38 | 2026-09-15 | 7 |
| 39 | 2026-08-20 | 33 |
| 40 | 2026-08-25 | 28 |
| 41 | 2026-09-22 | 0 |
| 42 | 2026-09-03 | 19 |
| 43 | 2026-09-12 | 10 |
| 44 | 2026-09-01 | 21 |
| 45 | 2026-09-17 | 5 |
| 46 | 2026-09-22 | 0 |
| 47 | 2026-09-15 | 7 |
| 48 | 2026-08-18 | 35 |
| 49 | 2026-09-01 | 21 |
| 50 | 2026-09-19 | 3 |
| 51 | 2026-09-10 | 12 |
| 52 | 2026-09-15 | 7 |
| 53 | 2026-09-10 | 12 |
| 54 | 2026-09-12 | 10 |
| 55 | 2026-09-01 | 21 |



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

