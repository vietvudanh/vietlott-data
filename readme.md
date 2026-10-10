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
| Power 655 | 1409 | 2017-08-01 | 2026-10-10 | 1409 | 00001 | 01409 |
| Power 645 | 1376 | 2017-10-25 | 2026-10-09 | 1376 | 00198 | 01573 |
| Power 535 | 433 | 2025-06-29 | 2026-10-10 | 863 | 00001 | 00937 |
| Keno | 702 | 2022-12-04 | 2026-10-10 | 87738 | #0110271 | #0298808 |
| 3D | 1139 | 2019-04-22 | 2026-10-09 | 1139 | 00001 | 01143 |
| 3D Pro | 786 | 2021-09-14 | 2026-10-10 | 786 | 00001 | 00790 |
| Bingo18 | 675 | 2024-12-03 | 2026-10-10 | 94677 | 0083123 | 0190621 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |
| 2026-09-24 | 01402 | [1, 13, 23, 25, 26, 28, 27] | 2026-09-25T00:01:22.421665 |
| 2026-09-22 | 01401 | [1, 3, 9, 11, 41, 46, 10] | 2026-09-23T00:01:18.071623 |
| 2026-09-19 | 01400 | [4, 7, 11, 18, 22, 25, 50] | 2026-09-20T00:01:07.511406 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 192 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 208 | 2.11 |
| 2 | 163 | 1.65 |  | 22 | 208 | 2.11 |  | 42 | 181 | 1.84 |
| 3 | 190 | 1.93 |  | 23 | 190 | 1.93 |  | 43 | 199 | 2.02 |
| 4 | 147 | 1.49 |  | 24 | 182 | 1.85 |  | 44 | 182 | 1.85 |
| 5 | 184 | 1.87 |  | 25 | 163 | 1.65 |  | 45 | 182 | 1.85 |
| 6 | 146 | 1.48 |  | 26 | 167 | 1.69 |  | 46 | 183 | 1.86 |
| 7 | 162 | 1.64 |  | 27 | 167 | 1.69 |  | 47 | 180 | 1.83 |
| 8 | 196 | 1.99 |  | 28 | 160 | 1.62 |  | 48 | 191 | 1.94 |
| 9 | 196 | 1.99 |  | 29 | 191 | 1.94 |  | 49 | 175 | 1.77 |
| 10 | 167 | 1.69 |  | 30 | 163 | 1.65 |  | 50 | 179 | 1.82 |
| 11 | 188 | 1.91 |  | 31 | 189 | 1.92 |  | 51 | 198 | 2.01 |
| 12 | 181 | 1.84 |  | 32 | 188 | 1.91 |  | 52 | 181 | 1.84 |
| 13 | 177 | 1.79 |  | 33 | 180 | 1.83 |  | 53 | 188 | 1.91 |
| 14 | 181 | 1.84 |  | 34 | 197 | 2.0 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 180 | 1.83 |
| 16 | 176 | 1.78 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 159 | 1.61 |  |  |  |  |
| 18 | 182 | 1.85 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 174 | 1.76 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 190 | 1.93 |  | 40 | 194 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 4.08 |  | 23 | 2 | 2.04 |  | 48 | 1 | 1.02 |
| 2 | 2 | 2.04 |  | 24 | 4 | 4.08 |  | 49 | 1 | 1.02 |
| 3 | 1 | 1.02 |  | 25 | 3 | 3.06 |  | 50 | 2 | 2.04 |
| 4 | 3 | 3.06 |  | 26 | 1 | 1.02 |  | 51 | 1 | 1.02 |
| 5 | 2 | 2.04 |  | 27 | 5 | 5.1 |  | 52 | 4 | 4.08 |
| 6 | 3 | 3.06 |  | 28 | 2 | 2.04 |  | 53 | 1 | 1.02 |
| 7 | 5 | 5.1 |  | 30 | 1 | 1.02 |  | 54 | 2 | 2.04 |
| 9 | 1 | 1.02 |  | 31 | 2 | 2.04 |  | 55 | 1 | 1.02 |
| 10 | 1 | 1.02 |  | 32 | 2 | 2.04 |  |  |  |  |
| 11 | 5 | 5.1 |  | 34 | 1 | 1.02 |  |  |  |  |
| 12 | 1 | 1.02 |  | 35 | 1 | 1.02 |  |  |  |  |
| 13 | 4 | 4.08 |  | 36 | 2 | 2.04 |  |  |  |  |
| 14 | 2 | 2.04 |  | 37 | 1 | 1.02 |  |  |  |  |
| 15 | 2 | 2.04 |  | 38 | 2 | 2.04 |  |  |  |  |
| 16 | 1 | 1.02 |  | 39 | 1 | 1.02 |  |  |  |  |
| 17 | 2 | 2.04 |  | 41 | 2 | 2.04 |  |  |  |  |
| 18 | 4 | 4.08 |  | 43 | 1 | 1.02 |  |  |  |  |
| 20 | 1 | 1.02 |  | 45 | 1 | 1.02 |  |  |  |  |
| 21 | 2 | 2.04 |  | 46 | 1 | 1.02 |  |  |  |  |
| 22 | 2 | 2.04 |  | 47 | 2 | 2.04 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.17 |  | 21 | 5 | 2.65 |  | 41 | 4 | 2.12 |
| 2 | 5 | 2.65 |  | 22 | 2 | 1.06 |  | 42 | 2 | 1.06 |
| 3 | 3 | 1.59 |  | 23 | 3 | 1.59 |  | 43 | 1 | 0.53 |
| 4 | 3 | 1.59 |  | 24 | 6 | 3.17 |  | 44 | 2 | 1.06 |
| 5 | 5 | 2.65 |  | 25 | 6 | 3.17 |  | 45 | 4 | 2.12 |
| 6 | 3 | 1.59 |  | 26 | 2 | 1.06 |  | 46 | 3 | 1.59 |
| 7 | 7 | 3.7 |  | 27 | 7 | 3.7 |  | 47 | 5 | 2.65 |
| 8 | 4 | 2.12 |  | 28 | 2 | 1.06 |  | 48 | 2 | 1.06 |
| 9 | 5 | 2.65 |  | 29 | 3 | 1.59 |  | 49 | 2 | 1.06 |
| 10 | 3 | 1.59 |  | 30 | 3 | 1.59 |  | 50 | 4 | 2.12 |
| 11 | 9 | 4.76 |  | 31 | 5 | 2.65 |  | 51 | 2 | 1.06 |
| 12 | 1 | 0.53 |  | 32 | 2 | 1.06 |  | 52 | 4 | 2.12 |
| 13 | 5 | 2.65 |  | 33 | 1 | 0.53 |  | 53 | 1 | 0.53 |
| 14 | 4 | 2.12 |  | 34 | 2 | 1.06 |  | 54 | 3 | 1.59 |
| 15 | 4 | 2.12 |  | 35 | 1 | 0.53 |  | 55 | 2 | 1.06 |
| 16 | 3 | 1.59 |  | 36 | 3 | 1.59 |  |  |  |  |
| 17 | 4 | 2.12 |  | 37 | 1 | 0.53 |  |  |  |  |
| 18 | 7 | 3.7 |  | 38 | 4 | 2.12 |  |  |  |  |
| 19 | 2 | 1.06 |  | 39 | 3 | 1.59 |  |  |  |  |
| 20 | 3 | 1.59 |  | 40 | 1 | 0.53 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 6 | 2.2 |  | 41 | 6 | 2.2 |
| 2 | 6 | 2.2 |  | 22 | 5 | 1.83 |  | 42 | 3 | 1.1 |
| 3 | 4 | 1.47 |  | 23 | 5 | 1.83 |  | 43 | 2 | 0.73 |
| 4 | 3 | 1.1 |  | 24 | 9 | 3.3 |  | 44 | 4 | 1.47 |
| 5 | 7 | 2.56 |  | 25 | 6 | 2.2 |  | 45 | 8 | 2.93 |
| 6 | 3 | 1.1 |  | 26 | 2 | 0.73 |  | 46 | 3 | 1.1 |
| 7 | 8 | 2.93 |  | 27 | 9 | 3.3 |  | 47 | 6 | 2.2 |
| 8 | 6 | 2.2 |  | 28 | 3 | 1.1 |  | 48 | 6 | 2.2 |
| 9 | 6 | 2.2 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 5 | 1.83 |
| 11 | 11 | 4.03 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 2 | 0.73 |  | 32 | 3 | 1.1 |  | 52 | 4 | 1.47 |
| 13 | 6 | 2.2 |  | 33 | 5 | 1.83 |  | 53 | 2 | 0.73 |
| 14 | 7 | 2.56 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 5 | 1.83 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 6 | 2.2 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 4 | 1.47 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 19 | 2026-08-22 | 49 |
| 40 | 2026-08-25 | 46 |
| 29 | 2026-08-29 | 42 |
| 44 | 2026-09-01 | 39 |
| 42 | 2026-09-03 | 37 |
| 33 | 2026-09-05 | 35 |
| 8 | 2026-09-08 | 32 |
| 51 | 2026-09-10 | 30 |
| 53 | 2026-09-10 | 30 |
| 43 | 2026-09-12 | 28 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-08 | 2 |
| 2 | 2026-09-29 | 11 |
| 3 | 2026-09-22 | 18 |
| 4 | 2026-10-01 | 9 |
| 5 | 2026-10-01 | 9 |
| 6 | 2026-10-08 | 2 |
| 7 | 2026-10-08 | 2 |
| 8 | 2026-09-08 | 32 |
| 9 | 2026-09-22 | 18 |
| 10 | 2026-09-22 | 18 |
| 11 | 2026-10-03 | 7 |
| 12 | 2026-10-08 | 2 |
| 13 | 2026-10-03 | 7 |
| 14 | 2026-10-10 | 0 |
| 15 | 2026-10-01 | 9 |
| 16 | 2026-10-03 | 7 |
| 17 | 2026-10-10 | 0 |
| 18 | 2026-10-06 | 4 |
| 19 | 2026-08-22 | 49 |
| 20 | 2026-10-06 | 4 |
| 21 | 2026-10-10 | 0 |
| 22 | 2026-09-19 | 21 |
| 23 | 2026-10-10 | 0 |
| 24 | 2026-10-10 | 0 |
| 25 | 2026-09-24 | 16 |
| 26 | 2026-09-24 | 16 |
| 27 | 2026-10-08 | 2 |
| 28 | 2026-09-24 | 16 |
| 29 | 2026-08-29 | 42 |
| 30 | 2026-10-10 | 0 |
| 31 | 2026-10-08 | 2 |
| 32 | 2026-09-15 | 25 |
| 33 | 2026-09-05 | 35 |
| 34 | 2026-10-01 | 9 |
| 35 | 2026-09-29 | 11 |
| 36 | 2026-09-29 | 11 |
| 37 | 2026-09-17 | 23 |
| 38 | 2026-09-26 | 14 |
| 39 | 2026-10-10 | 0 |
| 40 | 2026-08-25 | 46 |
| 41 | 2026-10-03 | 7 |
| 42 | 2026-09-03 | 37 |
| 43 | 2026-09-12 | 28 |
| 44 | 2026-09-01 | 39 |
| 45 | 2026-09-17 | 23 |
| 46 | 2026-09-22 | 18 |
| 47 | 2026-09-15 | 25 |
| 48 | 2026-09-26 | 14 |
| 49 | 2026-09-26 | 14 |
| 50 | 2026-09-19 | 21 |
| 51 | 2026-09-10 | 30 |
| 52 | 2026-10-08 | 2 |
| 53 | 2026-09-10 | 30 |
| 54 | 2026-10-03 | 7 |
| 55 | 2026-10-01 | 9 |



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

