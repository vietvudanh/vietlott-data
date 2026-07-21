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
| Power 655 | 1374 | 2017-08-01 | 2026-07-21 | 1374 | 00001 | 01374 |
| Power 645 | 1341 | 2017-10-25 | 2026-07-19 | 1341 | 00198 | 01538 |
| Power 535 | 351 | 2025-06-29 | 2026-07-21 | 700 | 00001 | 00776 |
| Keno | 618 | 2022-12-04 | 2026-07-21 | 77684 | #0110271 | #0289191 |
| 3D | 1104 | 2019-04-22 | 2026-07-20 | 1104 | 00001 | 01108 |
| 3D Pro | 751 | 2021-09-14 | 2026-07-21 | 751 | 00001 | 00755 |
| Bingo18 | 594 | 2024-12-03 | 2026-07-21 | 81850 | 0083123 | 0177771 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.91 |  | 21 | 172 | 1.79 |  | 41 | 203 | 2.11 |
| 2 | 157 | 1.63 |  | 22 | 205 | 2.13 |  | 42 | 178 | 1.85 |
| 3 | 186 | 1.93 |  | 23 | 185 | 1.92 |  | 43 | 197 | 2.05 |
| 4 | 144 | 1.5 |  | 24 | 175 | 1.82 |  | 44 | 178 | 1.85 |
| 5 | 177 | 1.84 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.84 |
| 6 | 143 | 1.49 |  | 26 | 165 | 1.72 |  | 46 | 180 | 1.87 |
| 7 | 154 | 1.6 |  | 27 | 158 | 1.64 |  | 47 | 174 | 1.81 |
| 8 | 191 | 1.99 |  | 28 | 157 | 1.63 |  | 48 | 187 | 1.94 |
| 9 | 190 | 1.98 |  | 29 | 187 | 1.94 |  | 49 | 171 | 1.78 |
| 10 | 164 | 1.71 |  | 30 | 160 | 1.66 |  | 50 | 174 | 1.81 |
| 11 | 178 | 1.85 |  | 31 | 183 | 1.9 |  | 51 | 194 | 2.02 |
| 12 | 179 | 1.86 |  | 32 | 186 | 1.93 |  | 52 | 177 | 1.84 |
| 13 | 172 | 1.79 |  | 33 | 177 | 1.84 |  | 53 | 187 | 1.94 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.03 |  | 54 | 166 | 1.73 |
| 15 | 164 | 1.71 |  | 35 | 169 | 1.76 |  | 55 | 175 | 1.82 |
| 16 | 172 | 1.79 |  | 36 | 165 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 156 | 1.62 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 168 | 1.75 |  |  |  |  |
| 19 | 172 | 1.79 |  | 39 | 168 | 1.75 |  |  |  |  |
| 20 | 187 | 1.94 |  | 40 | 190 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 22 | 3 | 3.3 |  | 47 | 1 | 1.1 |
| 2 | 1 | 1.1 |  | 23 | 3 | 3.3 |  | 48 | 2 | 2.2 |
| 3 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 49 | 2 | 2.2 |
| 4 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 28 | 3 | 3.3 |  | 52 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 54 | 2 | 2.2 |
| 8 | 3 | 3.3 |  | 32 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 9 | 2 | 2.2 |  | 33 | 4 | 4.4 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 35 | 2 | 2.2 |  |  |  |  |
| 13 | 4 | 4.4 |  | 38 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 39 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 4 | 4.4 |  |  |  |  |
| 17 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 18 | 2 | 2.2 |  | 43 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 44 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 45 | 4 | 4.4 |  |  |  |  |
| 21 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 22 | 4 | 2.2 |  | 42 | 5 | 2.75 |
| 2 | 4 | 2.2 |  | 23 | 6 | 3.3 |  | 43 | 3 | 1.65 |
| 3 | 4 | 2.2 |  | 24 | 5 | 2.75 |  | 44 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 45 | 5 | 2.75 |
| 5 | 5 | 2.75 |  | 26 | 1 | 0.55 |  | 46 | 4 | 2.2 |
| 6 | 2 | 1.1 |  | 27 | 2 | 1.1 |  | 47 | 2 | 1.1 |
| 7 | 2 | 1.1 |  | 28 | 5 | 2.75 |  | 48 | 3 | 1.65 |
| 8 | 8 | 4.4 |  | 29 | 2 | 1.1 |  | 49 | 4 | 2.2 |
| 9 | 2 | 1.1 |  | 30 | 2 | 1.1 |  | 51 | 2 | 1.1 |
| 10 | 2 | 1.1 |  | 31 | 3 | 1.65 |  | 52 | 2 | 1.1 |
| 11 | 4 | 2.2 |  | 32 | 3 | 1.65 |  | 53 | 3 | 1.65 |
| 13 | 4 | 2.2 |  | 33 | 5 | 2.75 |  | 54 | 3 | 1.65 |
| 14 | 4 | 2.2 |  | 34 | 3 | 1.65 |  | 55 | 2 | 1.1 |
| 15 | 3 | 1.65 |  | 35 | 3 | 1.65 |  |  |  |  |
| 16 | 5 | 2.75 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 3 | 1.65 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 4 | 2.2 |  |  |  |  |
| 21 | 4 | 2.2 |  | 41 | 5 | 2.75 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.2 |  | 21 | 7 | 2.56 |  | 41 | 7 | 2.56 |
| 2 | 5 | 1.83 |  | 22 | 7 | 2.56 |  | 42 | 5 | 1.83 |
| 3 | 5 | 1.83 |  | 23 | 6 | 2.2 |  | 43 | 4 | 1.47 |
| 4 | 5 | 1.83 |  | 24 | 6 | 2.2 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 6 | 2.2 |  | 45 | 7 | 2.56 |
| 6 | 3 | 1.1 |  | 26 | 4 | 1.47 |  | 46 | 7 | 2.56 |
| 7 | 3 | 1.1 |  | 27 | 2 | 0.73 |  | 47 | 4 | 1.47 |
| 8 | 10 | 3.66 |  | 28 | 7 | 2.56 |  | 48 | 5 | 1.83 |
| 9 | 4 | 1.47 |  | 29 | 4 | 1.47 |  | 49 | 4 | 1.47 |
| 10 | 4 | 1.47 |  | 30 | 3 | 1.1 |  | 50 | 5 | 1.83 |
| 11 | 5 | 1.83 |  | 31 | 4 | 1.47 |  | 51 | 4 | 1.47 |
| 12 | 1 | 0.37 |  | 32 | 7 | 2.56 |  | 52 | 3 | 1.1 |
| 13 | 5 | 1.83 |  | 33 | 8 | 2.93 |  | 53 | 6 | 2.2 |
| 14 | 5 | 1.83 |  | 34 | 5 | 1.83 |  | 54 | 3 | 1.1 |
| 15 | 5 | 1.83 |  | 35 | 4 | 1.47 |  | 55 | 5 | 1.83 |
| 16 | 8 | 2.93 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 7 | 2.56 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 3 | 1.1 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 6 | 2.2 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 6 | 2.2 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 50 | 2026-05-16 | 66 |
| 12 | 2026-05-19 | 63 |
| 29 | 2026-06-04 | 47 |
| 37 | 2026-06-06 | 45 |
| 27 | 2026-06-09 | 42 |
| 36 | 2026-06-18 | 33 |
| 26 | 2026-06-20 | 31 |
| 46 | 2026-06-23 | 28 |
| 38 | 2026-06-23 | 28 |
| 3 | 2026-06-25 | 26 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 26 |
| 2 | 2026-07-09 | 12 |
| 3 | 2026-06-25 | 26 |
| 4 | 2026-07-07 | 14 |
| 5 | 2026-07-02 | 19 |
| 6 | 2026-07-07 | 14 |
| 7 | 2026-06-27 | 24 |
| 8 | 2026-07-21 | 0 |
| 9 | 2026-07-11 | 10 |
| 10 | 2026-07-14 | 7 |
| 11 | 2026-07-21 | 0 |
| 12 | 2026-05-19 | 63 |
| 13 | 2026-07-21 | 0 |
| 14 | 2026-07-09 | 12 |
| 15 | 2026-07-04 | 17 |
| 16 | 2026-07-18 | 3 |
| 17 | 2026-07-11 | 10 |
| 18 | 2026-07-04 | 17 |
| 19 | 2026-07-16 | 5 |
| 20 | 2026-07-16 | 5 |
| 21 | 2026-07-16 | 5 |
| 22 | 2026-07-21 | 0 |
| 23 | 2026-07-04 | 17 |
| 24 | 2026-07-21 | 0 |
| 25 | 2026-07-07 | 14 |
| 26 | 2026-06-20 | 31 |
| 27 | 2026-06-09 | 42 |
| 28 | 2026-07-02 | 19 |
| 29 | 2026-06-04 | 47 |
| 30 | 2026-07-14 | 7 |
| 31 | 2026-07-04 | 17 |
| 32 | 2026-07-21 | 0 |
| 33 | 2026-07-16 | 5 |
| 34 | 2026-07-02 | 19 |
| 35 | 2026-07-14 | 7 |
| 36 | 2026-06-18 | 33 |
| 37 | 2026-06-06 | 45 |
| 38 | 2026-06-23 | 28 |
| 39 | 2026-07-21 | 0 |
| 40 | 2026-07-11 | 10 |
| 41 | 2026-07-18 | 3 |
| 42 | 2026-07-11 | 10 |
| 43 | 2026-07-04 | 17 |
| 44 | 2026-07-07 | 14 |
| 45 | 2026-07-18 | 3 |
| 46 | 2026-06-23 | 28 |
| 47 | 2026-06-30 | 21 |
| 48 | 2026-07-18 | 3 |
| 49 | 2026-07-09 | 12 |
| 50 | 2026-05-16 | 66 |
| 51 | 2026-07-14 | 7 |
| 52 | 2026-06-27 | 24 |
| 53 | 2026-07-16 | 5 |
| 54 | 2026-07-18 | 3 |
| 55 | 2026-07-18 | 3 |



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

