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
| Power 655 | 1393 | 2017-08-01 | 2026-09-03 | 1393 | 00001 | 01393 |
| Power 645 | 1361 | 2017-10-25 | 2026-09-04 | 1361 | 00198 | 01558 |
| Power 535 | 398 | 2025-06-29 | 2026-09-05 | 793 | 00001 | 00867 |
| Keno | 667 | 2022-12-04 | 2026-09-05 | 83601 | #0110271 | #0294612 |
| 3D | 1124 | 2019-04-22 | 2026-09-04 | 1124 | 00001 | 01128 |
| 3D Pro | 770 | 2021-09-14 | 2026-09-03 | 770 | 00001 | 00774 |
| Bingo18 | 640 | 2024-12-03 | 2026-09-05 | 89117 | 0083123 | 0185015 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-09-03 | 01393 | [8, 9, 16, 42, 46, 47, 11] | 2026-09-05T07:32:08.578861 |
| 2026-09-01 | 01392 | [1, 17, 41, 44, 49, 55, 45] | 2026-09-05T07:32:08.578975 |
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24] | 2026-09-05T07:32:08.579054 |
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10] | 2026-08-28T00:01:17.809418 |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42] | 2026-08-16T11:07:54.647468 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 188 | 1.93 |  | 21 | 174 | 1.78 |  | 41 | 206 | 2.11 |
| 2 | 161 | 1.65 |  | 22 | 206 | 2.11 |  | 42 | 181 | 1.86 |
| 3 | 189 | 1.94 |  | 23 | 187 | 1.92 |  | 43 | 198 | 2.03 |
| 4 | 144 | 1.48 |  | 24 | 177 | 1.82 |  | 44 | 182 | 1.87 |
| 5 | 182 | 1.87 |  | 25 | 159 | 1.63 |  | 45 | 181 | 1.86 |
| 6 | 143 | 1.47 |  | 26 | 166 | 1.7 |  | 46 | 182 | 1.87 |
| 7 | 157 | 1.61 |  | 27 | 162 | 1.66 |  | 47 | 177 | 1.82 |
| 8 | 195 | 2.0 |  | 28 | 158 | 1.62 |  | 48 | 190 | 1.95 |
| 9 | 194 | 1.99 |  | 29 | 191 | 1.96 |  | 49 | 174 | 1.78 |
| 10 | 166 | 1.7 |  | 30 | 162 | 1.66 |  | 50 | 177 | 1.82 |
| 11 | 181 | 1.86 |  | 31 | 186 | 1.91 |  | 51 | 197 | 2.02 |
| 12 | 180 | 1.85 |  | 32 | 186 | 1.91 |  | 52 | 177 | 1.82 |
| 13 | 173 | 1.77 |  | 33 | 179 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 178 | 1.83 |  | 34 | 196 | 2.01 |  | 54 | 167 | 1.71 |
| 15 | 166 | 1.7 |  | 35 | 170 | 1.74 |  | 55 | 179 | 1.84 |
| 16 | 175 | 1.79 |  | 36 | 167 | 1.71 |  |  |  |  |
| 17 | 160 | 1.64 |  | 37 | 158 | 1.62 |  |  |  |  |
| 18 | 178 | 1.83 |  | 38 | 172 | 1.76 |  |  |  |  |
| 19 | 174 | 1.78 |  | 39 | 172 | 1.76 |  |  |  |  |
| 20 | 189 | 1.94 |  | 40 | 194 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 25 | 2 | 2.2 |  | 48 | 1 | 1.1 |
| 2 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 49 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 27 | 2 | 2.2 |  | 50 | 2 | 2.2 |
| 5 | 4 | 4.4 |  | 29 | 4 | 4.4 |  | 51 | 2 | 2.2 |
| 7 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 8 | 3 | 3.3 |  | 31 | 2 | 2.2 |  |  |  |  |
| 9 | 3 | 3.3 |  | 33 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 38 | 3 | 3.3 |  |  |  |  |
| 16 | 2 | 2.2 |  | 39 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 18 | 4 | 4.4 |  | 41 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 45 | 4 | 4.4 |  |  |  |  |
| 23 | 1 | 1.1 |  | 46 | 2 | 2.2 |  |  |  |  |
| 24 | 1 | 1.1 |  | 47 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.2 |  | 21 | 3 | 1.65 |  | 41 | 5 | 2.75 |
| 2 | 5 | 2.75 |  | 22 | 3 | 1.65 |  | 42 | 4 | 2.2 |
| 3 | 3 | 1.65 |  | 23 | 2 | 1.1 |  | 43 | 1 | 0.55 |
| 4 | 1 | 0.55 |  | 24 | 4 | 2.2 |  | 44 | 5 | 2.75 |
| 5 | 5 | 2.75 |  | 25 | 3 | 1.65 |  | 45 | 8 | 4.4 |
| 6 | 1 | 0.55 |  | 26 | 1 | 0.55 |  | 46 | 2 | 1.1 |
| 7 | 3 | 1.65 |  | 27 | 4 | 2.2 |  | 47 | 3 | 1.65 |
| 8 | 6 | 3.3 |  | 28 | 1 | 0.55 |  | 48 | 5 | 2.75 |
| 9 | 6 | 3.3 |  | 29 | 4 | 2.2 |  | 49 | 4 | 2.2 |
| 10 | 4 | 2.2 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 11 | 4 | 2.2 |  | 31 | 3 | 1.65 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 53 | 1 | 0.55 |
| 13 | 2 | 1.1 |  | 33 | 6 | 3.3 |  | 54 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 55 | 5 | 2.75 |
| 15 | 2 | 1.1 |  | 35 | 2 | 1.1 |  |  |  |  |
| 16 | 4 | 2.2 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 4 | 2.2 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 5 | 2.75 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 4 | 1.5 |  | 41 | 7 | 2.63 |
| 2 | 7 | 2.63 |  | 22 | 4 | 1.5 |  | 42 | 6 | 2.26 |
| 3 | 4 | 1.5 |  | 23 | 6 | 2.26 |  | 43 | 3 | 1.13 |
| 4 | 3 | 1.13 |  | 24 | 5 | 1.88 |  | 44 | 6 | 2.26 |
| 5 | 9 | 3.38 |  | 25 | 3 | 1.13 |  | 45 | 8 | 3.01 |
| 6 | 2 | 0.75 |  | 26 | 2 | 0.75 |  | 46 | 6 | 2.26 |
| 7 | 5 | 1.88 |  | 27 | 5 | 1.88 |  | 47 | 5 | 1.88 |
| 8 | 10 | 3.76 |  | 28 | 4 | 1.5 |  | 48 | 6 | 2.26 |
| 9 | 6 | 2.26 |  | 29 | 4 | 1.5 |  | 49 | 6 | 2.26 |
| 10 | 4 | 1.5 |  | 30 | 4 | 1.5 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 5 | 1.88 |  | 51 | 4 | 1.5 |
| 12 | 1 | 0.38 |  | 32 | 3 | 1.13 |  | 52 | 2 | 0.75 |
| 13 | 5 | 1.88 |  | 33 | 7 | 2.63 |  | 53 | 2 | 0.75 |
| 14 | 7 | 2.63 |  | 34 | 3 | 1.13 |  | 54 | 3 | 1.13 |
| 15 | 4 | 1.5 |  | 35 | 4 | 1.5 |  | 55 | 6 | 2.26 |
| 16 | 6 | 2.26 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 2 | 0.75 |  |  |  |  |
| 18 | 7 | 2.63 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 4 | 1.5 |  | 39 | 5 | 1.88 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 8 | 3.01 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-06-27 | 68 |
| 6 | 2026-07-07 | 58 |
| 4 | 2026-07-07 | 58 |
| 53 | 2026-07-16 | 49 |
| 32 | 2026-07-21 | 44 |
| 22 | 2026-07-28 | 37 |
| 12 | 2026-07-30 | 35 |
| 43 | 2026-07-30 | 35 |
| 28 | 2026-07-30 | 35 |
| 54 | 2026-08-04 | 30 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-09-01 | 2 |
| 2 | 2026-08-20 | 14 |
| 3 | 2026-08-27 | 7 |
| 4 | 2026-07-07 | 58 |
| 5 | 2026-08-29 | 5 |
| 6 | 2026-07-07 | 58 |
| 7 | 2026-08-25 | 9 |
| 8 | 2026-09-03 | 0 |
| 9 | 2026-09-03 | 0 |
| 10 | 2026-08-29 | 5 |
| 11 | 2026-09-03 | 0 |
| 12 | 2026-07-30 | 35 |
| 13 | 2026-08-25 | 9 |
| 14 | 2026-08-25 | 9 |
| 15 | 2026-08-29 | 5 |
| 16 | 2026-09-03 | 0 |
| 17 | 2026-09-01 | 2 |
| 18 | 2026-08-25 | 9 |
| 19 | 2026-08-22 | 12 |
| 20 | 2026-08-15 | 19 |
| 21 | 2026-08-27 | 7 |
| 22 | 2026-07-28 | 37 |
| 23 | 2026-08-06 | 28 |
| 24 | 2026-08-29 | 5 |
| 25 | 2026-08-22 | 12 |
| 26 | 2026-08-27 | 7 |
| 27 | 2026-08-15 | 19 |
| 28 | 2026-07-30 | 35 |
| 29 | 2026-08-29 | 5 |
| 30 | 2026-08-18 | 16 |
| 31 | 2026-08-25 | 9 |
| 32 | 2026-07-21 | 44 |
| 33 | 2026-08-08 | 26 |
| 34 | 2026-08-29 | 5 |
| 35 | 2026-08-06 | 28 |
| 36 | 2026-08-22 | 12 |
| 37 | 2026-08-08 | 26 |
| 38 | 2026-08-20 | 14 |
| 39 | 2026-08-20 | 14 |
| 40 | 2026-08-25 | 9 |
| 41 | 2026-09-01 | 2 |
| 42 | 2026-09-03 | 0 |
| 43 | 2026-07-30 | 35 |
| 44 | 2026-09-01 | 2 |
| 45 | 2026-09-01 | 2 |
| 46 | 2026-09-03 | 0 |
| 47 | 2026-09-03 | 0 |
| 48 | 2026-08-18 | 16 |
| 49 | 2026-09-01 | 2 |
| 50 | 2026-08-15 | 19 |
| 51 | 2026-08-20 | 14 |
| 52 | 2026-06-27 | 68 |
| 53 | 2026-07-16 | 49 |
| 54 | 2026-08-04 | 30 |
| 55 | 2026-09-01 | 2 |



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

