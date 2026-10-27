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
| Power 655 | 1416 | 2017-08-01 | 2026-10-27 | 1416 | 00001 | 01416 |
| Power 645 | 1383 | 2017-10-25 | 2026-10-25 | 1383 | 00198 | 01580 |
| Power 535 | 486 | 2025-06-29 | 2026-10-27 | 971 | 00001 | 00971 |
| Keno | 719 | 2022-12-04 | 2026-10-27 | 89820 | #0110271 | #0300831 |
| 3D | 1150 | 2019-04-22 | 2026-10-26 | 1150 | 00001 | 01150 |
| 3D Pro | 797 | 2021-09-14 | 2026-10-27 | 797 | 00001 | 00797 |
| Bingo18 | 692 | 2024-12-03 | 2026-10-27 | 97487 | 0083123 | 0193323 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-27 | 01416 | [9, 18, 27, 28, 31, 35, 50] | 2026-10-27T12:00:09Z |
| 2026-10-24 | 01415 | [6, 7, 18, 41, 44, 50, 53] | 2026-10-24T12:01:16.734372 |
| 2026-10-22 | 01414 | [14, 19, 24, 31, 34, 42, 37] | 2026-10-22T12:01:27.562980 |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 209 | 2.11 |
| 2 | 164 | 1.65 |  | 22 | 208 | 2.1 |  | 42 | 183 | 1.85 |
| 3 | 190 | 1.92 |  | 23 | 192 | 1.94 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.49 |  | 24 | 183 | 1.85 |  | 44 | 183 | 1.85 |
| 5 | 184 | 1.86 |  | 25 | 164 | 1.65 |  | 45 | 184 | 1.86 |
| 6 | 147 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 164 | 1.65 |  | 27 | 169 | 1.71 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.98 |  | 28 | 161 | 1.62 |  | 48 | 192 | 1.94 |
| 9 | 197 | 1.99 |  | 29 | 191 | 1.93 |  | 49 | 175 | 1.77 |
| 10 | 168 | 1.7 |  | 30 | 164 | 1.65 |  | 50 | 183 | 1.85 |
| 11 | 189 | 1.91 |  | 31 | 191 | 1.93 |  | 51 | 199 | 2.01 |
| 12 | 182 | 1.84 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 178 | 1.8 |  | 33 | 180 | 1.82 |  | 53 | 190 | 1.92 |
| 14 | 183 | 1.85 |  | 34 | 198 | 2.0 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 172 | 1.74 |  | 55 | 181 | 1.83 |
| 16 | 177 | 1.79 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.64 |  | 37 | 161 | 1.62 |  |  |  |  |
| 18 | 184 | 1.86 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 175 | 1.77 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 191 | 1.93 |  | 40 | 195 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 24 | 3 | 3.3 |  | 52 | 2 | 2.2 |
| 2 | 2 | 2.2 |  | 25 | 1 | 1.1 |  | 53 | 2 | 2.2 |
| 4 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 27 | 4 | 4.4 |  | 55 | 2 | 2.2 |
| 6 | 3 | 3.3 |  | 28 | 1 | 1.1 |  |  |  |  |
| 7 | 5 | 5.49 |  | 30 | 2 | 2.2 |  |  |  |  |
| 9 | 1 | 1.1 |  | 31 | 3 | 3.3 |  |  |  |  |
| 10 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 11 | 3 | 3.3 |  | 35 | 2 | 2.2 |  |  |  |  |
| 12 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 4 | 4.4 |  | 37 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 39 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 40 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 18 | 4 | 4.4 |  | 44 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 48 | 1 | 1.1 |  |  |  |  |
| 21 | 1 | 1.1 |  | 50 | 4 | 4.4 |  |  |  |  |
| 23 | 3 | 3.3 |  | 51 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 21 | 3 | 1.65 |  | 41 | 4 | 2.2 |
| 2 | 3 | 1.65 |  | 22 | 2 | 1.1 |  | 42 | 3 | 1.65 |
| 3 | 1 | 0.55 |  | 23 | 5 | 2.75 |  | 43 | 1 | 0.55 |
| 4 | 4 | 2.2 |  | 24 | 7 | 3.85 |  | 44 | 2 | 1.1 |
| 5 | 3 | 1.65 |  | 25 | 5 | 2.75 |  | 45 | 5 | 2.75 |
| 6 | 4 | 2.2 |  | 26 | 2 | 1.1 |  | 46 | 2 | 1.1 |
| 7 | 7 | 3.85 |  | 27 | 7 | 3.85 |  | 47 | 4 | 2.2 |
| 8 | 2 | 1.1 |  | 28 | 3 | 1.65 |  | 48 | 2 | 1.1 |
| 9 | 4 | 2.2 |  | 29 | 1 | 0.55 |  | 49 | 2 | 1.1 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 6 | 3.3 |
| 11 | 9 | 4.95 |  | 31 | 5 | 2.75 |  | 51 | 2 | 1.1 |
| 12 | 2 | 1.1 |  | 32 | 2 | 1.1 |  | 52 | 4 | 2.2 |
| 13 | 5 | 2.75 |  | 33 | 1 | 0.55 |  | 53 | 3 | 1.65 |
| 14 | 5 | 2.75 |  | 34 | 3 | 1.65 |  | 54 | 3 | 1.65 |
| 15 | 3 | 1.65 |  | 35 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 16 | 3 | 1.65 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 6 | 3.3 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 1 | 0.55 |  | 39 | 1 | 0.55 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 1 | 0.55 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 5 | 1.83 |  | 41 | 5 | 1.83 |
| 2 | 7 | 2.56 |  | 22 | 2 | 0.73 |  | 42 | 5 | 1.83 |
| 3 | 3 | 1.1 |  | 23 | 6 | 2.2 |  | 43 | 2 | 0.73 |
| 4 | 4 | 1.47 |  | 24 | 8 | 2.93 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 7 | 2.56 |  | 45 | 7 | 2.56 |
| 6 | 4 | 1.47 |  | 26 | 3 | 1.1 |  | 46 | 3 | 1.1 |
| 7 | 9 | 3.3 |  | 27 | 9 | 3.3 |  | 47 | 6 | 2.2 |
| 8 | 4 | 1.47 |  | 28 | 4 | 1.47 |  | 48 | 3 | 1.1 |
| 9 | 6 | 2.2 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 8 | 2.93 |
| 11 | 11 | 4.03 |  | 31 | 8 | 2.93 |  | 51 | 5 | 1.83 |
| 12 | 3 | 1.1 |  | 32 | 2 | 0.73 |  | 52 | 4 | 1.47 |
| 13 | 6 | 2.2 |  | 33 | 2 | 0.73 |  | 53 | 3 | 1.1 |
| 14 | 9 | 3.3 |  | 34 | 3 | 1.1 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 3 | 1.1 |  | 55 | 5 | 1.83 |
| 16 | 5 | 1.83 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 10 | 3.66 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 4 | 1.47 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 29 | 2026-08-29 | 59 |
| 33 | 2026-09-05 | 52 |
| 8 | 2026-09-08 | 49 |
| 43 | 2026-09-12 | 45 |
| 32 | 2026-09-15 | 42 |
| 47 | 2026-09-15 | 42 |
| 22 | 2026-09-19 | 38 |
| 3 | 2026-09-22 | 35 |
| 46 | 2026-09-22 | 35 |
| 38 | 2026-09-26 | 31 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 10 |
| 2 | 2026-10-13 | 14 |
| 3 | 2026-09-22 | 35 |
| 4 | 2026-10-15 | 12 |
| 5 | 2026-10-01 | 26 |
| 6 | 2026-10-24 | 3 |
| 7 | 2026-10-24 | 3 |
| 8 | 2026-09-08 | 49 |
| 9 | 2026-10-27 | 0 |
| 10 | 2026-10-17 | 10 |
| 11 | 2026-10-17 | 10 |
| 12 | 2026-10-17 | 10 |
| 13 | 2026-10-20 | 7 |
| 14 | 2026-10-22 | 5 |
| 15 | 2026-10-01 | 26 |
| 16 | 2026-10-17 | 10 |
| 17 | 2026-10-10 | 17 |
| 18 | 2026-10-27 | 0 |
| 19 | 2026-10-22 | 5 |
| 20 | 2026-10-20 | 7 |
| 21 | 2026-10-10 | 17 |
| 22 | 2026-09-19 | 38 |
| 23 | 2026-10-20 | 7 |
| 24 | 2026-10-22 | 5 |
| 25 | 2026-10-15 | 12 |
| 26 | 2026-10-13 | 14 |
| 27 | 2026-10-27 | 0 |
| 28 | 2026-10-27 | 0 |
| 29 | 2026-08-29 | 59 |
| 30 | 2026-10-20 | 7 |
| 31 | 2026-10-27 | 0 |
| 32 | 2026-09-15 | 42 |
| 33 | 2026-09-05 | 52 |
| 34 | 2026-10-22 | 5 |
| 35 | 2026-10-27 | 0 |
| 36 | 2026-09-29 | 28 |
| 37 | 2026-10-22 | 5 |
| 38 | 2026-09-26 | 31 |
| 39 | 2026-10-10 | 17 |
| 40 | 2026-10-13 | 14 |
| 41 | 2026-10-24 | 3 |
| 42 | 2026-10-22 | 5 |
| 43 | 2026-09-12 | 45 |
| 44 | 2026-10-24 | 3 |
| 45 | 2026-10-20 | 7 |
| 46 | 2026-09-22 | 35 |
| 47 | 2026-09-15 | 42 |
| 48 | 2026-10-17 | 10 |
| 49 | 2026-09-26 | 31 |
| 50 | 2026-10-27 | 0 |
| 51 | 2026-10-15 | 12 |
| 52 | 2026-10-08 | 19 |
| 53 | 2026-10-24 | 3 |
| 54 | 2026-10-03 | 24 |
| 55 | 2026-10-20 | 7 |



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

