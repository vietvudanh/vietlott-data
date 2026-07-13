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
| Power 655 | 1370 | 2017-08-01 | 2026-07-11 | 1370 | 00001 | 01370 |
| Power 645 | 1338 | 2017-10-25 | 2026-07-12 | 1338 | 00198 | 01535 |
| Power 535 | 342 | 2025-06-29 | 2026-07-12 | 682 | 00001 | 00758 |
| Keno | 610 | 2022-12-04 | 2026-07-13 | 76657 | #0110271 | #0288164 |
| 3D | 1100 | 2019-04-22 | 2026-07-10 | 1100 | 00001 | 01104 |
| 3D Pro | 747 | 2021-09-14 | 2026-07-11 | 747 | 00001 | 00751 |
| Bingo18 | 586 | 2024-12-03 | 2026-07-13 | 80518 | 0083123 | 0176400 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54] | 2026-07-04T17:51:54.286368 |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23] | 2026-07-04T17:51:54.288114 |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5] | 2026-06-24T00:01:16.333044 |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53, 46] | 2026-06-21T00:01:15.642578 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.92 |  | 21 | 171 | 1.78 |  | 41 | 202 | 2.11 |
| 2 | 157 | 1.64 |  | 22 | 203 | 2.12 |  | 42 | 178 | 1.86 |
| 3 | 186 | 1.94 |  | 23 | 185 | 1.93 |  | 43 | 197 | 2.05 |
| 4 | 144 | 1.5 |  | 24 | 173 | 1.8 |  | 44 | 178 | 1.86 |
| 5 | 177 | 1.85 |  | 25 | 157 | 1.64 |  | 45 | 174 | 1.81 |
| 6 | 143 | 1.49 |  | 26 | 165 | 1.72 |  | 46 | 180 | 1.88 |
| 7 | 154 | 1.61 |  | 27 | 158 | 1.65 |  | 47 | 174 | 1.81 |
| 8 | 190 | 1.98 |  | 28 | 157 | 1.64 |  | 48 | 185 | 1.93 |
| 9 | 190 | 1.98 |  | 29 | 187 | 1.95 |  | 49 | 171 | 1.78 |
| 10 | 163 | 1.7 |  | 30 | 159 | 1.66 |  | 50 | 174 | 1.81 |
| 11 | 177 | 1.85 |  | 31 | 183 | 1.91 |  | 51 | 193 | 2.01 |
| 12 | 179 | 1.87 |  | 32 | 185 | 1.93 |  | 52 | 177 | 1.85 |
| 13 | 171 | 1.78 |  | 33 | 175 | 1.83 |  | 53 | 186 | 1.94 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.03 |  | 54 | 165 | 1.72 |
| 15 | 164 | 1.71 |  | 35 | 168 | 1.75 |  | 55 | 174 | 1.81 |
| 16 | 171 | 1.78 |  | 36 | 165 | 1.72 |  |  |  |  |
| 17 | 159 | 1.66 |  | 37 | 156 | 1.63 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 168 | 1.75 |  |  |  |  |
| 19 | 171 | 1.78 |  | 39 | 167 | 1.74 |  |  |  |  |
| 20 | 186 | 1.94 |  | 40 | 190 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 22 | 1 | 1.1 |  | 47 | 2 | 2.2 |
| 2 | 3 | 3.3 |  | 23 | 4 | 4.4 |  | 49 | 3 | 3.3 |
| 3 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 52 | 2 | 2.2 |
| 4 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 5 | 4 | 4.4 |  | 28 | 3 | 3.3 |  | 54 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 55 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 31 | 2 | 2.2 |  |  |  |  |
| 8 | 3 | 3.3 |  | 32 | 1 | 1.1 |  |  |  |  |
| 9 | 2 | 2.2 |  | 33 | 3 | 3.3 |  |  |  |  |
| 10 | 1 | 1.1 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 13 | 3 | 3.3 |  | 36 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 38 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 3 | 3.3 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 3 | 3.3 |  |  |  |  |
| 18 | 2 | 2.2 |  | 43 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 44 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 45 | 1 | 1.1 |  |  |  |  |
| 21 | 1 | 1.1 |  | 46 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 21 | 4 | 2.2 |  | 41 | 5 | 2.75 |
| 2 | 4 | 2.2 |  | 22 | 2 | 1.1 |  | 42 | 5 | 2.75 |
| 3 | 4 | 2.2 |  | 23 | 6 | 3.3 |  | 43 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 24 | 3 | 1.65 |  | 44 | 3 | 1.65 |
| 5 | 5 | 2.75 |  | 25 | 4 | 2.2 |  | 45 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 26 | 2 | 1.1 |  | 46 | 4 | 2.2 |
| 7 | 2 | 1.1 |  | 27 | 2 | 1.1 |  | 47 | 3 | 1.65 |
| 8 | 8 | 4.4 |  | 28 | 7 | 3.85 |  | 48 | 3 | 1.65 |
| 9 | 2 | 1.1 |  | 29 | 2 | 1.1 |  | 49 | 4 | 2.2 |
| 10 | 1 | 0.55 |  | 30 | 1 | 0.55 |  | 50 | 2 | 1.1 |
| 11 | 3 | 1.65 |  | 31 | 3 | 1.65 |  | 51 | 1 | 0.55 |
| 12 | 1 | 0.55 |  | 32 | 4 | 2.2 |  | 52 | 2 | 1.1 |
| 13 | 3 | 1.65 |  | 33 | 3 | 1.65 |  | 53 | 3 | 1.65 |
| 14 | 4 | 2.2 |  | 34 | 4 | 2.2 |  | 54 | 2 | 1.1 |
| 15 | 3 | 1.65 |  | 35 | 2 | 1.1 |  | 55 | 2 | 1.1 |
| 16 | 5 | 2.75 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 4 | 2.2 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 6 | 3.3 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.2 |  | 21 | 6 | 2.2 |  | 41 | 6 | 2.2 |
| 2 | 6 | 2.2 |  | 22 | 7 | 2.56 |  | 42 | 5 | 1.83 |
| 3 | 5 | 1.83 |  | 23 | 6 | 2.2 |  | 43 | 4 | 1.47 |
| 4 | 5 | 1.83 |  | 24 | 5 | 1.83 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 6 | 2.2 |  | 45 | 4 | 1.47 |
| 6 | 3 | 1.1 |  | 26 | 4 | 1.47 |  | 46 | 7 | 2.56 |
| 7 | 4 | 1.47 |  | 27 | 2 | 0.73 |  | 47 | 6 | 2.2 |
| 8 | 11 | 4.03 |  | 28 | 9 | 3.3 |  | 48 | 3 | 1.1 |
| 9 | 5 | 1.83 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 3 | 1.1 |  | 30 | 3 | 1.1 |  | 50 | 6 | 2.2 |
| 11 | 4 | 1.47 |  | 31 | 4 | 1.47 |  | 51 | 3 | 1.1 |
| 12 | 1 | 0.37 |  | 32 | 6 | 2.2 |  | 52 | 4 | 1.47 |
| 13 | 4 | 1.47 |  | 33 | 6 | 2.2 |  | 53 | 6 | 2.2 |
| 14 | 5 | 1.83 |  | 34 | 5 | 1.83 |  | 54 | 2 | 0.73 |
| 15 | 7 | 2.56 |  | 35 | 4 | 1.47 |  | 55 | 5 | 1.83 |
| 16 | 8 | 2.93 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 7 | 2.56 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 3 | 1.1 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 8 | 2.93 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 6 | 2.2 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 50 | 2026-05-16 | 56 |
| 12 | 2026-05-19 | 53 |
| 51 | 2026-06-02 | 39 |
| 29 | 2026-06-04 | 37 |
| 39 | 2026-06-06 | 35 |
| 37 | 2026-06-06 | 35 |
| 27 | 2026-06-09 | 32 |
| 48 | 2026-06-11 | 30 |
| 24 | 2026-06-11 | 30 |
| 19 | 2026-06-13 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 16 |
| 2 | 2026-07-09 | 2 |
| 3 | 2026-06-25 | 16 |
| 4 | 2026-07-07 | 4 |
| 5 | 2026-07-02 | 9 |
| 6 | 2026-07-07 | 4 |
| 7 | 2026-06-27 | 14 |
| 8 | 2026-07-07 | 4 |
| 9 | 2026-07-11 | 0 |
| 10 | 2026-07-09 | 2 |
| 11 | 2026-07-02 | 9 |
| 12 | 2026-05-19 | 53 |
| 13 | 2026-07-04 | 7 |
| 14 | 2026-07-09 | 2 |
| 15 | 2026-07-04 | 7 |
| 16 | 2026-06-27 | 14 |
| 17 | 2026-07-11 | 0 |
| 18 | 2026-07-04 | 7 |
| 19 | 2026-06-13 | 28 |
| 20 | 2026-07-11 | 0 |
| 21 | 2026-06-27 | 14 |
| 22 | 2026-06-30 | 11 |
| 23 | 2026-07-04 | 7 |
| 24 | 2026-06-11 | 30 |
| 25 | 2026-07-07 | 4 |
| 26 | 2026-06-20 | 21 |
| 27 | 2026-06-09 | 32 |
| 28 | 2026-07-02 | 9 |
| 29 | 2026-06-04 | 37 |
| 30 | 2026-06-20 | 21 |
| 31 | 2026-07-04 | 7 |
| 32 | 2026-07-07 | 4 |
| 33 | 2026-07-11 | 0 |
| 34 | 2026-07-02 | 9 |
| 35 | 2026-06-25 | 16 |
| 36 | 2026-06-18 | 23 |
| 37 | 2026-06-06 | 35 |
| 38 | 2026-06-23 | 18 |
| 39 | 2026-06-06 | 35 |
| 40 | 2026-07-11 | 0 |
| 41 | 2026-07-11 | 0 |
| 42 | 2026-07-11 | 0 |
| 43 | 2026-07-04 | 7 |
| 44 | 2026-07-07 | 4 |
| 45 | 2026-07-09 | 2 |
| 46 | 2026-06-23 | 18 |
| 47 | 2026-06-30 | 11 |
| 48 | 2026-06-11 | 30 |
| 49 | 2026-07-09 | 2 |
| 50 | 2026-05-16 | 56 |
| 51 | 2026-06-02 | 39 |
| 52 | 2026-06-27 | 14 |
| 53 | 2026-06-20 | 21 |
| 54 | 2026-06-27 | 14 |
| 55 | 2026-06-25 | 16 |



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

