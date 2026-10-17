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
| Power 655 | 1411 | 2017-08-01 | 2026-10-15 | 1411 | 00001 | 01411 |
| Power 645 | 1379 | 2017-10-25 | 2026-10-16 | 1379 | 00198 | 01576 |
| Power 535 | 439 | 2025-06-29 | 2026-10-16 | 876 | 00001 | 00950 |
| Keno | 709 | 2022-12-04 | 2026-10-17 | 88481 | #0110271 | #0299551 |
| 3D | 1142 | 2019-04-22 | 2026-10-16 | 1142 | 00001 | 01146 |
| 3D Pro | 788 | 2021-09-14 | 2026-10-15 | 788 | 00001 | 00792 |
| Bingo18 | 682 | 2024-12-03 | 2026-10-17 | 95751 | 0083123 | 0191614 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-15 | 01411 | [7, 23, 25, 42, 45, 51, 4] | 2026-10-15T12:01:13.712796 |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |
| 2026-09-24 | 01402 | [1, 13, 23, 25, 26, 28, 27] | 2026-09-25T00:01:22.421665 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 192 | 1.94 |  | 21 | 177 | 1.79 |  | 41 | 208 | 2.11 |
| 2 | 164 | 1.66 |  | 22 | 208 | 2.11 |  | 42 | 182 | 1.84 |
| 3 | 190 | 1.92 |  | 23 | 191 | 1.93 |  | 43 | 199 | 2.01 |
| 4 | 148 | 1.5 |  | 24 | 182 | 1.84 |  | 44 | 182 | 1.84 |
| 5 | 184 | 1.86 |  | 25 | 164 | 1.66 |  | 45 | 183 | 1.85 |
| 6 | 146 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 163 | 1.65 |  | 27 | 168 | 1.7 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.98 |  | 28 | 160 | 1.62 |  | 48 | 191 | 1.93 |
| 9 | 196 | 1.98 |  | 29 | 191 | 1.93 |  | 49 | 175 | 1.77 |
| 10 | 167 | 1.69 |  | 30 | 163 | 1.65 |  | 50 | 180 | 1.82 |
| 11 | 188 | 1.9 |  | 31 | 189 | 1.91 |  | 51 | 199 | 2.01 |
| 12 | 181 | 1.83 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 177 | 1.79 |  | 33 | 180 | 1.82 |  | 53 | 189 | 1.91 |
| 14 | 182 | 1.84 |  | 34 | 197 | 1.99 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 180 | 1.82 |
| 16 | 176 | 1.78 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 159 | 1.61 |  |  |  |  |
| 18 | 182 | 1.84 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 174 | 1.76 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 190 | 1.92 |  | 40 | 195 | 1.97 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 4.4 |  | 23 | 3 | 3.3 |  | 49 | 1 | 1.1 |
| 2 | 2 | 2.2 |  | 24 | 2 | 2.2 |  | 50 | 2 | 2.2 |
| 3 | 1 | 1.1 |  | 25 | 4 | 4.4 |  | 51 | 1 | 1.1 |
| 4 | 4 | 4.4 |  | 26 | 2 | 2.2 |  | 52 | 3 | 3.3 |
| 5 | 1 | 1.1 |  | 27 | 5 | 5.49 |  | 53 | 1 | 1.1 |
| 6 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 7 | 5 | 5.49 |  | 30 | 1 | 1.1 |  | 55 | 1 | 1.1 |
| 9 | 1 | 1.1 |  | 31 | 1 | 1.1 |  |  |  |  |
| 10 | 1 | 1.1 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 5 | 5.49 |  | 35 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 4 | 4.4 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 38 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 39 | 1 | 1.1 |  |  |  |  |
| 16 | 1 | 1.1 |  | 40 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 18 | 4 | 4.4 |  | 42 | 1 | 1.1 |  |  |  |  |
| 20 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 48 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 21 | 5 | 2.75 |  | 41 | 4 | 2.2 |
| 2 | 4 | 2.2 |  | 22 | 2 | 1.1 |  | 42 | 2 | 1.1 |
| 3 | 3 | 1.65 |  | 23 | 4 | 2.2 |  | 43 | 1 | 0.55 |
| 4 | 4 | 2.2 |  | 24 | 6 | 3.3 |  | 44 | 2 | 1.1 |
| 5 | 4 | 2.2 |  | 25 | 6 | 3.3 |  | 45 | 4 | 2.2 |
| 6 | 3 | 1.65 |  | 26 | 3 | 1.65 |  | 46 | 2 | 1.1 |
| 7 | 7 | 3.85 |  | 27 | 6 | 3.3 |  | 47 | 5 | 2.75 |
| 8 | 4 | 2.2 |  | 28 | 2 | 1.1 |  | 48 | 2 | 1.1 |
| 9 | 4 | 2.2 |  | 29 | 2 | 1.1 |  | 49 | 2 | 1.1 |
| 10 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 3 | 1.65 |
| 11 | 9 | 4.95 |  | 31 | 4 | 2.2 |  | 51 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 52 | 4 | 2.2 |
| 13 | 5 | 2.75 |  | 33 | 1 | 0.55 |  | 53 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 2 | 1.1 |  | 54 | 3 | 1.65 |
| 15 | 4 | 2.2 |  | 35 | 1 | 0.55 |  | 55 | 2 | 1.1 |
| 16 | 2 | 1.1 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 1 | 0.55 |  |  |  |  |
| 18 | 7 | 3.85 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 1 | 0.55 |  | 39 | 2 | 1.1 |  |  |  |  |
| 20 | 1 | 0.55 |  | 40 | 2 | 1.1 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 7 | 2.63 |  | 22 | 4 | 1.5 |  | 42 | 4 | 1.5 |
| 3 | 4 | 1.5 |  | 23 | 6 | 2.26 |  | 43 | 2 | 0.75 |
| 4 | 4 | 1.5 |  | 24 | 8 | 3.01 |  | 44 | 4 | 1.5 |
| 5 | 7 | 2.63 |  | 25 | 7 | 2.63 |  | 45 | 6 | 2.26 |
| 6 | 3 | 1.13 |  | 26 | 3 | 1.13 |  | 46 | 3 | 1.13 |
| 7 | 9 | 3.38 |  | 27 | 10 | 3.76 |  | 47 | 6 | 2.26 |
| 8 | 6 | 2.26 |  | 28 | 3 | 1.13 |  | 48 | 4 | 1.5 |
| 9 | 6 | 2.26 |  | 29 | 4 | 1.5 |  | 49 | 4 | 1.5 |
| 10 | 3 | 1.13 |  | 30 | 3 | 1.13 |  | 50 | 6 | 2.26 |
| 11 | 11 | 4.14 |  | 31 | 6 | 2.26 |  | 51 | 5 | 1.88 |
| 12 | 2 | 0.75 |  | 32 | 3 | 1.13 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 3 | 1.13 |  | 53 | 2 | 0.75 |
| 14 | 8 | 3.01 |  | 34 | 2 | 0.75 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 2 | 0.75 |  | 55 | 5 | 1.88 |
| 16 | 4 | 1.5 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 8 | 3.01 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 2 | 0.75 |  | 39 | 6 | 2.26 |  |  |  |  |
| 20 | 3 | 1.13 |  | 40 | 5 | 1.88 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 19 | 2026-08-22 | 54 |
| 29 | 2026-08-29 | 47 |
| 44 | 2026-09-01 | 44 |
| 33 | 2026-09-05 | 40 |
| 8 | 2026-09-08 | 37 |
| 43 | 2026-09-12 | 33 |
| 47 | 2026-09-15 | 30 |
| 32 | 2026-09-15 | 30 |
| 37 | 2026-09-17 | 28 |
| 22 | 2026-09-19 | 26 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-08 | 7 |
| 2 | 2026-10-13 | 2 |
| 3 | 2026-09-22 | 23 |
| 4 | 2026-10-15 | 0 |
| 5 | 2026-10-01 | 14 |
| 6 | 2026-10-08 | 7 |
| 7 | 2026-10-15 | 0 |
| 8 | 2026-09-08 | 37 |
| 9 | 2026-09-22 | 23 |
| 10 | 2026-09-22 | 23 |
| 11 | 2026-10-03 | 12 |
| 12 | 2026-10-08 | 7 |
| 13 | 2026-10-03 | 12 |
| 14 | 2026-10-13 | 2 |
| 15 | 2026-10-01 | 14 |
| 16 | 2026-10-03 | 12 |
| 17 | 2026-10-10 | 5 |
| 18 | 2026-10-06 | 9 |
| 19 | 2026-08-22 | 54 |
| 20 | 2026-10-06 | 9 |
| 21 | 2026-10-10 | 5 |
| 22 | 2026-09-19 | 26 |
| 23 | 2026-10-15 | 0 |
| 24 | 2026-10-10 | 5 |
| 25 | 2026-10-15 | 0 |
| 26 | 2026-10-13 | 2 |
| 27 | 2026-10-13 | 2 |
| 28 | 2026-09-24 | 21 |
| 29 | 2026-08-29 | 47 |
| 30 | 2026-10-10 | 5 |
| 31 | 2026-10-08 | 7 |
| 32 | 2026-09-15 | 30 |
| 33 | 2026-09-05 | 40 |
| 34 | 2026-10-01 | 14 |
| 35 | 2026-09-29 | 16 |
| 36 | 2026-09-29 | 16 |
| 37 | 2026-09-17 | 28 |
| 38 | 2026-09-26 | 19 |
| 39 | 2026-10-10 | 5 |
| 40 | 2026-10-13 | 2 |
| 41 | 2026-10-03 | 12 |
| 42 | 2026-10-15 | 0 |
| 43 | 2026-09-12 | 33 |
| 44 | 2026-09-01 | 44 |
| 45 | 2026-10-15 | 0 |
| 46 | 2026-09-22 | 23 |
| 47 | 2026-09-15 | 30 |
| 48 | 2026-09-26 | 19 |
| 49 | 2026-09-26 | 19 |
| 50 | 2026-10-13 | 2 |
| 51 | 2026-10-15 | 0 |
| 52 | 2026-10-08 | 7 |
| 53 | 2026-10-13 | 2 |
| 54 | 2026-10-03 | 12 |
| 55 | 2026-10-01 | 14 |



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

