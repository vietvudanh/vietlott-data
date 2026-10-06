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
| Power 655 | 1406 | 2017-08-01 | 2026-10-03 | 1406 | 00001 | 01406 |
| Power 645 | 1374 | 2017-10-25 | 2026-10-04 | 1374 | 00198 | 01571 |
| Power 535 | 427 | 2025-06-29 | 2026-10-04 | 852 | 00001 | 00926 |
| Keno | 693 | 2022-12-04 | 2026-10-05 | 86466 | #0110271 | #0298145 |
| 3D | 1136 | 2019-04-22 | 2026-10-02 | 1136 | 00001 | 01140 |
| 3D Pro | 783 | 2021-09-14 | 2026-10-03 | 783 | 00001 | 00787 |
| Bingo18 | 664 | 2024-12-03 | 2026-10-05 | 92819 | 0083123 | 0189735 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |
| 2026-09-24 | 01402 | [1, 13, 23, 25, 26, 28, 27] | 2026-09-25T00:01:22.421665 |
| 2026-09-22 | 01401 | [1, 3, 9, 11, 41, 46, 10] | 2026-09-23T00:01:18.071623 |
| 2026-09-19 | 01400 | [4, 7, 11, 18, 22, 25, 50] | 2026-09-20T00:01:07.511406 |
| 2026-09-17 | 01399 | [6, 11, 25, 27, 37, 45, 15] | 2026-09-18T00:01:15.250052 |
| 2026-09-15 | 01398 | [24, 27, 32, 36, 38, 47, 52] | 2026-09-16T00:01:46.289586 |
| 2026-09-12 | 01397 | [7, 24, 31, 43, 47, 54, 22] | 2026-09-13T00:01:08.403983 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 190 | 1.93 |  | 21 | 176 | 1.79 |  | 41 | 208 | 2.11 |
| 2 | 163 | 1.66 |  | 22 | 208 | 2.11 |  | 42 | 181 | 1.84 |
| 3 | 190 | 1.93 |  | 23 | 189 | 1.92 |  | 43 | 199 | 2.02 |
| 4 | 147 | 1.49 |  | 24 | 180 | 1.83 |  | 44 | 182 | 1.85 |
| 5 | 184 | 1.87 |  | 25 | 163 | 1.66 |  | 45 | 182 | 1.85 |
| 6 | 144 | 1.46 |  | 26 | 167 | 1.7 |  | 46 | 183 | 1.86 |
| 7 | 160 | 1.63 |  | 27 | 165 | 1.68 |  | 47 | 180 | 1.83 |
| 8 | 196 | 1.99 |  | 28 | 160 | 1.63 |  | 48 | 191 | 1.94 |
| 9 | 196 | 1.99 |  | 29 | 191 | 1.94 |  | 49 | 175 | 1.78 |
| 10 | 167 | 1.7 |  | 30 | 162 | 1.65 |  | 50 | 179 | 1.82 |
| 11 | 188 | 1.91 |  | 31 | 188 | 1.91 |  | 51 | 198 | 2.01 |
| 12 | 180 | 1.83 |  | 32 | 188 | 1.91 |  | 52 | 180 | 1.83 |
| 13 | 177 | 1.8 |  | 33 | 180 | 1.83 |  | 53 | 188 | 1.91 |
| 14 | 180 | 1.83 |  | 34 | 197 | 2.0 |  | 54 | 170 | 1.73 |
| 15 | 168 | 1.71 |  | 35 | 171 | 1.74 |  | 55 | 180 | 1.83 |
| 16 | 176 | 1.79 |  | 36 | 169 | 1.72 |  |  |  |  |
| 17 | 162 | 1.65 |  | 37 | 159 | 1.62 |  |  |  |  |
| 18 | 181 | 1.84 |  | 38 | 174 | 1.77 |  |  |  |  |
| 19 | 174 | 1.77 |  | 39 | 172 | 1.75 |  |  |  |  |
| 20 | 189 | 1.92 |  | 40 | 194 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 24 | 3 | 3.3 |  | 50 | 2 | 2.2 |
| 2 | 2 | 2.2 |  | 25 | 4 | 4.4 |  | 51 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 26 | 1 | 1.1 |  | 52 | 3 | 3.3 |
| 4 | 3 | 3.3 |  | 27 | 3 | 3.3 |  | 53 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 54 | 3 | 3.3 |
| 6 | 1 | 1.1 |  | 31 | 2 | 2.2 |  | 55 | 1 | 1.1 |
| 7 | 3 | 3.3 |  | 32 | 2 | 2.2 |  |  |  |  |
| 8 | 1 | 1.1 |  | 33 | 1 | 1.1 |  |  |  |  |
| 9 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 10 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 11 | 7 | 7.69 |  | 36 | 2 | 2.2 |  |  |  |  |
| 13 | 4 | 4.4 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 15 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 43 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 45 | 1 | 1.1 |  |  |  |  |
| 18 | 3 | 3.3 |  | 46 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 47 | 3 | 3.3 |  |  |  |  |
| 22 | 2 | 2.2 |  | 48 | 1 | 1.1 |  |  |  |  |
| 23 | 2 | 2.2 |  | 49 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.75 |  | 22 | 2 | 1.1 |  | 42 | 2 | 1.1 |
| 2 | 5 | 2.75 |  | 23 | 3 | 1.65 |  | 43 | 1 | 0.55 |
| 3 | 3 | 1.65 |  | 24 | 4 | 2.2 |  | 44 | 2 | 1.1 |
| 4 | 3 | 1.65 |  | 25 | 6 | 3.3 |  | 45 | 5 | 2.75 |
| 5 | 6 | 3.3 |  | 26 | 2 | 1.1 |  | 46 | 3 | 1.65 |
| 6 | 1 | 0.55 |  | 27 | 5 | 2.75 |  | 47 | 5 | 2.75 |
| 7 | 5 | 2.75 |  | 28 | 2 | 1.1 |  | 48 | 2 | 1.1 |
| 8 | 4 | 2.2 |  | 29 | 4 | 2.2 |  | 49 | 2 | 1.1 |
| 9 | 5 | 2.75 |  | 30 | 2 | 1.1 |  | 50 | 4 | 2.2 |
| 10 | 3 | 1.65 |  | 31 | 4 | 2.2 |  | 51 | 3 | 1.65 |
| 11 | 9 | 4.95 |  | 32 | 2 | 1.1 |  | 52 | 3 | 1.65 |
| 13 | 5 | 2.75 |  | 33 | 2 | 1.1 |  | 53 | 1 | 0.55 |
| 14 | 4 | 2.2 |  | 34 | 2 | 1.1 |  | 54 | 3 | 1.65 |
| 15 | 4 | 2.2 |  | 35 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 16 | 3 | 1.65 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 7 | 3.85 |  | 38 | 5 | 2.75 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 2 | 1.1 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 2 | 1.1 |  |  |  |  |
| 21 | 4 | 2.2 |  | 41 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.2 |  | 21 | 5 | 1.83 |  | 41 | 7 | 2.56 |
| 2 | 7 | 2.56 |  | 22 | 5 | 1.83 |  | 42 | 4 | 1.47 |
| 3 | 4 | 1.47 |  | 23 | 4 | 1.47 |  | 43 | 2 | 0.73 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 5 | 1.83 |
| 5 | 7 | 2.56 |  | 25 | 7 | 2.56 |  | 45 | 9 | 3.3 |
| 6 | 2 | 0.73 |  | 26 | 2 | 0.73 |  | 46 | 3 | 1.1 |
| 7 | 6 | 2.2 |  | 27 | 7 | 2.56 |  | 47 | 6 | 2.2 |
| 8 | 7 | 2.56 |  | 28 | 3 | 1.1 |  | 48 | 6 | 2.2 |
| 9 | 8 | 2.93 |  | 29 | 4 | 1.47 |  | 49 | 5 | 1.83 |
| 10 | 5 | 1.83 |  | 30 | 3 | 1.1 |  | 50 | 5 | 1.83 |
| 11 | 11 | 4.03 |  | 31 | 5 | 1.83 |  | 51 | 5 | 1.83 |
| 12 | 1 | 0.37 |  | 32 | 4 | 1.47 |  | 52 | 3 | 1.1 |
| 13 | 6 | 2.2 |  | 33 | 7 | 2.56 |  | 53 | 2 | 0.73 |
| 14 | 7 | 2.56 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 5 | 1.83 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 7 | 2.56 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-07-30 | 65 |
| 20 | 2026-08-15 | 49 |
| 30 | 2026-08-18 | 46 |
| 39 | 2026-08-20 | 44 |
| 19 | 2026-08-22 | 42 |
| 40 | 2026-08-25 | 39 |
| 29 | 2026-08-29 | 35 |
| 44 | 2026-09-01 | 32 |
| 42 | 2026-09-03 | 30 |
| 33 | 2026-09-05 | 28 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-24 | 9 |
| 2 | 2026-09-29 | 4 |
| 3 | 2026-09-22 | 11 |
| 4 | 2026-10-01 | 2 |
| 5 | 2026-10-01 | 2 |
| 6 | 2026-09-17 | 16 |
| 7 | 2026-10-03 | 0 |
| 8 | 2026-09-08 | 25 |
| 9 | 2026-09-22 | 11 |
| 10 | 2026-09-22 | 11 |
| 11 | 2026-10-03 | 0 |
| 12 | 2026-07-30 | 65 |
| 13 | 2026-10-03 | 0 |
| 14 | 2026-09-26 | 7 |
| 15 | 2026-10-01 | 2 |
| 16 | 2026-10-03 | 0 |
| 17 | 2026-09-29 | 4 |
| 18 | 2026-10-03 | 0 |
| 19 | 2026-08-22 | 42 |
| 20 | 2026-08-15 | 49 |
| 21 | 2026-09-26 | 7 |
| 22 | 2026-09-19 | 14 |
| 23 | 2026-09-24 | 9 |
| 24 | 2026-09-15 | 18 |
| 25 | 2026-09-24 | 9 |
| 26 | 2026-09-24 | 9 |
| 27 | 2026-09-24 | 9 |
| 28 | 2026-09-24 | 9 |
| 29 | 2026-08-29 | 35 |
| 30 | 2026-08-18 | 46 |
| 31 | 2026-09-12 | 21 |
| 32 | 2026-09-15 | 18 |
| 33 | 2026-09-05 | 28 |
| 34 | 2026-10-01 | 2 |
| 35 | 2026-09-29 | 4 |
| 36 | 2026-09-29 | 4 |
| 37 | 2026-09-17 | 16 |
| 38 | 2026-09-26 | 7 |
| 39 | 2026-08-20 | 44 |
| 40 | 2026-08-25 | 39 |
| 41 | 2026-10-03 | 0 |
| 42 | 2026-09-03 | 30 |
| 43 | 2026-09-12 | 21 |
| 44 | 2026-09-01 | 32 |
| 45 | 2026-09-17 | 16 |
| 46 | 2026-09-22 | 11 |
| 47 | 2026-09-15 | 18 |
| 48 | 2026-09-26 | 7 |
| 49 | 2026-09-26 | 7 |
| 50 | 2026-09-19 | 14 |
| 51 | 2026-09-10 | 23 |
| 52 | 2026-10-01 | 2 |
| 53 | 2026-09-10 | 23 |
| 54 | 2026-10-03 | 0 |
| 55 | 2026-10-01 | 2 |



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

