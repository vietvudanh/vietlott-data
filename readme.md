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
| Power 655 | 1320 | 2017-08-01 | 2026-03-17 | 1320 | 00001 | 01320 |
| Power 645 | 1288 | 2017-10-25 | 2026-03-18 | 1288 | 00198 | 01485 |
| Power 535 | 238 | 2025-06-29 | 2026-03-18 | 476 | 00001 | 00526 |
| Keno | 489 | 2022-12-04 | 2026-03-19 | 61821 | #0110271 | #0274363 |
| 3D | 1051 | 2019-04-22 | 2026-03-18 | 1051 | 00001 | 01055 |
| 3D Pro | 697 | 2021-09-14 | 2026-03-17 | 697 | 00001 | 00701 |
| Bingo18 | 463 | 2024-12-03 | 2026-03-19 | 54571 | 0083123 | 0157970 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-03-17 | 01320 | [12, 26, 28, 43, 50, 54, 52] | 2026-03-18T00:00:56.999640 |
| 2026-03-14 | 01319 | [7, 16, 27, 29, 47, 52, 26] | 2026-03-15T00:00:52.883799 |
| 2026-03-12 | 01318 | [12, 28, 36, 40, 53, 55, 54] | 2026-03-13T00:00:57.770966 |
| 2026-03-10 | 01317 | [3, 26, 31, 39, 47, 54, 20] | 2026-03-12T00:00:58.996922 |
| 2026-03-07 | 01316 | [4, 32, 41, 45, 50, 52, 29] | 2026-03-08T00:01:04.043596 |
| 2026-03-05 | 01315 | [14, 16, 35, 38, 43, 51, 37] | 2026-03-06T00:01:02.441420 |
| 2026-03-03 | 01314 | [7, 13, 27, 29, 43, 50, 25] | 2026-03-04T00:00:55.331151 |
| 2026-02-28 | 01313 | [22, 25, 31, 44, 51, 54, 36] | 2026-03-01T00:00:58.241470 |
| 2026-02-26 | 01312 | [1, 7, 10, 21, 44, 51, 46] | 2026-02-27T00:00:58.514222 |
| 2026-02-24 | 01311 | [5, 8, 18, 30, 39, 54, 51] | 2026-02-25T09:14:17.252048 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 176 | 1.9 |  | 21 | 163 | 1.76 |  | 41 | 195 | 2.11 |
| 2 | 151 | 1.63 |  | 22 | 193 | 2.09 |  | 42 | 172 | 1.86 |
| 3 | 178 | 1.93 |  | 23 | 177 | 1.92 |  | 43 | 191 | 2.07 |
| 4 | 139 | 1.5 |  | 24 | 168 | 1.82 |  | 44 | 172 | 1.86 |
| 5 | 170 | 1.84 |  | 25 | 150 | 1.62 |  | 45 | 169 | 1.83 |
| 6 | 139 | 1.5 |  | 26 | 159 | 1.72 |  | 46 | 173 | 1.87 |
| 7 | 146 | 1.58 |  | 27 | 156 | 1.69 |  | 47 | 167 | 1.81 |
| 8 | 179 | 1.94 |  | 28 | 148 | 1.6 |  | 48 | 181 | 1.96 |
| 9 | 182 | 1.97 |  | 29 | 181 | 1.96 |  | 49 | 166 | 1.8 |
| 10 | 158 | 1.71 |  | 30 | 154 | 1.67 |  | 50 | 168 | 1.82 |
| 11 | 172 | 1.86 |  | 31 | 177 | 1.92 |  | 51 | 189 | 2.05 |
| 12 | 177 | 1.92 |  | 32 | 176 | 1.9 |  | 52 | 172 | 1.86 |
| 13 | 164 | 1.78 |  | 33 | 168 | 1.82 |  | 53 | 175 | 1.89 |
| 14 | 169 | 1.83 |  | 34 | 187 | 2.02 |  | 54 | 162 | 1.75 |
| 15 | 156 | 1.69 |  | 35 | 164 | 1.78 |  | 55 | 168 | 1.82 |
| 16 | 161 | 1.74 |  | 36 | 160 | 1.73 |  |  |  |  |
| 17 | 151 | 1.63 |  | 37 | 152 | 1.65 |  |  |  |  |
| 18 | 169 | 1.83 |  | 38 | 161 | 1.74 |  |  |  |  |
| 19 | 167 | 1.81 |  | 39 | 158 | 1.71 |  |  |  |  |
| 20 | 181 | 1.96 |  | 40 | 182 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 30 | 3 | 3.57 |  | 54 | 5 | 5.95 |
| 3 | 1 | 1.19 |  | 31 | 2 | 2.38 |  | 55 | 1 | 1.19 |
| 4 | 1 | 1.19 |  | 32 | 1 | 1.19 |  |  |  |  |
| 5 | 2 | 2.38 |  | 35 | 1 | 1.19 |  |  |  |  |
| 7 | 4 | 4.76 |  | 36 | 2 | 2.38 |  |  |  |  |
| 8 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 10 | 1 | 1.19 |  | 38 | 1 | 1.19 |  |  |  |  |
| 12 | 3 | 3.57 |  | 39 | 2 | 2.38 |  |  |  |  |
| 13 | 1 | 1.19 |  | 40 | 1 | 1.19 |  |  |  |  |
| 14 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 16 | 2 | 2.38 |  | 43 | 4 | 4.76 |  |  |  |  |
| 18 | 1 | 1.19 |  | 44 | 2 | 2.38 |  |  |  |  |
| 20 | 1 | 1.19 |  | 45 | 3 | 3.57 |  |  |  |  |
| 21 | 1 | 1.19 |  | 46 | 2 | 2.38 |  |  |  |  |
| 22 | 1 | 1.19 |  | 47 | 2 | 2.38 |  |  |  |  |
| 25 | 2 | 2.38 |  | 48 | 1 | 1.19 |  |  |  |  |
| 26 | 4 | 4.76 |  | 50 | 3 | 3.57 |  |  |  |  |
| 27 | 3 | 3.57 |  | 51 | 4 | 4.76 |  |  |  |  |
| 28 | 2 | 2.38 |  | 52 | 3 | 3.57 |  |  |  |  |
| 29 | 3 | 3.57 |  | 53 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.79 |  | 22 | 5 | 2.98 |  | 44 | 2 | 1.19 |
| 2 | 2 | 1.19 |  | 24 | 1 | 0.6 |  | 45 | 4 | 2.38 |
| 3 | 2 | 1.19 |  | 25 | 4 | 2.38 |  | 46 | 4 | 2.38 |
| 4 | 3 | 1.79 |  | 26 | 9 | 5.36 |  | 47 | 2 | 1.19 |
| 5 | 4 | 2.38 |  | 27 | 3 | 1.79 |  | 48 | 3 | 1.79 |
| 7 | 5 | 2.98 |  | 28 | 4 | 2.38 |  | 49 | 1 | 0.6 |
| 8 | 2 | 1.19 |  | 29 | 6 | 3.57 |  | 50 | 4 | 2.38 |
| 9 | 1 | 0.6 |  | 30 | 4 | 2.38 |  | 51 | 4 | 2.38 |
| 10 | 2 | 1.19 |  | 31 | 3 | 1.79 |  | 52 | 3 | 1.79 |
| 11 | 2 | 1.19 |  | 32 | 7 | 4.17 |  | 53 | 5 | 2.98 |
| 12 | 4 | 2.38 |  | 34 | 1 | 0.6 |  | 54 | 7 | 4.17 |
| 13 | 6 | 3.57 |  | 35 | 2 | 1.19 |  | 55 | 3 | 1.79 |
| 14 | 3 | 1.79 |  | 36 | 4 | 2.38 |  |  |  |  |
| 15 | 3 | 1.79 |  | 37 | 2 | 1.19 |  |  |  |  |
| 16 | 3 | 1.79 |  | 38 | 1 | 0.6 |  |  |  |  |
| 17 | 2 | 1.19 |  | 39 | 2 | 1.19 |  |  |  |  |
| 18 | 3 | 1.79 |  | 40 | 1 | 0.6 |  |  |  |  |
| 19 | 1 | 0.6 |  | 41 | 3 | 1.79 |  |  |  |  |
| 20 | 4 | 2.38 |  | 42 | 2 | 1.19 |  |  |  |  |
| 21 | 3 | 1.79 |  | 43 | 4 | 2.38 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.16 |  | 21 | 6 | 2.32 |  | 41 | 5 | 1.93 |
| 2 | 3 | 1.16 |  | 22 | 8 | 3.09 |  | 42 | 4 | 1.54 |
| 3 | 4 | 1.54 |  | 23 | 3 | 1.16 |  | 43 | 6 | 2.32 |
| 4 | 4 | 1.54 |  | 24 | 1 | 0.39 |  | 44 | 2 | 0.77 |
| 5 | 5 | 1.93 |  | 25 | 7 | 2.7 |  | 45 | 5 | 1.93 |
| 6 | 1 | 0.39 |  | 26 | 9 | 3.47 |  | 46 | 5 | 1.93 |
| 7 | 5 | 1.93 |  | 27 | 4 | 1.54 |  | 47 | 4 | 1.54 |
| 8 | 2 | 0.77 |  | 28 | 5 | 1.93 |  | 48 | 7 | 2.7 |
| 9 | 2 | 0.77 |  | 29 | 8 | 3.09 |  | 49 | 2 | 0.77 |
| 10 | 4 | 1.54 |  | 30 | 8 | 3.09 |  | 50 | 5 | 1.93 |
| 11 | 3 | 1.16 |  | 31 | 4 | 1.54 |  | 51 | 5 | 1.93 |
| 12 | 5 | 1.93 |  | 32 | 10 | 3.86 |  | 52 | 4 | 1.54 |
| 13 | 8 | 3.09 |  | 33 | 4 | 1.54 |  | 53 | 5 | 1.93 |
| 14 | 4 | 1.54 |  | 34 | 4 | 1.54 |  | 54 | 9 | 3.47 |
| 15 | 3 | 1.16 |  | 35 | 4 | 1.54 |  | 55 | 6 | 2.32 |
| 16 | 8 | 3.09 |  | 36 | 6 | 2.32 |  |  |  |  |
| 17 | 3 | 1.16 |  | 37 | 4 | 1.54 |  |  |  |  |
| 18 | 3 | 1.16 |  | 38 | 5 | 1.93 |  |  |  |  |
| 19 | 1 | 0.39 |  | 39 | 4 | 1.54 |  |  |  |  |
| 20 | 6 | 2.32 |  | 40 | 4 | 1.54 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 6 | 2025-12-25 | 82 |
| 33 | 2026-01-10 | 66 |
| 23 | 2026-01-17 | 59 |
| 24 | 2026-01-24 | 52 |
| 34 | 2026-01-29 | 47 |
| 49 | 2026-01-31 | 45 |
| 11 | 2026-01-31 | 45 |
| 9 | 2026-02-05 | 40 |
| 15 | 2026-02-07 | 38 |
| 19 | 2026-02-12 | 33 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-02-26 | 19 |
| 2 | 2026-02-14 | 31 |
| 3 | 2026-03-10 | 7 |
| 4 | 2026-03-07 | 10 |
| 5 | 2026-02-24 | 21 |
| 6 | 2025-12-25 | 82 |
| 7 | 2026-03-14 | 3 |
| 8 | 2026-02-24 | 21 |
| 9 | 2026-02-05 | 40 |
| 10 | 2026-02-26 | 19 |
| 11 | 2026-01-31 | 45 |
| 12 | 2026-03-17 | 0 |
| 13 | 2026-03-03 | 14 |
| 14 | 2026-03-05 | 12 |
| 15 | 2026-02-07 | 38 |
| 16 | 2026-03-14 | 3 |
| 17 | 2026-02-12 | 33 |
| 18 | 2026-02-24 | 21 |
| 19 | 2026-02-12 | 33 |
| 20 | 2026-03-10 | 7 |
| 21 | 2026-02-26 | 19 |
| 22 | 2026-02-28 | 17 |
| 23 | 2026-01-17 | 59 |
| 24 | 2026-01-24 | 52 |
| 25 | 2026-03-03 | 14 |
| 26 | 2026-03-17 | 0 |
| 27 | 2026-03-14 | 3 |
| 28 | 2026-03-17 | 0 |
| 29 | 2026-03-14 | 3 |
| 30 | 2026-02-24 | 21 |
| 31 | 2026-03-10 | 7 |
| 32 | 2026-03-07 | 10 |
| 33 | 2026-01-10 | 66 |
| 34 | 2026-01-29 | 47 |
| 35 | 2026-03-05 | 12 |
| 36 | 2026-03-12 | 5 |
| 37 | 2026-03-05 | 12 |
| 38 | 2026-03-05 | 12 |
| 39 | 2026-03-10 | 7 |
| 40 | 2026-03-12 | 5 |
| 41 | 2026-03-07 | 10 |
| 42 | 2026-02-14 | 31 |
| 43 | 2026-03-17 | 0 |
| 44 | 2026-02-28 | 17 |
| 45 | 2026-03-07 | 10 |
| 46 | 2026-02-26 | 19 |
| 47 | 2026-03-14 | 3 |
| 48 | 2026-02-19 | 26 |
| 49 | 2026-01-31 | 45 |
| 50 | 2026-03-17 | 0 |
| 51 | 2026-03-05 | 12 |
| 52 | 2026-03-17 | 0 |
| 53 | 2026-03-12 | 5 |
| 54 | 2026-03-17 | 0 |
| 55 | 2026-03-12 | 5 |



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

