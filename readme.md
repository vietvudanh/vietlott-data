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
| Power 655 | 1352 | 2017-08-01 | 2026-05-30 | 1352 | 00001 | 01352 |
| Power 645 | 1320 | 2017-10-25 | 2026-05-31 | 1320 | 00198 | 01517 |
| Power 535 | 302 | 2025-06-29 | 2026-06-01 | 603 | 00001 | 00676 |
| Keno | 572 | 2022-12-04 | 2026-06-02 | 72271 | #0110271 | #0283285 |
| 3D | 1083 | 2019-04-22 | 2026-06-01 | 1083 | 00001 | 01087 |
| 3D Pro | 729 | 2021-09-14 | 2026-05-30 | 729 | 00001 | 00733 |
| Bingo18 | 545 | 2024-12-03 | 2026-06-02 | 73980 | 0083123 | 0169881 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-30 | 01352 | [2, 8, 20, 24, 25, 42, 44] | 2026-06-01T00:01:26.268124 |
| 2026-05-28 | 01351 | [8, 11, 21, 25, 31, 53, 54] | 2026-05-29T00:01:21.691058 |
| 2026-05-26 | 01350 | [1, 14, 15, 19, 23, 34, 29] | 2026-05-27T00:01:07.369677 |
| 2026-05-23 | 01349 | [17, 21, 22, 27, 38, 49, 3] | 2026-05-24T00:01:17.320252 |
| 2026-05-21 | 01348 | [16, 18, 20, 28, 32, 34, 40] | 2026-05-22T00:01:24.083070 |
| 2026-05-19 | 01347 | [12, 39, 40, 45, 48, 53, 21] | 2026-05-21T18:37:39.362594 |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |
| 2026-05-14 | 01345 | [26, 28, 39, 41, 48, 55, 50] | 2026-05-15T00:01:10.822513 |
| 2026-05-12 | 01344 | [2, 11, 22, 26, 31, 38, 15] | 2026-05-12T18:58:07.963930 |
| 2026-05-09 | 01343 | [3, 10, 32, 37, 45, 55, 46] | 2026-05-10T00:01:08.118122 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 179 | 1.89 |  | 21 | 170 | 1.8 |  | 41 | 198 | 2.09 |
| 2 | 154 | 1.63 |  | 22 | 202 | 2.13 |  | 42 | 174 | 1.84 |
| 3 | 183 | 1.93 |  | 23 | 180 | 1.9 |  | 43 | 194 | 2.05 |
| 4 | 141 | 1.49 |  | 24 | 171 | 1.81 |  | 44 | 176 | 1.86 |
| 5 | 172 | 1.82 |  | 25 | 156 | 1.65 |  | 45 | 172 | 1.82 |
| 6 | 141 | 1.49 |  | 26 | 164 | 1.73 |  | 46 | 176 | 1.86 |
| 7 | 152 | 1.61 |  | 27 | 157 | 1.66 |  | 47 | 172 | 1.82 |
| 8 | 185 | 1.95 |  | 28 | 152 | 1.61 |  | 48 | 184 | 1.94 |
| 9 | 188 | 1.99 |  | 29 | 186 | 1.97 |  | 49 | 168 | 1.78 |
| 10 | 162 | 1.71 |  | 30 | 158 | 1.67 |  | 50 | 174 | 1.84 |
| 11 | 175 | 1.85 |  | 31 | 181 | 1.91 |  | 51 | 192 | 2.03 |
| 12 | 179 | 1.89 |  | 32 | 183 | 1.93 |  | 52 | 175 | 1.85 |
| 13 | 168 | 1.78 |  | 33 | 172 | 1.82 |  | 53 | 185 | 1.95 |
| 14 | 171 | 1.81 |  | 34 | 193 | 2.04 |  | 54 | 164 | 1.73 |
| 15 | 162 | 1.71 |  | 35 | 166 | 1.75 |  | 55 | 173 | 1.83 |
| 16 | 167 | 1.76 |  | 36 | 163 | 1.72 |  |  |  |  |
| 17 | 156 | 1.65 |  | 37 | 154 | 1.63 |  |  |  |  |
| 18 | 171 | 1.81 |  | 38 | 167 | 1.76 |  |  |  |  |
| 19 | 170 | 1.8 |  | 39 | 165 | 1.74 |  |  |  |  |
| 20 | 184 | 1.94 |  | 40 | 186 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.19 |  | 24 | 1 | 1.19 |  | 46 | 2 | 2.38 |
| 2 | 2 | 2.38 |  | 25 | 3 | 3.57 |  | 47 | 2 | 2.38 |
| 3 | 2 | 2.38 |  | 26 | 2 | 2.38 |  | 48 | 2 | 2.38 |
| 4 | 1 | 1.19 |  | 27 | 1 | 1.19 |  | 49 | 1 | 1.19 |
| 6 | 1 | 1.19 |  | 28 | 2 | 2.38 |  | 50 | 4 | 4.76 |
| 8 | 4 | 4.76 |  | 29 | 1 | 1.19 |  | 53 | 2 | 2.38 |
| 10 | 1 | 1.19 |  | 30 | 1 | 1.19 |  | 54 | 1 | 1.19 |
| 11 | 2 | 2.38 |  | 31 | 2 | 2.38 |  | 55 | 2 | 2.38 |
| 12 | 1 | 1.19 |  | 32 | 4 | 4.76 |  |  |  |  |
| 13 | 1 | 1.19 |  | 33 | 1 | 1.19 |  |  |  |  |
| 14 | 2 | 2.38 |  | 34 | 2 | 2.38 |  |  |  |  |
| 15 | 2 | 2.38 |  | 36 | 1 | 1.19 |  |  |  |  |
| 16 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 17 | 2 | 2.38 |  | 38 | 2 | 2.38 |  |  |  |  |
| 18 | 1 | 1.19 |  | 39 | 3 | 3.57 |  |  |  |  |
| 19 | 1 | 1.19 |  | 40 | 2 | 2.38 |  |  |  |  |
| 20 | 2 | 2.38 |  | 41 | 1 | 1.19 |  |  |  |  |
| 21 | 3 | 3.57 |  | 42 | 1 | 1.19 |  |  |  |  |
| 22 | 2 | 2.38 |  | 44 | 2 | 2.38 |  |  |  |  |
| 23 | 1 | 1.19 |  | 45 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.14 |  | 21 | 5 | 2.86 |  | 41 | 3 | 1.71 |
| 2 | 3 | 1.71 |  | 22 | 7 | 4.0 |  | 42 | 1 | 0.57 |
| 3 | 2 | 1.14 |  | 23 | 3 | 1.71 |  | 43 | 1 | 0.57 |
| 4 | 2 | 1.14 |  | 24 | 3 | 1.71 |  | 44 | 3 | 1.71 |
| 5 | 2 | 1.14 |  | 25 | 5 | 2.86 |  | 45 | 2 | 1.14 |
| 6 | 1 | 0.57 |  | 26 | 4 | 2.29 |  | 46 | 3 | 1.71 |
| 7 | 4 | 2.29 |  | 27 | 1 | 0.57 |  | 47 | 4 | 2.29 |
| 8 | 6 | 3.43 |  | 28 | 4 | 2.29 |  | 48 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 29 | 5 | 2.86 |  | 49 | 2 | 1.14 |
| 10 | 3 | 1.71 |  | 30 | 3 | 1.71 |  | 50 | 6 | 3.43 |
| 11 | 2 | 1.14 |  | 31 | 3 | 1.71 |  | 51 | 2 | 1.14 |
| 12 | 1 | 0.57 |  | 32 | 5 | 2.86 |  | 52 | 2 | 1.14 |
| 13 | 3 | 1.71 |  | 33 | 3 | 1.71 |  | 53 | 8 | 4.57 |
| 14 | 2 | 1.14 |  | 34 | 3 | 1.71 |  | 54 | 2 | 1.14 |
| 15 | 5 | 2.86 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 16 | 5 | 2.86 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 2 | 1.14 |  | 38 | 4 | 2.29 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 6 | 3.43 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.13 |  | 21 | 7 | 2.63 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 9 | 3.38 |  | 42 | 2 | 0.75 |
| 3 | 6 | 2.26 |  | 23 | 3 | 1.13 |  | 43 | 5 | 1.88 |
| 4 | 3 | 1.13 |  | 24 | 3 | 1.13 |  | 44 | 4 | 1.5 |
| 5 | 2 | 0.75 |  | 25 | 6 | 2.26 |  | 45 | 4 | 1.5 |
| 6 | 2 | 0.75 |  | 26 | 8 | 3.01 |  | 46 | 3 | 1.13 |
| 7 | 7 | 2.63 |  | 27 | 2 | 0.75 |  | 47 | 7 | 2.63 |
| 8 | 6 | 2.26 |  | 28 | 6 | 2.26 |  | 48 | 3 | 1.13 |
| 9 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 2 | 0.75 |
| 10 | 4 | 1.5 |  | 30 | 4 | 1.5 |  | 50 | 8 | 3.01 |
| 11 | 3 | 1.13 |  | 31 | 5 | 1.88 |  | 51 | 4 | 1.5 |
| 12 | 4 | 1.5 |  | 32 | 8 | 3.01 |  | 52 | 6 | 2.26 |
| 13 | 4 | 1.5 |  | 33 | 4 | 1.5 |  | 53 | 11 | 4.14 |
| 14 | 3 | 1.13 |  | 34 | 6 | 2.26 |  | 54 | 5 | 1.88 |
| 15 | 6 | 2.26 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 8 | 3.01 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 2 | 0.75 |  | 38 | 7 | 2.63 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 5 | 1.88 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 5 | 2026-04-23 | 37 |
| 7 | 2026-04-25 | 35 |
| 43 | 2026-04-25 | 35 |
| 52 | 2026-04-28 | 32 |
| 35 | 2026-04-28 | 32 |
| 51 | 2026-05-02 | 28 |
| 9 | 2026-05-02 | 28 |
| 6 | 2026-05-05 | 25 |
| 30 | 2026-05-05 | 25 |
| 4 | 2026-05-05 | 25 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-05-26 | 4 |
| 2 | 2026-05-30 | 0 |
| 3 | 2026-05-23 | 7 |
| 4 | 2026-05-05 | 25 |
| 5 | 2026-04-23 | 37 |
| 6 | 2026-05-05 | 25 |
| 7 | 2026-04-25 | 35 |
| 8 | 2026-05-30 | 0 |
| 9 | 2026-05-02 | 28 |
| 10 | 2026-05-09 | 21 |
| 11 | 2026-05-28 | 2 |
| 12 | 2026-05-19 | 11 |
| 13 | 2026-05-07 | 23 |
| 14 | 2026-05-26 | 4 |
| 15 | 2026-05-26 | 4 |
| 16 | 2026-05-21 | 9 |
| 17 | 2026-05-23 | 7 |
| 18 | 2026-05-21 | 9 |
| 19 | 2026-05-26 | 4 |
| 20 | 2026-05-30 | 0 |
| 21 | 2026-05-28 | 2 |
| 22 | 2026-05-23 | 7 |
| 23 | 2026-05-26 | 4 |
| 24 | 2026-05-30 | 0 |
| 25 | 2026-05-30 | 0 |
| 26 | 2026-05-14 | 16 |
| 27 | 2026-05-23 | 7 |
| 28 | 2026-05-21 | 9 |
| 29 | 2026-05-26 | 4 |
| 30 | 2026-05-05 | 25 |
| 31 | 2026-05-28 | 2 |
| 32 | 2026-05-21 | 9 |
| 33 | 2026-05-07 | 23 |
| 34 | 2026-05-26 | 4 |
| 35 | 2026-04-28 | 32 |
| 36 | 2026-05-16 | 14 |
| 37 | 2026-05-09 | 21 |
| 38 | 2026-05-23 | 7 |
| 39 | 2026-05-19 | 11 |
| 40 | 2026-05-21 | 9 |
| 41 | 2026-05-14 | 16 |
| 42 | 2026-05-30 | 0 |
| 43 | 2026-04-25 | 35 |
| 44 | 2026-05-30 | 0 |
| 45 | 2026-05-19 | 11 |
| 46 | 2026-05-09 | 21 |
| 47 | 2026-05-16 | 14 |
| 48 | 2026-05-19 | 11 |
| 49 | 2026-05-23 | 7 |
| 50 | 2026-05-16 | 14 |
| 51 | 2026-05-02 | 28 |
| 52 | 2026-04-28 | 32 |
| 53 | 2026-05-28 | 2 |
| 54 | 2026-05-28 | 2 |
| 55 | 2026-05-14 | 16 |



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

