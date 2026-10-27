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
| Power 655 | 1415 | 2017-08-01 | 2026-10-24 | 1415 | 00001 | 01415 |
| Power 645 | 1383 | 2017-10-25 | 2026-10-25 | 1383 | 00198 | 01580 |
| Power 535 | 485 | 2025-06-29 | 2026-10-26 | 970 | 00001 | 00970 |
| Keno | 719 | 2022-12-04 | 2026-10-27 | 89730 | #0110271 | #0300741 |
| 3D | 1150 | 2019-04-22 | 2026-10-26 | 1150 | 00001 | 01150 |
| 3D Pro | 796 | 2021-09-14 | 2026-10-24 | 796 | 00001 | 00796 |
| Bingo18 | 692 | 2024-12-03 | 2026-10-27 | 97368 | 0083123 | 0193204 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-24 | 01415 | [6, 7, 18, 41, 44, 50, 53] | 2026-10-24T12:01:16.734372 |
| 2026-10-22 | 01414 | [14, 19, 24, 31, 34, 42, 37] | 2026-10-22T12:01:27.562980 |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 209 | 2.11 |
| 2 | 164 | 1.66 |  | 22 | 208 | 2.1 |  | 42 | 183 | 1.85 |
| 3 | 190 | 1.92 |  | 23 | 192 | 1.94 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.49 |  | 24 | 183 | 1.85 |  | 44 | 183 | 1.85 |
| 5 | 184 | 1.86 |  | 25 | 164 | 1.66 |  | 45 | 184 | 1.86 |
| 6 | 147 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 164 | 1.66 |  | 27 | 168 | 1.7 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.98 |  | 28 | 160 | 1.62 |  | 48 | 192 | 1.94 |
| 9 | 196 | 1.98 |  | 29 | 191 | 1.93 |  | 49 | 175 | 1.77 |
| 10 | 168 | 1.7 |  | 30 | 164 | 1.66 |  | 50 | 182 | 1.84 |
| 11 | 189 | 1.91 |  | 31 | 190 | 1.92 |  | 51 | 199 | 2.01 |
| 12 | 182 | 1.84 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 178 | 1.8 |  | 33 | 180 | 1.82 |  | 53 | 190 | 1.92 |
| 14 | 183 | 1.85 |  | 34 | 198 | 2.0 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 181 | 1.83 |
| 16 | 177 | 1.79 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 161 | 1.63 |  |  |  |  |
| 18 | 183 | 1.85 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 175 | 1.77 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 191 | 1.93 |  | 40 | 195 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.57 |  | 25 | 1 | 1.19 |  | 54 | 1 | 1.19 |
| 2 | 2 | 2.38 |  | 26 | 1 | 1.19 |  | 55 | 2 | 2.38 |
| 4 | 3 | 3.57 |  | 27 | 3 | 3.57 |  |  |  |  |
| 5 | 1 | 1.19 |  | 30 | 2 | 2.38 |  |  |  |  |
| 6 | 3 | 3.57 |  | 31 | 2 | 2.38 |  |  |  |  |
| 7 | 5 | 5.95 |  | 34 | 2 | 2.38 |  |  |  |  |
| 10 | 1 | 1.19 |  | 35 | 1 | 1.19 |  |  |  |  |
| 11 | 3 | 3.57 |  | 36 | 1 | 1.19 |  |  |  |  |
| 12 | 2 | 2.38 |  | 37 | 2 | 2.38 |  |  |  |  |
| 13 | 4 | 4.76 |  | 39 | 1 | 1.19 |  |  |  |  |
| 14 | 3 | 3.57 |  | 40 | 1 | 1.19 |  |  |  |  |
| 15 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 16 | 2 | 2.38 |  | 42 | 2 | 2.38 |  |  |  |  |
| 17 | 2 | 2.38 |  | 44 | 1 | 1.19 |  |  |  |  |
| 18 | 3 | 3.57 |  | 45 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 48 | 1 | 1.19 |  |  |  |  |
| 20 | 2 | 2.38 |  | 50 | 3 | 3.57 |  |  |  |  |
| 21 | 1 | 1.19 |  | 51 | 1 | 1.19 |  |  |  |  |
| 23 | 3 | 3.57 |  | 52 | 2 | 2.38 |  |  |  |  |
| 24 | 3 | 3.57 |  | 53 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.43 |  | 21 | 3 | 1.71 |  | 41 | 4 | 2.29 |
| 2 | 3 | 1.71 |  | 22 | 2 | 1.14 |  | 42 | 3 | 1.71 |
| 3 | 1 | 0.57 |  | 23 | 5 | 2.86 |  | 43 | 1 | 0.57 |
| 4 | 4 | 2.29 |  | 24 | 7 | 4.0 |  | 44 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 25 | 5 | 2.86 |  | 45 | 5 | 2.86 |
| 6 | 4 | 2.29 |  | 26 | 2 | 1.14 |  | 46 | 2 | 1.14 |
| 7 | 7 | 4.0 |  | 27 | 6 | 3.43 |  | 47 | 4 | 2.29 |
| 8 | 2 | 1.14 |  | 28 | 2 | 1.14 |  | 48 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 29 | 1 | 0.57 |  | 49 | 2 | 1.14 |
| 10 | 3 | 1.71 |  | 30 | 2 | 1.14 |  | 50 | 5 | 2.86 |
| 11 | 9 | 5.14 |  | 31 | 4 | 2.29 |  | 51 | 2 | 1.14 |
| 12 | 2 | 1.14 |  | 32 | 2 | 1.14 |  | 52 | 4 | 2.29 |
| 13 | 5 | 2.86 |  | 33 | 1 | 0.57 |  | 53 | 3 | 1.71 |
| 14 | 5 | 2.86 |  | 34 | 3 | 1.71 |  | 54 | 3 | 1.71 |
| 15 | 3 | 1.71 |  | 35 | 1 | 0.57 |  | 55 | 3 | 1.71 |
| 16 | 3 | 1.71 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 5 | 2.86 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 1 | 0.57 |  | 39 | 1 | 0.57 |  |  |  |  |
| 20 | 2 | 1.14 |  | 40 | 1 | 0.57 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 7 | 2.63 |  | 22 | 2 | 0.75 |  | 42 | 5 | 1.88 |
| 3 | 3 | 1.13 |  | 23 | 6 | 2.26 |  | 43 | 2 | 0.75 |
| 4 | 4 | 1.5 |  | 24 | 8 | 3.01 |  | 44 | 4 | 1.5 |
| 5 | 6 | 2.26 |  | 25 | 7 | 2.63 |  | 45 | 7 | 2.63 |
| 6 | 4 | 1.5 |  | 26 | 3 | 1.13 |  | 46 | 3 | 1.13 |
| 7 | 9 | 3.38 |  | 27 | 8 | 3.01 |  | 47 | 6 | 2.26 |
| 8 | 4 | 1.5 |  | 28 | 3 | 1.13 |  | 48 | 3 | 1.13 |
| 9 | 5 | 1.88 |  | 29 | 4 | 1.5 |  | 49 | 4 | 1.5 |
| 10 | 4 | 1.5 |  | 30 | 4 | 1.5 |  | 50 | 7 | 2.63 |
| 11 | 11 | 4.14 |  | 31 | 7 | 2.63 |  | 51 | 5 | 1.88 |
| 12 | 3 | 1.13 |  | 32 | 2 | 0.75 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 2 | 0.75 |  | 53 | 3 | 1.13 |
| 14 | 9 | 3.38 |  | 34 | 3 | 1.13 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 2 | 0.75 |  | 55 | 5 | 1.88 |
| 16 | 5 | 1.88 |  | 36 | 3 | 1.13 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 9 | 3.38 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 5 | 1.88 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 4 | 1.5 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 29 | 2026-08-29 | 56 |
| 33 | 2026-09-05 | 49 |
| 8 | 2026-09-08 | 46 |
| 43 | 2026-09-12 | 42 |
| 32 | 2026-09-15 | 39 |
| 47 | 2026-09-15 | 39 |
| 22 | 2026-09-19 | 35 |
| 3 | 2026-09-22 | 32 |
| 9 | 2026-09-22 | 32 |
| 46 | 2026-09-22 | 32 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 7 |
| 2 | 2026-10-13 | 11 |
| 3 | 2026-09-22 | 32 |
| 4 | 2026-10-15 | 9 |
| 5 | 2026-10-01 | 23 |
| 6 | 2026-10-24 | 0 |
| 7 | 2026-10-24 | 0 |
| 8 | 2026-09-08 | 46 |
| 9 | 2026-09-22 | 32 |
| 10 | 2026-10-17 | 7 |
| 11 | 2026-10-17 | 7 |
| 12 | 2026-10-17 | 7 |
| 13 | 2026-10-20 | 4 |
| 14 | 2026-10-22 | 2 |
| 15 | 2026-10-01 | 23 |
| 16 | 2026-10-17 | 7 |
| 17 | 2026-10-10 | 14 |
| 18 | 2026-10-24 | 0 |
| 19 | 2026-10-22 | 2 |
| 20 | 2026-10-20 | 4 |
| 21 | 2026-10-10 | 14 |
| 22 | 2026-09-19 | 35 |
| 23 | 2026-10-20 | 4 |
| 24 | 2026-10-22 | 2 |
| 25 | 2026-10-15 | 9 |
| 26 | 2026-10-13 | 11 |
| 27 | 2026-10-13 | 11 |
| 28 | 2026-09-24 | 30 |
| 29 | 2026-08-29 | 56 |
| 30 | 2026-10-20 | 4 |
| 31 | 2026-10-22 | 2 |
| 32 | 2026-09-15 | 39 |
| 33 | 2026-09-05 | 49 |
| 34 | 2026-10-22 | 2 |
| 35 | 2026-09-29 | 25 |
| 36 | 2026-09-29 | 25 |
| 37 | 2026-10-22 | 2 |
| 38 | 2026-09-26 | 28 |
| 39 | 2026-10-10 | 14 |
| 40 | 2026-10-13 | 11 |
| 41 | 2026-10-24 | 0 |
| 42 | 2026-10-22 | 2 |
| 43 | 2026-09-12 | 42 |
| 44 | 2026-10-24 | 0 |
| 45 | 2026-10-20 | 4 |
| 46 | 2026-09-22 | 32 |
| 47 | 2026-09-15 | 39 |
| 48 | 2026-10-17 | 7 |
| 49 | 2026-09-26 | 28 |
| 50 | 2026-10-24 | 0 |
| 51 | 2026-10-15 | 9 |
| 52 | 2026-10-08 | 16 |
| 53 | 2026-10-24 | 0 |
| 54 | 2026-10-03 | 21 |
| 55 | 2026-10-20 | 4 |



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

