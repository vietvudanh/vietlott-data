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
| Power 655 | 1351 | 2017-08-01 | 2026-05-28 | 1351 | 00001 | 01351 |
| Power 645 | 1318 | 2017-10-25 | 2026-05-27 | 1318 | 00198 | 01515 |
| Power 535 | 298 | 2025-06-29 | 2026-05-28 | 595 | 00001 | 00668 |
| Keno | 567 | 2022-12-04 | 2026-05-28 | 71684 | #0110271 | #0282765 |
| 3D | 1081 | 2019-04-22 | 2026-05-27 | 1081 | 00001 | 01085 |
| 3D Pro | 728 | 2021-09-14 | 2026-05-28 | 728 | 00001 | 00732 |
| Bingo18 | 540 | 2024-12-03 | 2026-05-28 | 73232 | 0083123 | 0169185 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-28 | 01351 | [8, 11, 21, 25, 31, 53, 54] | 2026-05-29T00:01:21.691058 |
| 2026-05-26 | 01350 | [1, 14, 15, 19, 23, 34, 29] | 2026-05-27T00:01:07.369677 |
| 2026-05-23 | 01349 | [17, 21, 22, 27, 38, 49, 3] | 2026-05-24T00:01:17.320252 |
| 2026-05-21 | 01348 | [16, 18, 20, 28, 32, 34, 40] | 2026-05-22T00:01:24.083070 |
| 2026-05-19 | 01347 | [12, 39, 40, 45, 48, 53, 21] | 2026-05-21T18:37:39.362594 |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |
| 2026-05-14 | 01345 | [26, 28, 39, 41, 48, 55, 50] | 2026-05-15T00:01:10.822513 |
| 2026-05-12 | 01344 | [2, 11, 22, 26, 31, 38, 15] | 2026-05-12T18:58:07.963930 |
| 2026-05-09 | 01343 | [3, 10, 32, 37, 45, 55, 46] | 2026-05-10T00:01:08.118122 |
| 2026-05-07 | 01342 | [13, 14, 33, 44, 46, 50, 47] | 2026-05-08T12:04:58.259525 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 179 | 1.89 |  | 21 | 170 | 1.8 |  | 41 | 198 | 2.09 |
| 2 | 153 | 1.62 |  | 22 | 202 | 2.14 |  | 42 | 173 | 1.83 |
| 3 | 183 | 1.94 |  | 23 | 180 | 1.9 |  | 43 | 194 | 2.05 |
| 4 | 141 | 1.49 |  | 24 | 170 | 1.8 |  | 44 | 175 | 1.85 |
| 5 | 172 | 1.82 |  | 25 | 155 | 1.64 |  | 45 | 172 | 1.82 |
| 6 | 141 | 1.49 |  | 26 | 164 | 1.73 |  | 46 | 176 | 1.86 |
| 7 | 152 | 1.61 |  | 27 | 157 | 1.66 |  | 47 | 172 | 1.82 |
| 8 | 184 | 1.95 |  | 28 | 152 | 1.61 |  | 48 | 184 | 1.95 |
| 9 | 188 | 1.99 |  | 29 | 186 | 1.97 |  | 49 | 168 | 1.78 |
| 10 | 162 | 1.71 |  | 30 | 158 | 1.67 |  | 50 | 174 | 1.84 |
| 11 | 175 | 1.85 |  | 31 | 181 | 1.91 |  | 51 | 192 | 2.03 |
| 12 | 179 | 1.89 |  | 32 | 183 | 1.94 |  | 52 | 175 | 1.85 |
| 13 | 168 | 1.78 |  | 33 | 172 | 1.82 |  | 53 | 185 | 1.96 |
| 14 | 171 | 1.81 |  | 34 | 193 | 2.04 |  | 54 | 164 | 1.73 |
| 15 | 162 | 1.71 |  | 35 | 166 | 1.76 |  | 55 | 173 | 1.83 |
| 16 | 167 | 1.77 |  | 36 | 163 | 1.72 |  |  |  |  |
| 17 | 156 | 1.65 |  | 37 | 154 | 1.63 |  |  |  |  |
| 18 | 171 | 1.81 |  | 38 | 167 | 1.77 |  |  |  |  |
| 19 | 170 | 1.8 |  | 39 | 165 | 1.74 |  |  |  |  |
| 20 | 183 | 1.94 |  | 40 | 186 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 23 | 1 | 1.1 |  | 47 | 2 | 2.2 |
| 2 | 1 | 1.1 |  | 25 | 3 | 3.3 |  | 48 | 2 | 2.2 |
| 3 | 2 | 2.2 |  | 26 | 3 | 3.3 |  | 49 | 1 | 1.1 |
| 4 | 1 | 1.1 |  | 27 | 1 | 1.1 |  | 50 | 5 | 5.49 |
| 6 | 1 | 1.1 |  | 28 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 8 | 3 | 3.3 |  | 29 | 2 | 2.2 |  | 53 | 2 | 2.2 |
| 9 | 2 | 2.2 |  | 30 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 10 | 1 | 1.1 |  | 31 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 32 | 4 | 4.4 |  |  |  |  |
| 12 | 1 | 1.1 |  | 33 | 2 | 2.2 |  |  |  |  |
| 13 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 14 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 17 | 3 | 3.3 |  | 39 | 3 | 3.3 |  |  |  |  |
| 18 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 1 | 1.1 |  |  |  |  |
| 20 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |
| 21 | 5 | 5.49 |  | 45 | 2 | 2.2 |  |  |  |  |
| 22 | 3 | 3.3 |  | 46 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.1 |  | 21 | 6 | 3.3 |  | 41 | 3 | 1.65 |
| 2 | 2 | 1.1 |  | 22 | 9 | 4.95 |  | 43 | 2 | 1.1 |
| 3 | 2 | 1.1 |  | 23 | 3 | 1.65 |  | 44 | 2 | 1.1 |
| 4 | 2 | 1.1 |  | 24 | 2 | 1.1 |  | 45 | 2 | 1.1 |
| 5 | 2 | 1.1 |  | 25 | 4 | 2.2 |  | 46 | 3 | 1.65 |
| 6 | 1 | 0.55 |  | 26 | 4 | 2.2 |  | 47 | 4 | 2.2 |
| 7 | 4 | 2.2 |  | 27 | 1 | 0.55 |  | 48 | 3 | 1.65 |
| 8 | 5 | 2.75 |  | 28 | 4 | 2.2 |  | 49 | 2 | 1.1 |
| 9 | 4 | 2.2 |  | 29 | 5 | 2.75 |  | 50 | 6 | 3.3 |
| 10 | 3 | 1.65 |  | 30 | 3 | 1.65 |  | 51 | 2 | 1.1 |
| 11 | 3 | 1.65 |  | 31 | 3 | 1.65 |  | 52 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 6 | 3.3 |  | 53 | 9 | 4.95 |
| 13 | 3 | 1.65 |  | 33 | 3 | 1.65 |  | 54 | 2 | 1.1 |
| 14 | 2 | 1.1 |  | 34 | 4 | 2.2 |  | 55 | 4 | 2.2 |
| 15 | 6 | 3.3 |  | 35 | 2 | 1.1 |  |  |  |  |
| 16 | 6 | 3.3 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 5 | 2.75 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 6 | 3.3 |  |  |  |  |
| 20 | 2 | 1.1 |  | 40 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.1 |  | 21 | 7 | 2.56 |  | 41 | 4 | 1.47 |
| 2 | 2 | 0.73 |  | 22 | 10 | 3.66 |  | 42 | 1 | 0.37 |
| 3 | 6 | 2.2 |  | 23 | 3 | 1.1 |  | 43 | 6 | 2.2 |
| 4 | 3 | 1.1 |  | 24 | 2 | 0.73 |  | 44 | 4 | 1.47 |
| 5 | 2 | 0.73 |  | 25 | 7 | 2.56 |  | 45 | 4 | 1.47 |
| 6 | 2 | 0.73 |  | 26 | 8 | 2.93 |  | 46 | 3 | 1.1 |
| 7 | 8 | 2.93 |  | 27 | 3 | 1.1 |  | 47 | 7 | 2.56 |
| 8 | 5 | 1.83 |  | 28 | 6 | 2.2 |  | 48 | 3 | 1.1 |
| 9 | 6 | 2.2 |  | 29 | 8 | 2.93 |  | 49 | 2 | 0.73 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 9 | 3.3 |
| 11 | 3 | 1.1 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 4 | 1.47 |  | 32 | 8 | 2.93 |  | 52 | 6 | 2.2 |
| 13 | 5 | 1.83 |  | 33 | 4 | 1.47 |  | 53 | 11 | 4.03 |
| 14 | 3 | 1.1 |  | 34 | 6 | 2.2 |  | 54 | 6 | 2.2 |
| 15 | 6 | 2.2 |  | 35 | 3 | 1.1 |  | 55 | 6 | 2.2 |
| 16 | 8 | 2.93 |  | 36 | 5 | 1.83 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 2 | 0.73 |  | 38 | 7 | 2.56 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 8 | 2.93 |  |  |  |  |
| 20 | 3 | 1.1 |  | 40 | 5 | 1.83 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 42 | 2026-03-28 | 61 |
| 5 | 2026-04-23 | 35 |
| 43 | 2026-04-25 | 33 |
| 7 | 2026-04-25 | 33 |
| 24 | 2026-04-28 | 30 |
| 52 | 2026-04-28 | 30 |
| 35 | 2026-04-28 | 30 |
| 9 | 2026-05-02 | 26 |
| 51 | 2026-05-02 | 26 |
| 6 | 2026-05-05 | 23 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-05-26 | 2 |
| 2 | 2026-05-12 | 16 |
| 3 | 2026-05-23 | 5 |
| 4 | 2026-05-05 | 23 |
| 5 | 2026-04-23 | 35 |
| 6 | 2026-05-05 | 23 |
| 7 | 2026-04-25 | 33 |
| 8 | 2026-05-28 | 0 |
| 9 | 2026-05-02 | 26 |
| 10 | 2026-05-09 | 19 |
| 11 | 2026-05-28 | 0 |
| 12 | 2026-05-19 | 9 |
| 13 | 2026-05-07 | 21 |
| 14 | 2026-05-26 | 2 |
| 15 | 2026-05-26 | 2 |
| 16 | 2026-05-21 | 7 |
| 17 | 2026-05-23 | 5 |
| 18 | 2026-05-21 | 7 |
| 19 | 2026-05-26 | 2 |
| 20 | 2026-05-21 | 7 |
| 21 | 2026-05-28 | 0 |
| 22 | 2026-05-23 | 5 |
| 23 | 2026-05-26 | 2 |
| 24 | 2026-04-28 | 30 |
| 25 | 2026-05-28 | 0 |
| 26 | 2026-05-14 | 14 |
| 27 | 2026-05-23 | 5 |
| 28 | 2026-05-21 | 7 |
| 29 | 2026-05-26 | 2 |
| 30 | 2026-05-05 | 23 |
| 31 | 2026-05-28 | 0 |
| 32 | 2026-05-21 | 7 |
| 33 | 2026-05-07 | 21 |
| 34 | 2026-05-26 | 2 |
| 35 | 2026-04-28 | 30 |
| 36 | 2026-05-16 | 12 |
| 37 | 2026-05-09 | 19 |
| 38 | 2026-05-23 | 5 |
| 39 | 2026-05-19 | 9 |
| 40 | 2026-05-21 | 7 |
| 41 | 2026-05-14 | 14 |
| 42 | 2026-03-28 | 61 |
| 43 | 2026-04-25 | 33 |
| 44 | 2026-05-07 | 21 |
| 45 | 2026-05-19 | 9 |
| 46 | 2026-05-09 | 19 |
| 47 | 2026-05-16 | 12 |
| 48 | 2026-05-19 | 9 |
| 49 | 2026-05-23 | 5 |
| 50 | 2026-05-16 | 12 |
| 51 | 2026-05-02 | 26 |
| 52 | 2026-04-28 | 30 |
| 53 | 2026-05-28 | 0 |
| 54 | 2026-05-28 | 0 |
| 55 | 2026-05-14 | 14 |



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

