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
| Power 655 | 1412 | 2017-08-01 | 2026-10-17 | 1412 | 00001 | 01412 |
| Power 645 | 1380 | 2017-10-25 | 2026-10-18 | 1380 | 00198 | 01577 |
| Power 535 | 442 | 2025-06-29 | 2026-10-19 | 882 | 00001 | 00956 |
| Keno | 712 | 2022-12-04 | 2026-10-20 | 88838 | #0110271 | #0299908 |
| 3D | 1143 | 2019-04-22 | 2026-10-19 | 1143 | 00001 | 01147 |
| 3D Pro | 789 | 2021-09-14 | 2026-10-17 | 789 | 00001 | 00793 |
| Bingo18 | 685 | 2024-12-03 | 2026-10-20 | 96228 | 0083123 | 0192091 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 208 | 2.1 |
| 2 | 164 | 1.66 |  | 22 | 208 | 2.1 |  | 42 | 182 | 1.84 |
| 3 | 190 | 1.92 |  | 23 | 191 | 1.93 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.5 |  | 24 | 182 | 1.84 |  | 44 | 182 | 1.84 |
| 5 | 184 | 1.86 |  | 25 | 164 | 1.66 |  | 45 | 183 | 1.85 |
| 6 | 146 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 163 | 1.65 |  | 27 | 168 | 1.7 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.98 |  | 28 | 160 | 1.62 |  | 48 | 192 | 1.94 |
| 9 | 196 | 1.98 |  | 29 | 191 | 1.93 |  | 49 | 175 | 1.77 |
| 10 | 168 | 1.7 |  | 30 | 163 | 1.65 |  | 50 | 180 | 1.82 |
| 11 | 189 | 1.91 |  | 31 | 189 | 1.91 |  | 51 | 199 | 2.01 |
| 12 | 182 | 1.84 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 177 | 1.79 |  | 33 | 180 | 1.82 |  | 53 | 189 | 1.91 |
| 14 | 182 | 1.84 |  | 34 | 197 | 1.99 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 180 | 1.82 |
| 16 | 177 | 1.79 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 160 | 1.62 |  |  |  |  |
| 18 | 182 | 1.84 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 174 | 1.76 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 190 | 1.92 |  | 40 | 195 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 5.95 |  | 24 | 2 | 2.38 |  | 50 | 1 | 1.19 |
| 2 | 2 | 2.38 |  | 25 | 2 | 2.38 |  | 51 | 1 | 1.19 |
| 3 | 1 | 1.19 |  | 26 | 2 | 2.38 |  | 52 | 3 | 3.57 |
| 4 | 3 | 3.57 |  | 27 | 4 | 4.76 |  | 53 | 1 | 1.19 |
| 5 | 1 | 1.19 |  | 28 | 1 | 1.19 |  | 54 | 1 | 1.19 |
| 6 | 2 | 2.38 |  | 30 | 1 | 1.19 |  | 55 | 1 | 1.19 |
| 7 | 4 | 4.76 |  | 31 | 1 | 1.19 |  |  |  |  |
| 9 | 1 | 1.19 |  | 34 | 1 | 1.19 |  |  |  |  |
| 10 | 2 | 2.38 |  | 35 | 1 | 1.19 |  |  |  |  |
| 11 | 4 | 4.76 |  | 36 | 1 | 1.19 |  |  |  |  |
| 12 | 2 | 2.38 |  | 37 | 1 | 1.19 |  |  |  |  |
| 13 | 4 | 4.76 |  | 38 | 1 | 1.19 |  |  |  |  |
| 14 | 3 | 3.57 |  | 39 | 1 | 1.19 |  |  |  |  |
| 15 | 1 | 1.19 |  | 40 | 1 | 1.19 |  |  |  |  |
| 16 | 2 | 2.38 |  | 41 | 2 | 2.38 |  |  |  |  |
| 17 | 2 | 2.38 |  | 42 | 1 | 1.19 |  |  |  |  |
| 18 | 3 | 3.57 |  | 45 | 1 | 1.19 |  |  |  |  |
| 20 | 1 | 1.19 |  | 46 | 1 | 1.19 |  |  |  |  |
| 21 | 2 | 2.38 |  | 48 | 2 | 2.38 |  |  |  |  |
| 23 | 3 | 3.57 |  | 49 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 4.0 |  | 21 | 5 | 2.86 |  | 41 | 3 | 1.71 |
| 2 | 3 | 1.71 |  | 22 | 2 | 1.14 |  | 42 | 2 | 1.14 |
| 3 | 2 | 1.14 |  | 23 | 4 | 2.29 |  | 43 | 1 | 0.57 |
| 4 | 4 | 2.29 |  | 24 | 6 | 3.43 |  | 44 | 2 | 1.14 |
| 5 | 4 | 2.29 |  | 25 | 6 | 3.43 |  | 45 | 4 | 2.29 |
| 6 | 3 | 1.71 |  | 26 | 3 | 1.71 |  | 46 | 2 | 1.14 |
| 7 | 7 | 4.0 |  | 27 | 6 | 3.43 |  | 47 | 4 | 2.29 |
| 8 | 3 | 1.71 |  | 28 | 2 | 1.14 |  | 48 | 2 | 1.14 |
| 9 | 4 | 2.29 |  | 29 | 1 | 0.57 |  | 49 | 2 | 1.14 |
| 10 | 4 | 2.29 |  | 30 | 1 | 0.57 |  | 50 | 3 | 1.71 |
| 11 | 10 | 5.71 |  | 31 | 4 | 2.29 |  | 51 | 2 | 1.14 |
| 12 | 2 | 1.14 |  | 32 | 2 | 1.14 |  | 52 | 4 | 2.29 |
| 13 | 5 | 2.86 |  | 33 | 1 | 0.57 |  | 53 | 2 | 1.14 |
| 14 | 5 | 2.86 |  | 34 | 2 | 1.14 |  | 54 | 3 | 1.71 |
| 15 | 3 | 1.71 |  | 35 | 1 | 0.57 |  | 55 | 2 | 1.14 |
| 16 | 3 | 1.71 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 6 | 3.43 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 1 | 0.57 |  | 39 | 1 | 0.57 |  |  |  |  |
| 20 | 1 | 0.57 |  | 40 | 2 | 1.14 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 9 | 3.38 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 7 | 2.63 |  | 22 | 3 | 1.13 |  | 42 | 4 | 1.5 |
| 3 | 4 | 1.5 |  | 23 | 6 | 2.26 |  | 43 | 2 | 0.75 |
| 4 | 4 | 1.5 |  | 24 | 7 | 2.63 |  | 44 | 4 | 1.5 |
| 5 | 7 | 2.63 |  | 25 | 7 | 2.63 |  | 45 | 6 | 2.26 |
| 6 | 3 | 1.13 |  | 26 | 3 | 1.13 |  | 46 | 3 | 1.13 |
| 7 | 9 | 3.38 |  | 27 | 10 | 3.76 |  | 47 | 6 | 2.26 |
| 8 | 5 | 1.88 |  | 28 | 3 | 1.13 |  | 48 | 5 | 1.88 |
| 9 | 6 | 2.26 |  | 29 | 4 | 1.5 |  | 49 | 4 | 1.5 |
| 10 | 4 | 1.5 |  | 30 | 3 | 1.13 |  | 50 | 6 | 2.26 |
| 11 | 11 | 4.14 |  | 31 | 6 | 2.26 |  | 51 | 5 | 1.88 |
| 12 | 3 | 1.13 |  | 32 | 2 | 0.75 |  | 52 | 4 | 1.5 |
| 13 | 5 | 1.88 |  | 33 | 3 | 1.13 |  | 53 | 2 | 0.75 |
| 14 | 8 | 3.01 |  | 34 | 2 | 0.75 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 2 | 0.75 |  | 55 | 5 | 1.88 |
| 16 | 5 | 1.88 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 8 | 3.01 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 2 | 0.75 |  | 39 | 5 | 1.88 |  |  |  |  |
| 20 | 3 | 1.13 |  | 40 | 5 | 1.88 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 19 | 2026-08-22 | 56 |
| 29 | 2026-08-29 | 49 |
| 44 | 2026-09-01 | 46 |
| 33 | 2026-09-05 | 42 |
| 8 | 2026-09-08 | 39 |
| 43 | 2026-09-12 | 35 |
| 47 | 2026-09-15 | 32 |
| 32 | 2026-09-15 | 32 |
| 22 | 2026-09-19 | 28 |
| 46 | 2026-09-22 | 25 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 0 |
| 2 | 2026-10-13 | 4 |
| 3 | 2026-09-22 | 25 |
| 4 | 2026-10-15 | 2 |
| 5 | 2026-10-01 | 16 |
| 6 | 2026-10-08 | 9 |
| 7 | 2026-10-15 | 2 |
| 8 | 2026-09-08 | 39 |
| 9 | 2026-09-22 | 25 |
| 10 | 2026-10-17 | 0 |
| 11 | 2026-10-17 | 0 |
| 12 | 2026-10-17 | 0 |
| 13 | 2026-10-03 | 14 |
| 14 | 2026-10-13 | 4 |
| 15 | 2026-10-01 | 16 |
| 16 | 2026-10-17 | 0 |
| 17 | 2026-10-10 | 7 |
| 18 | 2026-10-06 | 11 |
| 19 | 2026-08-22 | 56 |
| 20 | 2026-10-06 | 11 |
| 21 | 2026-10-10 | 7 |
| 22 | 2026-09-19 | 28 |
| 23 | 2026-10-15 | 2 |
| 24 | 2026-10-10 | 7 |
| 25 | 2026-10-15 | 2 |
| 26 | 2026-10-13 | 4 |
| 27 | 2026-10-13 | 4 |
| 28 | 2026-09-24 | 23 |
| 29 | 2026-08-29 | 49 |
| 30 | 2026-10-10 | 7 |
| 31 | 2026-10-08 | 9 |
| 32 | 2026-09-15 | 32 |
| 33 | 2026-09-05 | 42 |
| 34 | 2026-10-01 | 16 |
| 35 | 2026-09-29 | 18 |
| 36 | 2026-09-29 | 18 |
| 37 | 2026-10-17 | 0 |
| 38 | 2026-09-26 | 21 |
| 39 | 2026-10-10 | 7 |
| 40 | 2026-10-13 | 4 |
| 41 | 2026-10-03 | 14 |
| 42 | 2026-10-15 | 2 |
| 43 | 2026-09-12 | 35 |
| 44 | 2026-09-01 | 46 |
| 45 | 2026-10-15 | 2 |
| 46 | 2026-09-22 | 25 |
| 47 | 2026-09-15 | 32 |
| 48 | 2026-10-17 | 0 |
| 49 | 2026-09-26 | 21 |
| 50 | 2026-10-13 | 4 |
| 51 | 2026-10-15 | 2 |
| 52 | 2026-10-08 | 9 |
| 53 | 2026-10-13 | 4 |
| 54 | 2026-10-03 | 14 |
| 55 | 2026-10-01 | 16 |



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

