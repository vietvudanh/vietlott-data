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
| Power 655 | 1410 | 2017-08-01 | 2026-10-13 | 1410 | 00001 | 01410 |
| Power 645 | 1377 | 2017-10-25 | 2026-10-11 | 1377 | 00198 | 01574 |
| Power 535 | 436 | 2025-06-29 | 2026-10-13 | 870 | 00001 | 00944 |
| Keno | 706 | 2022-12-04 | 2026-10-14 | 88124 | #0110271 | #0299194 |
| 3D | 1140 | 2019-04-22 | 2026-10-12 | 1140 | 00001 | 01144 |
| 3D Pro | 787 | 2021-09-14 | 2026-10-13 | 787 | 00001 | 00791 |
| Bingo18 | 679 | 2024-12-03 | 2026-10-14 | 95274 | 0083123 | 0191137 |

## Power 6/55 Analysis

### Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-10-13 | 01410 | [2, 14, 27, 40, 50, 53, 26] | 2026-10-13T12:01:03.519892 |
| 2026-10-10 | 01409 | [14, 17, 21, 23, 24, 39, 30] | 2026-10-10T12:01:03.465743 |
| 2026-10-08 | 01408 | [1, 7, 12, 27, 31, 52, 6] | 2026-10-08T12:06:02.524706 |
| 2026-10-06 | 01407 | [6, 7, 18, 20, 24, 27, 1] | 2026-10-06T15:29:22.452062 |
| 2026-10-03 | 01406 | [7, 11, 13, 16, 18, 54, 41] | 2026-10-05T02:57:28.871868 |
| 2026-10-01 | 01405 | [4, 5, 13, 34, 52, 55, 15] | 2026-10-05T02:57:28.872862 |
| 2026-09-29 | 01404 | [2, 4, 13, 17, 35, 36, 11] | 2026-10-05T02:57:28.873725 |
| 2026-09-26 | 01403 | [14, 18, 21, 38, 48, 52, 49] | 2026-09-27T00:01:04.537528 |
| 2026-09-24 | 01402 | [1, 13, 23, 25, 26, 28, 27] | 2026-09-25T00:01:22.421665 |
| 2026-09-22 | 01401 | [1, 3, 9, 11, 41, 46, 10] | 2026-09-23T00:01:18.071623 |

### Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 192 | 1.95 |  | 21 | 177 | 1.79 |  | 41 | 208 | 2.11 |
| 2 | 164 | 1.66 |  | 22 | 208 | 2.11 |  | 42 | 181 | 1.83 |
| 3 | 190 | 1.93 |  | 23 | 190 | 1.93 |  | 43 | 199 | 2.02 |
| 4 | 147 | 1.49 |  | 24 | 182 | 1.84 |  | 44 | 182 | 1.84 |
| 5 | 184 | 1.86 |  | 25 | 163 | 1.65 |  | 45 | 182 | 1.84 |
| 6 | 146 | 1.48 |  | 26 | 168 | 1.7 |  | 46 | 183 | 1.85 |
| 7 | 162 | 1.64 |  | 27 | 168 | 1.7 |  | 47 | 180 | 1.82 |
| 8 | 196 | 1.99 |  | 28 | 160 | 1.62 |  | 48 | 191 | 1.94 |
| 9 | 196 | 1.99 |  | 29 | 191 | 1.94 |  | 49 | 175 | 1.77 |
| 10 | 167 | 1.69 |  | 30 | 163 | 1.65 |  | 50 | 180 | 1.82 |
| 11 | 188 | 1.9 |  | 31 | 189 | 1.92 |  | 51 | 198 | 2.01 |
| 12 | 181 | 1.83 |  | 32 | 188 | 1.9 |  | 52 | 181 | 1.83 |
| 13 | 177 | 1.79 |  | 33 | 180 | 1.82 |  | 53 | 189 | 1.92 |
| 14 | 182 | 1.84 |  | 34 | 197 | 2.0 |  | 54 | 170 | 1.72 |
| 15 | 168 | 1.7 |  | 35 | 171 | 1.73 |  | 55 | 180 | 1.82 |
| 16 | 176 | 1.78 |  | 36 | 169 | 1.71 |  |  |  |  |
| 17 | 163 | 1.65 |  | 37 | 159 | 1.61 |  |  |  |  |
| 18 | 182 | 1.84 |  | 38 | 174 | 1.76 |  |  |  |  |
| 19 | 174 | 1.76 |  | 39 | 173 | 1.75 |  |  |  |  |
| 20 | 190 | 1.93 |  | 40 | 195 | 1.98 |  |  |  |  |

### Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 4.4 |  | 23 | 2 | 2.2 |  | 48 | 1 | 1.1 |
| 2 | 2 | 2.2 |  | 24 | 3 | 3.3 |  | 49 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 25 | 3 | 3.3 |  | 50 | 2 | 2.2 |
| 4 | 3 | 3.3 |  | 26 | 2 | 2.2 |  | 52 | 4 | 4.4 |
| 5 | 1 | 1.1 |  | 27 | 6 | 6.59 |  | 53 | 1 | 1.1 |
| 6 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 7 | 4 | 4.4 |  | 30 | 1 | 1.1 |  | 55 | 1 | 1.1 |
| 9 | 1 | 1.1 |  | 31 | 1 | 1.1 |  |  |  |  |
| 10 | 1 | 1.1 |  | 32 | 1 | 1.1 |  |  |  |  |
| 11 | 5 | 5.49 |  | 34 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 13 | 4 | 4.4 |  | 36 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 39 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 40 | 1 | 1.1 |  |  |  |  |
| 18 | 4 | 4.4 |  | 41 | 2 | 2.2 |  |  |  |  |
| 20 | 1 | 1.1 |  | 45 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 47 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 21 | 5 | 2.75 |  | 41 | 4 | 2.2 |
| 2 | 5 | 2.75 |  | 22 | 2 | 1.1 |  | 42 | 1 | 0.55 |
| 3 | 3 | 1.65 |  | 23 | 3 | 1.65 |  | 43 | 1 | 0.55 |
| 4 | 3 | 1.65 |  | 24 | 6 | 3.3 |  | 44 | 2 | 1.1 |
| 5 | 4 | 2.2 |  | 25 | 6 | 3.3 |  | 45 | 3 | 1.65 |
| 6 | 3 | 1.65 |  | 26 | 3 | 1.65 |  | 46 | 2 | 1.1 |
| 7 | 6 | 3.3 |  | 27 | 7 | 3.85 |  | 47 | 5 | 2.75 |
| 8 | 4 | 2.2 |  | 28 | 2 | 1.1 |  | 48 | 2 | 1.1 |
| 9 | 4 | 2.2 |  | 29 | 2 | 1.1 |  | 49 | 2 | 1.1 |
| 10 | 3 | 1.65 |  | 30 | 3 | 1.65 |  | 50 | 4 | 2.2 |
| 11 | 9 | 4.95 |  | 31 | 4 | 2.2 |  | 51 | 2 | 1.1 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 52 | 4 | 2.2 |
| 13 | 5 | 2.75 |  | 33 | 1 | 0.55 |  | 53 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 2 | 1.1 |  | 54 | 3 | 1.65 |
| 15 | 4 | 2.2 |  | 35 | 1 | 0.55 |  | 55 | 2 | 1.1 |
| 16 | 3 | 1.65 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 1 | 0.55 |  |  |  |  |
| 18 | 7 | 3.85 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 1 | 0.55 |  | 39 | 2 | 1.1 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 2 | 1.1 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 6 | 2.2 |  | 41 | 6 | 2.2 |
| 2 | 7 | 2.56 |  | 22 | 5 | 1.83 |  | 42 | 3 | 1.1 |
| 3 | 4 | 1.47 |  | 23 | 5 | 1.83 |  | 43 | 2 | 0.73 |
| 4 | 3 | 1.1 |  | 24 | 8 | 2.93 |  | 44 | 4 | 1.47 |
| 5 | 7 | 2.56 |  | 25 | 6 | 2.2 |  | 45 | 7 | 2.56 |
| 6 | 3 | 1.1 |  | 26 | 3 | 1.1 |  | 46 | 3 | 1.1 |
| 7 | 8 | 2.93 |  | 27 | 10 | 3.66 |  | 47 | 6 | 2.2 |
| 8 | 6 | 2.2 |  | 28 | 3 | 1.1 |  | 48 | 6 | 2.2 |
| 9 | 6 | 2.2 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 3 | 1.1 |  | 30 | 3 | 1.1 |  | 50 | 6 | 2.2 |
| 11 | 11 | 4.03 |  | 31 | 6 | 2.2 |  | 51 | 4 | 1.47 |
| 12 | 2 | 0.73 |  | 32 | 3 | 1.1 |  | 52 | 4 | 1.47 |
| 13 | 6 | 2.2 |  | 33 | 4 | 1.47 |  | 53 | 3 | 1.1 |
| 14 | 8 | 2.93 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 15 | 4 | 1.47 |  | 35 | 2 | 0.73 |  | 55 | 6 | 2.2 |
| 16 | 5 | 1.83 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 8 | 2.93 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 6 | 2.2 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### Top 10 Numbers by Days Since Last Appearance
| result | last_date | days_since |
| --- | --- | --- |
| 19 | 2026-08-22 | 52 |
| 29 | 2026-08-29 | 45 |
| 44 | 2026-09-01 | 42 |
| 42 | 2026-09-03 | 40 |
| 33 | 2026-09-05 | 38 |
| 8 | 2026-09-08 | 35 |
| 51 | 2026-09-10 | 33 |
| 43 | 2026-09-12 | 31 |
| 32 | 2026-09-15 | 28 |
| 47 | 2026-09-15 | 28 |

### Days Since Last Appearance - All Numbers
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-10-08 | 5 |
| 2 | 2026-10-13 | 0 |
| 3 | 2026-09-22 | 21 |
| 4 | 2026-10-01 | 12 |
| 5 | 2026-10-01 | 12 |
| 6 | 2026-10-08 | 5 |
| 7 | 2026-10-08 | 5 |
| 8 | 2026-09-08 | 35 |
| 9 | 2026-09-22 | 21 |
| 10 | 2026-09-22 | 21 |
| 11 | 2026-10-03 | 10 |
| 12 | 2026-10-08 | 5 |
| 13 | 2026-10-03 | 10 |
| 14 | 2026-10-13 | 0 |
| 15 | 2026-10-01 | 12 |
| 16 | 2026-10-03 | 10 |
| 17 | 2026-10-10 | 3 |
| 18 | 2026-10-06 | 7 |
| 19 | 2026-08-22 | 52 |
| 20 | 2026-10-06 | 7 |
| 21 | 2026-10-10 | 3 |
| 22 | 2026-09-19 | 24 |
| 23 | 2026-10-10 | 3 |
| 24 | 2026-10-10 | 3 |
| 25 | 2026-09-24 | 19 |
| 26 | 2026-10-13 | 0 |
| 27 | 2026-10-13 | 0 |
| 28 | 2026-09-24 | 19 |
| 29 | 2026-08-29 | 45 |
| 30 | 2026-10-10 | 3 |
| 31 | 2026-10-08 | 5 |
| 32 | 2026-09-15 | 28 |
| 33 | 2026-09-05 | 38 |
| 34 | 2026-10-01 | 12 |
| 35 | 2026-09-29 | 14 |
| 36 | 2026-09-29 | 14 |
| 37 | 2026-09-17 | 26 |
| 38 | 2026-09-26 | 17 |
| 39 | 2026-10-10 | 3 |
| 40 | 2026-10-13 | 0 |
| 41 | 2026-10-03 | 10 |
| 42 | 2026-09-03 | 40 |
| 43 | 2026-09-12 | 31 |
| 44 | 2026-09-01 | 42 |
| 45 | 2026-09-17 | 26 |
| 46 | 2026-09-22 | 21 |
| 47 | 2026-09-15 | 28 |
| 48 | 2026-09-26 | 17 |
| 49 | 2026-09-26 | 17 |
| 50 | 2026-10-13 | 0 |
| 51 | 2026-09-10 | 33 |
| 52 | 2026-10-08 | 5 |
| 53 | 2026-10-13 | 0 |
| 54 | 2026-10-03 | 10 |
| 55 | 2026-10-01 | 12 |



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

