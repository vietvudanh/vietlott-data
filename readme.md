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
| Power 655 | 1379 | 2017-08-01 | 2026-08-01 | 1379 | 00001 | 01379 |
| Power 645 | 1347 | 2017-10-25 | 2026-08-02 | 1347 | 00198 | 01544 |
| Power 535 | 364 | 2025-06-29 | 2026-08-03 | 726 | 00001 | 00802 |
| Keno | 631 | 2022-12-04 | 2026-08-03 | 79231 | #0110271 | #0290738 |
| 3D | 1110 | 2019-04-22 | 2026-08-03 | 1110 | 00001 | 01114 |
| 3D Pro | 756 | 2021-09-14 | 2026-08-01 | 756 | 00001 | 00760 |
| Bingo18 | 607 | 2024-12-03 | 2026-08-03 | 83917 | 0083123 | 0179838 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] | 2026-08-02T00:01:09.345245 |
| 2026-07-30 | 01378 | [2, 12, 24, 28, 43, 49, 51] | 2026-07-31T00:01:13.443363 |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48] | 2026-07-29T00:01:42.996426 |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36] | 2026-07-24T00:01:33.770193 |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 185 | 1.92 |  | 21 | 172 | 1.78 |  | 41 | 204 | 2.11 |
| 2 | 158 | 1.64 |  | 22 | 206 | 2.13 |  | 42 | 178 | 1.84 |
| 3 | 187 | 1.94 |  | 23 | 186 | 1.93 |  | 43 | 198 | 2.05 |
| 4 | 144 | 1.49 |  | 24 | 176 | 1.82 |  | 44 | 180 | 1.86 |
| 5 | 178 | 1.84 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.83 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.71 |  | 46 | 180 | 1.86 |
| 7 | 155 | 1.61 |  | 27 | 160 | 1.66 |  | 47 | 174 | 1.8 |
| 8 | 192 | 1.99 |  | 28 | 158 | 1.64 |  | 48 | 189 | 1.96 |
| 9 | 191 | 1.98 |  | 29 | 187 | 1.94 |  | 49 | 173 | 1.79 |
| 10 | 164 | 1.7 |  | 30 | 160 | 1.66 |  | 50 | 175 | 1.81 |
| 11 | 179 | 1.85 |  | 31 | 183 | 1.9 |  | 51 | 195 | 2.02 |
| 12 | 180 | 1.86 |  | 32 | 186 | 1.93 |  | 52 | 177 | 1.83 |
| 13 | 172 | 1.78 |  | 33 | 178 | 1.84 |  | 53 | 187 | 1.94 |
| 14 | 175 | 1.81 |  | 34 | 195 | 2.02 |  | 54 | 166 | 1.72 |
| 15 | 164 | 1.7 |  | 35 | 169 | 1.75 |  | 55 | 177 | 1.83 |
| 16 | 173 | 1.79 |  | 36 | 166 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 157 | 1.63 |  |  |  |  |
| 18 | 174 | 1.8 |  | 38 | 169 | 1.75 |  |  |  |  |
| 19 | 172 | 1.78 |  | 39 | 169 | 1.75 |  |  |  |  |
| 20 | 187 | 1.94 |  | 40 | 191 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.19 |  | 23 | 1 | 1.19 |  | 49 | 3 | 3.57 |
| 2 | 2 | 2.38 |  | 24 | 3 | 3.57 |  | 50 | 1 | 1.19 |
| 3 | 1 | 1.19 |  | 25 | 1 | 1.19 |  | 51 | 2 | 2.38 |
| 4 | 1 | 1.19 |  | 27 | 2 | 2.38 |  | 53 | 1 | 1.19 |
| 5 | 1 | 1.19 |  | 28 | 1 | 1.19 |  | 54 | 1 | 1.19 |
| 6 | 1 | 1.19 |  | 30 | 1 | 1.19 |  | 55 | 3 | 3.57 |
| 7 | 1 | 1.19 |  | 32 | 2 | 2.38 |  |  |  |  |
| 8 | 3 | 3.57 |  | 33 | 5 | 5.95 |  |  |  |  |
| 9 | 3 | 3.57 |  | 35 | 1 | 1.19 |  |  |  |  |
| 10 | 2 | 2.38 |  | 36 | 1 | 1.19 |  |  |  |  |
| 11 | 2 | 2.38 |  | 37 | 1 | 1.19 |  |  |  |  |
| 12 | 1 | 1.19 |  | 38 | 1 | 1.19 |  |  |  |  |
| 13 | 1 | 1.19 |  | 39 | 2 | 2.38 |  |  |  |  |
| 14 | 2 | 2.38 |  | 40 | 2 | 2.38 |  |  |  |  |
| 16 | 2 | 2.38 |  | 41 | 3 | 3.57 |  |  |  |  |
| 17 | 2 | 2.38 |  | 42 | 1 | 1.19 |  |  |  |  |
| 19 | 1 | 1.19 |  | 43 | 1 | 1.19 |  |  |  |  |
| 20 | 2 | 2.38 |  | 44 | 3 | 3.57 |  |  |  |  |
| 21 | 1 | 1.19 |  | 45 | 4 | 4.76 |  |  |  |  |
| 22 | 3 | 3.57 |  | 48 | 4 | 4.76 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.86 |  | 21 | 2 | 1.14 |  | 42 | 3 | 1.71 |
| 2 | 4 | 2.29 |  | 22 | 4 | 2.29 |  | 43 | 3 | 1.71 |
| 3 | 3 | 1.71 |  | 23 | 5 | 2.86 |  | 44 | 4 | 2.29 |
| 4 | 3 | 1.71 |  | 24 | 4 | 2.29 |  | 45 | 4 | 2.29 |
| 5 | 5 | 2.86 |  | 25 | 1 | 0.57 |  | 46 | 4 | 2.29 |
| 6 | 2 | 1.14 |  | 26 | 1 | 0.57 |  | 47 | 2 | 1.14 |
| 7 | 3 | 1.71 |  | 27 | 3 | 1.71 |  | 48 | 5 | 2.86 |
| 8 | 7 | 4.0 |  | 28 | 5 | 2.86 |  | 49 | 5 | 2.86 |
| 9 | 3 | 1.71 |  | 30 | 2 | 1.14 |  | 50 | 1 | 0.57 |
| 10 | 2 | 1.14 |  | 31 | 2 | 1.14 |  | 51 | 2 | 1.14 |
| 11 | 4 | 2.29 |  | 32 | 3 | 1.71 |  | 52 | 2 | 1.14 |
| 12 | 1 | 0.57 |  | 33 | 6 | 3.43 |  | 53 | 2 | 1.14 |
| 13 | 4 | 2.29 |  | 34 | 2 | 1.14 |  | 54 | 2 | 1.14 |
| 14 | 4 | 2.29 |  | 35 | 3 | 1.71 |  | 55 | 4 | 2.29 |
| 15 | 2 | 1.14 |  | 36 | 3 | 1.71 |  |  |  |  |
| 16 | 5 | 2.86 |  | 37 | 2 | 1.14 |  |  |  |  |
| 17 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 39 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 40 | 5 | 2.86 |  |  |  |  |
| 20 | 3 | 1.71 |  | 41 | 6 | 3.43 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 5 | 1.88 |  | 41 | 7 | 2.63 |
| 2 | 6 | 2.26 |  | 22 | 6 | 2.26 |  | 42 | 5 | 1.88 |
| 3 | 6 | 2.26 |  | 23 | 7 | 2.63 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 6 | 2.26 |
| 5 | 6 | 2.26 |  | 25 | 4 | 1.5 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 3 | 1.13 |  | 46 | 6 | 2.26 |
| 7 | 3 | 1.13 |  | 27 | 4 | 1.5 |  | 47 | 4 | 1.5 |
| 8 | 10 | 3.76 |  | 28 | 8 | 3.01 |  | 48 | 7 | 2.63 |
| 9 | 3 | 1.13 |  | 29 | 2 | 0.75 |  | 49 | 6 | 2.26 |
| 10 | 3 | 1.13 |  | 30 | 2 | 0.75 |  | 50 | 4 | 1.5 |
| 11 | 6 | 2.26 |  | 31 | 4 | 1.5 |  | 51 | 3 | 1.13 |
| 12 | 2 | 0.75 |  | 32 | 6 | 2.26 |  | 52 | 2 | 0.75 |
| 13 | 5 | 1.88 |  | 33 | 7 | 2.63 |  | 53 | 4 | 1.5 |
| 14 | 6 | 2.26 |  | 34 | 4 | 1.5 |  | 54 | 3 | 1.13 |
| 15 | 4 | 1.5 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 4 | 1.5 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 7 | 2.63 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 7 | 2.63 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 29 | 2026-06-04 | 58 |
| 26 | 2026-06-20 | 42 |
| 46 | 2026-06-23 | 39 |
| 52 | 2026-06-27 | 35 |
| 47 | 2026-06-30 | 32 |
| 34 | 2026-07-02 | 30 |
| 18 | 2026-07-04 | 28 |
| 15 | 2026-07-04 | 28 |
| 31 | 2026-07-04 | 28 |
| 6 | 2026-07-07 | 25 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-07-23 | 9 |
| 2 | 2026-07-30 | 2 |
| 3 | 2026-07-23 | 9 |
| 4 | 2026-07-07 | 25 |
| 5 | 2026-07-25 | 7 |
| 6 | 2026-07-07 | 25 |
| 7 | 2026-07-28 | 4 |
| 8 | 2026-07-23 | 9 |
| 9 | 2026-07-25 | 7 |
| 10 | 2026-07-14 | 18 |
| 11 | 2026-08-01 | 0 |
| 12 | 2026-07-30 | 2 |
| 13 | 2026-07-21 | 11 |
| 14 | 2026-08-01 | 0 |
| 15 | 2026-07-04 | 28 |
| 16 | 2026-08-01 | 0 |
| 17 | 2026-07-11 | 21 |
| 18 | 2026-07-04 | 28 |
| 19 | 2026-07-16 | 16 |
| 20 | 2026-07-16 | 16 |
| 21 | 2026-07-16 | 16 |
| 22 | 2026-07-28 | 4 |
| 23 | 2026-07-28 | 4 |
| 24 | 2026-07-30 | 2 |
| 25 | 2026-07-07 | 25 |
| 26 | 2026-06-20 | 42 |
| 27 | 2026-07-28 | 4 |
| 28 | 2026-07-30 | 2 |
| 29 | 2026-06-04 | 58 |
| 30 | 2026-07-14 | 18 |
| 31 | 2026-07-04 | 28 |
| 32 | 2026-07-21 | 11 |
| 33 | 2026-07-25 | 7 |
| 34 | 2026-07-02 | 30 |
| 35 | 2026-07-14 | 18 |
| 36 | 2026-07-23 | 9 |
| 37 | 2026-07-25 | 7 |
| 38 | 2026-07-23 | 9 |
| 39 | 2026-08-01 | 0 |
| 40 | 2026-07-23 | 9 |
| 41 | 2026-07-28 | 4 |
| 42 | 2026-07-11 | 21 |
| 43 | 2026-07-30 | 2 |
| 44 | 2026-08-01 | 0 |
| 45 | 2026-07-18 | 14 |
| 46 | 2026-06-23 | 39 |
| 47 | 2026-06-30 | 32 |
| 48 | 2026-07-28 | 4 |
| 49 | 2026-08-01 | 0 |
| 50 | 2026-07-25 | 7 |
| 51 | 2026-07-30 | 2 |
| 52 | 2026-06-27 | 35 |
| 53 | 2026-07-16 | 16 |
| 54 | 2026-07-18 | 14 |
| 55 | 2026-08-01 | 0 |



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

