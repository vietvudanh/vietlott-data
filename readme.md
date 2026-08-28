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
| Power 655 | 1390 | 2017-08-01 | 2026-08-27 | 1390 | 00001 | 01390 |
| Power 645 | 1358 | 2017-10-25 | 2026-08-28 | 1358 | 00198 | 01555 |
| Power 535 | 390 | 2025-06-29 | 2026-08-28 | 778 | 00001 | 00852 |
| Keno | 658 | 2022-12-04 | 2026-08-28 | 82502 | #0110271 | #0293713 |
| 3D | 1121 | 2019-04-22 | 2026-08-28 | 1121 | 00001 | 01125 |
| 3D Pro | 767 | 2021-09-14 | 2026-08-27 | 767 | 00001 | 00771 |
| Bingo18 | 632 | 2024-12-03 | 2026-08-28 | 87889 | 0083123 | 0183813 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10] | 2026-08-28T00:01:17.809418 |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14] | 2026-08-26T00:01:20.568482 |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42] | 2026-08-16T11:07:54.647468 |
| 2026-08-11 | 01383 | [2, 7, 19, 20, 39, 50, 31] | 2026-08-12T00:02:10.803156 |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37] | 2026-08-09T00:01:07.514841 |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1] | 2026-08-07T00:01:13.032397 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 187 | 1.92 |  | 21 | 174 | 1.79 |  | 41 | 205 | 2.11 |
| 2 | 161 | 1.65 |  | 22 | 206 | 2.12 |  | 42 | 180 | 1.85 |
| 3 | 189 | 1.94 |  | 23 | 187 | 1.92 |  | 43 | 198 | 2.04 |
| 4 | 144 | 1.48 |  | 24 | 176 | 1.81 |  | 44 | 181 | 1.86 |
| 5 | 181 | 1.86 |  | 25 | 159 | 1.63 |  | 45 | 179 | 1.84 |
| 6 | 143 | 1.47 |  | 26 | 166 | 1.71 |  | 46 | 181 | 1.86 |
| 7 | 157 | 1.61 |  | 27 | 162 | 1.67 |  | 47 | 176 | 1.81 |
| 8 | 194 | 1.99 |  | 28 | 158 | 1.62 |  | 48 | 190 | 1.95 |
| 9 | 193 | 1.98 |  | 29 | 190 | 1.95 |  | 49 | 173 | 1.78 |
| 10 | 165 | 1.7 |  | 30 | 162 | 1.67 |  | 50 | 177 | 1.82 |
| 11 | 180 | 1.85 |  | 31 | 186 | 1.91 |  | 51 | 197 | 2.02 |
| 12 | 180 | 1.85 |  | 32 | 186 | 1.91 |  | 52 | 177 | 1.82 |
| 13 | 173 | 1.78 |  | 33 | 179 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 178 | 1.83 |  | 34 | 195 | 2.0 |  | 54 | 167 | 1.72 |
| 15 | 165 | 1.7 |  | 35 | 170 | 1.75 |  | 55 | 178 | 1.83 |
| 16 | 174 | 1.79 |  | 36 | 167 | 1.72 |  |  |  |  |
| 17 | 159 | 1.63 |  | 37 | 158 | 1.62 |  |  |  |  |
| 18 | 178 | 1.83 |  | 38 | 172 | 1.77 |  |  |  |  |
| 19 | 174 | 1.79 |  | 39 | 172 | 1.77 |  |  |  |  |
| 20 | 189 | 1.94 |  | 40 | 194 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 25 | 2 | 2.2 |  | 47 | 2 | 2.2 |
| 2 | 4 | 4.4 |  | 26 | 1 | 1.1 |  | 48 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 27 | 2 | 2.2 |  | 49 | 2 | 2.2 |
| 5 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 7 | 2 | 2.2 |  | 29 | 3 | 3.3 |  | 51 | 3 | 3.3 |
| 8 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 9 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 55 | 2 | 2.2 |
| 10 | 1 | 1.1 |  | 33 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 14 | 4 | 4.4 |  | 38 | 3 | 3.3 |  |  |  |  |
| 15 | 1 | 1.1 |  | 39 | 4 | 4.4 |  |  |  |  |
| 16 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 18 | 4 | 4.4 |  | 41 | 1 | 1.1 |  |  |  |  |
| 19 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 23 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 24 | 1 | 1.1 |  | 46 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.65 |  | 21 | 3 | 1.65 |  | 41 | 6 | 3.3 |
| 2 | 5 | 2.75 |  | 22 | 4 | 2.2 |  | 42 | 4 | 2.2 |
| 3 | 3 | 1.65 |  | 23 | 3 | 1.65 |  | 43 | 3 | 1.65 |
| 4 | 1 | 0.55 |  | 24 | 3 | 1.65 |  | 44 | 5 | 2.75 |
| 5 | 6 | 3.3 |  | 25 | 3 | 1.65 |  | 45 | 6 | 3.3 |
| 6 | 1 | 0.55 |  | 26 | 1 | 0.55 |  | 46 | 1 | 0.55 |
| 7 | 3 | 1.65 |  | 27 | 4 | 2.2 |  | 47 | 3 | 1.65 |
| 8 | 5 | 2.75 |  | 28 | 2 | 1.1 |  | 48 | 5 | 2.75 |
| 9 | 5 | 2.75 |  | 29 | 3 | 1.65 |  | 49 | 4 | 2.2 |
| 10 | 3 | 1.65 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 11 | 4 | 2.2 |  | 31 | 4 | 2.2 |  | 51 | 4 | 2.2 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 53 | 1 | 0.55 |
| 13 | 4 | 2.2 |  | 33 | 6 | 3.3 |  | 54 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 55 | 4 | 2.2 |
| 15 | 2 | 1.1 |  | 35 | 2 | 1.1 |  |  |  |  |
| 16 | 3 | 1.65 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 6 | 3.3 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 4 | 2.2 |  | 40 | 5 | 2.75 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 4 | 1.5 |  | 41 | 7 | 2.63 |
| 2 | 7 | 2.63 |  | 22 | 4 | 1.5 |  | 42 | 6 | 2.26 |
| 3 | 6 | 2.26 |  | 23 | 7 | 2.63 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 5 | 1.88 |  | 44 | 5 | 1.88 |
| 5 | 9 | 3.38 |  | 25 | 3 | 1.13 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 2 | 0.75 |  | 46 | 5 | 1.88 |
| 7 | 5 | 1.88 |  | 27 | 5 | 1.88 |  | 47 | 4 | 1.5 |
| 8 | 9 | 3.38 |  | 28 | 6 | 2.26 |  | 48 | 6 | 2.26 |
| 9 | 5 | 1.88 |  | 29 | 4 | 1.5 |  | 49 | 5 | 1.88 |
| 10 | 3 | 1.13 |  | 30 | 4 | 1.5 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 5 | 1.88 |  | 51 | 5 | 1.88 |
| 12 | 1 | 0.38 |  | 32 | 3 | 1.13 |  | 52 | 2 | 0.75 |
| 13 | 5 | 1.88 |  | 33 | 7 | 2.63 |  | 53 | 2 | 0.75 |
| 14 | 7 | 2.63 |  | 34 | 2 | 0.75 |  | 54 | 3 | 1.13 |
| 15 | 3 | 1.13 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 3 | 1.13 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 7 | 2.63 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 4 | 1.5 |  | 39 | 7 | 2.63 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 8 | 3.01 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-06-27 | 61 |
| 34 | 2026-07-02 | 56 |
| 6 | 2026-07-07 | 51 |
| 4 | 2026-07-07 | 51 |
| 17 | 2026-07-11 | 47 |
| 53 | 2026-07-16 | 42 |
| 32 | 2026-07-21 | 37 |
| 22 | 2026-07-28 | 30 |
| 24 | 2026-07-30 | 28 |
| 12 | 2026-07-30 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-08-27 | 0 |
| 2 | 2026-08-20 | 7 |
| 3 | 2026-08-27 | 0 |
| 4 | 2026-07-07 | 51 |
| 5 | 2026-08-25 | 2 |
| 6 | 2026-07-07 | 51 |
| 7 | 2026-08-25 | 2 |
| 8 | 2026-08-22 | 5 |
| 9 | 2026-08-22 | 5 |
| 10 | 2026-08-27 | 0 |
| 11 | 2026-08-27 | 0 |
| 12 | 2026-07-30 | 28 |
| 13 | 2026-08-25 | 2 |
| 14 | 2026-08-25 | 2 |
| 15 | 2026-08-18 | 9 |
| 16 | 2026-08-15 | 12 |
| 17 | 2026-07-11 | 47 |
| 18 | 2026-08-25 | 2 |
| 19 | 2026-08-22 | 5 |
| 20 | 2026-08-15 | 12 |
| 21 | 2026-08-27 | 0 |
| 22 | 2026-07-28 | 30 |
| 23 | 2026-08-06 | 21 |
| 24 | 2026-07-30 | 28 |
| 25 | 2026-08-22 | 5 |
| 26 | 2026-08-27 | 0 |
| 27 | 2026-08-15 | 12 |
| 28 | 2026-07-30 | 28 |
| 29 | 2026-08-20 | 7 |
| 30 | 2026-08-18 | 9 |
| 31 | 2026-08-25 | 2 |
| 32 | 2026-07-21 | 37 |
| 33 | 2026-08-08 | 19 |
| 34 | 2026-07-02 | 56 |
| 35 | 2026-08-06 | 21 |
| 36 | 2026-08-22 | 5 |
| 37 | 2026-08-08 | 19 |
| 38 | 2026-08-20 | 7 |
| 39 | 2026-08-20 | 7 |
| 40 | 2026-08-25 | 2 |
| 41 | 2026-08-18 | 9 |
| 42 | 2026-08-13 | 14 |
| 43 | 2026-07-30 | 28 |
| 44 | 2026-08-27 | 0 |
| 45 | 2026-08-13 | 14 |
| 46 | 2026-08-13 | 14 |
| 47 | 2026-08-20 | 7 |
| 48 | 2026-08-18 | 9 |
| 49 | 2026-08-01 | 26 |
| 50 | 2026-08-15 | 12 |
| 51 | 2026-08-20 | 7 |
| 52 | 2026-06-27 | 61 |
| 53 | 2026-07-16 | 42 |
| 54 | 2026-08-04 | 23 |
| 55 | 2026-08-06 | 21 |



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

