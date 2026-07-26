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
| Power 655 | 1376 | 2017-08-01 | 2026-07-25 | 1376 | 00001 | 01376 |
| Power 645 | 1344 | 2017-10-25 | 2026-07-26 | 1344 | 00198 | 01541 |
| Power 535 | 356 | 2025-06-29 | 2026-07-26 | 710 | 00001 | 00786 |
| Keno | 623 | 2022-12-04 | 2026-07-26 | 78279 | #0110271 | #0289786 |
| 3D | 1106 | 2019-04-22 | 2026-07-24 | 1106 | 00001 | 01110 |
| 3D Pro | 753 | 2021-09-14 | 2026-07-25 | 753 | 00001 | 00757 |
| Bingo18 | 599 | 2024-12-03 | 2026-07-26 | 82645 | 0083123 | 0178566 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36] | 2026-07-24T00:01:33.770193 |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 185 | 1.92 |  | 21 | 172 | 1.79 |  | 41 | 203 | 2.11 |
| 2 | 157 | 1.63 |  | 22 | 205 | 2.13 |  | 42 | 178 | 1.85 |
| 3 | 187 | 1.94 |  | 23 | 185 | 1.92 |  | 43 | 197 | 2.05 |
| 4 | 144 | 1.5 |  | 24 | 175 | 1.82 |  | 44 | 178 | 1.85 |
| 5 | 178 | 1.85 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.84 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.71 |  | 46 | 180 | 1.87 |
| 7 | 154 | 1.6 |  | 27 | 159 | 1.65 |  | 47 | 174 | 1.81 |
| 8 | 192 | 1.99 |  | 28 | 157 | 1.63 |  | 48 | 188 | 1.95 |
| 9 | 191 | 1.98 |  | 29 | 187 | 1.94 |  | 49 | 171 | 1.78 |
| 10 | 164 | 1.7 |  | 30 | 160 | 1.66 |  | 50 | 175 | 1.82 |
| 11 | 178 | 1.85 |  | 31 | 183 | 1.9 |  | 51 | 194 | 2.01 |
| 12 | 179 | 1.86 |  | 32 | 186 | 1.93 |  | 52 | 177 | 1.84 |
| 13 | 172 | 1.79 |  | 33 | 178 | 1.85 |  | 53 | 187 | 1.94 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.02 |  | 54 | 166 | 1.72 |
| 15 | 164 | 1.7 |  | 35 | 169 | 1.75 |  | 55 | 176 | 1.83 |
| 16 | 172 | 1.79 |  | 36 | 166 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 157 | 1.63 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 169 | 1.75 |  |  |  |  |
| 19 | 172 | 1.79 |  | 39 | 168 | 1.74 |  |  |  |  |
| 20 | 187 | 1.94 |  | 40 | 191 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 22 | 3 | 3.3 |  | 44 | 2 | 2.2 |
| 2 | 1 | 1.1 |  | 23 | 2 | 2.2 |  | 45 | 4 | 4.4 |
| 3 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 47 | 1 | 1.1 |
| 4 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 48 | 3 | 3.3 |
| 5 | 3 | 3.3 |  | 27 | 1 | 1.1 |  | 49 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 28 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 8 | 3 | 3.3 |  | 31 | 1 | 1.1 |  | 52 | 1 | 1.1 |
| 9 | 3 | 3.3 |  | 32 | 2 | 2.2 |  | 53 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 33 | 5 | 5.49 |  | 54 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 34 | 1 | 1.1 |  | 55 | 2 | 2.2 |
| 13 | 3 | 3.3 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 39 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 4 | 4.4 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 43 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 22 | 3 | 1.65 |  | 42 | 5 | 2.75 |
| 2 | 4 | 2.2 |  | 23 | 5 | 2.75 |  | 43 | 3 | 1.65 |
| 3 | 4 | 2.2 |  | 24 | 5 | 2.75 |  | 44 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 45 | 5 | 2.75 |
| 5 | 6 | 3.3 |  | 26 | 1 | 0.55 |  | 46 | 4 | 2.2 |
| 6 | 2 | 1.1 |  | 27 | 2 | 1.1 |  | 47 | 2 | 1.1 |
| 7 | 2 | 1.1 |  | 28 | 5 | 2.75 |  | 48 | 4 | 2.2 |
| 8 | 9 | 4.95 |  | 29 | 1 | 0.55 |  | 49 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 30 | 2 | 1.1 |  | 50 | 1 | 0.55 |
| 10 | 2 | 1.1 |  | 31 | 3 | 1.65 |  | 51 | 2 | 1.1 |
| 11 | 4 | 2.2 |  | 32 | 3 | 1.65 |  | 52 | 2 | 1.1 |
| 13 | 4 | 2.2 |  | 33 | 6 | 3.3 |  | 53 | 3 | 1.65 |
| 14 | 3 | 1.65 |  | 34 | 2 | 1.1 |  | 54 | 3 | 1.65 |
| 15 | 2 | 1.1 |  | 35 | 3 | 1.65 |  | 55 | 3 | 1.65 |
| 16 | 5 | 2.75 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 3 | 1.65 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 5 | 2.75 |  |  |  |  |
| 21 | 3 | 1.65 |  | 41 | 5 | 2.75 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.56 |  | 21 | 7 | 2.56 |  | 41 | 6 | 2.2 |
| 2 | 5 | 1.83 |  | 22 | 6 | 2.2 |  | 42 | 5 | 1.83 |
| 3 | 6 | 2.2 |  | 23 | 6 | 2.2 |  | 43 | 3 | 1.1 |
| 4 | 4 | 1.47 |  | 24 | 6 | 2.2 |  | 44 | 4 | 1.47 |
| 5 | 6 | 2.2 |  | 25 | 6 | 2.2 |  | 45 | 7 | 2.56 |
| 6 | 3 | 1.1 |  | 26 | 4 | 1.47 |  | 46 | 6 | 2.2 |
| 7 | 2 | 0.73 |  | 27 | 3 | 1.1 |  | 47 | 4 | 1.47 |
| 8 | 11 | 4.03 |  | 28 | 7 | 2.56 |  | 48 | 6 | 2.2 |
| 9 | 5 | 1.83 |  | 29 | 3 | 1.1 |  | 49 | 4 | 1.47 |
| 10 | 3 | 1.1 |  | 30 | 3 | 1.1 |  | 50 | 6 | 2.2 |
| 11 | 5 | 1.83 |  | 31 | 4 | 1.47 |  | 51 | 4 | 1.47 |
| 12 | 1 | 0.37 |  | 32 | 7 | 2.56 |  | 52 | 3 | 1.1 |
| 13 | 5 | 1.83 |  | 33 | 8 | 2.93 |  | 53 | 5 | 1.83 |
| 14 | 5 | 1.83 |  | 34 | 5 | 1.83 |  | 54 | 3 | 1.1 |
| 15 | 5 | 1.83 |  | 35 | 4 | 1.47 |  | 55 | 5 | 1.83 |
| 16 | 7 | 2.56 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 6 | 2.2 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 4 | 1.47 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 6 | 2.2 |  |  |  |  |
| 20 | 5 | 1.83 |  | 40 | 7 | 2.56 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-05-19 | 67 |
| 29 | 2026-06-04 | 51 |
| 26 | 2026-06-20 | 35 |
| 46 | 2026-06-23 | 32 |
| 7 | 2026-06-27 | 28 |
| 52 | 2026-06-27 | 28 |
| 47 | 2026-06-30 | 25 |
| 28 | 2026-07-02 | 23 |
| 34 | 2026-07-02 | 23 |
| 15 | 2026-07-04 | 21 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-07-23 | 2 |
| 2 | 2026-07-09 | 16 |
| 3 | 2026-07-23 | 2 |
| 4 | 2026-07-07 | 18 |
| 5 | 2026-07-25 | 0 |
| 6 | 2026-07-07 | 18 |
| 7 | 2026-06-27 | 28 |
| 8 | 2026-07-23 | 2 |
| 9 | 2026-07-25 | 0 |
| 10 | 2026-07-14 | 11 |
| 11 | 2026-07-21 | 4 |
| 12 | 2026-05-19 | 67 |
| 13 | 2026-07-21 | 4 |
| 14 | 2026-07-09 | 16 |
| 15 | 2026-07-04 | 21 |
| 16 | 2026-07-18 | 7 |
| 17 | 2026-07-11 | 14 |
| 18 | 2026-07-04 | 21 |
| 19 | 2026-07-16 | 9 |
| 20 | 2026-07-16 | 9 |
| 21 | 2026-07-16 | 9 |
| 22 | 2026-07-21 | 4 |
| 23 | 2026-07-04 | 21 |
| 24 | 2026-07-21 | 4 |
| 25 | 2026-07-07 | 18 |
| 26 | 2026-06-20 | 35 |
| 27 | 2026-07-25 | 0 |
| 28 | 2026-07-02 | 23 |
| 29 | 2026-06-04 | 51 |
| 30 | 2026-07-14 | 11 |
| 31 | 2026-07-04 | 21 |
| 32 | 2026-07-21 | 4 |
| 33 | 2026-07-25 | 0 |
| 34 | 2026-07-02 | 23 |
| 35 | 2026-07-14 | 11 |
| 36 | 2026-07-23 | 2 |
| 37 | 2026-07-25 | 0 |
| 38 | 2026-07-23 | 2 |
| 39 | 2026-07-21 | 4 |
| 40 | 2026-07-23 | 2 |
| 41 | 2026-07-18 | 7 |
| 42 | 2026-07-11 | 14 |
| 43 | 2026-07-04 | 21 |
| 44 | 2026-07-07 | 18 |
| 45 | 2026-07-18 | 7 |
| 46 | 2026-06-23 | 32 |
| 47 | 2026-06-30 | 25 |
| 48 | 2026-07-25 | 0 |
| 49 | 2026-07-09 | 16 |
| 50 | 2026-07-25 | 0 |
| 51 | 2026-07-14 | 11 |
| 52 | 2026-06-27 | 28 |
| 53 | 2026-07-16 | 9 |
| 54 | 2026-07-18 | 7 |
| 55 | 2026-07-23 | 2 |



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

