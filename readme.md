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
| Power 655 | 1382 | 2017-08-01 | 2026-08-08 | 1382 | 00001 | 01382 |
| Power 645 | 1350 | 2017-10-25 | 2026-08-09 | 1350 | 00198 | 01547 |
| Power 535 | 371 | 2025-06-29 | 2026-08-10 | 740 | 00001 | 00816 |
| Keno | 641 | 2022-12-04 | 2026-08-10 | 80516 | #0110271 | #0291571 |
| 3D | 1113 | 2019-04-22 | 2026-08-10 | 1113 | 00001 | 01117 |
| 3D Pro | 759 | 2021-09-14 | 2026-08-08 | 759 | 00001 | 00763 |
| Bingo18 | 614 | 2024-12-03 | 2026-08-10 | 85027 | 0083123 | 0180951 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37] | 2026-08-09T00:01:07.514841 |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1] | 2026-08-07T00:01:13.032397 |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] | 2026-08-06T00:02:27.504833 |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] | 2026-08-02T00:01:09.345245 |
| 2026-07-30 | 01378 | [2, 12, 24, 28, 43, 49, 51] | 2026-07-31T00:01:13.443363 |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48] | 2026-07-29T00:01:42.996426 |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36] | 2026-07-24T00:01:33.770193 |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 186 | 1.92 |  | 21 | 172 | 1.78 |  | 41 | 204 | 2.11 |
| 2 | 158 | 1.63 |  | 22 | 206 | 2.13 |  | 42 | 179 | 1.85 |
| 3 | 187 | 1.93 |  | 23 | 187 | 1.93 |  | 43 | 198 | 2.05 |
| 4 | 144 | 1.49 |  | 24 | 176 | 1.82 |  | 44 | 180 | 1.86 |
| 5 | 179 | 1.85 |  | 25 | 157 | 1.62 |  | 45 | 178 | 1.84 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.71 |  | 46 | 180 | 1.86 |
| 7 | 155 | 1.6 |  | 27 | 160 | 1.65 |  | 47 | 175 | 1.81 |
| 8 | 192 | 1.98 |  | 28 | 158 | 1.63 |  | 48 | 189 | 1.95 |
| 9 | 191 | 1.97 |  | 29 | 188 | 1.94 |  | 49 | 173 | 1.79 |
| 10 | 164 | 1.7 |  | 30 | 160 | 1.65 |  | 50 | 175 | 1.81 |
| 11 | 179 | 1.85 |  | 31 | 184 | 1.9 |  | 51 | 196 | 2.03 |
| 12 | 180 | 1.86 |  | 32 | 186 | 1.92 |  | 52 | 177 | 1.83 |
| 13 | 172 | 1.78 |  | 33 | 179 | 1.85 |  | 53 | 187 | 1.93 |
| 14 | 177 | 1.83 |  | 34 | 195 | 2.02 |  | 54 | 167 | 1.73 |
| 15 | 164 | 1.7 |  | 35 | 170 | 1.76 |  | 55 | 178 | 1.84 |
| 16 | 173 | 1.79 |  | 36 | 166 | 1.72 |  |  |  |  |
| 17 | 159 | 1.64 |  | 37 | 158 | 1.63 |  |  |  |  |
| 18 | 175 | 1.81 |  | 38 | 170 | 1.76 |  |  |  |  |
| 19 | 172 | 1.78 |  | 39 | 170 | 1.76 |  |  |  |  |
| 20 | 187 | 1.93 |  | 40 | 193 | 2.0 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 27 | 2 | 2.38 |  | 49 | 2 | 2.38 |
| 2 | 1 | 1.19 |  | 28 | 1 | 1.19 |  | 50 | 1 | 1.19 |
| 3 | 1 | 1.19 |  | 29 | 1 | 1.19 |  | 51 | 3 | 3.57 |
| 5 | 2 | 2.38 |  | 30 | 1 | 1.19 |  | 53 | 1 | 1.19 |
| 7 | 1 | 1.19 |  | 31 | 1 | 1.19 |  | 54 | 2 | 2.38 |
| 8 | 2 | 2.38 |  | 32 | 1 | 1.19 |  | 55 | 4 | 4.76 |
| 9 | 1 | 1.19 |  | 33 | 4 | 4.76 |  |  |  |  |
| 10 | 1 | 1.19 |  | 35 | 2 | 2.38 |  |  |  |  |
| 11 | 2 | 2.38 |  | 36 | 1 | 1.19 |  |  |  |  |
| 12 | 1 | 1.19 |  | 37 | 2 | 2.38 |  |  |  |  |
| 13 | 1 | 1.19 |  | 38 | 2 | 2.38 |  |  |  |  |
| 14 | 3 | 3.57 |  | 39 | 3 | 3.57 |  |  |  |  |
| 16 | 2 | 2.38 |  | 40 | 3 | 3.57 |  |  |  |  |
| 18 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 42 | 1 | 1.19 |  |  |  |  |
| 20 | 1 | 1.19 |  | 43 | 1 | 1.19 |  |  |  |  |
| 21 | 1 | 1.19 |  | 44 | 2 | 2.38 |  |  |  |  |
| 22 | 3 | 3.57 |  | 45 | 4 | 4.76 |  |  |  |  |
| 23 | 2 | 2.38 |  | 47 | 1 | 1.19 |  |  |  |  |
| 24 | 3 | 3.57 |  | 48 | 4 | 4.76 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.86 |  | 21 | 2 | 1.14 |  | 41 | 5 | 2.86 |
| 2 | 4 | 2.29 |  | 22 | 4 | 2.29 |  | 42 | 4 | 2.29 |
| 3 | 2 | 1.14 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 4 | 3 | 1.71 |  | 24 | 3 | 1.71 |  | 44 | 4 | 2.29 |
| 5 | 6 | 3.43 |  | 25 | 1 | 0.57 |  | 45 | 5 | 2.86 |
| 6 | 1 | 0.57 |  | 26 | 1 | 0.57 |  | 46 | 3 | 1.71 |
| 7 | 3 | 1.71 |  | 27 | 2 | 1.14 |  | 47 | 3 | 1.71 |
| 8 | 5 | 2.86 |  | 28 | 4 | 2.29 |  | 48 | 4 | 2.29 |
| 9 | 3 | 1.71 |  | 29 | 1 | 0.57 |  | 49 | 5 | 2.86 |
| 10 | 2 | 1.14 |  | 30 | 2 | 1.14 |  | 50 | 1 | 0.57 |
| 11 | 3 | 1.71 |  | 31 | 3 | 1.71 |  | 51 | 3 | 1.71 |
| 12 | 1 | 0.57 |  | 32 | 2 | 1.14 |  | 52 | 2 | 1.14 |
| 13 | 4 | 2.29 |  | 33 | 7 | 4.0 |  | 53 | 2 | 1.14 |
| 14 | 6 | 3.43 |  | 34 | 1 | 0.57 |  | 54 | 3 | 1.71 |
| 15 | 2 | 1.14 |  | 35 | 3 | 1.71 |  | 55 | 5 | 2.86 |
| 16 | 4 | 2.29 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 2 | 1.14 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 3 | 1.71 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 6 | 3.43 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 5 | 1.88 |  | 41 | 7 | 2.63 |
| 2 | 5 | 1.88 |  | 22 | 5 | 1.88 |  | 42 | 6 | 2.26 |
| 3 | 5 | 1.88 |  | 23 | 8 | 3.01 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 5 | 1.88 |
| 5 | 7 | 2.63 |  | 25 | 4 | 1.5 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 2 | 0.75 |  | 46 | 4 | 1.5 |
| 7 | 3 | 1.13 |  | 27 | 4 | 1.5 |  | 47 | 4 | 1.5 |
| 8 | 10 | 3.76 |  | 28 | 8 | 3.01 |  | 48 | 7 | 2.63 |
| 9 | 3 | 1.13 |  | 29 | 3 | 1.13 |  | 49 | 6 | 2.26 |
| 10 | 2 | 0.75 |  | 30 | 2 | 0.75 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 4 | 1.5 |  | 51 | 4 | 1.5 |
| 12 | 2 | 0.75 |  | 32 | 5 | 1.88 |  | 52 | 2 | 0.75 |
| 13 | 4 | 1.5 |  | 33 | 7 | 2.63 |  | 53 | 4 | 1.5 |
| 14 | 7 | 2.63 |  | 34 | 4 | 1.5 |  | 54 | 4 | 1.5 |
| 15 | 3 | 1.13 |  | 35 | 4 | 1.5 |  | 55 | 6 | 2.26 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 5 | 1.88 |  | 38 | 4 | 1.5 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 9 | 3.38 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 26 | 2026-06-20 | 49 |
| 46 | 2026-06-23 | 46 |
| 52 | 2026-06-27 | 42 |
| 34 | 2026-07-02 | 37 |
| 15 | 2026-07-04 | 35 |
| 6 | 2026-07-07 | 32 |
| 4 | 2026-07-07 | 32 |
| 25 | 2026-07-07 | 32 |
| 17 | 2026-07-11 | 28 |
| 30 | 2026-07-14 | 25 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-08-06 | 2 |
| 2 | 2026-07-30 | 9 |
| 3 | 2026-07-23 | 16 |
| 4 | 2026-07-07 | 32 |
| 5 | 2026-08-08 | 0 |
| 6 | 2026-07-07 | 32 |
| 7 | 2026-07-28 | 11 |
| 8 | 2026-07-23 | 16 |
| 9 | 2026-07-25 | 14 |
| 10 | 2026-07-14 | 25 |
| 11 | 2026-08-01 | 7 |
| 12 | 2026-07-30 | 9 |
| 13 | 2026-07-21 | 18 |
| 14 | 2026-08-06 | 2 |
| 15 | 2026-07-04 | 35 |
| 16 | 2026-08-01 | 7 |
| 17 | 2026-07-11 | 28 |
| 18 | 2026-08-06 | 2 |
| 19 | 2026-07-16 | 23 |
| 20 | 2026-07-16 | 23 |
| 21 | 2026-07-16 | 23 |
| 22 | 2026-07-28 | 11 |
| 23 | 2026-08-06 | 2 |
| 24 | 2026-07-30 | 9 |
| 25 | 2026-07-07 | 32 |
| 26 | 2026-06-20 | 49 |
| 27 | 2026-07-28 | 11 |
| 28 | 2026-07-30 | 9 |
| 29 | 2026-08-08 | 0 |
| 30 | 2026-07-14 | 25 |
| 31 | 2026-08-04 | 4 |
| 32 | 2026-07-21 | 18 |
| 33 | 2026-08-08 | 0 |
| 34 | 2026-07-02 | 37 |
| 35 | 2026-08-06 | 2 |
| 36 | 2026-07-23 | 16 |
| 37 | 2026-08-08 | 0 |
| 38 | 2026-08-08 | 0 |
| 39 | 2026-08-04 | 4 |
| 40 | 2026-08-08 | 0 |
| 41 | 2026-07-28 | 11 |
| 42 | 2026-08-04 | 4 |
| 43 | 2026-07-30 | 9 |
| 44 | 2026-08-01 | 7 |
| 45 | 2026-08-08 | 0 |
| 46 | 2026-06-23 | 46 |
| 47 | 2026-08-04 | 4 |
| 48 | 2026-07-28 | 11 |
| 49 | 2026-08-01 | 7 |
| 50 | 2026-07-25 | 14 |
| 51 | 2026-08-06 | 2 |
| 52 | 2026-06-27 | 42 |
| 53 | 2026-07-16 | 23 |
| 54 | 2026-08-04 | 4 |
| 55 | 2026-08-06 | 2 |



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

