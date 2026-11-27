# Vietlott Data

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing statistics and insights for all major lottery products.

**Dữ liệu kết quả xổ số Vietlott đầy đủ, miễn phí, cập nhật hàng ngày** (Power 6/55, Mega 6/45, Power 5/35, Keno, Max 3D, Max 3D Pro, Bingo18) - open historical Vietlott draw results in NDJSON, from the first draw, MIT licensed. Raw files live in [data/](data/); each line has the fields date, id, result, process_time. See [llms.txt](https://vietvudanh.github.io/vietlott-data/llms.txt) for a machine-readable summary.

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
| Power 655 | 1429 | 2017-08-01 | 2026-11-26 | 1429 | 00001 | 01429 |
| Power 645 | 1397 | 2017-10-25 | 2026-11-27 | 1397 | 00198 | 01594 |
| Power 535 | 517 | 2025-06-29 | 2026-11-27 | 1033 | 00001 | 01033 |
| Keno | 750 | 2022-12-04 | 2026-11-27 | 93509 | #0110271 | #0304520 |
| 3D | 1164 | 2019-04-22 | 2026-11-27 | 1164 | 00001 | 01164 |
| 3D Pro | 810 | 2021-09-14 | 2026-11-26 | 810 | 00001 | 00810 |
| Bingo18 | 723 | 2024-12-03 | 2026-11-27 | 102417 | 0083123 | 0198253 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-11-26 | 01429 | [14, 18, 24, 28, 34, 55, 32] | 2026-11-26T12:00:05Z |
| 2026-11-24 | 01428 | [36, 40, 43, 46, 50, 55, 15] | 2026-11-24T12:00:05Z |
| 2026-11-21 | 01427 | [7, 29, 44, 45, 50, 54, 39] | 2026-11-21T12:00:05Z |
| 2026-11-19 | 01426 | [3, 13, 21, 23, 38, 43, 16] | 2026-11-19T12:00:05Z |
| 2026-11-17 | 01425 | [6, 20, 36, 41, 49, 52, 34] | 2026-11-18T00:00:05Z |
| 2026-11-14 | 01424 | [5, 28, 36, 42, 45, 47, 51] | 2026-11-14T12:00:05Z |
| 2026-11-12 | 01423 | [17, 25, 33, 34, 35, 36, 48] | 2026-11-12T12:00:05Z |
| 2026-11-10 | 01422 | [1, 2, 21, 38, 39, 51, 12] | 2026-11-10T12:00:05Z |
| 2026-11-07 | 01421 | [5, 19, 20, 26, 44, 53, 39] | 2026-11-07T12:00:05Z |
| 2026-11-05 | 01420 | [6, 20, 34, 41, 49, 52, 36] | 2026-11-05T12:00:05Z |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 194 | 1.94 |  | 21 | 179 | 1.79 |  | 41 | 211 | 2.11 |
| 2 | 165 | 1.65 |  | 22 | 210 | 2.1 |  | 42 | 184 | 1.84 |
| 3 | 191 | 1.91 |  | 23 | 193 | 1.93 |  | 43 | 202 | 2.02 |
| 4 | 148 | 1.48 |  | 24 | 184 | 1.84 |  | 44 | 185 | 1.85 |
| 5 | 186 | 1.86 |  | 25 | 165 | 1.65 |  | 45 | 187 | 1.87 |
| 6 | 149 | 1.49 |  | 26 | 170 | 1.7 |  | 46 | 185 | 1.85 |
| 7 | 165 | 1.65 |  | 27 | 169 | 1.69 |  | 47 | 181 | 1.81 |
| 8 | 196 | 1.96 |  | 28 | 164 | 1.64 |  | 48 | 193 | 1.93 |
| 9 | 198 | 1.98 |  | 29 | 193 | 1.93 |  | 49 | 177 | 1.77 |
| 10 | 169 | 1.69 |  | 30 | 164 | 1.64 |  | 50 | 185 | 1.85 |
| 11 | 190 | 1.9 |  | 31 | 192 | 1.92 |  | 51 | 201 | 2.01 |
| 12 | 184 | 1.84 |  | 32 | 189 | 1.89 |  | 52 | 183 | 1.83 |
| 13 | 179 | 1.79 |  | 33 | 182 | 1.82 |  | 53 | 192 | 1.92 |
| 14 | 185 | 1.85 |  | 34 | 202 | 2.02 |  | 54 | 172 | 1.72 |
| 15 | 169 | 1.69 |  | 35 | 173 | 1.73 |  | 55 | 184 | 1.84 |
| 16 | 178 | 1.78 |  | 36 | 174 | 1.74 |  |  |  |  |
| 17 | 164 | 1.64 |  | 37 | 161 | 1.61 |  |  |  |  |
| 18 | 186 | 1.86 |  | 38 | 177 | 1.77 |  |  |  |  |
| 19 | 176 | 1.76 |  | 39 | 177 | 1.77 |  |  |  |  |
| 20 | 194 | 1.94 |  | 40 | 196 | 1.96 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 23 | 1 | 1.1 |  | 46 | 2 | 2.2 |
| 2 | 1 | 1.1 |  | 24 | 1 | 1.1 |  | 47 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 48 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 26 | 2 | 2.2 |  | 49 | 2 | 2.2 |
| 6 | 2 | 2.2 |  | 28 | 3 | 3.3 |  | 50 | 2 | 2.2 |
| 7 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 51 | 2 | 2.2 |
| 9 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 52 | 2 | 2.2 |
| 10 | 1 | 1.1 |  | 32 | 1 | 1.1 |  | 53 | 2 | 2.2 |
| 11 | 1 | 1.1 |  | 33 | 2 | 2.2 |  | 54 | 2 | 2.2 |
| 12 | 2 | 2.2 |  | 34 | 4 | 4.4 |  | 55 | 3 | 3.3 |
| 13 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 36 | 5 | 5.49 |  |  |  |  |
| 15 | 1 | 1.1 |  | 38 | 3 | 3.3 |  |  |  |  |
| 16 | 1 | 1.1 |  | 39 | 4 | 4.4 |  |  |  |  |
| 17 | 1 | 1.1 |  | 40 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 42 | 1 | 1.1 |  |  |  |  |
| 20 | 3 | 3.3 |  | 43 | 3 | 3.3 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 22 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 22 | 2 | 1.1 |  | 42 | 3 | 1.65 |
| 2 | 3 | 1.65 |  | 23 | 4 | 2.2 |  | 43 | 3 | 1.65 |
| 3 | 1 | 0.55 |  | 24 | 4 | 2.2 |  | 44 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 2 | 1.1 |  | 45 | 5 | 2.75 |
| 5 | 3 | 1.65 |  | 26 | 3 | 1.65 |  | 46 | 2 | 1.1 |
| 6 | 5 | 2.75 |  | 27 | 4 | 2.2 |  | 47 | 1 | 0.55 |
| 7 | 6 | 3.3 |  | 28 | 4 | 2.2 |  | 48 | 2 | 1.1 |
| 9 | 2 | 1.1 |  | 29 | 2 | 1.1 |  | 49 | 2 | 1.1 |
| 10 | 2 | 1.1 |  | 30 | 2 | 1.1 |  | 50 | 6 | 3.3 |
| 11 | 4 | 2.2 |  | 31 | 4 | 2.2 |  | 51 | 3 | 1.65 |
| 12 | 4 | 2.2 |  | 32 | 1 | 0.55 |  | 52 | 4 | 2.2 |
| 13 | 5 | 2.75 |  | 33 | 2 | 1.1 |  | 53 | 4 | 2.2 |
| 14 | 5 | 2.75 |  | 34 | 6 | 3.3 |  | 54 | 3 | 1.65 |
| 15 | 2 | 1.1 |  | 35 | 3 | 1.65 |  | 55 | 5 | 2.75 |
| 16 | 3 | 1.65 |  | 36 | 6 | 3.3 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 6 | 3.3 |  | 38 | 3 | 1.65 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 5 | 2.75 |  | 40 | 2 | 1.1 |  |  |  |  |
| 21 | 3 | 1.65 |  | 41 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.56 |  | 21 | 5 | 1.83 |  | 41 | 6 | 2.2 |
| 2 | 4 | 1.47 |  | 22 | 4 | 1.47 |  | 42 | 4 | 1.47 |
| 3 | 2 | 0.73 |  | 23 | 6 | 2.2 |  | 43 | 4 | 1.47 |
| 4 | 4 | 1.47 |  | 24 | 8 | 2.93 |  | 44 | 4 | 1.47 |
| 5 | 5 | 1.83 |  | 25 | 6 | 2.2 |  | 45 | 8 | 2.93 |
| 6 | 6 | 2.2 |  | 26 | 4 | 1.47 |  | 46 | 4 | 1.47 |
| 7 | 8 | 2.93 |  | 27 | 7 | 2.56 |  | 47 | 5 | 1.83 |
| 8 | 2 | 0.73 |  | 28 | 6 | 2.2 |  | 48 | 3 | 1.1 |
| 9 | 5 | 1.83 |  | 29 | 3 | 1.1 |  | 49 | 4 | 1.47 |
| 10 | 4 | 1.47 |  | 30 | 2 | 0.73 |  | 50 | 8 | 2.93 |
| 11 | 10 | 3.66 |  | 31 | 6 | 2.2 |  | 51 | 4 | 1.47 |
| 12 | 4 | 1.47 |  | 32 | 3 | 1.1 |  | 52 | 6 | 2.2 |
| 13 | 6 | 2.2 |  | 33 | 3 | 1.1 |  | 53 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 34 | 7 | 2.56 |  | 54 | 5 | 1.83 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 4 | 1.47 |  | 36 | 7 | 2.56 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 2 | 0.73 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 2 | 0.73 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 79 |
| 4 | 2026-10-15 | 42 |
| 30 | 2026-10-20 | 37 |
| 37 | 2026-10-22 | 35 |
| 27 | 2026-10-27 | 30 |
| 9 | 2026-10-29 | 28 |
| 11 | 2026-10-31 | 26 |
| 10 | 2026-11-03 | 23 |
| 22 | 2026-11-03 | 23 |
| 31 | 2026-11-03 | 23 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-11-10 | 16 |
| 2 | 2026-11-10 | 16 |
| 3 | 2026-11-19 | 7 |
| 4 | 2026-10-15 | 42 |
| 5 | 2026-11-14 | 12 |
| 6 | 2026-11-17 | 9 |
| 7 | 2026-11-21 | 5 |
| 8 | 2026-09-08 | 79 |
| 9 | 2026-10-29 | 28 |
| 10 | 2026-11-03 | 23 |
| 11 | 2026-10-31 | 26 |
| 12 | 2026-11-10 | 16 |
| 13 | 2026-11-19 | 7 |
| 14 | 2026-11-26 | 0 |
| 15 | 2026-11-24 | 2 |
| 16 | 2026-11-19 | 7 |
| 17 | 2026-11-12 | 14 |
| 18 | 2026-11-26 | 0 |
| 19 | 2026-11-07 | 19 |
| 20 | 2026-11-17 | 9 |
| 21 | 2026-11-19 | 7 |
| 22 | 2026-11-03 | 23 |
| 23 | 2026-11-19 | 7 |
| 24 | 2026-11-26 | 0 |
| 25 | 2026-11-12 | 14 |
| 26 | 2026-11-07 | 19 |
| 27 | 2026-10-27 | 30 |
| 28 | 2026-11-26 | 0 |
| 29 | 2026-11-21 | 5 |
| 30 | 2026-10-20 | 37 |
| 31 | 2026-11-03 | 23 |
| 32 | 2026-11-26 | 0 |
| 33 | 2026-11-12 | 14 |
| 34 | 2026-11-26 | 0 |
| 35 | 2026-11-12 | 14 |
| 36 | 2026-11-24 | 2 |
| 37 | 2026-10-22 | 35 |
| 38 | 2026-11-19 | 7 |
| 39 | 2026-11-21 | 5 |
| 40 | 2026-11-24 | 2 |
| 41 | 2026-11-17 | 9 |
| 42 | 2026-11-14 | 12 |
| 43 | 2026-11-24 | 2 |
| 44 | 2026-11-21 | 5 |
| 45 | 2026-11-21 | 5 |
| 46 | 2026-11-24 | 2 |
| 47 | 2026-11-14 | 12 |
| 48 | 2026-11-12 | 14 |
| 49 | 2026-11-17 | 9 |
| 50 | 2026-11-24 | 2 |
| 51 | 2026-11-14 | 12 |
| 52 | 2026-11-17 | 9 |
| 53 | 2026-11-07 | 19 |
| 54 | 2026-11-21 | 5 |
| 55 | 2026-11-26 | 0 |



## How It Works

Vietlott blocks non-Vietnam IPs ([issue #13](https://github.com/vietvudanh/vietlott-data/issues/13)), so crawling runs on a scheduled local runner (`bin/github_data.sh`) and commits updated data back to GitHub.

For architecture and runner setup, see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).


## Installation & Usage

### Go crawler (recommended)

Requires Go 1.27+. Vietlott only answers Vietnamese IPs, so run it from Vietnam.

```bash
make build-crawler                       # builds bin/vietlott-crawler
./bin/vietlott-crawler status            # existing vs latest draw per product
./bin/vietlott-crawler sync --all        # fetch latest draws and backfill gaps
./bin/vietlott-crawler sync --product keno --max-draws 100
./bin/vietlott-crawler render-readme     # regenerate readme.md
./bin/vietlott-crawler render-docs       # regenerate docs/index.html

# Products: power655, power645, power535, keno, bingo18, 3d, 3d_pro
```

### Python CLI (legacy, deprecated)

The Python crawler stays available through the PyPI package and will be removed in a future release.

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

