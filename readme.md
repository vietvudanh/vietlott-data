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
| Power 655 | 1380 | 2017-08-01 | 2026-08-04 | 1380 | 00001 | 01380 |
| Power 645 | 1348 | 2017-10-25 | 2026-08-05 | 1348 | 00198 | 01545 |
| Power 535 | 366 | 2025-06-29 | 2026-08-05 | 730 | 00001 | 00806 |
| Keno | 637 | 2022-12-04 | 2026-08-06 | 79965 | #0110271 | #0291020 |
| 3D | 1111 | 2019-04-22 | 2026-08-05 | 1111 | 00001 | 01115 |
| 3D Pro | 757 | 2021-09-14 | 2026-08-04 | 757 | 00001 | 00761 |
| Bingo18 | 610 | 2024-12-03 | 2026-08-06 | 84331 | 0083123 | 0180216 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] | 2026-08-06T00:02:27.504833 |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] | 2026-08-02T00:01:09.345245 |
| 2026-07-30 | 01378 | [2, 12, 24, 28, 43, 49, 51] | 2026-07-31T00:01:13.443363 |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48] | 2026-07-29T00:01:42.996426 |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36] | 2026-07-24T00:01:33.770193 |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 185 | 1.92 |  | 21 | 172 | 1.78 |  | 41 | 204 | 2.11 |
| 2 | 158 | 1.64 |  | 22 | 206 | 2.13 |  | 42 | 179 | 1.85 |
| 3 | 187 | 1.94 |  | 23 | 186 | 1.93 |  | 43 | 198 | 2.05 |
| 4 | 144 | 1.49 |  | 24 | 176 | 1.82 |  | 44 | 180 | 1.86 |
| 5 | 178 | 1.84 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.83 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.71 |  | 46 | 180 | 1.86 |
| 7 | 155 | 1.6 |  | 27 | 160 | 1.66 |  | 47 | 175 | 1.81 |
| 8 | 192 | 1.99 |  | 28 | 158 | 1.64 |  | 48 | 189 | 1.96 |
| 9 | 191 | 1.98 |  | 29 | 187 | 1.94 |  | 49 | 173 | 1.79 |
| 10 | 164 | 1.7 |  | 30 | 160 | 1.66 |  | 50 | 175 | 1.81 |
| 11 | 179 | 1.85 |  | 31 | 184 | 1.9 |  | 51 | 195 | 2.02 |
| 12 | 180 | 1.86 |  | 32 | 186 | 1.93 |  | 52 | 177 | 1.83 |
| 13 | 172 | 1.78 |  | 33 | 178 | 1.84 |  | 53 | 187 | 1.94 |
| 14 | 176 | 1.82 |  | 34 | 195 | 2.02 |  | 54 | 167 | 1.73 |
| 15 | 164 | 1.7 |  | 35 | 169 | 1.75 |  | 55 | 177 | 1.83 |
| 16 | 173 | 1.79 |  | 36 | 166 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 157 | 1.63 |  |  |  |  |
| 18 | 174 | 1.8 |  | 38 | 169 | 1.75 |  |  |  |  |
| 19 | 172 | 1.78 |  | 39 | 170 | 1.76 |  |  |  |  |
| 20 | 187 | 1.94 |  | 40 | 192 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 23 | 1 | 1.1 |  | 47 | 1 | 1.1 |
| 2 | 2 | 2.2 |  | 24 | 3 | 3.3 |  | 48 | 4 | 4.4 |
| 3 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 49 | 3 | 3.3 |
| 4 | 1 | 1.1 |  | 27 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 28 | 1 | 1.1 |  | 51 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 54 | 2 | 2.2 |
| 8 | 3 | 3.3 |  | 32 | 2 | 2.2 |  | 55 | 3 | 3.3 |
| 9 | 3 | 3.3 |  | 33 | 5 | 5.49 |  |  |  |  |
| 10 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 39 | 3 | 3.3 |  |  |  |  |
| 16 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 17 | 2 | 2.2 |  | 41 | 3 | 3.3 |  |  |  |  |
| 19 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 21 | 1 | 1.1 |  | 44 | 3 | 3.3 |  |  |  |  |
| 22 | 3 | 3.3 |  | 45 | 4 | 4.4 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.86 |  | 21 | 2 | 1.14 |  | 42 | 4 | 2.29 |
| 2 | 4 | 2.29 |  | 22 | 4 | 2.29 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 23 | 5 | 2.86 |  | 44 | 4 | 2.29 |
| 4 | 3 | 1.71 |  | 24 | 4 | 2.29 |  | 45 | 4 | 2.29 |
| 5 | 5 | 2.86 |  | 25 | 1 | 0.57 |  | 46 | 4 | 2.29 |
| 6 | 2 | 1.14 |  | 26 | 1 | 0.57 |  | 47 | 3 | 1.71 |
| 7 | 3 | 1.71 |  | 27 | 3 | 1.71 |  | 48 | 5 | 2.86 |
| 8 | 7 | 4.0 |  | 28 | 4 | 2.29 |  | 49 | 5 | 2.86 |
| 9 | 3 | 1.71 |  | 30 | 2 | 1.14 |  | 50 | 1 | 0.57 |
| 10 | 2 | 1.14 |  | 31 | 3 | 1.71 |  | 51 | 2 | 1.14 |
| 11 | 3 | 1.71 |  | 32 | 3 | 1.71 |  | 52 | 2 | 1.14 |
| 12 | 1 | 0.57 |  | 33 | 6 | 3.43 |  | 53 | 2 | 1.14 |
| 13 | 4 | 2.29 |  | 34 | 2 | 1.14 |  | 54 | 3 | 1.71 |
| 14 | 5 | 2.86 |  | 35 | 3 | 1.71 |  | 55 | 4 | 2.29 |
| 15 | 2 | 1.14 |  | 36 | 3 | 1.71 |  |  |  |  |
| 16 | 4 | 2.29 |  | 37 | 1 | 0.57 |  |  |  |  |
| 17 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 39 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 40 | 6 | 3.43 |  |  |  |  |
| 20 | 3 | 1.71 |  | 41 | 5 | 2.86 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 5 | 1.88 |  | 41 | 7 | 2.63 |
| 2 | 6 | 2.26 |  | 22 | 6 | 2.26 |  | 42 | 6 | 2.26 |
| 3 | 6 | 2.26 |  | 23 | 7 | 2.63 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 5 | 1.88 |
| 5 | 6 | 2.26 |  | 25 | 4 | 1.5 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 3 | 1.13 |  | 46 | 5 | 1.88 |
| 7 | 3 | 1.13 |  | 27 | 4 | 1.5 |  | 47 | 4 | 1.5 |
| 8 | 10 | 3.76 |  | 28 | 8 | 3.01 |  | 48 | 7 | 2.63 |
| 9 | 3 | 1.13 |  | 29 | 2 | 0.75 |  | 49 | 6 | 2.26 |
| 10 | 3 | 1.13 |  | 30 | 2 | 0.75 |  | 50 | 3 | 1.13 |
| 11 | 6 | 2.26 |  | 31 | 5 | 1.88 |  | 51 | 3 | 1.13 |
| 12 | 2 | 0.75 |  | 32 | 6 | 2.26 |  | 52 | 2 | 0.75 |
| 13 | 4 | 1.5 |  | 33 | 6 | 2.26 |  | 53 | 4 | 1.5 |
| 14 | 6 | 2.26 |  | 34 | 4 | 1.5 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 7 | 2.63 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 4 | 1.5 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 8 | 3.01 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 29 | 2026-06-04 | 61 |
| 26 | 2026-06-20 | 45 |
| 46 | 2026-06-23 | 42 |
| 52 | 2026-06-27 | 38 |
| 34 | 2026-07-02 | 33 |
| 15 | 2026-07-04 | 31 |
| 18 | 2026-07-04 | 31 |
| 6 | 2026-07-07 | 28 |
| 25 | 2026-07-07 | 28 |
| 4 | 2026-07-07 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-07-23 | 12 |
| 2 | 2026-07-30 | 5 |
| 3 | 2026-07-23 | 12 |
| 4 | 2026-07-07 | 28 |
| 5 | 2026-07-25 | 10 |
| 6 | 2026-07-07 | 28 |
| 7 | 2026-07-28 | 7 |
| 8 | 2026-07-23 | 12 |
| 9 | 2026-07-25 | 10 |
| 10 | 2026-07-14 | 21 |
| 11 | 2026-08-01 | 3 |
| 12 | 2026-07-30 | 5 |
| 13 | 2026-07-21 | 14 |
| 14 | 2026-08-04 | 0 |
| 15 | 2026-07-04 | 31 |
| 16 | 2026-08-01 | 3 |
| 17 | 2026-07-11 | 24 |
| 18 | 2026-07-04 | 31 |
| 19 | 2026-07-16 | 19 |
| 20 | 2026-07-16 | 19 |
| 21 | 2026-07-16 | 19 |
| 22 | 2026-07-28 | 7 |
| 23 | 2026-07-28 | 7 |
| 24 | 2026-07-30 | 5 |
| 25 | 2026-07-07 | 28 |
| 26 | 2026-06-20 | 45 |
| 27 | 2026-07-28 | 7 |
| 28 | 2026-07-30 | 5 |
| 29 | 2026-06-04 | 61 |
| 30 | 2026-07-14 | 21 |
| 31 | 2026-08-04 | 0 |
| 32 | 2026-07-21 | 14 |
| 33 | 2026-07-25 | 10 |
| 34 | 2026-07-02 | 33 |
| 35 | 2026-07-14 | 21 |
| 36 | 2026-07-23 | 12 |
| 37 | 2026-07-25 | 10 |
| 38 | 2026-07-23 | 12 |
| 39 | 2026-08-04 | 0 |
| 40 | 2026-08-04 | 0 |
| 41 | 2026-07-28 | 7 |
| 42 | 2026-08-04 | 0 |
| 43 | 2026-07-30 | 5 |
| 44 | 2026-08-01 | 3 |
| 45 | 2026-07-18 | 17 |
| 46 | 2026-06-23 | 42 |
| 47 | 2026-08-04 | 0 |
| 48 | 2026-07-28 | 7 |
| 49 | 2026-08-01 | 3 |
| 50 | 2026-07-25 | 10 |
| 51 | 2026-07-30 | 5 |
| 52 | 2026-06-27 | 38 |
| 53 | 2026-07-16 | 19 |
| 54 | 2026-08-04 | 0 |
| 55 | 2026-08-01 | 3 |



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

