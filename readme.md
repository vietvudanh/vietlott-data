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
| Power 655 | 1377 | 2017-08-01 | 2026-07-28 | 1377 | 00001 | 01377 |
| Power 645 | 1345 | 2017-10-25 | 2026-07-29 | 1345 | 00198 | 01542 |
| Power 535 | 359 | 2025-06-29 | 2026-07-29 | 716 | 00001 | 00792 |
| Keno | 627 | 2022-12-04 | 2026-07-30 | 78680 | #0110271 | #0290187 |
| 3D | 1108 | 2019-04-22 | 2026-07-29 | 1108 | 00001 | 01112 |
| 3D Pro | 754 | 2021-09-14 | 2026-07-28 | 754 | 00001 | 00758 |
| Bingo18 | 603 | 2024-12-03 | 2026-07-30 | 83221 | 0083123 | 0179103 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48] | 2026-07-29T00:01:42.996426 |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36] | 2026-07-24T00:01:33.770193 |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13] | 2026-07-22T00:01:11.328447 |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 185 | 1.92 |  | 21 | 172 | 1.78 |  | 41 | 204 | 2.12 |
| 2 | 157 | 1.63 |  | 22 | 206 | 2.14 |  | 42 | 178 | 1.85 |
| 3 | 187 | 1.94 |  | 23 | 186 | 1.93 |  | 43 | 197 | 2.04 |
| 4 | 144 | 1.49 |  | 24 | 175 | 1.82 |  | 44 | 179 | 1.86 |
| 5 | 178 | 1.85 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.84 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.71 |  | 46 | 180 | 1.87 |
| 7 | 155 | 1.61 |  | 27 | 160 | 1.66 |  | 47 | 174 | 1.81 |
| 8 | 192 | 1.99 |  | 28 | 157 | 1.63 |  | 48 | 189 | 1.96 |
| 9 | 191 | 1.98 |  | 29 | 187 | 1.94 |  | 49 | 171 | 1.77 |
| 10 | 164 | 1.7 |  | 30 | 160 | 1.66 |  | 50 | 175 | 1.82 |
| 11 | 178 | 1.85 |  | 31 | 183 | 1.9 |  | 51 | 194 | 2.01 |
| 12 | 179 | 1.86 |  | 32 | 186 | 1.93 |  | 52 | 177 | 1.84 |
| 13 | 172 | 1.78 |  | 33 | 178 | 1.85 |  | 53 | 187 | 1.94 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.02 |  | 54 | 166 | 1.72 |
| 15 | 164 | 1.7 |  | 35 | 169 | 1.75 |  | 55 | 176 | 1.83 |
| 16 | 172 | 1.78 |  | 36 | 166 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 157 | 1.63 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 169 | 1.75 |  |  |  |  |
| 19 | 172 | 1.78 |  | 39 | 168 | 1.74 |  |  |  |  |
| 20 | 187 | 1.94 |  | 40 | 191 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 22 | 4 | 4.4 |  | 44 | 3 | 3.3 |
| 2 | 1 | 1.1 |  | 23 | 2 | 2.2 |  | 45 | 4 | 4.4 |
| 3 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 47 | 1 | 1.1 |
| 4 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 48 | 4 | 4.4 |
| 5 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 49 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 28 | 1 | 1.1 |  | 50 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 8 | 3 | 3.3 |  | 31 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 9 | 3 | 3.3 |  | 32 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 10 | 2 | 2.2 |  | 33 | 5 | 5.49 |  | 55 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 13 | 3 | 3.3 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 1 | 1.1 |  |  |  |  |
| 16 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 39 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 41 | 5 | 5.49 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 43 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.43 |  | 22 | 4 | 2.29 |  | 42 | 4 | 2.29 |
| 2 | 3 | 1.71 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 3 | 4 | 2.29 |  | 24 | 4 | 2.29 |  | 44 | 3 | 1.71 |
| 4 | 3 | 1.71 |  | 25 | 1 | 0.57 |  | 45 | 5 | 2.86 |
| 5 | 6 | 3.43 |  | 26 | 1 | 0.57 |  | 46 | 4 | 2.29 |
| 6 | 2 | 1.14 |  | 27 | 3 | 1.71 |  | 47 | 2 | 1.14 |
| 7 | 3 | 1.71 |  | 28 | 5 | 2.86 |  | 48 | 5 | 2.86 |
| 8 | 7 | 4.0 |  | 29 | 1 | 0.57 |  | 49 | 3 | 1.71 |
| 9 | 3 | 1.71 |  | 30 | 2 | 1.14 |  | 50 | 1 | 0.57 |
| 10 | 2 | 1.14 |  | 31 | 2 | 1.14 |  | 51 | 2 | 1.14 |
| 11 | 3 | 1.71 |  | 32 | 3 | 1.71 |  | 52 | 2 | 1.14 |
| 13 | 4 | 2.29 |  | 33 | 6 | 3.43 |  | 53 | 2 | 1.14 |
| 14 | 3 | 1.71 |  | 34 | 2 | 1.14 |  | 54 | 2 | 1.14 |
| 15 | 2 | 1.14 |  | 35 | 3 | 1.71 |  | 55 | 3 | 1.71 |
| 16 | 5 | 2.86 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 3 | 1.71 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 3 | 1.71 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 5 | 2.86 |  |  |  |  |
| 21 | 2 | 1.14 |  | 41 | 6 | 3.43 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 6 | 2.26 |  | 41 | 7 | 2.63 |
| 2 | 5 | 1.88 |  | 22 | 7 | 2.63 |  | 42 | 5 | 1.88 |
| 3 | 6 | 2.26 |  | 23 | 7 | 2.63 |  | 43 | 3 | 1.13 |
| 4 | 4 | 1.5 |  | 24 | 5 | 1.88 |  | 44 | 5 | 1.88 |
| 5 | 6 | 2.26 |  | 25 | 4 | 1.5 |  | 45 | 7 | 2.63 |
| 6 | 3 | 1.13 |  | 26 | 4 | 1.5 |  | 46 | 6 | 2.26 |
| 7 | 3 | 1.13 |  | 27 | 4 | 1.5 |  | 47 | 4 | 1.5 |
| 8 | 11 | 4.14 |  | 28 | 7 | 2.63 |  | 48 | 7 | 2.63 |
| 9 | 4 | 1.5 |  | 29 | 2 | 0.75 |  | 49 | 4 | 1.5 |
| 10 | 3 | 1.13 |  | 30 | 3 | 1.13 |  | 50 | 5 | 1.88 |
| 11 | 5 | 1.88 |  | 31 | 4 | 1.5 |  | 51 | 3 | 1.13 |
| 12 | 1 | 0.38 |  | 32 | 7 | 2.63 |  | 52 | 2 | 0.75 |
| 13 | 5 | 1.88 |  | 33 | 8 | 3.01 |  | 53 | 4 | 1.5 |
| 14 | 5 | 1.88 |  | 34 | 4 | 1.5 |  | 54 | 3 | 1.13 |
| 15 | 4 | 1.5 |  | 35 | 3 | 1.13 |  | 55 | 5 | 1.88 |
| 16 | 6 | 2.26 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 6 | 2.26 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 4 | 1.5 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 6 | 2.26 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 7 | 2.63 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 12 | 2026-05-19 | 70 |
| 29 | 2026-06-04 | 54 |
| 26 | 2026-06-20 | 38 |
| 46 | 2026-06-23 | 35 |
| 52 | 2026-06-27 | 31 |
| 47 | 2026-06-30 | 28 |
| 28 | 2026-07-02 | 26 |
| 34 | 2026-07-02 | 26 |
| 18 | 2026-07-04 | 24 |
| 15 | 2026-07-04 | 24 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-07-23 | 5 |
| 2 | 2026-07-09 | 19 |
| 3 | 2026-07-23 | 5 |
| 4 | 2026-07-07 | 21 |
| 5 | 2026-07-25 | 3 |
| 6 | 2026-07-07 | 21 |
| 7 | 2026-07-28 | 0 |
| 8 | 2026-07-23 | 5 |
| 9 | 2026-07-25 | 3 |
| 10 | 2026-07-14 | 14 |
| 11 | 2026-07-21 | 7 |
| 12 | 2026-05-19 | 70 |
| 13 | 2026-07-21 | 7 |
| 14 | 2026-07-09 | 19 |
| 15 | 2026-07-04 | 24 |
| 16 | 2026-07-18 | 10 |
| 17 | 2026-07-11 | 17 |
| 18 | 2026-07-04 | 24 |
| 19 | 2026-07-16 | 12 |
| 20 | 2026-07-16 | 12 |
| 21 | 2026-07-16 | 12 |
| 22 | 2026-07-28 | 0 |
| 23 | 2026-07-28 | 0 |
| 24 | 2026-07-21 | 7 |
| 25 | 2026-07-07 | 21 |
| 26 | 2026-06-20 | 38 |
| 27 | 2026-07-28 | 0 |
| 28 | 2026-07-02 | 26 |
| 29 | 2026-06-04 | 54 |
| 30 | 2026-07-14 | 14 |
| 31 | 2026-07-04 | 24 |
| 32 | 2026-07-21 | 7 |
| 33 | 2026-07-25 | 3 |
| 34 | 2026-07-02 | 26 |
| 35 | 2026-07-14 | 14 |
| 36 | 2026-07-23 | 5 |
| 37 | 2026-07-25 | 3 |
| 38 | 2026-07-23 | 5 |
| 39 | 2026-07-21 | 7 |
| 40 | 2026-07-23 | 5 |
| 41 | 2026-07-28 | 0 |
| 42 | 2026-07-11 | 17 |
| 43 | 2026-07-04 | 24 |
| 44 | 2026-07-28 | 0 |
| 45 | 2026-07-18 | 10 |
| 46 | 2026-06-23 | 35 |
| 47 | 2026-06-30 | 28 |
| 48 | 2026-07-28 | 0 |
| 49 | 2026-07-09 | 19 |
| 50 | 2026-07-25 | 3 |
| 51 | 2026-07-14 | 14 |
| 52 | 2026-06-27 | 31 |
| 53 | 2026-07-16 | 12 |
| 54 | 2026-07-18 | 10 |
| 55 | 2026-07-23 | 5 |



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

