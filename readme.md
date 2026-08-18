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
| Power 655 | 1385 | 2017-08-01 | 2026-08-15 | 1385 | 00001 | 01385 |
| Power 645 | 1353 | 2017-10-25 | 2026-08-16 | 1353 | 00198 | 01550 |
| Power 535 | 378 | 2025-06-29 | 2026-08-17 | 754 | 00001 | 00830 |
| Keno | 648 | 2022-12-04 | 2026-08-18 | 81237 | #0110271 | #0292448 |
| 3D | 1116 | 2019-04-22 | 2026-08-17 | 1116 | 00001 | 01120 |
| 3D Pro | 762 | 2021-09-14 | 2026-08-15 | 762 | 00001 | 00766 |
| Bingo18 | 622 | 2024-12-03 | 2026-08-18 | 86239 | 0083123 | 0182124 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2] | 2026-08-16T11:07:54.645332 |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42] | 2026-08-16T11:07:54.647468 |
| 2026-08-11 | 01383 | [2, 7, 19, 20, 39, 50, 31] | 2026-08-12T00:02:10.803156 |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37] | 2026-08-09T00:01:07.514841 |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1] | 2026-08-07T00:01:13.032397 |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] | 2026-08-06T00:02:27.504833 |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] | 2026-08-02T00:01:09.345245 |
| 2026-07-30 | 01378 | [2, 12, 24, 28, 43, 49, 51] | 2026-07-31T00:01:13.443363 |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48] | 2026-07-29T00:01:42.996426 |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48] | 2026-07-26T00:01:20.210277 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 186 | 1.92 |  | 21 | 172 | 1.77 |  | 41 | 204 | 2.1 |
| 2 | 160 | 1.65 |  | 22 | 206 | 2.13 |  | 42 | 180 | 1.86 |
| 3 | 187 | 1.93 |  | 23 | 187 | 1.93 |  | 43 | 198 | 2.04 |
| 4 | 144 | 1.49 |  | 24 | 176 | 1.82 |  | 44 | 180 | 1.86 |
| 5 | 180 | 1.86 |  | 25 | 158 | 1.63 |  | 45 | 179 | 1.85 |
| 6 | 143 | 1.48 |  | 26 | 165 | 1.7 |  | 46 | 181 | 1.87 |
| 7 | 156 | 1.61 |  | 27 | 162 | 1.67 |  | 47 | 175 | 1.81 |
| 8 | 192 | 1.98 |  | 28 | 158 | 1.63 |  | 48 | 189 | 1.95 |
| 9 | 192 | 1.98 |  | 29 | 189 | 1.95 |  | 49 | 173 | 1.78 |
| 10 | 164 | 1.69 |  | 30 | 161 | 1.66 |  | 50 | 177 | 1.83 |
| 11 | 179 | 1.85 |  | 31 | 185 | 1.91 |  | 51 | 196 | 2.02 |
| 12 | 180 | 1.86 |  | 32 | 186 | 1.92 |  | 52 | 177 | 1.83 |
| 13 | 172 | 1.77 |  | 33 | 179 | 1.85 |  | 53 | 187 | 1.93 |
| 14 | 177 | 1.83 |  | 34 | 195 | 2.01 |  | 54 | 167 | 1.72 |
| 15 | 164 | 1.69 |  | 35 | 170 | 1.75 |  | 55 | 178 | 1.84 |
| 16 | 174 | 1.79 |  | 36 | 166 | 1.71 |  |  |  |  |
| 17 | 159 | 1.64 |  | 37 | 158 | 1.63 |  |  |  |  |
| 18 | 175 | 1.81 |  | 38 | 170 | 1.75 |  |  |  |  |
| 19 | 173 | 1.78 |  | 39 | 171 | 1.76 |  |  |  |  |
| 20 | 189 | 1.95 |  | 40 | 193 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 28 | 1 | 1.19 |  | 49 | 2 | 2.38 |
| 2 | 3 | 3.57 |  | 29 | 2 | 2.38 |  | 50 | 3 | 3.57 |
| 3 | 1 | 1.19 |  | 30 | 1 | 1.19 |  | 51 | 2 | 2.38 |
| 5 | 3 | 3.57 |  | 31 | 2 | 2.38 |  | 54 | 1 | 1.19 |
| 7 | 2 | 2.38 |  | 32 | 1 | 1.19 |  | 55 | 3 | 3.57 |
| 8 | 2 | 2.38 |  | 33 | 2 | 2.38 |  |  |  |  |
| 9 | 2 | 2.38 |  | 35 | 1 | 1.19 |  |  |  |  |
| 11 | 2 | 2.38 |  | 36 | 1 | 1.19 |  |  |  |  |
| 12 | 1 | 1.19 |  | 37 | 2 | 2.38 |  |  |  |  |
| 13 | 1 | 1.19 |  | 38 | 2 | 2.38 |  |  |  |  |
| 14 | 3 | 3.57 |  | 39 | 4 | 4.76 |  |  |  |  |
| 16 | 2 | 2.38 |  | 40 | 3 | 3.57 |  |  |  |  |
| 18 | 1 | 1.19 |  | 41 | 1 | 1.19 |  |  |  |  |
| 19 | 1 | 1.19 |  | 42 | 2 | 2.38 |  |  |  |  |
| 20 | 2 | 2.38 |  | 43 | 1 | 1.19 |  |  |  |  |
| 22 | 2 | 2.38 |  | 44 | 2 | 2.38 |  |  |  |  |
| 23 | 2 | 2.38 |  | 45 | 2 | 2.38 |  |  |  |  |
| 24 | 2 | 2.38 |  | 46 | 1 | 1.19 |  |  |  |  |
| 25 | 1 | 1.19 |  | 47 | 1 | 1.19 |  |  |  |  |
| 27 | 4 | 4.76 |  | 48 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.29 |  | 21 | 2 | 1.14 |  | 41 | 5 | 2.86 |
| 2 | 4 | 2.29 |  | 22 | 4 | 2.29 |  | 42 | 4 | 2.29 |
| 3 | 2 | 1.14 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 4 | 1 | 0.57 |  | 24 | 3 | 1.71 |  | 44 | 4 | 2.29 |
| 5 | 6 | 3.43 |  | 25 | 2 | 1.14 |  | 45 | 6 | 3.43 |
| 6 | 1 | 0.57 |  | 26 | 1 | 0.57 |  | 46 | 3 | 1.71 |
| 7 | 3 | 1.71 |  | 27 | 4 | 2.29 |  | 47 | 2 | 1.14 |
| 8 | 4 | 2.29 |  | 28 | 4 | 2.29 |  | 48 | 4 | 2.29 |
| 9 | 4 | 2.29 |  | 29 | 2 | 1.14 |  | 49 | 4 | 2.29 |
| 10 | 2 | 1.14 |  | 30 | 3 | 1.71 |  | 50 | 3 | 1.71 |
| 11 | 3 | 1.71 |  | 31 | 3 | 1.71 |  | 51 | 3 | 1.71 |
| 12 | 1 | 0.57 |  | 32 | 2 | 1.14 |  | 52 | 2 | 1.14 |
| 13 | 4 | 2.29 |  | 33 | 6 | 3.43 |  | 53 | 2 | 1.14 |
| 14 | 4 | 2.29 |  | 34 | 1 | 0.57 |  | 54 | 3 | 1.71 |
| 15 | 2 | 1.14 |  | 35 | 3 | 1.71 |  | 55 | 5 | 2.86 |
| 16 | 5 | 2.86 |  | 36 | 1 | 0.57 |  |  |  |  |
| 17 | 2 | 1.14 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 4 | 2.29 |  |  |  |  |
| 20 | 4 | 2.29 |  | 40 | 5 | 2.86 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 3.01 |  | 21 | 4 | 1.5 |  | 41 | 6 | 2.26 |
| 2 | 7 | 2.63 |  | 22 | 5 | 1.88 |  | 42 | 7 | 2.63 |
| 3 | 5 | 1.88 |  | 23 | 8 | 3.01 |  | 43 | 4 | 1.5 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 5 | 1.88 |
| 5 | 8 | 3.01 |  | 25 | 4 | 1.5 |  | 45 | 7 | 2.63 |
| 6 | 2 | 0.75 |  | 26 | 1 | 0.38 |  | 46 | 5 | 1.88 |
| 7 | 4 | 1.5 |  | 27 | 6 | 2.26 |  | 47 | 3 | 1.13 |
| 8 | 9 | 3.38 |  | 28 | 7 | 2.63 |  | 48 | 5 | 1.88 |
| 9 | 4 | 1.5 |  | 29 | 4 | 1.5 |  | 49 | 6 | 2.26 |
| 10 | 2 | 0.75 |  | 30 | 3 | 1.13 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 5 | 1.88 |  | 51 | 4 | 1.5 |
| 12 | 1 | 0.38 |  | 32 | 4 | 1.5 |  | 52 | 2 | 0.75 |
| 13 | 4 | 1.5 |  | 33 | 7 | 2.63 |  | 53 | 3 | 1.13 |
| 14 | 7 | 2.63 |  | 34 | 4 | 1.5 |  | 54 | 4 | 1.5 |
| 15 | 3 | 1.13 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 8 | 3.01 |  | 36 | 3 | 1.13 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 5 | 1.88 |  | 38 | 4 | 1.5 |  |  |  |  |
| 19 | 4 | 1.5 |  | 39 | 6 | 2.26 |  |  |  |  |
| 20 | 7 | 2.63 |  | 40 | 8 | 3.01 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 26 | 2026-06-20 | 56 |
| 52 | 2026-06-27 | 49 |
| 34 | 2026-07-02 | 44 |
| 15 | 2026-07-04 | 42 |
| 6 | 2026-07-07 | 39 |
| 4 | 2026-07-07 | 39 |
| 17 | 2026-07-11 | 35 |
| 10 | 2026-07-14 | 32 |
| 21 | 2026-07-16 | 30 |
| 53 | 2026-07-16 | 30 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-08-06 | 9 |
| 2 | 2026-08-15 | 0 |
| 3 | 2026-07-23 | 23 |
| 4 | 2026-07-07 | 39 |
| 5 | 2026-08-13 | 2 |
| 6 | 2026-07-07 | 39 |
| 7 | 2026-08-11 | 4 |
| 8 | 2026-07-23 | 23 |
| 9 | 2026-08-13 | 2 |
| 10 | 2026-07-14 | 32 |
| 11 | 2026-08-01 | 14 |
| 12 | 2026-07-30 | 16 |
| 13 | 2026-07-21 | 25 |
| 14 | 2026-08-06 | 9 |
| 15 | 2026-07-04 | 42 |
| 16 | 2026-08-15 | 0 |
| 17 | 2026-07-11 | 35 |
| 18 | 2026-08-06 | 9 |
| 19 | 2026-08-11 | 4 |
| 20 | 2026-08-15 | 0 |
| 21 | 2026-07-16 | 30 |
| 22 | 2026-07-28 | 18 |
| 23 | 2026-08-06 | 9 |
| 24 | 2026-07-30 | 16 |
| 25 | 2026-08-15 | 0 |
| 26 | 2026-06-20 | 56 |
| 27 | 2026-08-15 | 0 |
| 28 | 2026-07-30 | 16 |
| 29 | 2026-08-13 | 2 |
| 30 | 2026-08-15 | 0 |
| 31 | 2026-08-11 | 4 |
| 32 | 2026-07-21 | 25 |
| 33 | 2026-08-08 | 7 |
| 34 | 2026-07-02 | 44 |
| 35 | 2026-08-06 | 9 |
| 36 | 2026-07-23 | 23 |
| 37 | 2026-08-08 | 7 |
| 38 | 2026-08-08 | 7 |
| 39 | 2026-08-11 | 4 |
| 40 | 2026-08-08 | 7 |
| 41 | 2026-07-28 | 18 |
| 42 | 2026-08-13 | 2 |
| 43 | 2026-07-30 | 16 |
| 44 | 2026-08-01 | 14 |
| 45 | 2026-08-13 | 2 |
| 46 | 2026-08-13 | 2 |
| 47 | 2026-08-04 | 11 |
| 48 | 2026-07-28 | 18 |
| 49 | 2026-08-01 | 14 |
| 50 | 2026-08-15 | 0 |
| 51 | 2026-08-06 | 9 |
| 52 | 2026-06-27 | 49 |
| 53 | 2026-07-16 | 30 |
| 54 | 2026-08-04 | 11 |
| 55 | 2026-08-06 | 9 |



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

