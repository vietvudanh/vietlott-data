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
| Power 655 | 1354 | 2017-08-01 | 2026-06-04 | 1354 | 00001 | 01354 |
| Power 645 | 1321 | 2017-10-25 | 2026-06-03 | 1321 | 00198 | 01518 |
| Power 535 | 305 | 2025-06-29 | 2026-06-04 | 609 | 00001 | 00682 |
| Keno | 575 | 2022-12-04 | 2026-06-05 | 72628 | #0110271 | #0283642 |
| 3D | 1084 | 2019-04-22 | 2026-06-03 | 1084 | 00001 | 01088 |
| 3D Pro | 731 | 2021-09-14 | 2026-06-04 | 731 | 00001 | 00735 |
| Bingo18 | 548 | 2024-12-03 | 2026-06-05 | 74458 | 0083123 | 0170358 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-06-04 | 01354 | [23, 24, 28, 29, 39, 43, 45] | 2026-06-05T00:01:07.859417 |
| 2026-06-02 | 01353 | [1, 3, 5, 16, 37, 51, 42] | 2026-06-03T00:01:21.144685 |
| 2026-05-30 | 01352 | [2, 8, 20, 24, 25, 42, 44] | 2026-06-01T00:01:26.268124 |
| 2026-05-28 | 01351 | [8, 11, 21, 25, 31, 53, 54] | 2026-05-29T00:01:21.691058 |
| 2026-05-26 | 01350 | [1, 14, 15, 19, 23, 34, 29] | 2026-05-27T00:01:07.369677 |
| 2026-05-23 | 01349 | [17, 21, 22, 27, 38, 49, 3] | 2026-05-24T00:01:17.320252 |
| 2026-05-21 | 01348 | [16, 18, 20, 28, 32, 34, 40] | 2026-05-22T00:01:24.083070 |
| 2026-05-19 | 01347 | [12, 39, 40, 45, 48, 53, 21] | 2026-05-21T18:37:39.362594 |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |
| 2026-05-14 | 01345 | [26, 28, 39, 41, 48, 55, 50] | 2026-05-15T00:01:10.822513 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 180 | 1.9 |  | 21 | 170 | 1.79 |  | 41 | 198 | 2.09 |
| 2 | 154 | 1.62 |  | 22 | 202 | 2.13 |  | 42 | 175 | 1.85 |
| 3 | 184 | 1.94 |  | 23 | 181 | 1.91 |  | 43 | 195 | 2.06 |
| 4 | 141 | 1.49 |  | 24 | 172 | 1.81 |  | 44 | 176 | 1.86 |
| 5 | 173 | 1.83 |  | 25 | 156 | 1.65 |  | 45 | 173 | 1.83 |
| 6 | 141 | 1.49 |  | 26 | 164 | 1.73 |  | 46 | 176 | 1.86 |
| 7 | 152 | 1.6 |  | 27 | 157 | 1.66 |  | 47 | 172 | 1.81 |
| 8 | 185 | 1.95 |  | 28 | 153 | 1.61 |  | 48 | 184 | 1.94 |
| 9 | 188 | 1.98 |  | 29 | 187 | 1.97 |  | 49 | 168 | 1.77 |
| 10 | 162 | 1.71 |  | 30 | 158 | 1.67 |  | 50 | 174 | 1.84 |
| 11 | 175 | 1.85 |  | 31 | 181 | 1.91 |  | 51 | 193 | 2.04 |
| 12 | 179 | 1.89 |  | 32 | 183 | 1.93 |  | 52 | 175 | 1.85 |
| 13 | 168 | 1.77 |  | 33 | 172 | 1.81 |  | 53 | 185 | 1.95 |
| 14 | 171 | 1.8 |  | 34 | 193 | 2.04 |  | 54 | 164 | 1.73 |
| 15 | 162 | 1.71 |  | 35 | 166 | 1.75 |  | 55 | 173 | 1.83 |
| 16 | 168 | 1.77 |  | 36 | 163 | 1.72 |  |  |  |  |
| 17 | 156 | 1.65 |  | 37 | 155 | 1.64 |  |  |  |  |
| 18 | 171 | 1.8 |  | 38 | 167 | 1.76 |  |  |  |  |
| 19 | 170 | 1.79 |  | 39 | 166 | 1.75 |  |  |  |  |
| 20 | 184 | 1.94 |  | 40 | 186 | 1.96 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 25 | 3 | 3.3 |  | 47 | 2 | 2.2 |
| 2 | 2 | 2.2 |  | 26 | 2 | 2.2 |  | 48 | 2 | 2.2 |
| 3 | 3 | 3.3 |  | 27 | 1 | 1.1 |  | 49 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 28 | 3 | 3.3 |  | 50 | 3 | 3.3 |
| 8 | 3 | 3.3 |  | 29 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 10 | 1 | 1.1 |  | 31 | 2 | 2.2 |  | 53 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 32 | 3 | 3.3 |  | 54 | 1 | 1.1 |
| 12 | 1 | 1.1 |  | 33 | 1 | 1.1 |  | 55 | 2 | 2.2 |
| 13 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 14 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 39 | 4 | 4.4 |  |  |  |  |
| 18 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 1 | 1.1 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 46 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.65 |  | 21 | 5 | 2.75 |  | 41 | 3 | 1.65 |
| 2 | 3 | 1.65 |  | 22 | 7 | 3.85 |  | 42 | 2 | 1.1 |
| 3 | 3 | 1.65 |  | 23 | 3 | 1.65 |  | 43 | 2 | 1.1 |
| 4 | 2 | 1.1 |  | 24 | 4 | 2.2 |  | 44 | 3 | 1.65 |
| 5 | 2 | 1.1 |  | 25 | 5 | 2.75 |  | 45 | 3 | 1.65 |
| 6 | 1 | 0.55 |  | 26 | 4 | 2.2 |  | 46 | 3 | 1.65 |
| 7 | 3 | 1.65 |  | 27 | 1 | 0.55 |  | 47 | 4 | 2.2 |
| 8 | 6 | 3.3 |  | 28 | 5 | 2.75 |  | 48 | 2 | 1.1 |
| 9 | 3 | 1.65 |  | 29 | 6 | 3.3 |  | 49 | 2 | 1.1 |
| 10 | 2 | 1.1 |  | 30 | 2 | 1.1 |  | 50 | 6 | 3.3 |
| 11 | 2 | 1.1 |  | 31 | 3 | 1.65 |  | 51 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 5 | 2.75 |  | 52 | 2 | 1.1 |
| 13 | 3 | 1.65 |  | 33 | 3 | 1.65 |  | 53 | 8 | 4.4 |
| 14 | 2 | 1.1 |  | 34 | 3 | 1.65 |  | 54 | 1 | 0.55 |
| 15 | 5 | 2.75 |  | 35 | 2 | 1.1 |  | 55 | 4 | 2.2 |
| 16 | 6 | 3.3 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 7 | 3.85 |  |  |  |  |
| 20 | 3 | 1.65 |  | 40 | 2 | 1.1 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.47 |  | 21 | 7 | 2.56 |  | 41 | 4 | 1.47 |
| 2 | 3 | 1.1 |  | 22 | 9 | 3.3 |  | 42 | 3 | 1.1 |
| 3 | 7 | 2.56 |  | 23 | 4 | 1.47 |  | 43 | 5 | 1.83 |
| 4 | 3 | 1.1 |  | 24 | 4 | 1.47 |  | 44 | 4 | 1.47 |
| 5 | 3 | 1.1 |  | 25 | 6 | 2.2 |  | 45 | 5 | 1.83 |
| 6 | 2 | 0.73 |  | 26 | 8 | 2.93 |  | 46 | 3 | 1.1 |
| 7 | 7 | 2.56 |  | 27 | 2 | 0.73 |  | 47 | 7 | 2.56 |
| 8 | 6 | 2.2 |  | 28 | 7 | 2.56 |  | 48 | 3 | 1.1 |
| 9 | 6 | 2.2 |  | 29 | 8 | 2.93 |  | 49 | 2 | 0.73 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 8 | 2.93 |
| 11 | 3 | 1.1 |  | 31 | 5 | 1.83 |  | 51 | 4 | 1.47 |
| 12 | 4 | 1.47 |  | 32 | 8 | 2.93 |  | 52 | 6 | 2.2 |
| 13 | 4 | 1.47 |  | 33 | 4 | 1.47 |  | 53 | 11 | 4.03 |
| 14 | 2 | 0.73 |  | 34 | 6 | 2.2 |  | 54 | 5 | 1.83 |
| 15 | 6 | 2.2 |  | 35 | 2 | 0.73 |  | 55 | 6 | 2.2 |
| 16 | 8 | 2.93 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 5 | 1.83 |  | 37 | 3 | 1.1 |  |  |  |  |
| 18 | 2 | 0.73 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 3 | 1.1 |  | 39 | 9 | 3.3 |  |  |  |  |
| 20 | 4 | 1.47 |  | 40 | 5 | 1.83 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 7 | 2026-04-25 | 40 |
| 52 | 2026-04-28 | 37 |
| 35 | 2026-04-28 | 37 |
| 9 | 2026-05-02 | 33 |
| 6 | 2026-05-05 | 30 |
| 30 | 2026-05-05 | 30 |
| 4 | 2026-05-05 | 30 |
| 33 | 2026-05-07 | 28 |
| 13 | 2026-05-07 | 28 |
| 10 | 2026-05-09 | 26 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-02 | 2 |
| 2 | 2026-05-30 | 5 |
| 3 | 2026-06-02 | 2 |
| 4 | 2026-05-05 | 30 |
| 5 | 2026-06-02 | 2 |
| 6 | 2026-05-05 | 30 |
| 7 | 2026-04-25 | 40 |
| 8 | 2026-05-30 | 5 |
| 9 | 2026-05-02 | 33 |
| 10 | 2026-05-09 | 26 |
| 11 | 2026-05-28 | 7 |
| 12 | 2026-05-19 | 16 |
| 13 | 2026-05-07 | 28 |
| 14 | 2026-05-26 | 9 |
| 15 | 2026-05-26 | 9 |
| 16 | 2026-06-02 | 2 |
| 17 | 2026-05-23 | 12 |
| 18 | 2026-05-21 | 14 |
| 19 | 2026-05-26 | 9 |
| 20 | 2026-05-30 | 5 |
| 21 | 2026-05-28 | 7 |
| 22 | 2026-05-23 | 12 |
| 23 | 2026-06-04 | 0 |
| 24 | 2026-06-04 | 0 |
| 25 | 2026-05-30 | 5 |
| 26 | 2026-05-14 | 21 |
| 27 | 2026-05-23 | 12 |
| 28 | 2026-06-04 | 0 |
| 29 | 2026-06-04 | 0 |
| 30 | 2026-05-05 | 30 |
| 31 | 2026-05-28 | 7 |
| 32 | 2026-05-21 | 14 |
| 33 | 2026-05-07 | 28 |
| 34 | 2026-05-26 | 9 |
| 35 | 2026-04-28 | 37 |
| 36 | 2026-05-16 | 19 |
| 37 | 2026-06-02 | 2 |
| 38 | 2026-05-23 | 12 |
| 39 | 2026-06-04 | 0 |
| 40 | 2026-05-21 | 14 |
| 41 | 2026-05-14 | 21 |
| 42 | 2026-06-02 | 2 |
| 43 | 2026-06-04 | 0 |
| 44 | 2026-05-30 | 5 |
| 45 | 2026-06-04 | 0 |
| 46 | 2026-05-09 | 26 |
| 47 | 2026-05-16 | 19 |
| 48 | 2026-05-19 | 16 |
| 49 | 2026-05-23 | 12 |
| 50 | 2026-05-16 | 19 |
| 51 | 2026-06-02 | 2 |
| 52 | 2026-04-28 | 37 |
| 53 | 2026-05-28 | 7 |
| 54 | 2026-05-28 | 7 |
| 55 | 2026-05-14 | 21 |



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

