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
| Power 655 | 1389 | 2017-08-01 | 2026-08-25 | 1389 | 00001 | 01389 |
| Power 645 | 1356 | 2017-10-25 | 2026-08-23 | 1356 | 00198 | 01553 |
| Power 535 | 387 | 2025-06-29 | 2026-08-25 | 772 | 00001 | 00846 |
| Keno | 655 | 2022-12-04 | 2026-08-25 | 82145 | #0110271 | #0293356 |
| 3D | 1119 | 2019-04-22 | 2026-08-24 | 1119 | 00001 | 01123 |
| 3D Pro | 766 | 2021-09-14 | 2026-08-25 | 766 | 00001 | 00770 |
| Bingo18 | 629 | 2024-12-03 | 2026-08-25 | 87412 | 0083123 | 0183336 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42] | 2026-08-16T11:07:54.647468 |
| 2026-08-11 | 01383 | [2, 7, 19, 20, 39, 50, 31] | 2026-08-12T00:02:10.803156 |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37] | 2026-08-09T00:01:07.514841 |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1] | 2026-08-07T00:01:13.032397 |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] | 2026-08-06T00:02:27.504833 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 186 | 1.91 |  | 21 | 173 | 1.78 |  | 41 | 205 | 2.11 |
| 2 | 161 | 1.66 |  | 22 | 206 | 2.12 |  | 42 | 180 | 1.85 |
| 3 | 188 | 1.93 |  | 23 | 187 | 1.92 |  | 43 | 198 | 2.04 |
| 4 | 144 | 1.48 |  | 24 | 176 | 1.81 |  | 44 | 180 | 1.85 |
| 5 | 181 | 1.86 |  | 25 | 159 | 1.64 |  | 45 | 179 | 1.84 |
| 6 | 143 | 1.47 |  | 26 | 165 | 1.7 |  | 46 | 181 | 1.86 |
| 7 | 157 | 1.61 |  | 27 | 162 | 1.67 |  | 47 | 176 | 1.81 |
| 8 | 194 | 2.0 |  | 28 | 158 | 1.63 |  | 48 | 190 | 1.95 |
| 9 | 193 | 1.99 |  | 29 | 190 | 1.95 |  | 49 | 173 | 1.78 |
| 10 | 164 | 1.69 |  | 30 | 162 | 1.67 |  | 50 | 177 | 1.82 |
| 11 | 179 | 1.84 |  | 31 | 186 | 1.91 |  | 51 | 197 | 2.03 |
| 12 | 180 | 1.85 |  | 32 | 186 | 1.91 |  | 52 | 177 | 1.82 |
| 13 | 173 | 1.78 |  | 33 | 179 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 178 | 1.83 |  | 34 | 195 | 2.01 |  | 54 | 167 | 1.72 |
| 15 | 165 | 1.7 |  | 35 | 170 | 1.75 |  | 55 | 178 | 1.83 |
| 16 | 174 | 1.79 |  | 36 | 167 | 1.72 |  |  |  |  |
| 17 | 159 | 1.64 |  | 37 | 158 | 1.63 |  |  |  |  |
| 18 | 178 | 1.83 |  | 38 | 172 | 1.77 |  |  |  |  |
| 19 | 174 | 1.79 |  | 39 | 172 | 1.77 |  |  |  |  |
| 20 | 189 | 1.94 |  | 40 | 194 | 2.0 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 25 | 2 | 2.2 |  | 48 | 2 | 2.2 |
| 2 | 4 | 4.4 |  | 27 | 3 | 3.3 |  | 49 | 2 | 2.2 |
| 3 | 1 | 1.1 |  | 28 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 5 | 3 | 3.3 |  | 29 | 3 | 3.3 |  | 51 | 3 | 3.3 |
| 7 | 3 | 3.3 |  | 30 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 8 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 55 | 2 | 2.2 |
| 9 | 2 | 2.2 |  | 33 | 1 | 1.1 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 4 | 4.4 |  | 38 | 3 | 3.3 |  |  |  |  |
| 15 | 1 | 1.1 |  | 39 | 4 | 4.4 |  |  |  |  |
| 16 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 18 | 4 | 4.4 |  | 41 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 21 | 1 | 1.1 |  | 44 | 2 | 2.2 |  |  |  |  |
| 22 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |
| 24 | 1 | 1.1 |  | 47 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.1 |  | 21 | 3 | 1.65 |  | 42 | 4 | 2.2 |
| 2 | 5 | 2.75 |  | 22 | 4 | 2.2 |  | 43 | 3 | 1.65 |
| 3 | 2 | 1.1 |  | 23 | 4 | 2.2 |  | 44 | 4 | 2.2 |
| 4 | 1 | 0.55 |  | 24 | 3 | 1.65 |  | 45 | 6 | 3.3 |
| 5 | 6 | 3.3 |  | 25 | 3 | 1.65 |  | 46 | 1 | 0.55 |
| 6 | 1 | 0.55 |  | 27 | 4 | 2.2 |  | 47 | 3 | 1.65 |
| 7 | 4 | 2.2 |  | 28 | 3 | 1.65 |  | 48 | 5 | 2.75 |
| 8 | 5 | 2.75 |  | 29 | 3 | 1.65 |  | 49 | 4 | 2.2 |
| 9 | 5 | 2.75 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 10 | 2 | 1.1 |  | 31 | 4 | 2.2 |  | 51 | 4 | 2.2 |
| 11 | 3 | 1.65 |  | 32 | 2 | 1.1 |  | 52 | 1 | 0.55 |
| 12 | 1 | 0.55 |  | 33 | 6 | 3.3 |  | 53 | 1 | 0.55 |
| 13 | 4 | 2.2 |  | 34 | 1 | 0.55 |  | 54 | 3 | 1.65 |
| 14 | 5 | 2.75 |  | 35 | 2 | 1.1 |  | 55 | 4 | 2.2 |
| 15 | 2 | 1.1 |  | 36 | 2 | 1.1 |  |  |  |  |
| 16 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 38 | 4 | 2.2 |  |  |  |  |
| 18 | 6 | 3.3 |  | 39 | 5 | 2.75 |  |  |  |  |
| 19 | 3 | 1.65 |  | 40 | 5 | 2.75 |  |  |  |  |
| 20 | 4 | 2.2 |  | 41 | 6 | 3.3 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.56 |  | 21 | 4 | 1.47 |  | 41 | 7 | 2.56 |
| 2 | 8 | 2.93 |  | 22 | 4 | 1.47 |  | 42 | 7 | 2.56 |
| 3 | 5 | 1.83 |  | 23 | 7 | 2.56 |  | 43 | 4 | 1.47 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 5 | 1.83 |
| 5 | 9 | 3.3 |  | 25 | 5 | 1.83 |  | 45 | 7 | 2.56 |
| 6 | 2 | 0.73 |  | 26 | 1 | 0.37 |  | 46 | 5 | 1.83 |
| 7 | 5 | 1.83 |  | 27 | 5 | 1.83 |  | 47 | 4 | 1.47 |
| 8 | 11 | 4.03 |  | 28 | 6 | 2.2 |  | 48 | 6 | 2.2 |
| 9 | 5 | 1.83 |  | 29 | 4 | 1.47 |  | 49 | 5 | 1.83 |
| 10 | 2 | 0.73 |  | 30 | 4 | 1.47 |  | 50 | 3 | 1.1 |
| 11 | 5 | 1.83 |  | 31 | 6 | 2.2 |  | 51 | 5 | 1.83 |
| 12 | 1 | 0.37 |  | 32 | 3 | 1.1 |  | 52 | 2 | 0.73 |
| 13 | 5 | 1.83 |  | 33 | 7 | 2.56 |  | 53 | 3 | 1.1 |
| 14 | 7 | 2.56 |  | 34 | 2 | 0.73 |  | 54 | 4 | 1.47 |
| 15 | 3 | 1.1 |  | 35 | 4 | 1.47 |  | 55 | 5 | 1.83 |
| 16 | 7 | 2.56 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 3 | 1.1 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 7 | 2.56 |  | 38 | 5 | 1.83 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 7 | 2.56 |  |  |  |  |
| 20 | 6 | 2.2 |  | 40 | 8 | 2.93 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 26 | 2026-06-20 | 66 |
| 52 | 2026-06-27 | 59 |
| 34 | 2026-07-02 | 54 |
| 6 | 2026-07-07 | 49 |
| 4 | 2026-07-07 | 49 |
| 17 | 2026-07-11 | 45 |
| 10 | 2026-07-14 | 42 |
| 53 | 2026-07-16 | 40 |
| 32 | 2026-07-21 | 35 |
| 22 | 2026-07-28 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-08-06 | 19 |
| 2 | 2026-08-20 | 5 |
| 3 | 2026-08-18 | 7 |
| 4 | 2026-07-07 | 49 |
| 5 | 2026-08-25 | 0 |
| 6 | 2026-07-07 | 49 |
| 7 | 2026-08-25 | 0 |
| 8 | 2026-08-22 | 3 |
| 9 | 2026-08-22 | 3 |
| 10 | 2026-07-14 | 42 |
| 11 | 2026-08-01 | 24 |
| 12 | 2026-07-30 | 26 |
| 13 | 2026-08-25 | 0 |
| 14 | 2026-08-25 | 0 |
| 15 | 2026-08-18 | 7 |
| 16 | 2026-08-15 | 10 |
| 17 | 2026-07-11 | 45 |
| 18 | 2026-08-25 | 0 |
| 19 | 2026-08-22 | 3 |
| 20 | 2026-08-15 | 10 |
| 21 | 2026-08-22 | 3 |
| 22 | 2026-07-28 | 28 |
| 23 | 2026-08-06 | 19 |
| 24 | 2026-07-30 | 26 |
| 25 | 2026-08-22 | 3 |
| 26 | 2026-06-20 | 66 |
| 27 | 2026-08-15 | 10 |
| 28 | 2026-07-30 | 26 |
| 29 | 2026-08-20 | 5 |
| 30 | 2026-08-18 | 7 |
| 31 | 2026-08-25 | 0 |
| 32 | 2026-07-21 | 35 |
| 33 | 2026-08-08 | 17 |
| 34 | 2026-07-02 | 54 |
| 35 | 2026-08-06 | 19 |
| 36 | 2026-08-22 | 3 |
| 37 | 2026-08-08 | 17 |
| 38 | 2026-08-20 | 5 |
| 39 | 2026-08-20 | 5 |
| 40 | 2026-08-25 | 0 |
| 41 | 2026-08-18 | 7 |
| 42 | 2026-08-13 | 12 |
| 43 | 2026-07-30 | 26 |
| 44 | 2026-08-01 | 24 |
| 45 | 2026-08-13 | 12 |
| 46 | 2026-08-13 | 12 |
| 47 | 2026-08-20 | 5 |
| 48 | 2026-08-18 | 7 |
| 49 | 2026-08-01 | 24 |
| 50 | 2026-08-15 | 10 |
| 51 | 2026-08-20 | 5 |
| 52 | 2026-06-27 | 59 |
| 53 | 2026-07-16 | 40 |
| 54 | 2026-08-04 | 21 |
| 55 | 2026-08-06 | 19 |



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

