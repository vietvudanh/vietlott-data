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
| Power 645 | 1316 | 2017-10-25 | 2026-05-22 | 1316 | 00198 | 01513 |
| Power 535 | 293 | 2025-06-29 | 2026-05-23 | 585 | 00001 | 00658 |
| Keno | 562 | 2022-12-04 | 2026-05-23 | 71089 | #0110271 | #0282170 |
| 3D | 1079 | 2019-04-22 | 2026-05-22 | 1079 | 00001 | 01083 |
| 3D Pro | 726 | 2021-09-14 | 2026-05-23 | 726 | 00001 | 00730 |
| Bingo18 | 535 | 2024-12-03 | 2026-05-23 | 72437 | 0083123 | 0168390 |

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
| 2 | 1 | 1.1 |  | 25 | 3 | 3.3 |  | 46 | 3 | 3.3 |
| 3 | 2 | 2.2 |  | 26 | 3 | 3.3 |  | 47 | 2 | 2.2 |
| 4 | 2 | 2.2 |  | 27 | 1 | 1.1 |  | 48 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 28 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 50 | 5 | 5.49 |
| 8 | 2 | 2.2 |  | 30 | 1 | 1.1 |  | 51 | 2 | 2.2 |
| 9 | 2 | 2.2 |  | 31 | 1 | 1.1 |  | 52 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 32 | 4 | 4.4 |  | 53 | 2 | 2.2 |
| 11 | 1 | 1.1 |  | 33 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 12 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 13 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 17 | 3 | 3.3 |  | 39 | 3 | 3.3 |  |  |  |  |
| 18 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 20 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 21 | 4 | 4.4 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 3 | 3.3 |  | 44 | 1 | 1.1 |  |  |  |  |
| 24 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 21 | 6 | 3.3 |  | 41 | 3 | 1.65 |
| 2 | 2 | 1.1 |  | 22 | 9 | 4.95 |  | 42 | 1 | 0.55 |
| 3 | 3 | 1.65 |  | 23 | 2 | 1.1 |  | 43 | 2 | 1.1 |
| 4 | 2 | 1.1 |  | 24 | 2 | 1.1 |  | 44 | 3 | 1.65 |
| 5 | 2 | 1.1 |  | 25 | 3 | 1.65 |  | 45 | 2 | 1.1 |
| 6 | 1 | 0.55 |  | 26 | 4 | 2.2 |  | 46 | 3 | 1.65 |
| 7 | 5 | 2.75 |  | 27 | 1 | 0.55 |  | 47 | 4 | 2.2 |
| 8 | 4 | 2.2 |  | 28 | 4 | 2.2 |  | 48 | 3 | 1.65 |
| 9 | 5 | 2.75 |  | 29 | 4 | 2.2 |  | 49 | 2 | 1.1 |
| 10 | 4 | 2.2 |  | 30 | 4 | 2.2 |  | 50 | 6 | 3.3 |
| 11 | 2 | 1.1 |  | 31 | 2 | 1.1 |  | 51 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 6 | 3.3 |  | 52 | 3 | 1.65 |
| 13 | 4 | 2.2 |  | 33 | 4 | 2.2 |  | 53 | 8 | 4.4 |
| 14 | 1 | 0.55 |  | 34 | 4 | 2.2 |  | 54 | 1 | 0.55 |
| 15 | 5 | 2.75 |  | 35 | 2 | 1.1 |  | 55 | 4 | 2.2 |
| 16 | 6 | 3.3 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 6 | 3.3 |  |  |  |  |
| 19 | 1 | 0.55 |  | 39 | 7 | 3.85 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.1 |  | 21 | 7 | 2.56 |  | 41 | 4 | 1.47 |
| 2 | 2 | 0.73 |  | 22 | 10 | 3.66 |  | 42 | 1 | 0.37 |
| 3 | 6 | 2.2 |  | 23 | 2 | 0.73 |  | 43 | 6 | 2.2 |
| 4 | 3 | 1.1 |  | 24 | 2 | 0.73 |  | 44 | 5 | 1.83 |
| 5 | 3 | 1.1 |  | 25 | 6 | 2.2 |  | 45 | 4 | 1.47 |
| 6 | 2 | 0.73 |  | 26 | 8 | 2.93 |  | 46 | 4 | 1.47 |
| 7 | 9 | 3.3 |  | 27 | 3 | 1.1 |  | 47 | 7 | 2.56 |
| 8 | 5 | 1.83 |  | 28 | 6 | 2.2 |  | 48 | 3 | 1.1 |
| 9 | 6 | 2.2 |  | 29 | 7 | 2.56 |  | 49 | 2 | 0.73 |
| 10 | 5 | 1.83 |  | 30 | 5 | 1.83 |  | 50 | 9 | 3.3 |
| 11 | 2 | 0.73 |  | 31 | 5 | 1.83 |  | 51 | 7 | 2.56 |
| 12 | 4 | 1.47 |  | 32 | 8 | 2.93 |  | 52 | 6 | 2.2 |
| 13 | 5 | 1.83 |  | 33 | 4 | 1.47 |  | 53 | 10 | 3.66 |
| 14 | 2 | 0.73 |  | 34 | 5 | 1.83 |  | 54 | 6 | 2.2 |
| 15 | 5 | 1.83 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 8 | 2.93 |  | 36 | 5 | 1.83 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 3 | 1.1 |  | 38 | 7 | 2.56 |  |  |  |  |
| 19 | 2 | 0.73 |  | 39 | 9 | 3.3 |  |  |  |  |
| 20 | 3 | 1.1 |  | 40 | 5 | 1.83 |  |  |  |  |

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

