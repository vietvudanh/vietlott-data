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
| Power 645 | 1352 | 2017-10-25 | 2026-08-14 | 1352 | 00198 | 01549 |
| Power 535 | 376 | 2025-06-29 | 2026-08-15 | 750 | 00001 | 00826 |
| Keno | 646 | 2022-12-04 | 2026-08-16 | 80999 | #0110271 | #0292210 |
| 3D | 1115 | 2019-04-22 | 2026-08-14 | 1115 | 00001 | 01119 |
| 3D Pro | 762 | 2021-09-14 | 2026-08-15 | 762 | 00001 | 00766 |
| Bingo18 | 618 | 2024-12-03 | 2026-08-16 | 85513 | 0083123 | 0181806 |

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
| 1 | 2 | 2.2 |  | 28 | 1 | 1.1 |  | 49 | 2 | 2.2 |
| 2 | 3 | 3.3 |  | 29 | 2 | 2.2 |  | 50 | 3 | 3.3 |
| 3 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 51 | 2 | 2.2 |
| 5 | 3 | 3.3 |  | 31 | 2 | 2.2 |  | 54 | 2 | 2.2 |
| 7 | 2 | 2.2 |  | 32 | 1 | 1.1 |  | 55 | 4 | 4.4 |
| 8 | 2 | 2.2 |  | 33 | 2 | 2.2 |  |  |  |  |
| 9 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 13 | 1 | 1.1 |  | 38 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 39 | 4 | 4.4 |  |  |  |  |
| 16 | 3 | 3.3 |  | 40 | 3 | 3.3 |  |  |  |  |
| 18 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 20 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 3 | 3.3 |  | 44 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 45 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 46 | 1 | 1.1 |  |  |  |  |
| 25 | 1 | 1.1 |  | 47 | 1 | 1.1 |  |  |  |  |
| 27 | 4 | 4.4 |  | 48 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.75 |  | 21 | 2 | 1.1 |  | 41 | 5 | 2.75 |
| 2 | 4 | 2.2 |  | 22 | 4 | 2.2 |  | 42 | 4 | 2.2 |
| 3 | 2 | 1.1 |  | 23 | 6 | 3.3 |  | 43 | 3 | 1.65 |
| 4 | 2 | 1.1 |  | 24 | 3 | 1.65 |  | 44 | 4 | 2.2 |
| 5 | 6 | 3.3 |  | 25 | 2 | 1.1 |  | 45 | 6 | 3.3 |
| 6 | 1 | 0.55 |  | 26 | 1 | 0.55 |  | 46 | 4 | 2.2 |
| 7 | 3 | 1.65 |  | 27 | 4 | 2.2 |  | 47 | 2 | 1.1 |
| 8 | 4 | 2.2 |  | 28 | 4 | 2.2 |  | 48 | 4 | 2.2 |
| 9 | 4 | 2.2 |  | 29 | 2 | 1.1 |  | 49 | 5 | 2.75 |
| 10 | 2 | 1.1 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 11 | 3 | 1.65 |  | 31 | 3 | 1.65 |  | 51 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 2 | 1.1 |  | 52 | 2 | 1.1 |
| 13 | 4 | 2.2 |  | 33 | 6 | 3.3 |  | 53 | 2 | 1.1 |
| 14 | 5 | 2.75 |  | 34 | 1 | 0.55 |  | 54 | 3 | 1.65 |
| 15 | 2 | 1.1 |  | 35 | 3 | 1.65 |  | 55 | 5 | 2.75 |
| 16 | 5 | 2.75 |  | 36 | 2 | 1.1 |  |  |  |  |
| 17 | 2 | 1.1 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 3 | 1.65 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 4 | 2.2 |  |  |  |  |
| 20 | 5 | 2.75 |  | 40 | 5 | 2.75 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8 | 2.93 |  | 21 | 5 | 1.83 |  | 41 | 6 | 2.2 |
| 2 | 7 | 2.56 |  | 22 | 5 | 1.83 |  | 42 | 7 | 2.56 |
| 3 | 5 | 1.83 |  | 23 | 8 | 2.93 |  | 43 | 4 | 1.47 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 5 | 1.83 |
| 5 | 8 | 2.93 |  | 25 | 4 | 1.47 |  | 45 | 8 | 2.93 |
| 6 | 2 | 0.73 |  | 26 | 1 | 0.37 |  | 46 | 5 | 1.83 |
| 7 | 4 | 1.47 |  | 27 | 6 | 2.2 |  | 47 | 3 | 1.1 |
| 8 | 9 | 3.3 |  | 28 | 7 | 2.56 |  | 48 | 6 | 2.2 |
| 9 | 4 | 1.47 |  | 29 | 4 | 1.47 |  | 49 | 6 | 2.2 |
| 10 | 2 | 0.73 |  | 30 | 3 | 1.1 |  | 50 | 3 | 1.1 |
| 11 | 5 | 1.83 |  | 31 | 5 | 1.83 |  | 51 | 4 | 1.47 |
| 12 | 2 | 0.73 |  | 32 | 4 | 1.47 |  | 52 | 2 | 0.73 |
| 13 | 4 | 1.47 |  | 33 | 7 | 2.56 |  | 53 | 4 | 1.47 |
| 14 | 7 | 2.56 |  | 34 | 4 | 1.47 |  | 54 | 4 | 1.47 |
| 15 | 3 | 1.1 |  | 35 | 4 | 1.47 |  | 55 | 5 | 1.83 |
| 16 | 8 | 2.93 |  | 36 | 3 | 1.1 |  |  |  |  |
| 17 | 4 | 1.47 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 5 | 1.83 |  | 38 | 4 | 1.47 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 7 | 2.56 |  |  |  |  |
| 20 | 7 | 2.56 |  | 40 | 9 | 3.3 |  |  |  |  |

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

