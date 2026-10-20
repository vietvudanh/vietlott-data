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
| Power 655 | 1413 | 2017-08-01 | 2026-10-20 | 1413 | 00001 | 01413 |
| Power 645 | 1380 | 2017-10-25 | 2026-10-18 | 1380 | 00198 | 01577 |
| Power 535 | 443 | 2025-06-29 | 2026-10-20 | 883 | 00001 | 00957 |
| Keno | 712 | 2022-12-04 | 2026-10-20 | 88928 | #0110271 | #0299998 |
| 3D | 1143 | 2019-04-22 | 2026-10-19 | 1143 | 00001 | 01147 |
| 3D Pro | 790 | 2021-09-14 | 2026-10-20 | 790 | 00001 | 00794 |
| Bingo18 | 685 | 2024-12-03 | 2026-10-20 | 96267 | 0083123 | 0192211 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-20 | 01413 | [13, 20, 23, 30, 50, 55, 45] | 2026-10-20T12:01:23.653270 |
| 2026-10-17 | 01412 | [1, 10, 11, 12, 16, 37, 48] | 2026-10-17T12:01:15.757708 |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 193 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 208 | 2.1 |
| 2 | 164 | 1.66 |  | 22 | 208 | 2.1 |  | 42 | 182 | 1.84 |
| 3 | 190 | 1.92 |  | 23 | 192 | 1.94 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.5 |  | 24 | 182 | 1.84 |  | 44 | 182 | 1.84 |
| 5 | 184 | 1.86 |  | 25 | 164 | 1.66 |  | 45 | 184 | 1.86 |
| 6 | 146 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 163 | 1.65 |  | 27 | 168 | 1.7 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.98 |  | 28 | 160 | 1.62 |  | 48 | 192 | 1.94 |
| 9 | 196 | 1.98 |  | 29 | 191 | 1.93 |  | 49 | 175 | 1.77 |
| 10 | 168 | 1.7 |  | 30 | 164 | 1.66 |  | 50 | 181 | 1.83 |
| 11 | 189 | 1.91 |  | 31 | 189 | 1.91 |  | 51 | 199 | 2.01 |
| 12 | 182 | 1.84 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 178 | 1.8 |  | 33 | 180 | 1.82 |  | 53 | 189 | 1.91 |
| 14 | 182 | 1.84 |  | 34 | 197 | 1.99 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 181 | 1.83 |
| 16 | 177 | 1.79 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 160 | 1.62 |  |  |  |  |
| 18 | 182 | 1.84 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 174 | 1.76 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 191 | 1.93 |  | 40 | 195 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 5.49 |  | 24 | 2 | 2.2 |  | 50 | 2 | 2.2 |
| 2 | 2 | 2.2 |  | 25 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 52 | 3 | 3.3 |
| 4 | 3 | 3.3 |  | 27 | 4 | 4.4 |  | 53 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 28 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 6 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 7 | 4 | 4.4 |  | 31 | 1 | 1.1 |  |  |  |  |
| 9 | 1 | 1.1 |  | 34 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 11 | 4 | 4.4 |  | 36 | 1 | 1.1 |  |  |  |  |
| 12 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 13 | 5 | 5.49 |  | 38 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 39 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 40 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 1 | 1.1 |  |  |  |  |
| 18 | 3 | 3.3 |  | 45 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 48 | 2 | 2.2 |  |  |  |  |
| 23 | 4 | 4.4 |  | 49 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 3.85 |  | 21 | 5 | 2.75 |  | 41 | 3 | 1.65 |
| 2 | 3 | 1.65 |  | 22 | 2 | 1.1 |  | 42 | 2 | 1.1 |
| 3 | 2 | 1.1 |  | 23 | 5 | 2.75 |  | 43 | 1 | 0.55 |
| 4 | 4 | 2.2 |  | 24 | 6 | 3.3 |  | 44 | 2 | 1.1 |
| 5 | 4 | 2.2 |  | 25 | 6 | 3.3 |  | 45 | 5 | 2.75 |
| 6 | 3 | 1.65 |  | 26 | 3 | 1.65 |  | 46 | 2 | 1.1 |
| 7 | 7 | 3.85 |  | 27 | 6 | 3.3 |  | 47 | 4 | 2.2 |
| 8 | 3 | 1.65 |  | 28 | 2 | 1.1 |  | 48 | 2 | 1.1 |
| 9 | 4 | 2.2 |  | 29 | 1 | 0.55 |  | 49 | 2 | 1.1 |
| 10 | 4 | 2.2 |  | 30 | 2 | 1.1 |  | 50 | 4 | 2.2 |
| 11 | 10 | 5.49 |  | 31 | 4 | 2.2 |  | 51 | 2 | 1.1 |
| 12 | 2 | 1.1 |  | 32 | 2 | 1.1 |  | 52 | 4 | 2.2 |
| 13 | 6 | 3.3 |  | 33 | 1 | 0.55 |  | 53 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 2 | 1.1 |  | 54 | 3 | 1.65 |
| 15 | 3 | 1.65 |  | 35 | 1 | 0.55 |  | 55 | 3 | 1.65 |
| 16 | 3 | 1.65 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 6 | 3.3 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 1 | 0.55 |  | 39 | 1 | 0.55 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 2 | 1.1 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 9 | 3.3 |  | 21 | 5 | 1.83 |  | 41 | 5 | 1.83 |
| 2 | 7 | 2.56 |  | 22 | 3 | 1.1 |  | 42 | 4 | 1.47 |
| 3 | 4 | 1.47 |  | 23 | 7 | 2.56 |  | 43 | 2 | 0.73 |
| 4 | 4 | 1.47 |  | 24 | 7 | 2.56 |  | 44 | 4 | 1.47 |
| 5 | 7 | 2.56 |  | 25 | 7 | 2.56 |  | 45 | 7 | 2.56 |
| 6 | 3 | 1.1 |  | 26 | 3 | 1.1 |  | 46 | 3 | 1.1 |
| 7 | 9 | 3.3 |  | 27 | 10 | 3.66 |  | 47 | 6 | 2.2 |
| 8 | 5 | 1.83 |  | 28 | 3 | 1.1 |  | 48 | 5 | 1.83 |
| 9 | 6 | 2.2 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 7 | 2.56 |
| 11 | 11 | 4.03 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 3 | 1.1 |  | 32 | 2 | 0.73 |  | 52 | 4 | 1.47 |
| 13 | 6 | 2.2 |  | 33 | 3 | 1.1 |  | 53 | 2 | 0.73 |
| 14 | 8 | 2.93 |  | 34 | 2 | 0.73 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 2 | 0.73 |  | 55 | 6 | 2.2 |
| 16 | 5 | 1.83 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 2 | 0.73 |  | 39 | 5 | 1.83 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 19 | 2026-08-22 | 59 |
| 29 | 2026-08-29 | 52 |
| 44 | 2026-09-01 | 49 |
| 33 | 2026-09-05 | 45 |
| 8 | 2026-09-08 | 42 |
| 43 | 2026-09-12 | 38 |
| 47 | 2026-09-15 | 35 |
| 32 | 2026-09-15 | 35 |
| 22 | 2026-09-19 | 31 |
| 46 | 2026-09-22 | 28 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-17 | 3 |
| 2 | 2026-10-13 | 7 |
| 3 | 2026-09-22 | 28 |
| 4 | 2026-10-15 | 5 |
| 5 | 2026-10-01 | 19 |
| 6 | 2026-10-08 | 12 |
| 7 | 2026-10-15 | 5 |
| 8 | 2026-09-08 | 42 |
| 9 | 2026-09-22 | 28 |
| 10 | 2026-10-17 | 3 |
| 11 | 2026-10-17 | 3 |
| 12 | 2026-10-17 | 3 |
| 13 | 2026-10-20 | 0 |
| 14 | 2026-10-13 | 7 |
| 15 | 2026-10-01 | 19 |
| 16 | 2026-10-17 | 3 |
| 17 | 2026-10-10 | 10 |
| 18 | 2026-10-06 | 14 |
| 19 | 2026-08-22 | 59 |
| 20 | 2026-10-20 | 0 |
| 21 | 2026-10-10 | 10 |
| 22 | 2026-09-19 | 31 |
| 23 | 2026-10-20 | 0 |
| 24 | 2026-10-10 | 10 |
| 25 | 2026-10-15 | 5 |
| 26 | 2026-10-13 | 7 |
| 27 | 2026-10-13 | 7 |
| 28 | 2026-09-24 | 26 |
| 29 | 2026-08-29 | 52 |
| 30 | 2026-10-20 | 0 |
| 31 | 2026-10-08 | 12 |
| 32 | 2026-09-15 | 35 |
| 33 | 2026-09-05 | 45 |
| 34 | 2026-10-01 | 19 |
| 35 | 2026-09-29 | 21 |
| 36 | 2026-09-29 | 21 |
| 37 | 2026-10-17 | 3 |
| 38 | 2026-09-26 | 24 |
| 39 | 2026-10-10 | 10 |
| 40 | 2026-10-13 | 7 |
| 41 | 2026-10-03 | 17 |
| 42 | 2026-10-15 | 5 |
| 43 | 2026-09-12 | 38 |
| 44 | 2026-09-01 | 49 |
| 45 | 2026-10-20 | 0 |
| 46 | 2026-09-22 | 28 |
| 47 | 2026-09-15 | 35 |
| 48 | 2026-10-17 | 3 |
| 49 | 2026-09-26 | 24 |
| 50 | 2026-10-20 | 0 |
| 51 | 2026-10-15 | 5 |
| 52 | 2026-10-08 | 12 |
| 53 | 2026-10-13 | 7 |
| 54 | 2026-10-03 | 17 |
| 55 | 2026-10-20 | 0 |



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

