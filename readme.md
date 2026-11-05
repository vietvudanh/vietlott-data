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
| Power 655 | 1419 | 2017-08-01 | 2026-11-03 | 1419 | 00001 | 01419 |
| Power 645 | 1387 | 2017-10-25 | 2026-11-04 | 1387 | 00198 | 01584 |
| Power 535 | 494 | 2025-06-29 | 2026-11-04 | 988 | 00001 | 00988 |
| Keno | 728 | 2022-12-04 | 2026-11-05 | 90801 | #0110271 | #0301812 |
| 3D | 1154 | 2019-04-22 | 2026-11-04 | 1154 | 00001 | 01154 |
| 3D Pro | 800 | 2021-09-14 | 2026-11-03 | 800 | 00001 | 00800 |
| Bingo18 | 701 | 2024-12-03 | 2026-11-05 | 98799 | 0083123 | 0194635 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-11-03 | 01419 | [10, 22, 31, 39, 43, 54, 14] | 2026-11-03T12:00:05Z |
| 2026-10-31 | 01418 | [12, 18, 22, 26, 28, 55, 11] | 2026-10-31T12:00:05Z |
| 2026-10-29 | 01417 | [9, 29, 33, 38, 45, 46, 53] | 2026-10-29T12:00:05Z |
| 2026-10-27 | 01416 | [9, 18, 27, 28, 31, 35, 50] | 2026-10-27T12:00:09Z |
| 2026-10-24 | 01415 | [6, 7, 18, 41, 44, 50, 53] | 2026-10-24T12:01:16.734372 |
| 2026-10-22 | 01414 | [14, 19, 24, 31, 34, 42, 37] | 2026-10-22T12:01:27.562980 |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.94 |  | 21 | 177 | 1.78 |  | 41 | 209 | 2.1 |
| 2 | 164 | 1.65 |  | 22 | 210 | 2.11 |  | 42 | 183 | 1.84 |
| 3 | 190 | 1.91 |  | 23 | 192 | 1.93 |  | 43 | 200 | 2.01 |
| 4 | 148 | 1.49 |  | 24 | 183 | 1.84 |  | 44 | 183 | 1.84 |
| 5 | 184 | 1.85 |  | 25 | 164 | 1.65 |  | 45 | 185 | 1.86 |
| 6 | 147 | 1.48 |  | 26 | 169 | 1.7 |  | 46 | 184 | 1.85 |
| 7 | 164 | 1.65 |  | 27 | 169 | 1.7 |  | 47 | 180 | 1.81 |
| 8 | 196 | 1.97 |  | 28 | 162 | 1.63 |  | 48 | 192 | 1.93 |
| 9 | 198 | 1.99 |  | 29 | 192 | 1.93 |  | 49 | 175 | 1.76 |
| 10 | 169 | 1.7 |  | 30 | 164 | 1.65 |  | 50 | 183 | 1.84 |
| 11 | 190 | 1.91 |  | 31 | 192 | 1.93 |  | 51 | 199 | 2.0 |
| 12 | 183 | 1.84 |  | 32 | 188 | 1.89 |  | 52 | 181 | 1.82 |
| 13 | 178 | 1.79 |  | 33 | 181 | 1.82 |  | 53 | 191 | 1.92 |
| 14 | 184 | 1.85 |  | 34 | 198 | 1.99 |  | 54 | 171 | 1.72 |
| 15 | 168 | 1.69 |  | 35 | 172 | 1.73 |  | 55 | 182 | 1.83 |
| 16 | 177 | 1.78 |  | 36 | 169 | 1.7 |  |  |  |  |
| 17 | 163 | 1.64 |  | 37 | 161 | 1.62 |  |  |  |  |
| 18 | 185 | 1.86 |  | 38 | 175 | 1.76 |  |  |  |  |
| 19 | 175 | 1.76 |  | 39 | 174 | 1.75 |  |  |  |  |
| 20 | 191 | 1.92 |  | 40 | 195 | 1.96 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 25 | 1 | 1.1 |  | 48 | 1 | 1.1 |
| 2 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 50 | 4 | 4.4 |
| 4 | 1 | 1.1 |  | 27 | 4 | 4.4 |  | 51 | 1 | 1.1 |
| 6 | 3 | 3.3 |  | 28 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 7 | 4 | 4.4 |  | 29 | 1 | 1.1 |  | 53 | 3 | 3.3 |
| 9 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 31 | 4 | 4.4 |  | 55 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 33 | 1 | 1.1 |  |  |  |  |
| 12 | 3 | 3.3 |  | 34 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 4 | 4.4 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 17 | 1 | 1.1 |  | 39 | 2 | 2.2 |  |  |  |  |
| 18 | 4 | 4.4 |  | 40 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 1 | 1.1 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |
| 23 | 3 | 3.3 |  | 45 | 3 | 3.3 |  |  |  |  |
| 24 | 3 | 3.3 |  | 46 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.86 |  | 21 | 2 | 1.14 |  | 41 | 3 | 1.71 |
| 2 | 3 | 1.71 |  | 22 | 4 | 2.29 |  | 42 | 2 | 1.14 |
| 3 | 1 | 0.57 |  | 23 | 5 | 2.86 |  | 43 | 2 | 1.14 |
| 4 | 4 | 2.29 |  | 24 | 5 | 2.86 |  | 44 | 1 | 0.57 |
| 5 | 2 | 1.14 |  | 25 | 5 | 2.86 |  | 45 | 4 | 2.29 |
| 6 | 4 | 2.29 |  | 26 | 3 | 1.71 |  | 46 | 2 | 1.14 |
| 7 | 7 | 4.0 |  | 27 | 7 | 4.0 |  | 47 | 2 | 1.14 |
| 8 | 1 | 0.57 |  | 28 | 4 | 2.29 |  | 48 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 29 | 1 | 0.57 |  | 49 | 1 | 0.57 |
| 10 | 3 | 1.71 |  | 30 | 2 | 1.14 |  | 50 | 6 | 3.43 |
| 11 | 8 | 4.57 |  | 31 | 5 | 2.86 |  | 51 | 2 | 1.14 |
| 12 | 3 | 1.71 |  | 32 | 2 | 1.14 |  | 52 | 4 | 2.29 |
| 13 | 5 | 2.86 |  | 33 | 1 | 0.57 |  | 53 | 4 | 2.29 |
| 14 | 6 | 3.43 |  | 34 | 2 | 1.14 |  | 54 | 4 | 2.29 |
| 15 | 2 | 1.14 |  | 35 | 2 | 1.14 |  | 55 | 3 | 1.71 |
| 16 | 2 | 1.14 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 3 | 1.71 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 7 | 4.0 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 1 | 0.57 |  | 39 | 2 | 1.14 |  |  |  |  |
| 20 | 2 | 1.14 |  | 40 | 1 | 0.57 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 6 | 2.26 |  | 22 | 4 | 1.5 |  | 42 | 4 | 1.5 |
| 3 | 3 | 1.13 |  | 23 | 5 | 1.88 |  | 43 | 2 | 0.75 |
| 4 | 4 | 1.5 |  | 24 | 7 | 2.63 |  | 44 | 3 | 1.13 |
| 5 | 6 | 2.26 |  | 25 | 7 | 2.63 |  | 45 | 8 | 3.01 |
| 6 | 4 | 1.5 |  | 26 | 4 | 1.5 |  | 46 | 4 | 1.5 |
| 7 | 9 | 3.38 |  | 27 | 9 | 3.38 |  | 47 | 5 | 1.88 |
| 8 | 4 | 1.5 |  | 28 | 4 | 1.5 |  | 48 | 3 | 1.13 |
| 9 | 7 | 2.63 |  | 29 | 5 | 1.88 |  | 49 | 2 | 0.75 |
| 10 | 5 | 1.88 |  | 30 | 4 | 1.5 |  | 50 | 8 | 3.01 |
| 11 | 11 | 4.14 |  | 31 | 8 | 3.01 |  | 51 | 3 | 1.13 |
| 12 | 3 | 1.13 |  | 32 | 2 | 0.75 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 3 | 1.13 |  | 53 | 4 | 1.5 |
| 14 | 7 | 2.63 |  | 34 | 3 | 1.13 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 2 | 0.75 |  | 55 | 4 | 1.5 |
| 16 | 4 | 1.5 |  | 36 | 3 | 1.13 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 10 | 3.76 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 4 | 1.5 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 3 | 1.13 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 56 |
| 32 | 2026-09-15 | 49 |
| 47 | 2026-09-15 | 49 |
| 3 | 2026-09-22 | 42 |
| 49 | 2026-09-26 | 38 |
| 36 | 2026-09-29 | 35 |
| 5 | 2026-10-01 | 33 |
| 15 | 2026-10-01 | 33 |
| 52 | 2026-10-08 | 26 |
| 17 | 2026-10-10 | 24 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 17 |
| 2 | 2026-10-13 | 21 |
| 3 | 2026-09-22 | 42 |
| 4 | 2026-10-15 | 19 |
| 5 | 2026-10-01 | 33 |
| 6 | 2026-10-24 | 10 |
| 7 | 2026-10-24 | 10 |
| 8 | 2026-09-08 | 56 |
| 9 | 2026-10-29 | 5 |
| 10 | 2026-11-03 | 0 |
| 11 | 2026-10-31 | 3 |
| 12 | 2026-10-31 | 3 |
| 13 | 2026-10-20 | 14 |
| 14 | 2026-11-03 | 0 |
| 15 | 2026-10-01 | 33 |
| 16 | 2026-10-17 | 17 |
| 17 | 2026-10-10 | 24 |
| 18 | 2026-10-31 | 3 |
| 19 | 2026-10-22 | 12 |
| 20 | 2026-10-20 | 14 |
| 21 | 2026-10-10 | 24 |
| 22 | 2026-11-03 | 0 |
| 23 | 2026-10-20 | 14 |
| 24 | 2026-10-22 | 12 |
| 25 | 2026-10-15 | 19 |
| 26 | 2026-10-31 | 3 |
| 27 | 2026-10-27 | 7 |
| 28 | 2026-10-31 | 3 |
| 29 | 2026-10-29 | 5 |
| 30 | 2026-10-20 | 14 |
| 31 | 2026-11-03 | 0 |
| 32 | 2026-09-15 | 49 |
| 33 | 2026-10-29 | 5 |
| 34 | 2026-10-22 | 12 |
| 35 | 2026-10-27 | 7 |
| 36 | 2026-09-29 | 35 |
| 37 | 2026-10-22 | 12 |
| 38 | 2026-10-29 | 5 |
| 39 | 2026-11-03 | 0 |
| 40 | 2026-10-13 | 21 |
| 41 | 2026-10-24 | 10 |
| 42 | 2026-10-22 | 12 |
| 43 | 2026-11-03 | 0 |
| 44 | 2026-10-24 | 10 |
| 45 | 2026-10-29 | 5 |
| 46 | 2026-10-29 | 5 |
| 47 | 2026-09-15 | 49 |
| 48 | 2026-10-17 | 17 |
| 49 | 2026-09-26 | 38 |
| 50 | 2026-10-27 | 7 |
| 51 | 2026-10-15 | 19 |
| 52 | 2026-10-08 | 26 |
| 53 | 2026-10-29 | 5 |
| 54 | 2026-11-03 | 0 |
| 55 | 2026-10-31 | 3 |



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

