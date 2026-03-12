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
| Power 655 | 1317 | 2017-08-01 | 2026-03-10 | 1317 | 00001 | 01317 |
| Power 645 | 1285 | 2017-10-25 | 2026-03-11 | 1285 | 00198 | 01482 |
| Power 535 | 231 | 2025-06-29 | 2026-03-11 | 462 | 00001 | 00512 |
| Keno | 481 | 2022-12-04 | 2026-03-11 | 60988 | #0110271 | #0273486 |
| 3D | 1048 | 2019-04-22 | 2026-03-11 | 1048 | 00001 | 01052 |
| 3D Pro | 694 | 2021-09-14 | 2026-03-10 | 694 | 00001 | 00698 |
| Bingo18 | 455 | 2024-12-03 | 2026-03-11 | 54408 | 0083123 | 0156797 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-03-10 | 01317 | [3, 26, 31, 39, 47, 54, 20] | 2026-03-12T00:00:58.996922 |
| 2026-03-07 | 01316 | [4, 32, 41, 45, 50, 52, 29] | 2026-03-08T00:01:04.043596 |
| 2026-03-05 | 01315 | [14, 16, 35, 38, 43, 51, 37] | 2026-03-06T00:01:02.441420 |
| 2026-03-03 | 01314 | [7, 13, 27, 29, 43, 50, 25] | 2026-03-04T00:00:55.331151 |
| 2026-02-28 | 01313 | [22, 25, 31, 44, 51, 54, 36] | 2026-03-01T00:00:58.241470 |
| 2026-02-26 | 01312 | [1, 7, 10, 21, 44, 51, 46] | 2026-02-27T00:00:58.514222 |
| 2026-02-24 | 01311 | [5, 8, 18, 30, 39, 54, 51] | 2026-02-25T09:14:17.252048 |
| 2026-02-21 | 01310 | [5, 7, 26, 30, 41, 45, 12] | 2026-02-23T00:01:21.197262 |
| 2026-02-19 | 01309 | [1, 27, 30, 43, 45, 46, 48] | 2026-02-21T00:00:56.973082 |
| 2026-02-14 | 01308 | [2, 13, 26, 32, 36, 42, 48] | 2026-02-21T00:00:56.975209 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 176 | 1.91 |  | 21 | 163 | 1.77 |  | 41 | 195 | 2.12 |
| 2 | 151 | 1.64 |  | 22 | 193 | 2.09 |  | 42 | 172 | 1.87 |
| 3 | 178 | 1.93 |  | 23 | 177 | 1.92 |  | 43 | 190 | 2.06 |
| 4 | 139 | 1.51 |  | 24 | 168 | 1.82 |  | 44 | 172 | 1.87 |
| 5 | 170 | 1.84 |  | 25 | 150 | 1.63 |  | 45 | 169 | 1.83 |
| 6 | 139 | 1.51 |  | 26 | 157 | 1.7 |  | 46 | 173 | 1.88 |
| 7 | 145 | 1.57 |  | 27 | 155 | 1.68 |  | 47 | 166 | 1.8 |
| 8 | 179 | 1.94 |  | 28 | 146 | 1.58 |  | 48 | 181 | 1.96 |
| 9 | 182 | 1.97 |  | 29 | 180 | 1.95 |  | 49 | 166 | 1.8 |
| 10 | 158 | 1.71 |  | 30 | 154 | 1.67 |  | 50 | 167 | 1.81 |
| 11 | 172 | 1.87 |  | 31 | 177 | 1.92 |  | 51 | 189 | 2.05 |
| 12 | 175 | 1.9 |  | 32 | 176 | 1.91 |  | 52 | 170 | 1.84 |
| 13 | 164 | 1.78 |  | 33 | 168 | 1.82 |  | 53 | 174 | 1.89 |
| 14 | 169 | 1.83 |  | 34 | 187 | 2.03 |  | 54 | 160 | 1.74 |
| 15 | 156 | 1.69 |  | 35 | 164 | 1.78 |  | 55 | 167 | 1.81 |
| 16 | 160 | 1.74 |  | 36 | 159 | 1.72 |  |  |  |  |
| 17 | 151 | 1.64 |  | 37 | 152 | 1.65 |  |  |  |  |
| 18 | 169 | 1.83 |  | 38 | 161 | 1.75 |  |  |  |  |
| 19 | 167 | 1.81 |  | 39 | 158 | 1.71 |  |  |  |  |
| 20 | 181 | 1.96 |  | 40 | 181 | 1.96 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 27 | 2 | 2.38 |  | 52 | 1 | 1.19 |
| 2 | 1 | 1.19 |  | 29 | 2 | 2.38 |  | 54 | 3 | 3.57 |
| 3 | 1 | 1.19 |  | 30 | 3 | 3.57 |  | 55 | 1 | 1.19 |
| 4 | 1 | 1.19 |  | 31 | 3 | 3.57 |  |  |  |  |
| 5 | 2 | 2.38 |  | 32 | 4 | 4.76 |  |  |  |  |
| 7 | 3 | 3.57 |  | 35 | 1 | 1.19 |  |  |  |  |
| 8 | 2 | 2.38 |  | 36 | 2 | 2.38 |  |  |  |  |
| 10 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 12 | 1 | 1.19 |  | 38 | 1 | 1.19 |  |  |  |  |
| 13 | 3 | 3.57 |  | 39 | 2 | 2.38 |  |  |  |  |
| 14 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 16 | 1 | 1.19 |  | 42 | 1 | 1.19 |  |  |  |  |
| 17 | 1 | 1.19 |  | 43 | 3 | 3.57 |  |  |  |  |
| 18 | 1 | 1.19 |  | 44 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 45 | 3 | 3.57 |  |  |  |  |
| 20 | 2 | 2.38 |  | 46 | 3 | 3.57 |  |  |  |  |
| 21 | 2 | 2.38 |  | 47 | 1 | 1.19 |  |  |  |  |
| 22 | 2 | 2.38 |  | 48 | 2 | 2.38 |  |  |  |  |
| 25 | 2 | 2.38 |  | 50 | 2 | 2.38 |  |  |  |  |
| 26 | 5 | 5.95 |  | 51 | 4 | 4.76 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.79 |  | 22 | 5 | 2.98 |  | 44 | 2 | 1.19 |
| 2 | 2 | 1.19 |  | 23 | 1 | 0.6 |  | 45 | 4 | 2.38 |
| 3 | 3 | 1.79 |  | 24 | 1 | 0.6 |  | 46 | 5 | 2.98 |
| 4 | 3 | 1.79 |  | 25 | 6 | 3.57 |  | 47 | 1 | 0.6 |
| 5 | 4 | 2.38 |  | 26 | 7 | 4.17 |  | 48 | 5 | 2.98 |
| 7 | 4 | 2.38 |  | 27 | 3 | 1.79 |  | 49 | 1 | 0.6 |
| 8 | 2 | 1.19 |  | 28 | 2 | 1.19 |  | 50 | 3 | 1.79 |
| 9 | 1 | 0.6 |  | 29 | 5 | 2.98 |  | 51 | 5 | 2.98 |
| 10 | 2 | 1.19 |  | 30 | 4 | 2.38 |  | 52 | 2 | 1.19 |
| 11 | 2 | 1.19 |  | 31 | 4 | 2.38 |  | 53 | 4 | 2.38 |
| 12 | 3 | 1.79 |  | 32 | 7 | 4.17 |  | 54 | 6 | 3.57 |
| 13 | 7 | 4.17 |  | 34 | 2 | 1.19 |  | 55 | 4 | 2.38 |
| 14 | 4 | 2.38 |  | 35 | 2 | 1.19 |  |  |  |  |
| 15 | 3 | 1.79 |  | 36 | 3 | 1.79 |  |  |  |  |
| 16 | 2 | 1.19 |  | 37 | 2 | 1.19 |  |  |  |  |
| 17 | 2 | 1.19 |  | 38 | 1 | 0.6 |  |  |  |  |
| 18 | 3 | 1.79 |  | 39 | 2 | 1.19 |  |  |  |  |
| 19 | 1 | 0.6 |  | 41 | 3 | 1.79 |  |  |  |  |
| 20 | 4 | 2.38 |  | 42 | 2 | 1.19 |  |  |  |  |
| 21 | 5 | 2.98 |  | 43 | 4 | 2.38 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.16 |  | 21 | 6 | 2.32 |  | 41 | 5 | 1.93 |
| 2 | 3 | 1.16 |  | 22 | 8 | 3.09 |  | 42 | 4 | 1.54 |
| 3 | 4 | 1.54 |  | 23 | 3 | 1.16 |  | 43 | 5 | 1.93 |
| 4 | 4 | 1.54 |  | 24 | 1 | 0.39 |  | 44 | 2 | 0.77 |
| 5 | 6 | 2.32 |  | 25 | 7 | 2.7 |  | 45 | 5 | 1.93 |
| 6 | 1 | 0.39 |  | 26 | 7 | 2.7 |  | 46 | 6 | 2.32 |
| 7 | 5 | 1.93 |  | 27 | 3 | 1.16 |  | 47 | 3 | 1.16 |
| 8 | 3 | 1.16 |  | 28 | 3 | 1.16 |  | 48 | 7 | 2.7 |
| 9 | 2 | 0.77 |  | 29 | 8 | 3.09 |  | 49 | 2 | 0.77 |
| 10 | 4 | 1.54 |  | 30 | 9 | 3.47 |  | 50 | 5 | 1.93 |
| 11 | 3 | 1.16 |  | 31 | 4 | 1.54 |  | 51 | 5 | 1.93 |
| 12 | 5 | 1.93 |  | 32 | 10 | 3.86 |  | 52 | 4 | 1.54 |
| 13 | 8 | 3.09 |  | 33 | 4 | 1.54 |  | 53 | 4 | 1.54 |
| 14 | 5 | 1.93 |  | 34 | 4 | 1.54 |  | 54 | 7 | 2.7 |
| 15 | 3 | 1.16 |  | 35 | 4 | 1.54 |  | 55 | 7 | 2.7 |
| 16 | 7 | 2.7 |  | 36 | 6 | 2.32 |  |  |  |  |
| 17 | 3 | 1.16 |  | 37 | 5 | 1.93 |  |  |  |  |
| 18 | 4 | 1.54 |  | 38 | 7 | 2.7 |  |  |  |  |
| 19 | 1 | 0.39 |  | 39 | 5 | 1.93 |  |  |  |  |
| 20 | 7 | 2.7 |  | 40 | 3 | 1.16 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 6 | 2025-12-25 | 68 |
| 40 | 2025-12-27 | 66 |
| 47 | 2026-01-08 | 54 |
| 33 | 2026-01-10 | 52 |
| 38 | 2026-01-10 | 52 |
| 52 | 2026-01-13 | 49 |
| 23 | 2026-01-17 | 45 |
| 37 | 2026-01-20 | 42 |
| 24 | 2026-01-24 | 38 |
| 35 | 2026-01-24 | 38 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-02-26 | 5 |
| 2 | 2026-02-14 | 17 |
| 3 | 2026-02-07 | 24 |
| 4 | 2026-01-31 | 31 |
| 5 | 2026-02-24 | 7 |
| 6 | 2025-12-25 | 68 |
| 7 | 2026-03-03 | 0 |
| 8 | 2026-02-24 | 7 |
| 9 | 2026-02-05 | 26 |
| 10 | 2026-02-26 | 5 |
| 11 | 2026-01-31 | 31 |
| 12 | 2026-02-21 | 10 |
| 13 | 2026-03-03 | 0 |
| 14 | 2026-01-31 | 31 |
| 15 | 2026-02-07 | 24 |
| 16 | 2026-02-05 | 26 |
| 17 | 2026-02-12 | 19 |
| 18 | 2026-02-24 | 7 |
| 19 | 2026-02-12 | 19 |
| 20 | 2026-02-10 | 21 |
| 21 | 2026-02-26 | 5 |
| 22 | 2026-02-28 | 3 |
| 23 | 2026-01-17 | 45 |
| 24 | 2026-01-24 | 38 |
| 25 | 2026-03-03 | 0 |
| 26 | 2026-02-21 | 10 |
| 27 | 2026-03-03 | 0 |
| 28 | 2026-01-29 | 33 |
| 29 | 2026-03-03 | 0 |
| 30 | 2026-02-24 | 7 |
| 31 | 2026-02-28 | 3 |
| 32 | 2026-02-14 | 17 |
| 33 | 2026-01-10 | 52 |
| 34 | 2026-01-29 | 33 |
| 35 | 2026-01-24 | 38 |
| 36 | 2026-02-28 | 3 |
| 37 | 2026-01-20 | 42 |
| 38 | 2026-01-10 | 52 |
| 39 | 2026-02-24 | 7 |
| 40 | 2025-12-27 | 66 |
| 41 | 2026-02-21 | 10 |
| 42 | 2026-02-14 | 17 |
| 43 | 2026-03-03 | 0 |
| 44 | 2026-02-28 | 3 |
| 45 | 2026-02-21 | 10 |
| 46 | 2026-02-26 | 5 |
| 47 | 2026-01-08 | 54 |
| 48 | 2026-02-19 | 12 |
| 49 | 2026-01-31 | 31 |
| 50 | 2026-03-03 | 0 |
| 51 | 2026-02-28 | 3 |
| 52 | 2026-01-13 | 49 |
| 53 | 2026-02-03 | 28 |
| 54 | 2026-02-28 | 3 |
| 55 | 2026-02-10 | 21 |



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

