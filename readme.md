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
| Power 655 | 1421 | 2017-08-01 | 2026-11-07 | 1421 | 00001 | 01421 |
| Power 645 | 1389 | 2017-10-25 | 2026-11-08 | 1389 | 00198 | 01586 |
| Power 535 | 498 | 2025-06-29 | 2026-11-08 | 996 | 00001 | 00996 |
| Keno | 732 | 2022-12-04 | 2026-11-09 | 91277 | #0110271 | #0302288 |
| 3D | 1155 | 2019-04-22 | 2026-11-06 | 1155 | 00001 | 01155 |
| 3D Pro | 802 | 2021-09-14 | 2026-11-07 | 802 | 00001 | 00802 |
| Bingo18 | 705 | 2024-12-03 | 2026-11-09 | 99435 | 0083123 | 0195271 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-11-07 | 01421 | [5, 19, 20, 26, 44, 53, 39] | 2026-11-07T12:00:05Z |
| 2026-11-05 | 01420 | [6, 20, 34, 41, 49, 52, 36] | 2026-11-05T12:00:05Z |
| 2026-11-03 | 01419 | [10, 22, 31, 39, 43, 54, 14] | 2026-11-03T12:00:05Z |
| 2026-10-31 | 01418 | [12, 18, 22, 26, 28, 55, 11] | 2026-10-31T12:00:05Z |
| 2026-10-29 | 01417 | [9, 29, 33, 38, 45, 46, 53] | 2026-10-29T12:00:05Z |
| 2026-10-27 | 01416 | [9, 18, 27, 28, 31, 35, 50] | 2026-10-27T12:00:09Z |
| 2026-10-24 | 01415 | [6, 7, 18, 41, 44, 50, 53] | 2026-10-24T12:01:16.734372 |
| 2026-10-22 | 01414 | [14, 19, 24, 31, 34, 42, 37] | 2026-10-22T12:01:27.562980 |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.94 |  | 21 | 177 | 1.78 |  | 41 | 210 | 2.11 |
| 2 | 164 | 1.65 |  | 22 | 210 | 2.11 |  | 42 | 183 | 1.84 |
| 3 | 190 | 1.91 |  | 23 | 192 | 1.93 |  | 43 | 200 | 2.01 |
| 4 | 148 | 1.49 |  | 24 | 183 | 1.84 |  | 44 | 184 | 1.85 |
| 5 | 185 | 1.86 |  | 25 | 164 | 1.65 |  | 45 | 185 | 1.86 |
| 6 | 148 | 1.49 |  | 26 | 170 | 1.71 |  | 46 | 184 | 1.85 |
| 7 | 164 | 1.65 |  | 27 | 169 | 1.7 |  | 47 | 180 | 1.81 |
| 8 | 196 | 1.97 |  | 28 | 162 | 1.63 |  | 48 | 192 | 1.93 |
| 9 | 198 | 1.99 |  | 29 | 192 | 1.93 |  | 49 | 176 | 1.77 |
| 10 | 169 | 1.7 |  | 30 | 164 | 1.65 |  | 50 | 183 | 1.84 |
| 11 | 190 | 1.91 |  | 31 | 192 | 1.93 |  | 51 | 199 | 2.0 |
| 12 | 183 | 1.84 |  | 32 | 188 | 1.89 |  | 52 | 182 | 1.83 |
| 13 | 178 | 1.79 |  | 33 | 181 | 1.82 |  | 53 | 192 | 1.93 |
| 14 | 184 | 1.85 |  | 34 | 199 | 2.0 |  | 54 | 171 | 1.72 |
| 15 | 168 | 1.69 |  | 35 | 172 | 1.73 |  | 55 | 182 | 1.83 |
| 16 | 177 | 1.78 |  | 36 | 170 | 1.71 |  |  |  |  |
| 17 | 163 | 1.64 |  | 37 | 161 | 1.62 |  |  |  |  |
| 18 | 185 | 1.86 |  | 38 | 175 | 1.76 |  |  |  |  |
| 19 | 176 | 1.77 |  | 39 | 175 | 1.76 |  |  |  |  |
| 20 | 193 | 1.94 |  | 40 | 195 | 1.96 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 45 | 3 | 3.3 |
| 2 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 46 | 1 | 1.1 |
| 4 | 1 | 1.1 |  | 26 | 3 | 3.3 |  | 48 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 27 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 6 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 50 | 4 | 4.4 |
| 7 | 2 | 2.2 |  | 29 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 9 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 53 | 4 | 4.4 |
| 11 | 2 | 2.2 |  | 33 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 12 | 2 | 2.2 |  | 34 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 13 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 4 | 4.4 |  | 36 | 1 | 1.1 |  |  |  |  |
| 16 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 18 | 3 | 3.3 |  | 39 | 3 | 3.3 |  |  |  |  |
| 19 | 2 | 2.2 |  | 40 | 1 | 1.1 |  |  |  |  |
| 20 | 3 | 3.3 |  | 41 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 22 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 23 | 3 | 3.3 |  | 44 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.75 |  | 22 | 4 | 2.2 |  | 42 | 2 | 1.1 |
| 2 | 3 | 1.65 |  | 23 | 4 | 2.2 |  | 43 | 2 | 1.1 |
| 3 | 1 | 0.55 |  | 24 | 5 | 2.75 |  | 44 | 2 | 1.1 |
| 4 | 4 | 2.2 |  | 25 | 4 | 2.2 |  | 45 | 4 | 2.2 |
| 5 | 3 | 1.65 |  | 26 | 4 | 2.2 |  | 46 | 2 | 1.1 |
| 6 | 5 | 2.75 |  | 27 | 7 | 3.85 |  | 47 | 2 | 1.1 |
| 7 | 7 | 3.85 |  | 28 | 4 | 2.2 |  | 48 | 2 | 1.1 |
| 9 | 3 | 1.65 |  | 29 | 1 | 0.55 |  | 49 | 2 | 1.1 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 6 | 3.3 |
| 11 | 7 | 3.85 |  | 31 | 5 | 2.75 |  | 51 | 2 | 1.1 |
| 12 | 3 | 1.65 |  | 32 | 2 | 1.1 |  | 52 | 5 | 2.75 |
| 13 | 5 | 2.75 |  | 33 | 1 | 0.55 |  | 53 | 5 | 2.75 |
| 14 | 5 | 2.75 |  | 34 | 3 | 1.65 |  | 54 | 3 | 1.65 |
| 15 | 2 | 1.1 |  | 35 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 16 | 2 | 1.1 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 7 | 3.85 |  | 38 | 3 | 1.65 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 3 | 1.65 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 1 | 0.55 |  |  |  |  |
| 21 | 2 | 1.1 |  | 41 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.56 |  | 21 | 5 | 1.83 |  | 41 | 6 | 2.2 |
| 2 | 6 | 2.2 |  | 22 | 4 | 1.47 |  | 42 | 4 | 1.47 |
| 3 | 3 | 1.1 |  | 23 | 5 | 1.83 |  | 43 | 2 | 0.73 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 7 | 2.56 |  | 45 | 7 | 2.56 |
| 6 | 5 | 1.83 |  | 26 | 5 | 1.83 |  | 46 | 4 | 1.47 |
| 7 | 9 | 3.3 |  | 27 | 9 | 3.3 |  | 47 | 5 | 1.83 |
| 8 | 4 | 1.47 |  | 28 | 4 | 1.47 |  | 48 | 3 | 1.1 |
| 9 | 7 | 2.56 |  | 29 | 4 | 1.47 |  | 49 | 3 | 1.1 |
| 10 | 5 | 1.83 |  | 30 | 4 | 1.47 |  | 50 | 8 | 2.93 |
| 11 | 11 | 4.03 |  | 31 | 8 | 2.93 |  | 51 | 3 | 1.1 |
| 12 | 3 | 1.1 |  | 32 | 2 | 0.73 |  | 52 | 5 | 1.83 |
| 13 | 6 | 2.2 |  | 33 | 2 | 0.73 |  | 53 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 34 | 4 | 1.47 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 2 | 0.73 |  | 55 | 4 | 1.47 |
| 16 | 4 | 1.47 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 10 | 3.66 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 6 | 2.2 |  | 40 | 2 | 0.73 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 60 |
| 32 | 2026-09-15 | 53 |
| 47 | 2026-09-15 | 53 |
| 3 | 2026-09-22 | 46 |
| 15 | 2026-10-01 | 37 |
| 17 | 2026-10-10 | 28 |
| 21 | 2026-10-10 | 28 |
| 2 | 2026-10-13 | 25 |
| 40 | 2026-10-13 | 25 |
| 4 | 2026-10-15 | 23 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 21 |
| 2 | 2026-10-13 | 25 |
| 3 | 2026-09-22 | 46 |
| 4 | 2026-10-15 | 23 |
| 5 | 2026-11-07 | 0 |
| 6 | 2026-11-05 | 2 |
| 7 | 2026-10-24 | 14 |
| 8 | 2026-09-08 | 60 |
| 9 | 2026-10-29 | 9 |
| 10 | 2026-11-03 | 4 |
| 11 | 2026-10-31 | 7 |
| 12 | 2026-10-31 | 7 |
| 13 | 2026-10-20 | 18 |
| 14 | 2026-11-03 | 4 |
| 15 | 2026-10-01 | 37 |
| 16 | 2026-10-17 | 21 |
| 17 | 2026-10-10 | 28 |
| 18 | 2026-10-31 | 7 |
| 19 | 2026-11-07 | 0 |
| 20 | 2026-11-07 | 0 |
| 21 | 2026-10-10 | 28 |
| 22 | 2026-11-03 | 4 |
| 23 | 2026-10-20 | 18 |
| 24 | 2026-10-22 | 16 |
| 25 | 2026-10-15 | 23 |
| 26 | 2026-11-07 | 0 |
| 27 | 2026-10-27 | 11 |
| 28 | 2026-10-31 | 7 |
| 29 | 2026-10-29 | 9 |
| 30 | 2026-10-20 | 18 |
| 31 | 2026-11-03 | 4 |
| 32 | 2026-09-15 | 53 |
| 33 | 2026-10-29 | 9 |
| 34 | 2026-11-05 | 2 |
| 35 | 2026-10-27 | 11 |
| 36 | 2026-11-05 | 2 |
| 37 | 2026-10-22 | 16 |
| 38 | 2026-10-29 | 9 |
| 39 | 2026-11-07 | 0 |
| 40 | 2026-10-13 | 25 |
| 41 | 2026-11-05 | 2 |
| 42 | 2026-10-22 | 16 |
| 43 | 2026-11-03 | 4 |
| 44 | 2026-11-07 | 0 |
| 45 | 2026-10-29 | 9 |
| 46 | 2026-10-29 | 9 |
| 47 | 2026-09-15 | 53 |
| 48 | 2026-10-17 | 21 |
| 49 | 2026-11-05 | 2 |
| 50 | 2026-10-27 | 11 |
| 51 | 2026-10-15 | 23 |
| 52 | 2026-11-05 | 2 |
| 53 | 2026-11-07 | 0 |
| 54 | 2026-11-03 | 4 |
| 55 | 2026-10-31 | 7 |



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

