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
| Power 655 | 1367 | 2017-08-01 | 2026-07-04 | 1367 | 00001 | 01367 |
| Power 645 | 1335 | 2017-10-25 | 2026-07-05 | 1335 | 00198 | 01532 |
| Power 535 | 336 | 2025-06-29 | 2026-07-06 | 670 | 00001 | 00746 |
| Keno | 600 | 2022-12-04 | 2026-07-07 | 75474 | #0110271 | #0287450 |
| 3D | 1098 | 2019-04-22 | 2026-07-06 | 1098 | 00001 | 01102 |
| 3D Pro | 744 | 2021-09-14 | 2026-07-04 | 744 | 00001 | 00748 |
| Bingo18 | 580 | 2024-12-03 | 2026-07-07 | 79564 | 0083123 | 0175446 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54] | 2026-07-04T17:51:54.286368 |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23] | 2026-07-04T17:51:54.288114 |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5] | 2026-06-24T00:01:16.333044 |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53, 46] | 2026-06-21T00:01:15.642578 |
| 2026-06-18 | 01360 | [1, 4, 14, 20, 46, 49, 36] | 2026-06-19T00:01:20.356025 |
| 2026-06-16 | 01359 | [2, 4, 5, 7, 31, 40, 14] | 2026-06-17T00:01:06.923555 |
| 2026-06-13 | 01358 | [2, 8, 19, 33, 36, 47, 42] | 2026-06-14T00:01:35.675726 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.92 |  | 21 | 171 | 1.79 |  | 41 | 201 | 2.1 |
| 2 | 156 | 1.63 |  | 22 | 203 | 2.12 |  | 42 | 177 | 1.85 |
| 3 | 186 | 1.94 |  | 23 | 185 | 1.93 |  | 43 | 197 | 2.06 |
| 4 | 143 | 1.49 |  | 24 | 173 | 1.81 |  | 44 | 177 | 1.85 |
| 5 | 177 | 1.85 |  | 25 | 156 | 1.63 |  | 45 | 173 | 1.81 |
| 6 | 142 | 1.48 |  | 26 | 165 | 1.72 |  | 46 | 180 | 1.88 |
| 7 | 154 | 1.61 |  | 27 | 158 | 1.65 |  | 47 | 174 | 1.82 |
| 8 | 189 | 1.98 |  | 28 | 157 | 1.64 |  | 48 | 185 | 1.93 |
| 9 | 188 | 1.96 |  | 29 | 187 | 1.95 |  | 49 | 170 | 1.78 |
| 10 | 162 | 1.69 |  | 30 | 159 | 1.66 |  | 50 | 174 | 1.82 |
| 11 | 177 | 1.85 |  | 31 | 183 | 1.91 |  | 51 | 193 | 2.02 |
| 12 | 179 | 1.87 |  | 32 | 184 | 1.92 |  | 52 | 177 | 1.85 |
| 13 | 171 | 1.79 |  | 33 | 173 | 1.81 |  | 53 | 186 | 1.94 |
| 14 | 173 | 1.81 |  | 34 | 195 | 2.04 |  | 54 | 165 | 1.72 |
| 15 | 164 | 1.71 |  | 35 | 168 | 1.76 |  | 55 | 174 | 1.82 |
| 16 | 171 | 1.79 |  | 36 | 165 | 1.72 |  |  |  |  |
| 17 | 157 | 1.64 |  | 37 | 156 | 1.63 |  |  |  |  |
| 18 | 174 | 1.82 |  | 38 | 168 | 1.76 |  |  |  |  |
| 19 | 171 | 1.79 |  | 39 | 167 | 1.75 |  |  |  |  |
| 20 | 185 | 1.93 |  | 40 | 189 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 4.76 |  | 24 | 1 | 1.19 |  | 49 | 2 | 2.38 |
| 2 | 2 | 2.38 |  | 26 | 1 | 1.19 |  | 52 | 2 | 2.38 |
| 3 | 1 | 1.19 |  | 27 | 1 | 1.19 |  | 53 | 1 | 1.19 |
| 4 | 2 | 2.38 |  | 28 | 3 | 3.57 |  | 54 | 1 | 1.19 |
| 5 | 4 | 4.76 |  | 30 | 1 | 1.19 |  | 55 | 1 | 1.19 |
| 6 | 1 | 1.19 |  | 31 | 2 | 2.38 |  |  |  |  |
| 7 | 2 | 2.38 |  | 32 | 1 | 1.19 |  |  |  |  |
| 8 | 4 | 4.76 |  | 33 | 1 | 1.19 |  |  |  |  |
| 11 | 1 | 1.19 |  | 34 | 2 | 2.38 |  |  |  |  |
| 13 | 3 | 3.57 |  | 35 | 2 | 2.38 |  |  |  |  |
| 14 | 2 | 2.38 |  | 36 | 2 | 2.38 |  |  |  |  |
| 15 | 2 | 2.38 |  | 38 | 1 | 1.19 |  |  |  |  |
| 16 | 2 | 2.38 |  | 40 | 3 | 3.57 |  |  |  |  |
| 17 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 18 | 3 | 3.57 |  | 42 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 43 | 2 | 2.38 |  |  |  |  |
| 20 | 1 | 1.19 |  | 44 | 1 | 1.19 |  |  |  |  |
| 21 | 1 | 1.19 |  | 46 | 4 | 4.76 |  |  |  |  |
| 22 | 1 | 1.19 |  | 47 | 2 | 2.38 |  |  |  |  |
| 23 | 4 | 4.76 |  | 48 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.43 |  | 22 | 3 | 1.71 |  | 42 | 4 | 2.29 |
| 2 | 4 | 2.29 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 3 | 5 | 2.86 |  | 24 | 3 | 1.71 |  | 44 | 2 | 1.14 |
| 4 | 2 | 1.14 |  | 25 | 3 | 1.71 |  | 45 | 3 | 1.71 |
| 5 | 5 | 2.86 |  | 26 | 3 | 1.71 |  | 46 | 5 | 2.86 |
| 6 | 1 | 0.57 |  | 27 | 2 | 1.14 |  | 47 | 3 | 1.71 |
| 7 | 2 | 1.14 |  | 28 | 7 | 4.0 |  | 48 | 3 | 1.71 |
| 8 | 7 | 4.0 |  | 29 | 2 | 1.14 |  | 49 | 3 | 1.71 |
| 10 | 1 | 0.57 |  | 30 | 1 | 0.57 |  | 50 | 2 | 1.14 |
| 11 | 4 | 2.29 |  | 31 | 4 | 2.29 |  | 51 | 1 | 0.57 |
| 12 | 1 | 0.57 |  | 32 | 4 | 2.29 |  | 52 | 2 | 1.14 |
| 13 | 3 | 1.71 |  | 33 | 1 | 0.57 |  | 53 | 3 | 1.71 |
| 14 | 3 | 1.71 |  | 34 | 4 | 2.29 |  | 54 | 2 | 1.14 |
| 15 | 4 | 2.29 |  | 35 | 2 | 1.14 |  | 55 | 3 | 1.71 |
| 16 | 5 | 2.86 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 2 | 1.14 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 4 | 2.29 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 5 | 2.86 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 5 | 2.86 |  |  |  |  |
| 21 | 4 | 2.29 |  | 41 | 4 | 2.29 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.26 |  | 21 | 6 | 2.26 |  | 41 | 6 | 2.26 |
| 2 | 5 | 1.88 |  | 22 | 8 | 3.01 |  | 42 | 4 | 1.5 |
| 3 | 5 | 1.88 |  | 23 | 6 | 2.26 |  | 43 | 4 | 1.5 |
| 4 | 4 | 1.5 |  | 24 | 5 | 1.88 |  | 44 | 3 | 1.13 |
| 5 | 6 | 2.26 |  | 25 | 5 | 1.88 |  | 45 | 3 | 1.13 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 7 | 2.63 |
| 7 | 5 | 1.88 |  | 27 | 2 | 0.75 |  | 47 | 6 | 2.26 |
| 8 | 10 | 3.76 |  | 28 | 9 | 3.38 |  | 48 | 3 | 1.13 |
| 9 | 3 | 1.13 |  | 29 | 6 | 2.26 |  | 49 | 4 | 1.5 |
| 10 | 2 | 0.75 |  | 30 | 3 | 1.13 |  | 50 | 6 | 2.26 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 3 | 1.13 |
| 12 | 1 | 0.38 |  | 32 | 5 | 1.88 |  | 52 | 4 | 1.5 |
| 13 | 5 | 1.88 |  | 33 | 4 | 1.5 |  | 53 | 8 | 3.01 |
| 14 | 4 | 1.5 |  | 34 | 5 | 1.88 |  | 54 | 2 | 0.75 |
| 15 | 7 | 2.63 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 9 | 3.38 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 5 | 1.88 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 5 | 1.88 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 9 | 2026-05-02 | 63 |
| 10 | 2026-05-09 | 56 |
| 50 | 2026-05-16 | 49 |
| 12 | 2026-05-19 | 46 |
| 25 | 2026-05-30 | 35 |
| 51 | 2026-06-02 | 32 |
| 45 | 2026-06-04 | 30 |
| 29 | 2026-06-04 | 30 |
| 39 | 2026-06-06 | 28 |
| 37 | 2026-06-06 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 9 |
| 2 | 2026-06-16 | 18 |
| 3 | 2026-06-25 | 9 |
| 4 | 2026-06-18 | 16 |
| 5 | 2026-07-02 | 2 |
| 6 | 2026-06-09 | 25 |
| 7 | 2026-06-27 | 7 |
| 8 | 2026-06-25 | 9 |
| 9 | 2026-05-02 | 63 |
| 10 | 2026-05-09 | 56 |
| 11 | 2026-07-02 | 2 |
| 12 | 2026-05-19 | 46 |
| 13 | 2026-07-04 | 0 |
| 14 | 2026-06-18 | 16 |
| 15 | 2026-07-04 | 0 |
| 16 | 2026-06-27 | 7 |
| 17 | 2026-06-11 | 23 |
| 18 | 2026-07-04 | 0 |
| 19 | 2026-06-13 | 21 |
| 20 | 2026-06-18 | 16 |
| 21 | 2026-06-27 | 7 |
| 22 | 2026-06-30 | 4 |
| 23 | 2026-07-04 | 0 |
| 24 | 2026-06-11 | 23 |
| 25 | 2026-05-30 | 35 |
| 26 | 2026-06-20 | 14 |
| 27 | 2026-06-09 | 25 |
| 28 | 2026-07-02 | 2 |
| 29 | 2026-06-04 | 30 |
| 30 | 2026-06-20 | 14 |
| 31 | 2026-07-04 | 0 |
| 32 | 2026-06-09 | 25 |
| 33 | 2026-06-13 | 21 |
| 34 | 2026-07-02 | 2 |
| 35 | 2026-06-25 | 9 |
| 36 | 2026-06-18 | 16 |
| 37 | 2026-06-06 | 28 |
| 38 | 2026-06-23 | 11 |
| 39 | 2026-06-06 | 28 |
| 40 | 2026-06-23 | 11 |
| 41 | 2026-07-04 | 0 |
| 42 | 2026-07-02 | 2 |
| 43 | 2026-07-04 | 0 |
| 44 | 2026-06-30 | 4 |
| 45 | 2026-06-04 | 30 |
| 46 | 2026-06-23 | 11 |
| 47 | 2026-06-30 | 4 |
| 48 | 2026-06-11 | 23 |
| 49 | 2026-07-02 | 2 |
| 50 | 2026-05-16 | 49 |
| 51 | 2026-06-02 | 32 |
| 52 | 2026-06-27 | 7 |
| 53 | 2026-06-20 | 14 |
| 54 | 2026-06-27 | 7 |
| 55 | 2026-06-25 | 9 |



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

