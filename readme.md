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
| Power 655 | 1426 | 2017-08-01 | 2026-11-19 | 1426 | 00001 | 01426 |
| Power 645 | 1393 | 2017-10-25 | 2026-11-18 | 1393 | 00198 | 01590 |
| Power 535 | 509 | 2025-06-29 | 2026-11-19 | 1017 | 00001 | 01017 |
| Keno | 742 | 2022-12-04 | 2026-11-19 | 92557 | #0110271 | #0303568 |
| 3D | 1160 | 2019-04-22 | 2026-11-18 | 1160 | 00001 | 01160 |
| 3D Pro | 807 | 2021-09-14 | 2026-11-19 | 807 | 00001 | 00807 |
| Bingo18 | 715 | 2024-12-03 | 2026-11-19 | 101145 | 0083123 | 0196981 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-11-19 | 01426 | [3, 13, 21, 23, 38, 43, 16] | 2026-11-19T12:00:05Z |
| 2026-11-17 | 01425 | [6, 20, 36, 41, 49, 52, 34] | 2026-11-18T00:00:05Z |
| 2026-11-14 | 01424 | [5, 28, 36, 42, 45, 47, 51] | 2026-11-14T12:00:05Z |
| 2026-11-12 | 01423 | [17, 25, 33, 34, 35, 36, 48] | 2026-11-12T12:00:05Z |
| 2026-11-10 | 01422 | [1, 2, 21, 38, 39, 51, 12] | 2026-11-10T12:00:05Z |
| 2026-11-07 | 01421 | [5, 19, 20, 26, 44, 53, 39] | 2026-11-07T12:00:05Z |
| 2026-11-05 | 01420 | [6, 20, 34, 41, 49, 52, 36] | 2026-11-05T12:00:05Z |
| 2026-11-03 | 01419 | [10, 22, 31, 39, 43, 54, 14] | 2026-11-03T12:00:05Z |
| 2026-10-31 | 01418 | [12, 18, 22, 26, 28, 55, 11] | 2026-10-31T12:00:05Z |
| 2026-10-29 | 01417 | [9, 29, 33, 38, 45, 46, 53] | 2026-10-29T12:00:05Z |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 194 | 1.94 |  | 21 | 179 | 1.79 |  | 41 | 211 | 2.11 |
| 2 | 165 | 1.65 |  | 22 | 210 | 2.1 |  | 42 | 184 | 1.84 |
| 3 | 191 | 1.91 |  | 23 | 193 | 1.93 |  | 43 | 201 | 2.01 |
| 4 | 148 | 1.48 |  | 24 | 183 | 1.83 |  | 44 | 184 | 1.84 |
| 5 | 186 | 1.86 |  | 25 | 165 | 1.65 |  | 45 | 186 | 1.86 |
| 6 | 149 | 1.49 |  | 26 | 170 | 1.7 |  | 46 | 184 | 1.84 |
| 7 | 164 | 1.64 |  | 27 | 169 | 1.69 |  | 47 | 181 | 1.81 |
| 8 | 196 | 1.96 |  | 28 | 163 | 1.63 |  | 48 | 193 | 1.93 |
| 9 | 198 | 1.98 |  | 29 | 192 | 1.92 |  | 49 | 177 | 1.77 |
| 10 | 169 | 1.69 |  | 30 | 164 | 1.64 |  | 50 | 183 | 1.83 |
| 11 | 190 | 1.9 |  | 31 | 192 | 1.92 |  | 51 | 201 | 2.01 |
| 12 | 184 | 1.84 |  | 32 | 188 | 1.88 |  | 52 | 183 | 1.83 |
| 13 | 179 | 1.79 |  | 33 | 182 | 1.82 |  | 53 | 192 | 1.92 |
| 14 | 184 | 1.84 |  | 34 | 201 | 2.01 |  | 54 | 171 | 1.71 |
| 15 | 168 | 1.68 |  | 35 | 173 | 1.73 |  | 55 | 182 | 1.82 |
| 16 | 178 | 1.78 |  | 36 | 173 | 1.73 |  |  |  |  |
| 17 | 164 | 1.64 |  | 37 | 161 | 1.61 |  |  |  |  |
| 18 | 185 | 1.85 |  | 38 | 177 | 1.77 |  |  |  |  |
| 19 | 176 | 1.76 |  | 39 | 176 | 1.76 |  |  |  |  |
| 20 | 194 | 1.94 |  | 40 | 195 | 1.95 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.02 |  | 24 | 1 | 1.02 |  | 46 | 1 | 1.02 |
| 2 | 1 | 1.02 |  | 25 | 1 | 1.02 |  | 47 | 1 | 1.02 |
| 3 | 1 | 1.02 |  | 26 | 2 | 2.04 |  | 48 | 1 | 1.02 |
| 5 | 2 | 2.04 |  | 27 | 1 | 1.02 |  | 49 | 2 | 2.04 |
| 6 | 3 | 3.06 |  | 28 | 3 | 3.06 |  | 50 | 3 | 3.06 |
| 7 | 1 | 1.02 |  | 29 | 1 | 1.02 |  | 51 | 2 | 2.04 |
| 9 | 2 | 2.04 |  | 30 | 1 | 1.02 |  | 52 | 2 | 2.04 |
| 10 | 1 | 1.02 |  | 31 | 3 | 3.06 |  | 53 | 3 | 3.06 |
| 11 | 1 | 1.02 |  | 33 | 2 | 2.04 |  | 54 | 1 | 1.02 |
| 12 | 2 | 2.04 |  | 34 | 4 | 4.08 |  | 55 | 2 | 2.04 |
| 13 | 2 | 2.04 |  | 35 | 2 | 2.04 |  |  |  |  |
| 14 | 2 | 2.04 |  | 36 | 4 | 4.08 |  |  |  |  |
| 16 | 1 | 1.02 |  | 37 | 1 | 1.02 |  |  |  |  |
| 17 | 1 | 1.02 |  | 38 | 3 | 3.06 |  |  |  |  |
| 18 | 3 | 3.06 |  | 39 | 3 | 3.06 |  |  |  |  |
| 19 | 2 | 2.04 |  | 41 | 3 | 3.06 |  |  |  |  |
| 20 | 4 | 4.08 |  | 42 | 2 | 2.04 |  |  |  |  |
| 21 | 2 | 2.04 |  | 43 | 2 | 2.04 |  |  |  |  |
| 22 | 2 | 2.04 |  | 44 | 2 | 2.04 |  |  |  |  |
| 23 | 2 | 2.04 |  | 45 | 3 | 3.06 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 22 | 2 | 1.1 |  | 43 | 2 | 1.1 |
| 2 | 3 | 1.65 |  | 23 | 5 | 2.75 |  | 44 | 2 | 1.1 |
| 3 | 2 | 1.1 |  | 24 | 3 | 1.65 |  | 45 | 4 | 2.2 |
| 4 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 46 | 2 | 1.1 |
| 5 | 3 | 1.65 |  | 26 | 4 | 2.2 |  | 47 | 1 | 0.55 |
| 6 | 5 | 2.75 |  | 27 | 5 | 2.75 |  | 48 | 3 | 1.65 |
| 7 | 5 | 2.75 |  | 28 | 4 | 2.2 |  | 49 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 29 | 1 | 0.55 |  | 50 | 4 | 2.2 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 51 | 3 | 1.65 |
| 11 | 5 | 2.75 |  | 31 | 4 | 2.2 |  | 52 | 5 | 2.75 |
| 12 | 4 | 2.2 |  | 33 | 2 | 1.1 |  | 53 | 4 | 2.2 |
| 13 | 6 | 3.3 |  | 34 | 5 | 2.75 |  | 54 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 35 | 3 | 1.65 |  | 55 | 3 | 1.65 |
| 15 | 1 | 0.55 |  | 36 | 5 | 2.75 |  |  |  |  |
| 16 | 3 | 1.65 |  | 37 | 2 | 1.1 |  |  |  |  |
| 17 | 3 | 1.65 |  | 38 | 4 | 2.2 |  |  |  |  |
| 18 | 6 | 3.3 |  | 39 | 4 | 2.2 |  |  |  |  |
| 19 | 2 | 1.1 |  | 40 | 1 | 0.55 |  |  |  |  |
| 20 | 5 | 2.75 |  | 41 | 5 | 2.75 |  |  |  |  |
| 21 | 4 | 2.2 |  | 42 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 7 | 2.56 |  | 41 | 6 | 2.2 |
| 2 | 4 | 1.47 |  | 22 | 4 | 1.47 |  | 42 | 4 | 1.47 |
| 3 | 3 | 1.1 |  | 23 | 6 | 2.2 |  | 43 | 3 | 1.1 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 7 | 2.56 |  | 45 | 7 | 2.56 |
| 6 | 6 | 2.2 |  | 26 | 5 | 1.83 |  | 46 | 3 | 1.1 |
| 7 | 8 | 2.93 |  | 27 | 7 | 2.56 |  | 47 | 5 | 1.83 |
| 8 | 3 | 1.1 |  | 28 | 5 | 1.83 |  | 48 | 3 | 1.1 |
| 9 | 6 | 2.2 |  | 29 | 2 | 0.73 |  | 49 | 4 | 1.47 |
| 10 | 5 | 1.83 |  | 30 | 2 | 0.73 |  | 50 | 6 | 2.2 |
| 11 | 11 | 4.03 |  | 31 | 7 | 2.56 |  | 51 | 4 | 1.47 |
| 12 | 4 | 1.47 |  | 32 | 2 | 0.73 |  | 52 | 6 | 2.2 |
| 13 | 7 | 2.56 |  | 33 | 3 | 1.1 |  | 53 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 34 | 6 | 2.2 |  | 54 | 4 | 1.47 |
| 15 | 3 | 1.1 |  | 35 | 3 | 1.1 |  | 55 | 4 | 1.47 |
| 16 | 4 | 1.47 |  | 36 | 7 | 2.56 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 9 | 3.3 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 4 | 1.47 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 2 | 0.73 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 72 |
| 32 | 2026-09-15 | 65 |
| 15 | 2026-10-01 | 49 |
| 40 | 2026-10-13 | 37 |
| 4 | 2026-10-15 | 35 |
| 30 | 2026-10-20 | 30 |
| 24 | 2026-10-22 | 28 |
| 37 | 2026-10-22 | 28 |
| 7 | 2026-10-24 | 26 |
| 27 | 2026-10-27 | 23 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-11-10 | 9 |
| 2 | 2026-11-10 | 9 |
| 3 | 2026-11-19 | 0 |
| 4 | 2026-10-15 | 35 |
| 5 | 2026-11-14 | 5 |
| 6 | 2026-11-17 | 2 |
| 7 | 2026-10-24 | 26 |
| 8 | 2026-09-08 | 72 |
| 9 | 2026-10-29 | 21 |
| 10 | 2026-11-03 | 16 |
| 11 | 2026-10-31 | 19 |
| 12 | 2026-11-10 | 9 |
| 13 | 2026-11-19 | 0 |
| 14 | 2026-11-03 | 16 |
| 15 | 2026-10-01 | 49 |
| 16 | 2026-11-19 | 0 |
| 17 | 2026-11-12 | 7 |
| 18 | 2026-10-31 | 19 |
| 19 | 2026-11-07 | 12 |
| 20 | 2026-11-17 | 2 |
| 21 | 2026-11-19 | 0 |
| 22 | 2026-11-03 | 16 |
| 23 | 2026-11-19 | 0 |
| 24 | 2026-10-22 | 28 |
| 25 | 2026-11-12 | 7 |
| 26 | 2026-11-07 | 12 |
| 27 | 2026-10-27 | 23 |
| 28 | 2026-11-14 | 5 |
| 29 | 2026-10-29 | 21 |
| 30 | 2026-10-20 | 30 |
| 31 | 2026-11-03 | 16 |
| 32 | 2026-09-15 | 65 |
| 33 | 2026-11-12 | 7 |
| 34 | 2026-11-17 | 2 |
| 35 | 2026-11-12 | 7 |
| 36 | 2026-11-17 | 2 |
| 37 | 2026-10-22 | 28 |
| 38 | 2026-11-19 | 0 |
| 39 | 2026-11-10 | 9 |
| 40 | 2026-10-13 | 37 |
| 41 | 2026-11-17 | 2 |
| 42 | 2026-11-14 | 5 |
| 43 | 2026-11-19 | 0 |
| 44 | 2026-11-07 | 12 |
| 45 | 2026-11-14 | 5 |
| 46 | 2026-10-29 | 21 |
| 47 | 2026-11-14 | 5 |
| 48 | 2026-11-12 | 7 |
| 49 | 2026-11-17 | 2 |
| 50 | 2026-10-27 | 23 |
| 51 | 2026-11-14 | 5 |
| 52 | 2026-11-17 | 2 |
| 53 | 2026-11-07 | 12 |
| 54 | 2026-11-03 | 16 |
| 55 | 2026-10-31 | 19 |



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

