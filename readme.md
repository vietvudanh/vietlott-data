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
| Power 655 | 1388 | 2017-08-01 | 2026-08-22 | 1388 | 00001 | 01388 |
| Power 645 | 1356 | 2017-10-25 | 2026-08-23 | 1356 | 00198 | 01553 |
| Power 535 | 386 | 2025-06-29 | 2026-08-24 | 770 | 00001 | 00844 |
| Keno | 655 | 2022-12-04 | 2026-08-25 | 82070 | #0110271 | #0293281 |
| 3D | 1119 | 2019-04-22 | 2026-08-24 | 1119 | 00001 | 01123 |
| 3D Pro | 765 | 2021-09-14 | 2026-08-22 | 765 | 00001 | 00769 |
| Bingo18 | 629 | 2024-12-03 | 2026-08-25 | 87352 | 0083123 | 0183237 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8] | 2026-08-23T00:01:15.219616 |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47] | 2026-08-21T00:01:21.664308 |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30] | 2026-08-19T00:01:15.794745 |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42] | 2026-08-16T11:07:54.647468 |
| 2026-08-11 | 01383 | [2, 7, 19, 20, 39, 50, 31] | 2026-08-12T00:02:10.803156 |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37] | 2026-08-09T00:01:07.514841 |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1] | 2026-08-07T00:01:13.032397 |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] | 2026-08-06T00:02:27.504833 |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] | 2026-08-02T00:01:09.345245 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 186 | 1.91 |  | 21 | 173 | 1.78 |  | 41 | 205 | 2.11 |
| 2 | 161 | 1.66 |  | 22 | 206 | 2.12 |  | 42 | 180 | 1.85 |
| 3 | 188 | 1.94 |  | 23 | 187 | 1.92 |  | 43 | 198 | 2.04 |
| 4 | 144 | 1.48 |  | 24 | 176 | 1.81 |  | 44 | 180 | 1.85 |
| 5 | 180 | 1.85 |  | 25 | 159 | 1.64 |  | 45 | 179 | 1.84 |
| 6 | 143 | 1.47 |  | 26 | 165 | 1.7 |  | 46 | 181 | 1.86 |
| 7 | 156 | 1.61 |  | 27 | 162 | 1.67 |  | 47 | 176 | 1.81 |
| 8 | 194 | 2.0 |  | 28 | 158 | 1.63 |  | 48 | 190 | 1.96 |
| 9 | 193 | 1.99 |  | 29 | 190 | 1.96 |  | 49 | 173 | 1.78 |
| 10 | 164 | 1.69 |  | 30 | 162 | 1.67 |  | 50 | 177 | 1.82 |
| 11 | 179 | 1.84 |  | 31 | 185 | 1.9 |  | 51 | 197 | 2.03 |
| 12 | 180 | 1.85 |  | 32 | 186 | 1.91 |  | 52 | 177 | 1.82 |
| 13 | 172 | 1.77 |  | 33 | 179 | 1.84 |  | 53 | 187 | 1.92 |
| 14 | 177 | 1.82 |  | 34 | 195 | 2.01 |  | 54 | 167 | 1.72 |
| 15 | 165 | 1.7 |  | 35 | 170 | 1.75 |  | 55 | 178 | 1.83 |
| 16 | 174 | 1.79 |  | 36 | 167 | 1.72 |  |  |  |  |
| 17 | 159 | 1.64 |  | 37 | 158 | 1.63 |  |  |  |  |
| 18 | 177 | 1.82 |  | 38 | 172 | 1.77 |  |  |  |  |
| 19 | 174 | 1.79 |  | 39 | 172 | 1.77 |  |  |  |  |
| 20 | 189 | 1.95 |  | 40 | 193 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.19 |  | 27 | 3 | 3.57 |  | 49 | 2 | 2.38 |
| 2 | 4 | 4.76 |  | 28 | 1 | 1.19 |  | 50 | 2 | 2.38 |
| 3 | 1 | 1.19 |  | 29 | 3 | 3.57 |  | 51 | 3 | 3.57 |
| 5 | 2 | 2.38 |  | 30 | 2 | 2.38 |  | 54 | 1 | 1.19 |
| 7 | 2 | 2.38 |  | 31 | 2 | 2.38 |  | 55 | 2 | 2.38 |
| 8 | 2 | 2.38 |  | 33 | 1 | 1.19 |  |  |  |  |
| 9 | 2 | 2.38 |  | 35 | 1 | 1.19 |  |  |  |  |
| 11 | 1 | 1.19 |  | 36 | 1 | 1.19 |  |  |  |  |
| 12 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 14 | 3 | 3.57 |  | 38 | 3 | 3.57 |  |  |  |  |
| 15 | 1 | 1.19 |  | 39 | 4 | 4.76 |  |  |  |  |
| 16 | 2 | 2.38 |  | 40 | 2 | 2.38 |  |  |  |  |
| 18 | 3 | 3.57 |  | 41 | 2 | 2.38 |  |  |  |  |
| 19 | 2 | 2.38 |  | 42 | 2 | 2.38 |  |  |  |  |
| 20 | 2 | 2.38 |  | 43 | 1 | 1.19 |  |  |  |  |
| 21 | 1 | 1.19 |  | 44 | 2 | 2.38 |  |  |  |  |
| 22 | 1 | 1.19 |  | 45 | 2 | 2.38 |  |  |  |  |
| 23 | 2 | 2.38 |  | 46 | 1 | 1.19 |  |  |  |  |
| 24 | 1 | 1.19 |  | 47 | 2 | 2.38 |  |  |  |  |
| 25 | 2 | 2.38 |  | 48 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.14 |  | 21 | 3 | 1.71 |  | 42 | 4 | 2.29 |
| 2 | 5 | 2.86 |  | 22 | 4 | 2.29 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 23 | 4 | 2.29 |  | 44 | 4 | 2.29 |
| 4 | 1 | 0.57 |  | 24 | 3 | 1.71 |  | 45 | 6 | 3.43 |
| 5 | 5 | 2.86 |  | 25 | 3 | 1.71 |  | 46 | 1 | 0.57 |
| 6 | 1 | 0.57 |  | 27 | 4 | 2.29 |  | 47 | 3 | 1.71 |
| 7 | 3 | 1.71 |  | 28 | 3 | 1.71 |  | 48 | 5 | 2.86 |
| 8 | 5 | 2.86 |  | 29 | 3 | 1.71 |  | 49 | 4 | 2.29 |
| 9 | 5 | 2.86 |  | 30 | 3 | 1.71 |  | 50 | 3 | 1.71 |
| 10 | 2 | 1.14 |  | 31 | 3 | 1.71 |  | 51 | 4 | 2.29 |
| 11 | 3 | 1.71 |  | 32 | 2 | 1.14 |  | 52 | 1 | 0.57 |
| 12 | 1 | 0.57 |  | 33 | 6 | 3.43 |  | 53 | 1 | 0.57 |
| 13 | 3 | 1.71 |  | 34 | 1 | 0.57 |  | 54 | 3 | 1.71 |
| 14 | 4 | 2.29 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 15 | 2 | 1.14 |  | 36 | 2 | 1.14 |  |  |  |  |
| 16 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 17 | 2 | 1.14 |  | 38 | 4 | 2.29 |  |  |  |  |
| 18 | 5 | 2.86 |  | 39 | 5 | 2.86 |  |  |  |  |
| 19 | 3 | 1.71 |  | 40 | 4 | 2.29 |  |  |  |  |
| 20 | 4 | 2.29 |  | 41 | 6 | 3.43 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 4 | 1.5 |  | 41 | 7 | 2.63 |
| 2 | 8 | 3.01 |  | 22 | 4 | 1.5 |  | 42 | 7 | 2.63 |
| 3 | 5 | 1.88 |  | 23 | 7 | 2.63 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 5 | 1.88 |
| 5 | 8 | 3.01 |  | 25 | 5 | 1.88 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 1 | 0.38 |  | 46 | 5 | 1.88 |
| 7 | 4 | 1.5 |  | 27 | 5 | 1.88 |  | 47 | 4 | 1.5 |
| 8 | 11 | 4.14 |  | 28 | 6 | 2.26 |  | 48 | 6 | 2.26 |
| 9 | 5 | 1.88 |  | 29 | 4 | 1.5 |  | 49 | 5 | 1.88 |
| 10 | 2 | 0.75 |  | 30 | 4 | 1.5 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 5 | 1.88 |  | 51 | 5 | 1.88 |
| 12 | 1 | 0.38 |  | 32 | 3 | 1.13 |  | 52 | 2 | 0.75 |
| 13 | 4 | 1.5 |  | 33 | 7 | 2.63 |  | 53 | 3 | 1.13 |
| 14 | 6 | 2.26 |  | 34 | 2 | 0.75 |  | 54 | 4 | 1.5 |
| 15 | 3 | 1.13 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 3 | 1.13 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 6 | 2.26 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 4 | 1.5 |  | 39 | 7 | 2.63 |  |  |  |  |
| 20 | 6 | 2.26 |  | 40 | 7 | 2.63 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 26 | 2026-06-20 | 63 |
| 52 | 2026-06-27 | 56 |
| 34 | 2026-07-02 | 51 |
| 6 | 2026-07-07 | 46 |
| 4 | 2026-07-07 | 46 |
| 17 | 2026-07-11 | 42 |
| 10 | 2026-07-14 | 39 |
| 53 | 2026-07-16 | 37 |
| 13 | 2026-07-21 | 32 |
| 32 | 2026-07-21 | 32 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-08-06 | 16 |
| 2 | 2026-08-20 | 2 |
| 3 | 2026-08-18 | 4 |
| 4 | 2026-07-07 | 46 |
| 5 | 2026-08-13 | 9 |
| 6 | 2026-07-07 | 46 |
| 7 | 2026-08-11 | 11 |
| 8 | 2026-08-22 | 0 |
| 9 | 2026-08-22 | 0 |
| 10 | 2026-07-14 | 39 |
| 11 | 2026-08-01 | 21 |
| 12 | 2026-07-30 | 23 |
| 13 | 2026-07-21 | 32 |
| 14 | 2026-08-06 | 16 |
| 15 | 2026-08-18 | 4 |
| 16 | 2026-08-15 | 7 |
| 17 | 2026-07-11 | 42 |
| 18 | 2026-08-22 | 0 |
| 19 | 2026-08-22 | 0 |
| 20 | 2026-08-15 | 7 |
| 21 | 2026-08-22 | 0 |
| 22 | 2026-07-28 | 25 |
| 23 | 2026-08-06 | 16 |
| 24 | 2026-07-30 | 23 |
| 25 | 2026-08-22 | 0 |
| 26 | 2026-06-20 | 63 |
| 27 | 2026-08-15 | 7 |
| 28 | 2026-07-30 | 23 |
| 29 | 2026-08-20 | 2 |
| 30 | 2026-08-18 | 4 |
| 31 | 2026-08-11 | 11 |
| 32 | 2026-07-21 | 32 |
| 33 | 2026-08-08 | 14 |
| 34 | 2026-07-02 | 51 |
| 35 | 2026-08-06 | 16 |
| 36 | 2026-08-22 | 0 |
| 37 | 2026-08-08 | 14 |
| 38 | 2026-08-20 | 2 |
| 39 | 2026-08-20 | 2 |
| 40 | 2026-08-08 | 14 |
| 41 | 2026-08-18 | 4 |
| 42 | 2026-08-13 | 9 |
| 43 | 2026-07-30 | 23 |
| 44 | 2026-08-01 | 21 |
| 45 | 2026-08-13 | 9 |
| 46 | 2026-08-13 | 9 |
| 47 | 2026-08-20 | 2 |
| 48 | 2026-08-18 | 4 |
| 49 | 2026-08-01 | 21 |
| 50 | 2026-08-15 | 7 |
| 51 | 2026-08-20 | 2 |
| 52 | 2026-06-27 | 56 |
| 53 | 2026-07-16 | 37 |
| 54 | 2026-08-04 | 18 |
| 55 | 2026-08-06 | 16 |



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

