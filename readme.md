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
| Power 655 | 1427 | 2017-08-01 | 2026-11-21 | 1427 | 00001 | 01427 |
| Power 645 | 1394 | 2017-10-25 | 2026-11-20 | 1394 | 00198 | 01591 |
| Power 535 | 511 | 2025-06-29 | 2026-11-21 | 1021 | 00001 | 01021 |
| Keno | 744 | 2022-12-04 | 2026-11-21 | 92795 | #0110271 | #0303806 |
| 3D | 1161 | 2019-04-22 | 2026-11-20 | 1161 | 00001 | 01161 |
| 3D Pro | 808 | 2021-09-14 | 2026-11-21 | 808 | 00001 | 00808 |
| Bingo18 | 717 | 2024-12-03 | 2026-11-21 | 101462 | 0083123 | 0197298 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-11-21 | 01427 | [7, 29, 44, 45, 50, 54, 39] | 2026-11-21T12:00:05Z |
| 2026-11-19 | 01426 | [3, 13, 21, 23, 38, 43, 16] | 2026-11-19T12:00:05Z |
| 2026-11-17 | 01425 | [6, 20, 36, 41, 49, 52, 34] | 2026-11-18T00:00:05Z |
| 2026-11-14 | 01424 | [5, 28, 36, 42, 45, 47, 51] | 2026-11-14T12:00:05Z |
| 2026-11-12 | 01423 | [17, 25, 33, 34, 35, 36, 48] | 2026-11-12T12:00:05Z |
| 2026-11-10 | 01422 | [1, 2, 21, 38, 39, 51, 12] | 2026-11-10T12:00:05Z |
| 2026-11-07 | 01421 | [5, 19, 20, 26, 44, 53, 39] | 2026-11-07T12:00:05Z |
| 2026-11-05 | 01420 | [6, 20, 34, 41, 49, 52, 36] | 2026-11-05T12:00:05Z |
| 2026-11-03 | 01419 | [10, 22, 31, 39, 43, 54, 14] | 2026-11-03T12:00:05Z |
| 2026-10-31 | 01418 | [12, 18, 22, 26, 28, 55, 11] | 2026-10-31T12:00:05Z |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 194 | 1.94 |  | 21 | 179 | 1.79 |  | 41 | 211 | 2.11 |
| 2 | 165 | 1.65 |  | 22 | 210 | 2.1 |  | 42 | 184 | 1.84 |
| 3 | 191 | 1.91 |  | 23 | 193 | 1.93 |  | 43 | 201 | 2.01 |
| 4 | 148 | 1.48 |  | 24 | 183 | 1.83 |  | 44 | 185 | 1.85 |
| 5 | 186 | 1.86 |  | 25 | 165 | 1.65 |  | 45 | 187 | 1.87 |
| 6 | 149 | 1.49 |  | 26 | 170 | 1.7 |  | 46 | 184 | 1.84 |
| 7 | 165 | 1.65 |  | 27 | 169 | 1.69 |  | 47 | 181 | 1.81 |
| 8 | 196 | 1.96 |  | 28 | 163 | 1.63 |  | 48 | 193 | 1.93 |
| 9 | 198 | 1.98 |  | 29 | 193 | 1.93 |  | 49 | 177 | 1.77 |
| 10 | 169 | 1.69 |  | 30 | 164 | 1.64 |  | 50 | 184 | 1.84 |
| 11 | 190 | 1.9 |  | 31 | 192 | 1.92 |  | 51 | 201 | 2.01 |
| 12 | 184 | 1.84 |  | 32 | 188 | 1.88 |  | 52 | 183 | 1.83 |
| 13 | 179 | 1.79 |  | 33 | 182 | 1.82 |  | 53 | 192 | 1.92 |
| 14 | 184 | 1.84 |  | 34 | 201 | 2.01 |  | 54 | 172 | 1.72 |
| 15 | 168 | 1.68 |  | 35 | 173 | 1.73 |  | 55 | 182 | 1.82 |
| 16 | 178 | 1.78 |  | 36 | 173 | 1.73 |  |  |  |  |
| 17 | 164 | 1.64 |  | 37 | 161 | 1.61 |  |  |  |  |
| 18 | 185 | 1.85 |  | 38 | 177 | 1.77 |  |  |  |  |
| 19 | 176 | 1.76 |  | 39 | 177 | 1.77 |  |  |  |  |
| 20 | 194 | 1.94 |  | 40 | 195 | 1.95 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.02 |  | 24 | 1 | 1.02 |  | 47 | 1 | 1.02 |
| 2 | 1 | 1.02 |  | 25 | 1 | 1.02 |  | 48 | 1 | 1.02 |
| 3 | 1 | 1.02 |  | 26 | 2 | 2.04 |  | 49 | 2 | 2.04 |
| 5 | 2 | 2.04 |  | 27 | 1 | 1.02 |  | 50 | 3 | 3.06 |
| 6 | 3 | 3.06 |  | 28 | 3 | 3.06 |  | 51 | 2 | 2.04 |
| 7 | 2 | 2.04 |  | 29 | 2 | 2.04 |  | 52 | 2 | 2.04 |
| 9 | 2 | 2.04 |  | 31 | 3 | 3.06 |  | 53 | 3 | 3.06 |
| 10 | 1 | 1.02 |  | 33 | 2 | 2.04 |  | 54 | 2 | 2.04 |
| 11 | 1 | 1.02 |  | 34 | 4 | 4.08 |  | 55 | 1 | 1.02 |
| 12 | 2 | 2.04 |  | 35 | 2 | 2.04 |  |  |  |  |
| 13 | 1 | 1.02 |  | 36 | 4 | 4.08 |  |  |  |  |
| 14 | 2 | 2.04 |  | 37 | 1 | 1.02 |  |  |  |  |
| 16 | 1 | 1.02 |  | 38 | 3 | 3.06 |  |  |  |  |
| 17 | 1 | 1.02 |  | 39 | 4 | 4.08 |  |  |  |  |
| 18 | 3 | 3.06 |  | 41 | 3 | 3.06 |  |  |  |  |
| 19 | 2 | 2.04 |  | 42 | 2 | 2.04 |  |  |  |  |
| 20 | 3 | 3.06 |  | 43 | 2 | 2.04 |  |  |  |  |
| 21 | 2 | 2.04 |  | 44 | 3 | 3.06 |  |  |  |  |
| 22 | 2 | 2.04 |  | 45 | 3 | 3.06 |  |  |  |  |
| 23 | 1 | 1.02 |  | 46 | 1 | 1.02 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.17 |  | 22 | 2 | 1.06 |  | 43 | 2 | 1.06 |
| 2 | 3 | 1.59 |  | 23 | 5 | 2.65 |  | 44 | 3 | 1.59 |
| 3 | 2 | 1.06 |  | 24 | 3 | 1.59 |  | 45 | 5 | 2.65 |
| 4 | 3 | 1.59 |  | 25 | 3 | 1.59 |  | 46 | 2 | 1.06 |
| 5 | 3 | 1.59 |  | 26 | 4 | 2.12 |  | 47 | 1 | 0.53 |
| 6 | 5 | 2.65 |  | 27 | 5 | 2.65 |  | 48 | 3 | 1.59 |
| 7 | 6 | 3.17 |  | 28 | 4 | 2.12 |  | 49 | 3 | 1.59 |
| 9 | 3 | 1.59 |  | 29 | 2 | 1.06 |  | 50 | 5 | 2.65 |
| 10 | 3 | 1.59 |  | 30 | 2 | 1.06 |  | 51 | 3 | 1.59 |
| 11 | 5 | 2.65 |  | 31 | 4 | 2.12 |  | 52 | 5 | 2.65 |
| 12 | 4 | 2.12 |  | 33 | 2 | 1.06 |  | 53 | 4 | 2.12 |
| 13 | 6 | 3.17 |  | 34 | 5 | 2.65 |  | 54 | 3 | 1.59 |
| 14 | 5 | 2.65 |  | 35 | 3 | 1.59 |  | 55 | 3 | 1.59 |
| 15 | 1 | 0.53 |  | 36 | 5 | 2.65 |  |  |  |  |
| 16 | 3 | 1.59 |  | 37 | 2 | 1.06 |  |  |  |  |
| 17 | 3 | 1.59 |  | 38 | 4 | 2.12 |  |  |  |  |
| 18 | 6 | 3.17 |  | 39 | 5 | 2.65 |  |  |  |  |
| 19 | 2 | 1.06 |  | 40 | 1 | 0.53 |  |  |  |  |
| 20 | 5 | 2.65 |  | 41 | 5 | 2.65 |  |  |  |  |
| 21 | 4 | 2.12 |  | 42 | 3 | 1.59 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 6 | 2.2 |  | 41 | 6 | 2.2 |
| 2 | 4 | 1.47 |  | 22 | 4 | 1.47 |  | 42 | 4 | 1.47 |
| 3 | 3 | 1.1 |  | 23 | 6 | 2.2 |  | 43 | 3 | 1.1 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 5 | 1.83 |
| 5 | 6 | 2.2 |  | 25 | 6 | 2.2 |  | 45 | 8 | 2.93 |
| 6 | 6 | 2.2 |  | 26 | 5 | 1.83 |  | 46 | 3 | 1.1 |
| 7 | 9 | 3.3 |  | 27 | 7 | 2.56 |  | 47 | 5 | 1.83 |
| 8 | 2 | 0.73 |  | 28 | 5 | 1.83 |  | 48 | 3 | 1.1 |
| 9 | 5 | 1.83 |  | 29 | 3 | 1.1 |  | 49 | 4 | 1.47 |
| 10 | 5 | 1.83 |  | 30 | 2 | 0.73 |  | 50 | 7 | 2.56 |
| 11 | 11 | 4.03 |  | 31 | 7 | 2.56 |  | 51 | 4 | 1.47 |
| 12 | 4 | 1.47 |  | 32 | 2 | 0.73 |  | 52 | 6 | 2.2 |
| 13 | 7 | 2.56 |  | 33 | 3 | 1.1 |  | 53 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 34 | 6 | 2.2 |  | 54 | 5 | 1.83 |
| 15 | 3 | 1.1 |  | 35 | 3 | 1.1 |  | 55 | 4 | 1.47 |
| 16 | 4 | 1.47 |  | 36 | 6 | 2.2 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 2 | 0.73 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 2 | 0.73 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 8 | 2026-09-08 | 74 |
| 32 | 2026-09-15 | 67 |
| 15 | 2026-10-01 | 51 |
| 40 | 2026-10-13 | 39 |
| 4 | 2026-10-15 | 37 |
| 30 | 2026-10-20 | 32 |
| 24 | 2026-10-22 | 30 |
| 37 | 2026-10-22 | 30 |
| 27 | 2026-10-27 | 25 |
| 9 | 2026-10-29 | 23 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-11-10 | 11 |
| 2 | 2026-11-10 | 11 |
| 3 | 2026-11-19 | 2 |
| 4 | 2026-10-15 | 37 |
| 5 | 2026-11-14 | 7 |
| 6 | 2026-11-17 | 4 |
| 7 | 2026-11-21 | 0 |
| 8 | 2026-09-08 | 74 |
| 9 | 2026-10-29 | 23 |
| 10 | 2026-11-03 | 18 |
| 11 | 2026-10-31 | 21 |
| 12 | 2026-11-10 | 11 |
| 13 | 2026-11-19 | 2 |
| 14 | 2026-11-03 | 18 |
| 15 | 2026-10-01 | 51 |
| 16 | 2026-11-19 | 2 |
| 17 | 2026-11-12 | 9 |
| 18 | 2026-10-31 | 21 |
| 19 | 2026-11-07 | 14 |
| 20 | 2026-11-17 | 4 |
| 21 | 2026-11-19 | 2 |
| 22 | 2026-11-03 | 18 |
| 23 | 2026-11-19 | 2 |
| 24 | 2026-10-22 | 30 |
| 25 | 2026-11-12 | 9 |
| 26 | 2026-11-07 | 14 |
| 27 | 2026-10-27 | 25 |
| 28 | 2026-11-14 | 7 |
| 29 | 2026-11-21 | 0 |
| 30 | 2026-10-20 | 32 |
| 31 | 2026-11-03 | 18 |
| 32 | 2026-09-15 | 67 |
| 33 | 2026-11-12 | 9 |
| 34 | 2026-11-17 | 4 |
| 35 | 2026-11-12 | 9 |
| 36 | 2026-11-17 | 4 |
| 37 | 2026-10-22 | 30 |
| 38 | 2026-11-19 | 2 |
| 39 | 2026-11-21 | 0 |
| 40 | 2026-10-13 | 39 |
| 41 | 2026-11-17 | 4 |
| 42 | 2026-11-14 | 7 |
| 43 | 2026-11-19 | 2 |
| 44 | 2026-11-21 | 0 |
| 45 | 2026-11-21 | 0 |
| 46 | 2026-10-29 | 23 |
| 47 | 2026-11-14 | 7 |
| 48 | 2026-11-12 | 9 |
| 49 | 2026-11-17 | 4 |
| 50 | 2026-11-21 | 0 |
| 51 | 2026-11-14 | 7 |
| 52 | 2026-11-17 | 4 |
| 53 | 2026-11-07 | 14 |
| 54 | 2026-11-21 | 0 |
| 55 | 2026-10-31 | 21 |



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

