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
| Power 655 | 1355 | 2017-08-01 | 2026-06-06 | 1355 | 00001 | 01355 |
| Power 645 | 1323 | 2017-10-25 | 2026-06-07 | 1323 | 00198 | 01520 |
| Power 535 | 309 | 2025-06-29 | 2026-06-08 | 617 | 00001 | 00690 |
| Keno | 577 | 2022-12-04 | 2026-06-08 | 72856 | #0110271 | #0284074 |
| 3D | 1086 | 2019-04-22 | 2026-06-08 | 1086 | 00001 | 01090 |
| 3D Pro | 732 | 2021-09-14 | 2026-06-06 | 732 | 00001 | 00736 |
| Bingo18 | 549 | 2024-12-03 | 2026-06-08 | 74617 | 0083123 | 0170934 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-06-06 | 01355 | [3, 11, 16, 37, 39, 41, 28] | 2026-06-09T00:01:21.410974 |
| 2026-06-04 | 01354 | [23, 24, 28, 29, 39, 43, 45] | 2026-06-05T00:01:07.859417 |
| 2026-06-02 | 01353 | [1, 3, 5, 16, 37, 51, 42] | 2026-06-03T00:01:21.144685 |
| 2026-05-30 | 01352 | [2, 8, 20, 24, 25, 42, 44] | 2026-06-01T00:01:26.268124 |
| 2026-05-28 | 01351 | [8, 11, 21, 25, 31, 53, 54] | 2026-05-29T00:01:21.691058 |
| 2026-05-26 | 01350 | [1, 14, 15, 19, 23, 34, 29] | 2026-05-27T00:01:07.369677 |
| 2026-05-23 | 01349 | [17, 21, 22, 27, 38, 49, 3] | 2026-05-24T00:01:17.320252 |
| 2026-05-21 | 01348 | [16, 18, 20, 28, 32, 34, 40] | 2026-05-22T00:01:24.083070 |
| 2026-05-19 | 01347 | [12, 39, 40, 45, 48, 53, 21] | 2026-05-21T18:37:39.362594 |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 180 | 1.9 |  | 21 | 170 | 1.79 |  | 41 | 199 | 2.1 |
| 2 | 154 | 1.62 |  | 22 | 202 | 2.13 |  | 42 | 175 | 1.85 |
| 3 | 185 | 1.95 |  | 23 | 181 | 1.91 |  | 43 | 195 | 2.06 |
| 4 | 141 | 1.49 |  | 24 | 172 | 1.81 |  | 44 | 176 | 1.86 |
| 5 | 173 | 1.82 |  | 25 | 156 | 1.64 |  | 45 | 173 | 1.82 |
| 6 | 141 | 1.49 |  | 26 | 164 | 1.73 |  | 46 | 176 | 1.86 |
| 7 | 152 | 1.6 |  | 27 | 157 | 1.66 |  | 47 | 172 | 1.81 |
| 8 | 185 | 1.95 |  | 28 | 154 | 1.62 |  | 48 | 184 | 1.94 |
| 9 | 188 | 1.98 |  | 29 | 187 | 1.97 |  | 49 | 168 | 1.77 |
| 10 | 162 | 1.71 |  | 30 | 158 | 1.67 |  | 50 | 174 | 1.83 |
| 11 | 176 | 1.86 |  | 31 | 181 | 1.91 |  | 51 | 193 | 2.04 |
| 12 | 179 | 1.89 |  | 32 | 183 | 1.93 |  | 52 | 175 | 1.85 |
| 13 | 168 | 1.77 |  | 33 | 172 | 1.81 |  | 53 | 185 | 1.95 |
| 14 | 171 | 1.8 |  | 34 | 193 | 2.04 |  | 54 | 164 | 1.73 |
| 15 | 162 | 1.71 |  | 35 | 166 | 1.75 |  | 55 | 173 | 1.82 |
| 16 | 169 | 1.78 |  | 36 | 163 | 1.72 |  |  |  |  |
| 17 | 156 | 1.64 |  | 37 | 156 | 1.64 |  |  |  |  |
| 18 | 171 | 1.8 |  | 38 | 167 | 1.76 |  |  |  |  |
| 19 | 170 | 1.79 |  | 39 | 167 | 1.76 |  |  |  |  |
| 20 | 184 | 1.94 |  | 40 | 186 | 1.96 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 27 | 1 | 1.19 |  | 51 | 1 | 1.19 |
| 2 | 2 | 2.38 |  | 28 | 4 | 4.76 |  | 53 | 2 | 2.38 |
| 3 | 3 | 3.57 |  | 29 | 2 | 2.38 |  | 54 | 1 | 1.19 |
| 5 | 1 | 1.19 |  | 31 | 2 | 2.38 |  | 55 | 1 | 1.19 |
| 8 | 3 | 3.57 |  | 32 | 2 | 2.38 |  |  |  |  |
| 11 | 3 | 3.57 |  | 34 | 2 | 2.38 |  |  |  |  |
| 12 | 1 | 1.19 |  | 36 | 1 | 1.19 |  |  |  |  |
| 14 | 1 | 1.19 |  | 37 | 2 | 2.38 |  |  |  |  |
| 15 | 2 | 2.38 |  | 38 | 2 | 2.38 |  |  |  |  |
| 16 | 3 | 3.57 |  | 39 | 5 | 5.95 |  |  |  |  |
| 17 | 1 | 1.19 |  | 40 | 2 | 2.38 |  |  |  |  |
| 18 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 42 | 2 | 2.38 |  |  |  |  |
| 20 | 2 | 2.38 |  | 43 | 1 | 1.19 |  |  |  |  |
| 21 | 3 | 3.57 |  | 44 | 1 | 1.19 |  |  |  |  |
| 22 | 2 | 2.38 |  | 45 | 2 | 2.38 |  |  |  |  |
| 23 | 2 | 2.38 |  | 47 | 1 | 1.19 |  |  |  |  |
| 24 | 2 | 2.38 |  | 48 | 2 | 2.38 |  |  |  |  |
| 25 | 3 | 3.57 |  | 49 | 1 | 1.19 |  |  |  |  |
| 26 | 2 | 2.38 |  | 50 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.14 |  | 21 | 5 | 2.86 |  | 41 | 3 | 1.71 |
| 2 | 3 | 1.71 |  | 22 | 6 | 3.43 |  | 42 | 2 | 1.14 |
| 3 | 4 | 2.29 |  | 23 | 2 | 1.14 |  | 43 | 2 | 1.14 |
| 4 | 2 | 1.14 |  | 24 | 4 | 2.29 |  | 44 | 2 | 1.14 |
| 5 | 2 | 1.14 |  | 25 | 5 | 2.86 |  | 45 | 3 | 1.71 |
| 6 | 1 | 0.57 |  | 26 | 4 | 2.29 |  | 46 | 3 | 1.71 |
| 7 | 3 | 1.71 |  | 27 | 1 | 0.57 |  | 47 | 4 | 2.29 |
| 8 | 6 | 3.43 |  | 28 | 6 | 3.43 |  | 48 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 29 | 5 | 2.86 |  | 49 | 2 | 1.14 |
| 10 | 2 | 1.14 |  | 30 | 2 | 1.14 |  | 50 | 6 | 3.43 |
| 11 | 3 | 1.71 |  | 31 | 2 | 1.14 |  | 51 | 3 | 1.71 |
| 12 | 1 | 0.57 |  | 32 | 4 | 2.29 |  | 52 | 2 | 1.14 |
| 13 | 2 | 1.14 |  | 33 | 3 | 1.71 |  | 53 | 6 | 3.43 |
| 14 | 2 | 1.14 |  | 34 | 3 | 1.71 |  | 54 | 1 | 0.57 |
| 15 | 5 | 2.86 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 16 | 6 | 3.43 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 4 | 2.29 |  |  |  |  |
| 18 | 1 | 0.57 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 8 | 4.57 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 2 | 1.14 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.5 |  | 21 | 7 | 2.63 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 9 | 3.38 |  | 42 | 3 | 1.13 |
| 3 | 7 | 2.63 |  | 23 | 4 | 1.5 |  | 43 | 5 | 1.88 |
| 4 | 2 | 0.75 |  | 24 | 4 | 1.5 |  | 44 | 4 | 1.5 |
| 5 | 3 | 1.13 |  | 25 | 6 | 2.26 |  | 45 | 4 | 1.5 |
| 6 | 2 | 0.75 |  | 26 | 7 | 2.63 |  | 46 | 3 | 1.13 |
| 7 | 7 | 2.63 |  | 27 | 2 | 0.75 |  | 47 | 6 | 2.26 |
| 8 | 6 | 2.26 |  | 28 | 8 | 3.01 |  | 48 | 3 | 1.13 |
| 9 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 2 | 0.75 |
| 10 | 4 | 1.5 |  | 30 | 4 | 1.5 |  | 50 | 7 | 2.63 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 4 | 1.5 |
| 12 | 4 | 1.5 |  | 32 | 7 | 2.63 |  | 52 | 5 | 1.88 |
| 13 | 4 | 1.5 |  | 33 | 4 | 1.5 |  | 53 | 11 | 4.14 |
| 14 | 2 | 0.75 |  | 34 | 6 | 2.26 |  | 54 | 4 | 1.5 |
| 15 | 6 | 2.26 |  | 35 | 2 | 0.75 |  | 55 | 6 | 2.26 |
| 16 | 9 | 3.38 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 2 | 0.75 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 9 | 3.38 |  |  |  |  |
| 20 | 3 | 1.13 |  | 40 | 5 | 1.88 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 7 | 2026-04-25 | 42 |
| 52 | 2026-04-28 | 39 |
| 35 | 2026-04-28 | 39 |
| 9 | 2026-05-02 | 35 |
| 6 | 2026-05-05 | 32 |
| 30 | 2026-05-05 | 32 |
| 4 | 2026-05-05 | 32 |
| 33 | 2026-05-07 | 30 |
| 13 | 2026-05-07 | 30 |
| 46 | 2026-05-09 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-02 | 4 |
| 2 | 2026-05-30 | 7 |
| 3 | 2026-06-06 | 0 |
| 4 | 2026-05-05 | 32 |
| 5 | 2026-06-02 | 4 |
| 6 | 2026-05-05 | 32 |
| 7 | 2026-04-25 | 42 |
| 8 | 2026-05-30 | 7 |
| 9 | 2026-05-02 | 35 |
| 10 | 2026-05-09 | 28 |
| 11 | 2026-06-06 | 0 |
| 12 | 2026-05-19 | 18 |
| 13 | 2026-05-07 | 30 |
| 14 | 2026-05-26 | 11 |
| 15 | 2026-05-26 | 11 |
| 16 | 2026-06-06 | 0 |
| 17 | 2026-05-23 | 14 |
| 18 | 2026-05-21 | 16 |
| 19 | 2026-05-26 | 11 |
| 20 | 2026-05-30 | 7 |
| 21 | 2026-05-28 | 9 |
| 22 | 2026-05-23 | 14 |
| 23 | 2026-06-04 | 2 |
| 24 | 2026-06-04 | 2 |
| 25 | 2026-05-30 | 7 |
| 26 | 2026-05-14 | 23 |
| 27 | 2026-05-23 | 14 |
| 28 | 2026-06-06 | 0 |
| 29 | 2026-06-04 | 2 |
| 30 | 2026-05-05 | 32 |
| 31 | 2026-05-28 | 9 |
| 32 | 2026-05-21 | 16 |
| 33 | 2026-05-07 | 30 |
| 34 | 2026-05-26 | 11 |
| 35 | 2026-04-28 | 39 |
| 36 | 2026-05-16 | 21 |
| 37 | 2026-06-06 | 0 |
| 38 | 2026-05-23 | 14 |
| 39 | 2026-06-06 | 0 |
| 40 | 2026-05-21 | 16 |
| 41 | 2026-06-06 | 0 |
| 42 | 2026-06-02 | 4 |
| 43 | 2026-06-04 | 2 |
| 44 | 2026-05-30 | 7 |
| 45 | 2026-06-04 | 2 |
| 46 | 2026-05-09 | 28 |
| 47 | 2026-05-16 | 21 |
| 48 | 2026-05-19 | 18 |
| 49 | 2026-05-23 | 14 |
| 50 | 2026-05-16 | 21 |
| 51 | 2026-06-02 | 4 |
| 52 | 2026-04-28 | 39 |
| 53 | 2026-05-28 | 9 |
| 54 | 2026-05-28 | 9 |
| 55 | 2026-05-14 | 23 |



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

