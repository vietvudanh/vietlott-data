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
| Power 655 | 1371 | 2017-08-01 | 2026-07-14 | 1371 | 00001 | 01371 |
| Power 645 | 1339 | 2017-10-25 | 2026-07-15 | 1339 | 00198 | 01536 |
| Power 535 | 345 | 2025-06-29 | 2026-07-15 | 688 | 00001 | 00764 |
| Keno | 612 | 2022-12-04 | 2026-07-15 | 76970 | #0110271 | #0288477 |
| 3D | 1102 | 2019-04-22 | 2026-07-15 | 1102 | 00001 | 01106 |
| 3D Pro | 748 | 2021-09-14 | 2026-07-14 | 748 | 00001 | 00752 |
| Bingo18 | 588 | 2024-12-03 | 2026-07-15 | 80896 | 0083123 | 0176817 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54] | 2026-07-04T17:51:54.286368 |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23] | 2026-07-04T17:51:54.288114 |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5] | 2026-06-24T00:01:16.333044 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.92 |  | 21 | 171 | 1.78 |  | 41 | 202 | 2.11 |
| 2 | 157 | 1.64 |  | 22 | 203 | 2.12 |  | 42 | 178 | 1.85 |
| 3 | 186 | 1.94 |  | 23 | 185 | 1.93 |  | 43 | 197 | 2.05 |
| 4 | 144 | 1.5 |  | 24 | 174 | 1.81 |  | 44 | 178 | 1.85 |
| 5 | 177 | 1.84 |  | 25 | 157 | 1.64 |  | 45 | 175 | 1.82 |
| 6 | 143 | 1.49 |  | 26 | 165 | 1.72 |  | 46 | 180 | 1.88 |
| 7 | 154 | 1.6 |  | 27 | 158 | 1.65 |  | 47 | 174 | 1.81 |
| 8 | 190 | 1.98 |  | 28 | 157 | 1.64 |  | 48 | 185 | 1.93 |
| 9 | 190 | 1.98 |  | 29 | 187 | 1.95 |  | 49 | 171 | 1.78 |
| 10 | 164 | 1.71 |  | 30 | 160 | 1.67 |  | 50 | 174 | 1.81 |
| 11 | 177 | 1.84 |  | 31 | 183 | 1.91 |  | 51 | 194 | 2.02 |
| 12 | 179 | 1.87 |  | 32 | 185 | 1.93 |  | 52 | 177 | 1.84 |
| 13 | 171 | 1.78 |  | 33 | 176 | 1.83 |  | 53 | 186 | 1.94 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.03 |  | 54 | 165 | 1.72 |
| 15 | 164 | 1.71 |  | 35 | 169 | 1.76 |  | 55 | 174 | 1.81 |
| 16 | 171 | 1.78 |  | 36 | 165 | 1.72 |  |  |  |  |
| 17 | 159 | 1.66 |  | 37 | 156 | 1.63 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 168 | 1.75 |  |  |  |  |
| 19 | 171 | 1.78 |  | 39 | 167 | 1.74 |  |  |  |  |
| 20 | 186 | 1.94 |  | 40 | 190 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 23 | 4 | 4.4 |  | 47 | 1 | 1.1 |
| 2 | 2 | 2.2 |  | 24 | 1 | 1.1 |  | 49 | 3 | 3.3 |
| 3 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 4 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 52 | 2 | 2.2 |
| 5 | 4 | 4.4 |  | 28 | 3 | 3.3 |  | 53 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 30 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 31 | 2 | 2.2 |  | 55 | 1 | 1.1 |
| 8 | 2 | 2.2 |  | 32 | 1 | 1.1 |  |  |  |  |
| 9 | 2 | 2.2 |  | 33 | 3 | 3.3 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 2 | 2.2 |  |  |  |  |
| 13 | 3 | 3.3 |  | 36 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 38 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 3 | 3.3 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 18 | 2 | 2.2 |  | 43 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 22 | 1 | 1.1 |  | 46 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.43 |  | 21 | 4 | 2.29 |  | 41 | 4 | 2.29 |
| 2 | 4 | 2.29 |  | 22 | 2 | 1.14 |  | 42 | 5 | 2.86 |
| 3 | 4 | 2.29 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 4 | 3 | 1.71 |  | 24 | 4 | 2.29 |  | 44 | 3 | 1.71 |
| 5 | 5 | 2.86 |  | 25 | 3 | 1.71 |  | 45 | 4 | 2.29 |
| 6 | 2 | 1.14 |  | 26 | 1 | 0.57 |  | 46 | 4 | 2.29 |
| 7 | 2 | 1.14 |  | 27 | 2 | 1.14 |  | 47 | 2 | 1.14 |
| 8 | 7 | 4.0 |  | 28 | 6 | 3.43 |  | 48 | 2 | 1.14 |
| 9 | 2 | 1.14 |  | 29 | 2 | 1.14 |  | 49 | 4 | 2.29 |
| 10 | 2 | 1.14 |  | 30 | 2 | 1.14 |  | 51 | 2 | 1.14 |
| 11 | 3 | 1.71 |  | 31 | 3 | 1.71 |  | 52 | 2 | 1.14 |
| 12 | 1 | 0.57 |  | 32 | 3 | 1.71 |  | 53 | 3 | 1.71 |
| 13 | 3 | 1.71 |  | 33 | 4 | 2.29 |  | 54 | 2 | 1.14 |
| 14 | 4 | 2.29 |  | 34 | 4 | 2.29 |  | 55 | 1 | 0.57 |
| 15 | 3 | 1.71 |  | 35 | 3 | 1.71 |  |  |  |  |
| 16 | 5 | 2.86 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 4 | 2.29 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 3 | 1.71 |  |  |  |  |
| 20 | 4 | 2.29 |  | 40 | 6 | 3.43 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.26 |  | 21 | 6 | 2.26 |  | 41 | 6 | 2.26 |
| 2 | 5 | 1.88 |  | 22 | 5 | 1.88 |  | 42 | 5 | 1.88 |
| 3 | 5 | 1.88 |  | 23 | 6 | 2.26 |  | 43 | 4 | 1.5 |
| 4 | 5 | 1.88 |  | 24 | 6 | 2.26 |  | 44 | 4 | 1.5 |
| 5 | 6 | 2.26 |  | 25 | 6 | 2.26 |  | 45 | 5 | 1.88 |
| 6 | 3 | 1.13 |  | 26 | 4 | 1.5 |  | 46 | 7 | 2.63 |
| 7 | 3 | 1.13 |  | 27 | 2 | 0.75 |  | 47 | 4 | 1.5 |
| 8 | 10 | 3.76 |  | 28 | 8 | 3.01 |  | 48 | 3 | 1.13 |
| 9 | 5 | 1.88 |  | 29 | 4 | 1.5 |  | 49 | 4 | 1.5 |
| 10 | 4 | 1.5 |  | 30 | 4 | 1.5 |  | 50 | 6 | 2.26 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 4 | 1.5 |
| 12 | 1 | 0.38 |  | 32 | 6 | 2.26 |  | 52 | 3 | 1.13 |
| 13 | 4 | 1.5 |  | 33 | 7 | 2.63 |  | 53 | 6 | 2.26 |
| 14 | 5 | 1.88 |  | 34 | 5 | 1.88 |  | 54 | 2 | 0.75 |
| 15 | 6 | 2.26 |  | 35 | 4 | 1.5 |  | 55 | 4 | 1.5 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 7 | 2.63 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 3 | 1.13 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 7 | 2.63 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 6 | 2.26 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 50 | 2026-05-16 | 59 |
| 12 | 2026-05-19 | 56 |
| 29 | 2026-06-04 | 40 |
| 39 | 2026-06-06 | 38 |
| 37 | 2026-06-06 | 38 |
| 27 | 2026-06-09 | 35 |
| 48 | 2026-06-11 | 33 |
| 19 | 2026-06-13 | 31 |
| 36 | 2026-06-18 | 26 |
| 26 | 2026-06-20 | 24 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 19 |
| 2 | 2026-07-09 | 5 |
| 3 | 2026-06-25 | 19 |
| 4 | 2026-07-07 | 7 |
| 5 | 2026-07-02 | 12 |
| 6 | 2026-07-07 | 7 |
| 7 | 2026-06-27 | 17 |
| 8 | 2026-07-07 | 7 |
| 9 | 2026-07-11 | 3 |
| 10 | 2026-07-14 | 0 |
| 11 | 2026-07-02 | 12 |
| 12 | 2026-05-19 | 56 |
| 13 | 2026-07-04 | 10 |
| 14 | 2026-07-09 | 5 |
| 15 | 2026-07-04 | 10 |
| 16 | 2026-06-27 | 17 |
| 17 | 2026-07-11 | 3 |
| 18 | 2026-07-04 | 10 |
| 19 | 2026-06-13 | 31 |
| 20 | 2026-07-11 | 3 |
| 21 | 2026-06-27 | 17 |
| 22 | 2026-06-30 | 14 |
| 23 | 2026-07-04 | 10 |
| 24 | 2026-07-14 | 0 |
| 25 | 2026-07-07 | 7 |
| 26 | 2026-06-20 | 24 |
| 27 | 2026-06-09 | 35 |
| 28 | 2026-07-02 | 12 |
| 29 | 2026-06-04 | 40 |
| 30 | 2026-07-14 | 0 |
| 31 | 2026-07-04 | 10 |
| 32 | 2026-07-07 | 7 |
| 33 | 2026-07-14 | 0 |
| 34 | 2026-07-02 | 12 |
| 35 | 2026-07-14 | 0 |
| 36 | 2026-06-18 | 26 |
| 37 | 2026-06-06 | 38 |
| 38 | 2026-06-23 | 21 |
| 39 | 2026-06-06 | 38 |
| 40 | 2026-07-11 | 3 |
| 41 | 2026-07-11 | 3 |
| 42 | 2026-07-11 | 3 |
| 43 | 2026-07-04 | 10 |
| 44 | 2026-07-07 | 7 |
| 45 | 2026-07-14 | 0 |
| 46 | 2026-06-23 | 21 |
| 47 | 2026-06-30 | 14 |
| 48 | 2026-06-11 | 33 |
| 49 | 2026-07-09 | 5 |
| 50 | 2026-05-16 | 59 |
| 51 | 2026-07-14 | 0 |
| 52 | 2026-06-27 | 17 |
| 53 | 2026-06-20 | 24 |
| 54 | 2026-06-27 | 17 |
| 55 | 2026-06-25 | 19 |



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

