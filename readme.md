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
| Power 655 | 1418 | 2017-08-01 | 2026-10-31 | 1418 | 00001 | 01418 |
| Power 645 | 1385 | 2017-10-25 | 2026-10-30 | 1385 | 00198 | 01582 |
| Power 535 | 490 | 2025-06-29 | 2026-10-31 | 979 | 00001 | 00979 |
| Keno | 723 | 2022-12-04 | 2026-10-31 | 90296 | #0110271 | #0301307 |
| 3D | 1152 | 2019-04-22 | 2026-10-30 | 1152 | 00001 | 01152 |
| 3D Pro | 799 | 2021-09-14 | 2026-10-31 | 799 | 00001 | 00799 |
| Bingo18 | 696 | 2024-12-03 | 2026-10-31 | 98123 | 0083123 | 0193959 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-31 | 01418 | [12, 18, 22, 26, 28, 55, 11] | 2026-10-31T12:00:05Z |
| 2026-10-29 | 01417 | [9, 29, 33, 38, 45, 46, 53] | 2026-10-29T12:00:05Z |
| 2026-10-27 | 01416 | [9, 18, 27, 28, 31, 35, 50] | 2026-10-27T12:00:09Z |
| 2026-10-24 | 01415 | [6, 7, 18, 41, 44, 50, 53] | 2026-10-24T12:01:16.734372 |
| 2026-10-22 | 01414 | [14, 19, 24, 31, 34, 42, 37] | 2026-10-22T12:01:27.562980 |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.94 |  | 21 | 177 | 1.78 |  | 41 | 209 | 2.11 |
| 2 | 164 | 1.65 |  | 22 | 209 | 2.11 |  | 42 | 183 | 1.84 |
| 3 | 190 | 1.91 |  | 23 | 192 | 1.93 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.49 |  | 24 | 183 | 1.84 |  | 44 | 183 | 1.84 |
| 5 | 184 | 1.85 |  | 25 | 164 | 1.65 |  | 45 | 185 | 1.86 |
| 6 | 147 | 1.48 |  | 26 | 169 | 1.7 |  | 46 | 184 | 1.85 |
| 7 | 164 | 1.65 |  | 27 | 169 | 1.7 |  | 47 | 180 | 1.81 |
| 8 | 196 | 1.97 |  | 28 | 162 | 1.63 |  | 48 | 192 | 1.93 |
| 9 | 198 | 1.99 |  | 29 | 192 | 1.93 |  | 49 | 175 | 1.76 |
| 10 | 168 | 1.69 |  | 30 | 164 | 1.65 |  | 50 | 183 | 1.84 |
| 11 | 190 | 1.91 |  | 31 | 191 | 1.92 |  | 51 | 199 | 2.01 |
| 12 | 183 | 1.84 |  | 32 | 188 | 1.89 |  | 52 | 181 | 1.82 |
| 13 | 178 | 1.79 |  | 33 | 181 | 1.82 |  | 53 | 191 | 1.92 |
| 14 | 183 | 1.84 |  | 34 | 198 | 1.99 |  | 54 | 170 | 1.71 |
| 15 | 168 | 1.69 |  | 35 | 172 | 1.73 |  | 55 | 182 | 1.83 |
| 16 | 177 | 1.78 |  | 36 | 169 | 1.7 |  |  |  |  |
| 17 | 163 | 1.64 |  | 37 | 161 | 1.62 |  |  |  |  |
| 18 | 185 | 1.86 |  | 38 | 175 | 1.76 |  |  |  |  |
| 19 | 175 | 1.76 |  | 39 | 173 | 1.74 |  |  |  |  |
| 20 | 191 | 1.92 |  | 40 | 195 | 1.96 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.06 |  | 23 | 3 | 3.06 |  | 46 | 1 | 1.02 |
| 2 | 1 | 1.02 |  | 24 | 3 | 3.06 |  | 48 | 1 | 1.02 |
| 4 | 2 | 2.04 |  | 25 | 1 | 1.02 |  | 50 | 4 | 4.08 |
| 5 | 1 | 1.02 |  | 26 | 2 | 2.04 |  | 51 | 1 | 1.02 |
| 6 | 3 | 3.06 |  | 27 | 4 | 4.08 |  | 52 | 2 | 2.04 |
| 7 | 5 | 5.1 |  | 28 | 2 | 2.04 |  | 53 | 3 | 3.06 |
| 9 | 2 | 2.04 |  | 29 | 1 | 1.02 |  | 54 | 1 | 1.02 |
| 10 | 1 | 1.02 |  | 30 | 2 | 2.04 |  | 55 | 3 | 3.06 |
| 11 | 3 | 3.06 |  | 31 | 3 | 3.06 |  |  |  |  |
| 12 | 3 | 3.06 |  | 33 | 1 | 1.02 |  |  |  |  |
| 13 | 3 | 3.06 |  | 34 | 2 | 2.04 |  |  |  |  |
| 14 | 3 | 3.06 |  | 35 | 1 | 1.02 |  |  |  |  |
| 15 | 1 | 1.02 |  | 37 | 2 | 2.04 |  |  |  |  |
| 16 | 2 | 2.04 |  | 38 | 1 | 1.02 |  |  |  |  |
| 17 | 1 | 1.02 |  | 39 | 1 | 1.02 |  |  |  |  |
| 18 | 5 | 5.1 |  | 40 | 1 | 1.02 |  |  |  |  |
| 19 | 1 | 1.02 |  | 41 | 2 | 2.04 |  |  |  |  |
| 20 | 2 | 2.04 |  | 42 | 2 | 2.04 |  |  |  |  |
| 21 | 1 | 1.02 |  | 44 | 1 | 1.02 |  |  |  |  |
| 22 | 1 | 1.02 |  | 45 | 3 | 3.06 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.17 |  | 21 | 3 | 1.59 |  | 41 | 4 | 2.12 |
| 2 | 3 | 1.59 |  | 22 | 3 | 1.59 |  | 42 | 3 | 1.59 |
| 3 | 1 | 0.53 |  | 23 | 5 | 2.65 |  | 43 | 1 | 0.53 |
| 4 | 4 | 2.12 |  | 24 | 6 | 3.17 |  | 44 | 2 | 1.06 |
| 5 | 2 | 1.06 |  | 25 | 5 | 2.65 |  | 45 | 5 | 2.65 |
| 6 | 4 | 2.12 |  | 26 | 3 | 1.59 |  | 46 | 3 | 1.59 |
| 7 | 7 | 3.7 |  | 27 | 7 | 3.7 |  | 47 | 4 | 2.12 |
| 8 | 2 | 1.06 |  | 28 | 4 | 2.12 |  | 48 | 2 | 1.06 |
| 9 | 5 | 2.65 |  | 29 | 1 | 0.53 |  | 49 | 2 | 1.06 |
| 10 | 2 | 1.06 |  | 30 | 2 | 1.06 |  | 50 | 6 | 3.17 |
| 11 | 10 | 5.29 |  | 31 | 5 | 2.65 |  | 51 | 2 | 1.06 |
| 12 | 3 | 1.59 |  | 32 | 2 | 1.06 |  | 52 | 4 | 2.12 |
| 13 | 5 | 2.65 |  | 33 | 2 | 1.06 |  | 53 | 4 | 2.12 |
| 14 | 5 | 2.65 |  | 34 | 2 | 1.06 |  | 54 | 3 | 1.59 |
| 15 | 2 | 1.06 |  | 35 | 2 | 1.06 |  | 55 | 4 | 2.12 |
| 16 | 3 | 1.59 |  | 36 | 2 | 1.06 |  |  |  |  |
| 17 | 4 | 2.12 |  | 37 | 3 | 1.59 |  |  |  |  |
| 18 | 7 | 3.7 |  | 38 | 3 | 1.59 |  |  |  |  |
| 19 | 1 | 0.53 |  | 39 | 1 | 0.53 |  |  |  |  |
| 20 | 2 | 1.06 |  | 40 | 1 | 0.53 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 5 | 1.83 |  | 41 | 5 | 1.83 |
| 2 | 6 | 2.2 |  | 22 | 3 | 1.1 |  | 42 | 5 | 1.83 |
| 3 | 3 | 1.1 |  | 23 | 6 | 2.2 |  | 43 | 1 | 0.37 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 3 | 1.1 |
| 5 | 6 | 2.2 |  | 25 | 7 | 2.56 |  | 45 | 8 | 2.93 |
| 6 | 4 | 1.47 |  | 26 | 4 | 1.47 |  | 46 | 4 | 1.47 |
| 7 | 9 | 3.3 |  | 27 | 9 | 3.3 |  | 47 | 6 | 2.2 |
| 8 | 4 | 1.47 |  | 28 | 4 | 1.47 |  | 48 | 3 | 1.1 |
| 9 | 7 | 2.56 |  | 29 | 5 | 1.83 |  | 49 | 2 | 0.73 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 8 | 2.93 |
| 11 | 11 | 4.03 |  | 31 | 8 | 2.93 |  | 51 | 4 | 1.47 |
| 12 | 3 | 1.1 |  | 32 | 2 | 0.73 |  | 52 | 4 | 1.47 |
| 13 | 6 | 2.2 |  | 33 | 3 | 1.1 |  | 53 | 4 | 1.47 |
| 14 | 8 | 2.93 |  | 34 | 3 | 1.1 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 5 | 1.83 |
| 16 | 4 | 1.47 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 11 | 4.03 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 4 | 1.47 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 4 | 1.47 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 53 |
| 43 | 2026-09-12 | 49 |
| 32 | 2026-09-15 | 46 |
| 47 | 2026-09-15 | 46 |
| 3 | 2026-09-22 | 39 |
| 49 | 2026-09-26 | 35 |
| 36 | 2026-09-29 | 32 |
| 5 | 2026-10-01 | 30 |
| 15 | 2026-10-01 | 30 |
| 54 | 2026-10-03 | 28 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 14 |
| 2 | 2026-10-13 | 18 |
| 3 | 2026-09-22 | 39 |
| 4 | 2026-10-15 | 16 |
| 5 | 2026-10-01 | 30 |
| 6 | 2026-10-24 | 7 |
| 7 | 2026-10-24 | 7 |
| 8 | 2026-09-08 | 53 |
| 9 | 2026-10-29 | 2 |
| 10 | 2026-10-17 | 14 |
| 11 | 2026-10-31 | 0 |
| 12 | 2026-10-31 | 0 |
| 13 | 2026-10-20 | 11 |
| 14 | 2026-10-22 | 9 |
| 15 | 2026-10-01 | 30 |
| 16 | 2026-10-17 | 14 |
| 17 | 2026-10-10 | 21 |
| 18 | 2026-10-31 | 0 |
| 19 | 2026-10-22 | 9 |
| 20 | 2026-10-20 | 11 |
| 21 | 2026-10-10 | 21 |
| 22 | 2026-10-31 | 0 |
| 23 | 2026-10-20 | 11 |
| 24 | 2026-10-22 | 9 |
| 25 | 2026-10-15 | 16 |
| 26 | 2026-10-31 | 0 |
| 27 | 2026-10-27 | 4 |
| 28 | 2026-10-31 | 0 |
| 29 | 2026-10-29 | 2 |
| 30 | 2026-10-20 | 11 |
| 31 | 2026-10-27 | 4 |
| 32 | 2026-09-15 | 46 |
| 33 | 2026-10-29 | 2 |
| 34 | 2026-10-22 | 9 |
| 35 | 2026-10-27 | 4 |
| 36 | 2026-09-29 | 32 |
| 37 | 2026-10-22 | 9 |
| 38 | 2026-10-29 | 2 |
| 39 | 2026-10-10 | 21 |
| 40 | 2026-10-13 | 18 |
| 41 | 2026-10-24 | 7 |
| 42 | 2026-10-22 | 9 |
| 43 | 2026-09-12 | 49 |
| 44 | 2026-10-24 | 7 |
| 45 | 2026-10-29 | 2 |
| 46 | 2026-10-29 | 2 |
| 47 | 2026-09-15 | 46 |
| 48 | 2026-10-17 | 14 |
| 49 | 2026-09-26 | 35 |
| 50 | 2026-10-27 | 4 |
| 51 | 2026-10-15 | 16 |
| 52 | 2026-10-08 | 23 |
| 53 | 2026-10-29 | 2 |
| 54 | 2026-10-03 | 28 |
| 55 | 2026-10-31 | 0 |



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

