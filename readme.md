# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

## 🔗 Links

- 🌐 [Website](https://vietvudanh.github.io/vietlott-data/) - Interactive data visualization
- 📝 [Blog Post](https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the) - About this project

## 🎯 Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Power 5/35** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535) | Choose 5 numbers from 1-35 |
| **Keno** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |
| **Bingo18** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game |


## 📋 Table of Contents

- [🔗 Links](#-links)
- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [Predictions](#-predictions)
- [📊 Data Statistics](#-data-statistics)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
  - [⏳ Top 10 Numbers by Days Since Last Appearance](#-top-10-số-lâu-chưa-xuất-hiện-top-10-numbers-by-days-since-last-appearance)
  - [📆 Days Since Last Appearance - All Numbers](#-số-ngày-từ-lần-xuất-hiện-cuối-cùng-days-since-last-appearance---all-numbers)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## Predictions

Predicitons models are at [/src/predictions](./src/machine_learning/).

For background on these models, see the [Machine Learning README](./src/machine_learning/).

## 📊 Data Statistics

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 1349 | 2017-08-01 | 2026-05-23 | 1349 | 00001 | 01349 |
| Power 645 | 1317 | 2017-10-25 | 2026-05-24 | 1317 | 00198 | 01514 |
| Power 535 | 295 | 2025-06-29 | 2026-05-25 | 589 | 00001 | 00662 |
| Keno | 564 | 2022-12-04 | 2026-05-25 | 71327 | #0110271 | #0282408 |
| 3D | 1080 | 2019-04-22 | 2026-05-25 | 1080 | 00001 | 01084 |
| 3D Pro | 726 | 2021-09-14 | 2026-05-23 | 726 | 00001 | 00730 |
| Bingo18 | 537 | 2024-12-03 | 2026-05-25 | 72755 | 0083123 | 0168708 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-23 | 01349 | [17, 21, 22, 27, 38, 49, 3] | 2026-05-24T00:01:17.320252 |
| 2026-05-21 | 01348 | [16, 18, 20, 28, 32, 34, 40] | 2026-05-22T00:01:24.083070 |
| 2026-05-19 | 01347 | [12, 39, 40, 45, 48, 53, 21] | 2026-05-21T18:37:39.362594 |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |
| 2026-05-14 | 01345 | [26, 28, 39, 41, 48, 55, 50] | 2026-05-15T00:01:10.822513 |
| 2026-05-12 | 01344 | [2, 11, 22, 26, 31, 38, 15] | 2026-05-12T18:58:07.963930 |
| 2026-05-09 | 01343 | [3, 10, 32, 37, 45, 55, 46] | 2026-05-10T00:01:08.118122 |
| 2026-05-07 | 01342 | [13, 14, 33, 44, 46, 50, 47] | 2026-05-08T12:04:58.259525 |
| 2026-05-05 | 01341 | [4, 6, 8, 17, 30, 50, 32] | 2026-05-08T12:04:58.261267 |
| 2026-05-02 | 01340 | [9, 21, 22, 26, 33, 51, 17] | 2026-05-02T18:53:23.258397 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 1.89 |  | 21 | 169 | 1.79 |  | 41 | 198 | 2.1 |
| 2 | 153 | 1.62 |  | 22 | 202 | 2.14 |  | 42 | 173 | 1.83 |
| 3 | 183 | 1.94 |  | 23 | 179 | 1.9 |  | 43 | 194 | 2.05 |
| 4 | 141 | 1.49 |  | 24 | 170 | 1.8 |  | 44 | 175 | 1.85 |
| 5 | 172 | 1.82 |  | 25 | 154 | 1.63 |  | 45 | 172 | 1.82 |
| 6 | 141 | 1.49 |  | 26 | 164 | 1.74 |  | 46 | 176 | 1.86 |
| 7 | 152 | 1.61 |  | 27 | 157 | 1.66 |  | 47 | 172 | 1.82 |
| 8 | 183 | 1.94 |  | 28 | 152 | 1.61 |  | 48 | 184 | 1.95 |
| 9 | 188 | 1.99 |  | 29 | 185 | 1.96 |  | 49 | 168 | 1.78 |
| 10 | 162 | 1.72 |  | 30 | 158 | 1.67 |  | 50 | 174 | 1.84 |
| 11 | 174 | 1.84 |  | 31 | 180 | 1.91 |  | 51 | 192 | 2.03 |
| 12 | 179 | 1.9 |  | 32 | 183 | 1.94 |  | 52 | 175 | 1.85 |
| 13 | 168 | 1.78 |  | 33 | 172 | 1.82 |  | 53 | 184 | 1.95 |
| 14 | 170 | 1.8 |  | 34 | 192 | 2.03 |  | 54 | 163 | 1.73 |
| 15 | 161 | 1.71 |  | 35 | 166 | 1.76 |  | 55 | 173 | 1.83 |
| 16 | 167 | 1.77 |  | 36 | 163 | 1.73 |  |  |  |  |
| 17 | 156 | 1.65 |  | 37 | 154 | 1.63 |  |  |  |  |
| 18 | 171 | 1.81 |  | 38 | 167 | 1.77 |  |  |  |  |
| 19 | 169 | 1.79 |  | 39 | 165 | 1.75 |  |  |  |  |
| 20 | 183 | 1.94 |  | 40 | 186 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.19 |  | 26 | 3 | 3.57 |  | 48 | 2 | 2.38 |
| 3 | 2 | 2.38 |  | 27 | 1 | 1.19 |  | 49 | 1 | 1.19 |
| 4 | 1 | 1.19 |  | 28 | 2 | 2.38 |  | 50 | 5 | 5.95 |
| 6 | 1 | 1.19 |  | 29 | 1 | 1.19 |  | 51 | 2 | 2.38 |
| 8 | 2 | 2.38 |  | 30 | 1 | 1.19 |  | 52 | 1 | 1.19 |
| 9 | 2 | 2.38 |  | 31 | 1 | 1.19 |  | 53 | 2 | 2.38 |
| 10 | 1 | 1.19 |  | 32 | 4 | 4.76 |  | 55 | 2 | 2.38 |
| 11 | 1 | 1.19 |  | 33 | 2 | 2.38 |  |  |  |  |
| 12 | 1 | 1.19 |  | 34 | 2 | 2.38 |  |  |  |  |
| 13 | 1 | 1.19 |  | 35 | 1 | 1.19 |  |  |  |  |
| 14 | 1 | 1.19 |  | 36 | 1 | 1.19 |  |  |  |  |
| 15 | 2 | 2.38 |  | 37 | 1 | 1.19 |  |  |  |  |
| 16 | 2 | 2.38 |  | 38 | 2 | 2.38 |  |  |  |  |
| 17 | 3 | 3.57 |  | 39 | 3 | 3.57 |  |  |  |  |
| 18 | 1 | 1.19 |  | 40 | 2 | 2.38 |  |  |  |  |
| 20 | 1 | 1.19 |  | 41 | 1 | 1.19 |  |  |  |  |
| 21 | 4 | 4.76 |  | 44 | 1 | 1.19 |  |  |  |  |
| 22 | 3 | 3.57 |  | 45 | 2 | 2.38 |  |  |  |  |
| 24 | 1 | 1.19 |  | 46 | 2 | 2.38 |  |  |  |  |
| 25 | 3 | 3.57 |  | 47 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.57 |  | 21 | 6 | 3.43 |  | 41 | 3 | 1.71 |
| 2 | 2 | 1.14 |  | 22 | 9 | 5.14 |  | 42 | 1 | 0.57 |
| 3 | 2 | 1.14 |  | 23 | 2 | 1.14 |  | 43 | 2 | 1.14 |
| 4 | 2 | 1.14 |  | 24 | 2 | 1.14 |  | 44 | 2 | 1.14 |
| 5 | 2 | 1.14 |  | 25 | 3 | 1.71 |  | 45 | 2 | 1.14 |
| 6 | 1 | 0.57 |  | 26 | 4 | 2.29 |  | 46 | 3 | 1.71 |
| 7 | 5 | 2.86 |  | 27 | 1 | 0.57 |  | 47 | 4 | 2.29 |
| 8 | 4 | 2.29 |  | 28 | 4 | 2.29 |  | 48 | 3 | 1.71 |
| 9 | 4 | 2.29 |  | 29 | 4 | 2.29 |  | 49 | 2 | 1.14 |
| 10 | 3 | 1.71 |  | 30 | 4 | 2.29 |  | 50 | 6 | 3.43 |
| 11 | 2 | 1.14 |  | 31 | 2 | 1.14 |  | 51 | 2 | 1.14 |
| 12 | 1 | 0.57 |  | 32 | 6 | 3.43 |  | 52 | 3 | 1.71 |
| 13 | 4 | 2.29 |  | 33 | 4 | 2.29 |  | 53 | 8 | 4.57 |
| 14 | 1 | 0.57 |  | 34 | 3 | 1.71 |  | 54 | 1 | 0.57 |
| 15 | 5 | 2.86 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 16 | 6 | 3.43 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 2 | 1.14 |  | 38 | 5 | 2.86 |  |  |  |  |
| 19 | 1 | 0.57 |  | 39 | 7 | 4.0 |  |  |  |  |
| 20 | 2 | 1.14 |  | 40 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.13 |  | 21 | 7 | 2.63 |  | 41 | 4 | 1.5 |
| 2 | 2 | 0.75 |  | 22 | 10 | 3.76 |  | 42 | 1 | 0.38 |
| 3 | 6 | 2.26 |  | 23 | 2 | 0.75 |  | 43 | 6 | 2.26 |
| 4 | 3 | 1.13 |  | 24 | 2 | 0.75 |  | 44 | 5 | 1.88 |
| 5 | 2 | 0.75 |  | 25 | 6 | 2.26 |  | 45 | 4 | 1.5 |
| 6 | 2 | 0.75 |  | 26 | 8 | 3.01 |  | 46 | 4 | 1.5 |
| 7 | 9 | 3.38 |  | 27 | 3 | 1.13 |  | 47 | 7 | 2.63 |
| 8 | 4 | 1.5 |  | 28 | 6 | 2.26 |  | 48 | 3 | 1.13 |
| 9 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 2 | 0.75 |
| 10 | 5 | 1.88 |  | 30 | 4 | 1.5 |  | 50 | 9 | 3.38 |
| 11 | 2 | 0.75 |  | 31 | 5 | 1.88 |  | 51 | 6 | 2.26 |
| 12 | 4 | 1.5 |  | 32 | 8 | 3.01 |  | 52 | 6 | 2.26 |
| 13 | 5 | 1.88 |  | 33 | 4 | 1.5 |  | 53 | 10 | 3.76 |
| 14 | 2 | 0.75 |  | 34 | 5 | 1.88 |  | 54 | 5 | 1.88 |
| 15 | 5 | 1.88 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 8 | 3.01 |  | 36 | 5 | 1.88 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 2 | 0.75 |  | 38 | 7 | 2.63 |  |  |  |  |
| 19 | 2 | 0.75 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 3 | 1.13 |  | 40 | 5 | 1.88 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 42 | 2026-03-28 | 56 |
| 54 | 2026-04-04 | 49 |
| 1 | 2026-04-07 | 46 |
| 23 | 2026-04-07 | 46 |
| 19 | 2026-04-18 | 35 |
| 5 | 2026-04-23 | 30 |
| 7 | 2026-04-25 | 28 |
| 43 | 2026-04-25 | 28 |
| 24 | 2026-04-28 | 25 |
| 52 | 2026-04-28 | 25 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-04-07 | 46 |
| 2 | 2026-05-12 | 11 |
| 3 | 2026-05-23 | 0 |
| 4 | 2026-05-05 | 18 |
| 5 | 2026-04-23 | 30 |
| 6 | 2026-05-05 | 18 |
| 7 | 2026-04-25 | 28 |
| 8 | 2026-05-16 | 7 |
| 9 | 2026-05-02 | 21 |
| 10 | 2026-05-09 | 14 |
| 11 | 2026-05-12 | 11 |
| 12 | 2026-05-19 | 4 |
| 13 | 2026-05-07 | 16 |
| 14 | 2026-05-07 | 16 |
| 15 | 2026-05-12 | 11 |
| 16 | 2026-05-21 | 2 |
| 17 | 2026-05-23 | 0 |
| 18 | 2026-05-21 | 2 |
| 19 | 2026-04-18 | 35 |
| 20 | 2026-05-21 | 2 |
| 21 | 2026-05-23 | 0 |
| 22 | 2026-05-23 | 0 |
| 23 | 2026-04-07 | 46 |
| 24 | 2026-04-28 | 25 |
| 25 | 2026-05-16 | 7 |
| 26 | 2026-05-14 | 9 |
| 27 | 2026-05-23 | 0 |
| 28 | 2026-05-21 | 2 |
| 29 | 2026-04-30 | 23 |
| 30 | 2026-05-05 | 18 |
| 31 | 2026-05-12 | 11 |
| 32 | 2026-05-21 | 2 |
| 33 | 2026-05-07 | 16 |
| 34 | 2026-05-21 | 2 |
| 35 | 2026-04-28 | 25 |
| 36 | 2026-05-16 | 7 |
| 37 | 2026-05-09 | 14 |
| 38 | 2026-05-23 | 0 |
| 39 | 2026-05-19 | 4 |
| 40 | 2026-05-21 | 2 |
| 41 | 2026-05-14 | 9 |
| 42 | 2026-03-28 | 56 |
| 43 | 2026-04-25 | 28 |
| 44 | 2026-05-07 | 16 |
| 45 | 2026-05-19 | 4 |
| 46 | 2026-05-09 | 14 |
| 47 | 2026-05-16 | 7 |
| 48 | 2026-05-19 | 4 |
| 49 | 2026-05-23 | 0 |
| 50 | 2026-05-16 | 7 |
| 51 | 2026-05-02 | 21 |
| 52 | 2026-04-28 | 25 |
| 53 | 2026-05-19 | 4 |
| 54 | 2026-04-04 | 49 |
| 55 | 2026-05-14 | 9 |



## ⚙️ How It Works

### 🤖 Automated Data Collection

This project runs completely automatically using **GitHub Actions** - no server required!

- **⏰ Schedule**: Runs daily via [GitHub Actions workflow](.github/workflows/crawl.yaml)
- **🔄 Process**: Fetches latest results → Processes data → Commits to repository
- **📊 Analysis**: Generates statistics and updates README automatically

### 🕵️ Data Crawling Method

The data collection works by:
1. **🔍 Network Analysis**: Inspecting browser-server communication
2. **🐍 Python Replication**: Recreating the data fetch logic in Python
3. **📋 Structured Storage**: Saving results in JSONL format for easy analysis
4. **🔄 Continuous Updates**: Daily automated runs ensure fresh data

> **Note**: This is purely for educational and research purposes. No gambling advice is provided.


## 🚀 Installation & Usage

### 📦 Install via pip

```bash
pip install -i vietlott-data
```

### 💻 Command Line Interface

#### 🔍 Crawl Data

```bash
vietlott-crawl [OPTIONS] PRODUCT

# Options:
#   --run-date TEXT       Specific date to crawl (default: current date)
#   --index-from INTEGER  Starting page index (default: 0)
#   --index-to INTEGER    Ending page index (default: None)
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process (default: 20)
#   --help          Show help message
```

> **Available Products**: power_655, power_645, power_535, keno, 3d, 3d_pro, bingo18

### 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/vietvudanh/vietlott-data.git ; cd vietlott-data

# Install dependencies (recommend using uv and virtual environment)
uv sync --dev

# Run tests
uv run pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>

