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
| Power 655 | 1324 | 2017-08-01 | 2026-03-26 | 1324 | 00001 | 01324 |
| Power 645 | 1292 | 2017-10-25 | 2026-03-27 | 1292 | 00198 | 01489 |
| Power 535 | 247 | 2025-06-29 | 2026-03-27 | 494 | 00001 | 00544 |
| Keno | 498 | 2022-12-04 | 2026-03-28 | 62892 | #0110271 | #0275434 |
| 3D | 1055 | 2019-04-22 | 2026-03-27 | 1055 | 00001 | 01059 |
| 3D Pro | 701 | 2021-09-14 | 2026-03-26 | 701 | 00001 | 00705 |
| Bingo18 | 472 | 2024-12-03 | 2026-03-28 | 54787 | 0083123 | 0159401 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-03-26 | 01324 | [3, 9, 10, 34, 38, 44, 51] | 2026-03-27T00:01:03.257686 |
| 2026-03-24 | 01323 | [12, 19, 25, 26, 32, 45, 3] | 2026-03-25T00:00:56.311562 |
| 2026-03-21 | 01322 | [1, 6, 40, 43, 47, 53, 3] | 2026-03-22T00:00:58.677766 |
| 2026-03-19 | 01321 | [7, 9, 17, 31, 34, 36, 55] | 2026-03-20T00:00:58.910179 |
| 2026-03-17 | 01320 | [12, 26, 28, 43, 50, 54, 52] | 2026-03-18T00:00:56.999640 |
| 2026-03-14 | 01319 | [7, 16, 27, 29, 47, 52, 26] | 2026-03-15T00:00:52.883799 |
| 2026-03-12 | 01318 | [12, 28, 36, 40, 53, 55, 54] | 2026-03-13T00:00:57.770966 |
| 2026-03-10 | 01317 | [3, 26, 31, 39, 47, 54, 20] | 2026-03-12T00:00:58.996922 |
| 2026-03-07 | 01316 | [4, 32, 41, 45, 50, 52, 29] | 2026-03-08T00:01:04.043596 |
| 2026-03-05 | 01315 | [14, 16, 35, 38, 43, 51, 37] | 2026-03-06T00:01:02.441420 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 177 | 1.91 |  | 21 | 163 | 1.76 |  | 41 | 195 | 2.1 |
| 2 | 151 | 1.63 |  | 22 | 193 | 2.08 |  | 42 | 172 | 1.86 |
| 3 | 181 | 1.95 |  | 23 | 177 | 1.91 |  | 43 | 192 | 2.07 |
| 4 | 139 | 1.5 |  | 24 | 168 | 1.81 |  | 44 | 173 | 1.87 |
| 5 | 170 | 1.83 |  | 25 | 151 | 1.63 |  | 45 | 170 | 1.83 |
| 6 | 140 | 1.51 |  | 26 | 160 | 1.73 |  | 46 | 173 | 1.87 |
| 7 | 147 | 1.59 |  | 27 | 156 | 1.68 |  | 47 | 168 | 1.81 |
| 8 | 179 | 1.93 |  | 28 | 148 | 1.6 |  | 48 | 181 | 1.95 |
| 9 | 184 | 1.99 |  | 29 | 181 | 1.95 |  | 49 | 166 | 1.79 |
| 10 | 159 | 1.72 |  | 30 | 154 | 1.66 |  | 50 | 168 | 1.81 |
| 11 | 172 | 1.86 |  | 31 | 178 | 1.92 |  | 51 | 190 | 2.05 |
| 12 | 178 | 1.92 |  | 32 | 177 | 1.91 |  | 52 | 172 | 1.86 |
| 13 | 164 | 1.77 |  | 33 | 168 | 1.81 |  | 53 | 176 | 1.9 |
| 14 | 169 | 1.82 |  | 34 | 189 | 2.04 |  | 54 | 162 | 1.75 |
| 15 | 156 | 1.68 |  | 35 | 164 | 1.77 |  | 55 | 169 | 1.82 |
| 16 | 161 | 1.74 |  | 36 | 161 | 1.74 |  |  |  |  |
| 17 | 152 | 1.64 |  | 37 | 152 | 1.64 |  |  |  |  |
| 18 | 169 | 1.82 |  | 38 | 162 | 1.75 |  |  |  |  |
| 19 | 168 | 1.81 |  | 39 | 158 | 1.7 |  |  |  |  |
| 20 | 181 | 1.95 |  | 40 | 183 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 29 | 3 | 3.3 |  | 54 | 4 | 4.4 |
| 3 | 4 | 4.4 |  | 31 | 3 | 3.3 |  | 55 | 2 | 2.2 |
| 4 | 1 | 1.1 |  | 32 | 2 | 2.2 |  |  |  |  |
| 6 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 7 | 4 | 4.4 |  | 35 | 1 | 1.1 |  |  |  |  |
| 9 | 2 | 2.2 |  | 36 | 3 | 3.3 |  |  |  |  |
| 10 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 12 | 3 | 3.3 |  | 38 | 2 | 2.2 |  |  |  |  |
| 13 | 1 | 1.1 |  | 39 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 17 | 1 | 1.1 |  | 43 | 4 | 4.4 |  |  |  |  |
| 19 | 1 | 1.1 |  | 44 | 3 | 3.3 |  |  |  |  |
| 20 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 46 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 47 | 3 | 3.3 |  |  |  |  |
| 25 | 3 | 3.3 |  | 50 | 3 | 3.3 |  |  |  |  |
| 26 | 4 | 4.4 |  | 51 | 4 | 4.4 |  |  |  |  |
| 27 | 2 | 2.2 |  | 52 | 3 | 3.3 |  |  |  |  |
| 28 | 2 | 2.2 |  | 53 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.29 |  | 21 | 2 | 1.14 |  | 44 | 3 | 1.71 |
| 2 | 1 | 0.57 |  | 22 | 5 | 2.86 |  | 45 | 5 | 2.86 |
| 3 | 5 | 2.86 |  | 25 | 4 | 2.29 |  | 46 | 4 | 2.29 |
| 4 | 2 | 1.14 |  | 26 | 9 | 5.14 |  | 47 | 3 | 1.71 |
| 5 | 3 | 1.71 |  | 27 | 3 | 1.71 |  | 48 | 3 | 1.71 |
| 6 | 1 | 0.57 |  | 28 | 3 | 1.71 |  | 49 | 1 | 0.57 |
| 7 | 6 | 3.43 |  | 29 | 5 | 2.86 |  | 50 | 3 | 1.71 |
| 8 | 2 | 1.14 |  | 30 | 3 | 1.71 |  | 51 | 5 | 2.86 |
| 9 | 3 | 1.71 |  | 31 | 4 | 2.29 |  | 52 | 3 | 1.71 |
| 10 | 3 | 1.71 |  | 32 | 7 | 4.0 |  | 53 | 5 | 2.86 |
| 11 | 2 | 1.14 |  | 34 | 3 | 1.71 |  | 54 | 7 | 4.0 |
| 12 | 5 | 2.86 |  | 35 | 1 | 0.57 |  | 55 | 4 | 2.29 |
| 13 | 6 | 3.43 |  | 36 | 4 | 2.29 |  |  |  |  |
| 14 | 2 | 1.14 |  | 37 | 1 | 0.57 |  |  |  |  |
| 15 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 16 | 3 | 1.71 |  | 39 | 2 | 1.14 |  |  |  |  |
| 17 | 3 | 1.71 |  | 40 | 2 | 1.14 |  |  |  |  |
| 18 | 2 | 1.14 |  | 41 | 2 | 1.14 |  |  |  |  |
| 19 | 2 | 1.14 |  | 42 | 2 | 1.14 |  |  |  |  |
| 20 | 2 | 1.14 |  | 43 | 5 | 2.86 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.54 |  | 21 | 5 | 1.93 |  | 41 | 4 | 1.54 |
| 2 | 2 | 0.77 |  | 22 | 7 | 2.7 |  | 42 | 4 | 1.54 |
| 3 | 6 | 2.32 |  | 23 | 2 | 0.77 |  | 43 | 7 | 2.7 |
| 4 | 3 | 1.16 |  | 24 | 1 | 0.39 |  | 44 | 3 | 1.16 |
| 5 | 5 | 1.93 |  | 25 | 7 | 2.7 |  | 45 | 6 | 2.32 |
| 6 | 1 | 0.39 |  | 26 | 10 | 3.86 |  | 46 | 5 | 1.93 |
| 7 | 6 | 2.32 |  | 27 | 4 | 1.54 |  | 47 | 5 | 1.93 |
| 8 | 2 | 0.77 |  | 28 | 5 | 1.93 |  | 48 | 6 | 2.32 |
| 9 | 4 | 1.54 |  | 29 | 8 | 3.09 |  | 49 | 2 | 0.77 |
| 10 | 4 | 1.54 |  | 30 | 7 | 2.7 |  | 50 | 5 | 1.93 |
| 11 | 3 | 1.16 |  | 31 | 5 | 1.93 |  | 51 | 6 | 2.32 |
| 12 | 6 | 2.32 |  | 32 | 8 | 3.09 |  | 52 | 4 | 1.54 |
| 13 | 7 | 2.7 |  | 33 | 3 | 1.16 |  | 53 | 6 | 2.32 |
| 14 | 4 | 1.54 |  | 34 | 6 | 2.32 |  | 54 | 9 | 3.47 |
| 15 | 3 | 1.16 |  | 35 | 3 | 1.16 |  | 55 | 7 | 2.7 |
| 16 | 6 | 2.32 |  | 36 | 7 | 2.7 |  |  |  |  |
| 17 | 4 | 1.54 |  | 37 | 2 | 0.77 |  |  |  |  |
| 18 | 3 | 1.16 |  | 38 | 4 | 1.54 |  |  |  |  |
| 19 | 2 | 0.77 |  | 39 | 3 | 1.16 |  |  |  |  |
| 20 | 6 | 2.32 |  | 40 | 2 | 0.77 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 33 | 2026-01-10 | 75 |
| 23 | 2026-01-17 | 68 |
| 24 | 2026-01-24 | 61 |
| 49 | 2026-01-31 | 54 |
| 11 | 2026-01-31 | 54 |
| 15 | 2026-02-07 | 47 |
| 42 | 2026-02-14 | 40 |
| 2 | 2026-02-14 | 40 |
| 48 | 2026-02-19 | 35 |
| 18 | 2026-02-24 | 30 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-03-21 | 5 |
| 2 | 2026-02-14 | 40 |
| 3 | 2026-03-26 | 0 |
| 4 | 2026-03-07 | 19 |
| 5 | 2026-02-24 | 30 |
| 6 | 2026-03-21 | 5 |
| 7 | 2026-03-19 | 7 |
| 8 | 2026-02-24 | 30 |
| 9 | 2026-03-26 | 0 |
| 10 | 2026-03-26 | 0 |
| 11 | 2026-01-31 | 54 |
| 12 | 2026-03-24 | 2 |
| 13 | 2026-03-03 | 23 |
| 14 | 2026-03-05 | 21 |
| 15 | 2026-02-07 | 47 |
| 16 | 2026-03-14 | 12 |
| 17 | 2026-03-19 | 7 |
| 18 | 2026-02-24 | 30 |
| 19 | 2026-03-24 | 2 |
| 20 | 2026-03-10 | 16 |
| 21 | 2026-02-26 | 28 |
| 22 | 2026-02-28 | 26 |
| 23 | 2026-01-17 | 68 |
| 24 | 2026-01-24 | 61 |
| 25 | 2026-03-24 | 2 |
| 26 | 2026-03-24 | 2 |
| 27 | 2026-03-14 | 12 |
| 28 | 2026-03-17 | 9 |
| 29 | 2026-03-14 | 12 |
| 30 | 2026-02-24 | 30 |
| 31 | 2026-03-19 | 7 |
| 32 | 2026-03-24 | 2 |
| 33 | 2026-01-10 | 75 |
| 34 | 2026-03-26 | 0 |
| 35 | 2026-03-05 | 21 |
| 36 | 2026-03-19 | 7 |
| 37 | 2026-03-05 | 21 |
| 38 | 2026-03-26 | 0 |
| 39 | 2026-03-10 | 16 |
| 40 | 2026-03-21 | 5 |
| 41 | 2026-03-07 | 19 |
| 42 | 2026-02-14 | 40 |
| 43 | 2026-03-21 | 5 |
| 44 | 2026-03-26 | 0 |
| 45 | 2026-03-24 | 2 |
| 46 | 2026-02-26 | 28 |
| 47 | 2026-03-21 | 5 |
| 48 | 2026-02-19 | 35 |
| 49 | 2026-01-31 | 54 |
| 50 | 2026-03-17 | 9 |
| 51 | 2026-03-26 | 0 |
| 52 | 2026-03-17 | 9 |
| 53 | 2026-03-21 | 5 |
| 54 | 2026-03-17 | 9 |
| 55 | 2026-03-19 | 7 |



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

