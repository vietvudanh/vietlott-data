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
| Power 655 | 1403 | 2017-08-01 | 2026-09-26 | 1403 | 00001 | 01403 |
| Power 645 | 1370 | 2017-10-25 | 2026-09-25 | 1370 | 00198 | 01567 |
| Power 535 | 419 | 2025-06-29 | 2026-09-26 | 836 | 00001 | 00910 |
| Keno | 688 | 2022-12-04 | 2026-09-26 | 86109 | #0110271 | #0297164 |
| 3D | 1133 | 2019-04-22 | 2026-09-25 | 1133 | 00001 | 01137 |
| 3D Pro | 780 | 2021-09-14 | 2026-09-26 | 780 | 00001 | 00784 |
| Bingo18 | 661 | 2024-12-03 | 2026-09-26 | 92501 | 0083123 | 0188424 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |
| 2026-09-24 | 01402 | [1, 13, 23, 25, 26, 28, 27] | 2026-09-25T00:01:22.421665 |
| 2026-09-22 | 01401 | [1, 3, 9, 11, 41, 46, 10] | 2026-09-23T00:01:18.071623 |
| 2026-09-19 | 01400 | [4, 7, 11, 18, 22, 25, 50] | 2026-09-20T00:01:07.511406 |
| 2026-09-17 | 01399 | [6, 11, 25, 27, 37, 45, 15] | 2026-09-18T00:01:15.250052 |
| 2026-09-15 | 01398 | [24, 27, 32, 36, 38, 47, 52] | 2026-09-16T00:01:46.289586 |
| 2026-09-12 | 01397 | [7, 24, 31, 43, 47, 54, 22] | 2026-09-13T00:01:08.403983 |
| 2026-09-10 | 01396 | [2, 5, 28, 32, 51, 53, 50] | 2026-09-12T12:01:58.169601 |
| 2026-09-08 | 01395 | [8, 11, 14, 23, 25, 54, 17] | 2026-09-09T00:01:06.966495 |
| 2026-09-05 | 01394 | [9, 11, 24, 31, 33, 47, 21] | 2026-09-06T00:01:37.018893 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 190 | 1.93 |  | 21 | 176 | 1.79 |  | 41 | 207 | 2.11 |
| 2 | 162 | 1.65 |  | 22 | 208 | 2.12 |  | 42 | 181 | 1.84 |
| 3 | 190 | 1.93 |  | 23 | 189 | 1.92 |  | 43 | 199 | 2.03 |
| 4 | 145 | 1.48 |  | 24 | 180 | 1.83 |  | 44 | 182 | 1.85 |
| 5 | 183 | 1.86 |  | 25 | 163 | 1.66 |  | 45 | 182 | 1.85 |
| 6 | 144 | 1.47 |  | 26 | 167 | 1.7 |  | 46 | 183 | 1.86 |
| 7 | 159 | 1.62 |  | 27 | 165 | 1.68 |  | 47 | 180 | 1.83 |
| 8 | 196 | 2.0 |  | 28 | 160 | 1.63 |  | 48 | 191 | 1.95 |
| 9 | 196 | 2.0 |  | 29 | 191 | 1.95 |  | 49 | 175 | 1.78 |
| 10 | 167 | 1.7 |  | 30 | 162 | 1.65 |  | 50 | 179 | 1.82 |
| 11 | 186 | 1.89 |  | 31 | 188 | 1.91 |  | 51 | 198 | 2.02 |
| 12 | 180 | 1.83 |  | 32 | 188 | 1.91 |  | 52 | 179 | 1.82 |
| 13 | 174 | 1.77 |  | 33 | 180 | 1.83 |  | 53 | 188 | 1.91 |
| 14 | 180 | 1.83 |  | 34 | 196 | 2.0 |  | 54 | 169 | 1.72 |
| 15 | 167 | 1.7 |  | 35 | 170 | 1.73 |  | 55 | 179 | 1.82 |
| 16 | 175 | 1.78 |  | 36 | 168 | 1.71 |  |  |  |  |
| 17 | 161 | 1.64 |  | 37 | 159 | 1.62 |  |  |  |  |
| 18 | 180 | 1.83 |  | 38 | 174 | 1.77 |  |  |  |  |
| 19 | 174 | 1.77 |  | 39 | 172 | 1.75 |  |  |  |  |
| 20 | 189 | 1.92 |  | 40 | 194 | 1.98 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 24 | 4 | 4.4 |  | 48 | 1 | 1.1 |
| 2 | 1 | 1.1 |  | 25 | 4 | 4.4 |  | 49 | 2 | 2.2 |
| 3 | 1 | 1.1 |  | 26 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 4 | 1 | 1.1 |  | 27 | 3 | 3.3 |  | 51 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 52 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 29 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 31 | 2 | 2.2 |  | 54 | 2 | 2.2 |
| 8 | 2 | 2.2 |  | 32 | 2 | 2.2 |  | 55 | 1 | 1.1 |
| 9 | 3 | 3.3 |  | 33 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 6 | 6.59 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 15 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 42 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |
| 22 | 2 | 2.2 |  | 46 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 47 | 4 | 4.4 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.75 |  | 21 | 4 | 2.2 |  | 41 | 3 | 1.65 |
| 2 | 5 | 2.75 |  | 22 | 2 | 1.1 |  | 42 | 3 | 1.65 |
| 3 | 3 | 1.65 |  | 23 | 3 | 1.65 |  | 43 | 2 | 1.1 |
| 4 | 1 | 0.55 |  | 24 | 5 | 2.75 |  | 44 | 3 | 1.65 |
| 5 | 5 | 2.75 |  | 25 | 6 | 3.3 |  | 45 | 5 | 2.75 |
| 6 | 1 | 0.55 |  | 26 | 2 | 1.1 |  | 46 | 3 | 1.65 |
| 7 | 4 | 2.2 |  | 27 | 5 | 2.75 |  | 47 | 6 | 3.3 |
| 8 | 4 | 2.2 |  | 28 | 3 | 1.65 |  | 48 | 2 | 1.1 |
| 9 | 5 | 2.75 |  | 29 | 4 | 2.2 |  | 49 | 4 | 2.2 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 4 | 2.2 |
| 11 | 8 | 4.4 |  | 31 | 5 | 2.75 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 52 | 2 | 1.1 |
| 13 | 2 | 1.1 |  | 33 | 2 | 1.1 |  | 53 | 1 | 0.55 |
| 14 | 6 | 3.3 |  | 34 | 1 | 0.55 |  | 54 | 3 | 1.65 |
| 15 | 3 | 1.65 |  | 35 | 1 | 0.55 |  | 55 | 3 | 1.65 |
| 16 | 3 | 1.65 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 6 | 3.3 |  | 38 | 5 | 2.75 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 4 | 2.2 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.2 |  | 21 | 5 | 1.83 |  | 41 | 8 | 2.93 |
| 2 | 6 | 2.2 |  | 22 | 6 | 2.2 |  | 42 | 5 | 1.83 |
| 3 | 4 | 1.47 |  | 23 | 5 | 1.83 |  | 43 | 4 | 1.47 |
| 4 | 2 | 0.73 |  | 24 | 7 | 2.56 |  | 44 | 6 | 2.2 |
| 5 | 8 | 2.93 |  | 25 | 7 | 2.56 |  | 45 | 9 | 3.3 |
| 6 | 2 | 0.73 |  | 26 | 2 | 0.73 |  | 46 | 3 | 1.1 |
| 7 | 5 | 1.83 |  | 27 | 7 | 2.56 |  | 47 | 7 | 2.56 |
| 8 | 7 | 2.56 |  | 28 | 4 | 1.47 |  | 48 | 6 | 2.2 |
| 9 | 8 | 2.93 |  | 29 | 4 | 1.47 |  | 49 | 6 | 2.2 |
| 10 | 5 | 1.83 |  | 30 | 3 | 1.1 |  | 50 | 5 | 1.83 |
| 11 | 10 | 3.66 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 1 | 0.37 |  | 32 | 4 | 1.47 |  | 52 | 2 | 0.73 |
| 13 | 5 | 1.83 |  | 33 | 7 | 2.56 |  | 53 | 2 | 0.73 |
| 14 | 7 | 2.56 |  | 34 | 2 | 0.73 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 2 | 0.73 |  | 55 | 5 | 1.83 |
| 16 | 4 | 1.47 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-07-30 | 58 |
| 35 | 2026-08-06 | 51 |
| 20 | 2026-08-15 | 42 |
| 30 | 2026-08-18 | 39 |
| 39 | 2026-08-20 | 37 |
| 19 | 2026-08-22 | 35 |
| 40 | 2026-08-25 | 32 |
| 34 | 2026-08-29 | 28 |
| 29 | 2026-08-29 | 28 |
| 55 | 2026-09-01 | 25 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-24 | 2 |
| 2 | 2026-09-10 | 16 |
| 3 | 2026-09-22 | 4 |
| 4 | 2026-09-19 | 7 |
| 5 | 2026-09-10 | 16 |
| 6 | 2026-09-17 | 9 |
| 7 | 2026-09-19 | 7 |
| 8 | 2026-09-08 | 18 |
| 9 | 2026-09-22 | 4 |
| 10 | 2026-09-22 | 4 |
| 11 | 2026-09-22 | 4 |
| 12 | 2026-07-30 | 58 |
| 13 | 2026-09-24 | 2 |
| 14 | 2026-09-26 | 0 |
| 15 | 2026-09-17 | 9 |
| 16 | 2026-09-03 | 23 |
| 17 | 2026-09-08 | 18 |
| 18 | 2026-09-26 | 0 |
| 19 | 2026-08-22 | 35 |
| 20 | 2026-08-15 | 42 |
| 21 | 2026-09-26 | 0 |
| 22 | 2026-09-19 | 7 |
| 23 | 2026-09-24 | 2 |
| 24 | 2026-09-15 | 11 |
| 25 | 2026-09-24 | 2 |
| 26 | 2026-09-24 | 2 |
| 27 | 2026-09-24 | 2 |
| 28 | 2026-09-24 | 2 |
| 29 | 2026-08-29 | 28 |
| 30 | 2026-08-18 | 39 |
| 31 | 2026-09-12 | 14 |
| 32 | 2026-09-15 | 11 |
| 33 | 2026-09-05 | 21 |
| 34 | 2026-08-29 | 28 |
| 35 | 2026-08-06 | 51 |
| 36 | 2026-09-15 | 11 |
| 37 | 2026-09-17 | 9 |
| 38 | 2026-09-26 | 0 |
| 39 | 2026-08-20 | 37 |
| 40 | 2026-08-25 | 32 |
| 41 | 2026-09-22 | 4 |
| 42 | 2026-09-03 | 23 |
| 43 | 2026-09-12 | 14 |
| 44 | 2026-09-01 | 25 |
| 45 | 2026-09-17 | 9 |
| 46 | 2026-09-22 | 4 |
| 47 | 2026-09-15 | 11 |
| 48 | 2026-09-26 | 0 |
| 49 | 2026-09-26 | 0 |
| 50 | 2026-09-19 | 7 |
| 51 | 2026-09-10 | 16 |
| 52 | 2026-09-26 | 0 |
| 53 | 2026-09-10 | 16 |
| 54 | 2026-09-12 | 14 |
| 55 | 2026-09-01 | 25 |



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

