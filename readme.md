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
| Power 655 | 1366 | 2017-08-01 | 2026-07-02 | 1366 | 00001 | 01366 |
| Power 645 | 1334 | 2017-10-25 | 2026-07-03 | 1334 | 00198 | 01531 |
| Power 535 | 334 | 2025-06-29 | 2026-07-04 | 665 | 00001 | 00741 |
| Keno | 597 | 2022-12-04 | 2026-07-04 | 75162 | #0110271 | #0287138 |
| 3D | 1097 | 2019-04-22 | 2026-07-03 | 1097 | 00001 | 01101 |
| 3D Pro | 743 | 2021-09-14 | 2026-07-02 | 743 | 00001 | 00747 |
| Bingo18 | 569 | 2024-12-03 | 2026-07-04 | 77718 | 0083123 | 0175029 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54] | 2026-07-04T17:51:54.286368 |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23] | 2026-07-04T17:51:54.288114 |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5] | 2026-06-24T00:01:16.333044 |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53, 46] | 2026-06-21T00:01:15.642578 |
| 2026-06-18 | 01360 | [1, 4, 14, 20, 46, 49, 36] | 2026-06-19T00:01:20.356025 |
| 2026-06-16 | 01359 | [2, 4, 5, 7, 31, 40, 14] | 2026-06-17T00:01:06.923555 |
| 2026-06-13 | 01358 | [2, 8, 19, 33, 36, 47, 42] | 2026-06-14T00:01:35.675726 |
| 2026-06-11 | 01357 | [1, 8, 17, 24, 40, 48, 46] | 2026-06-12T00:01:08.901627 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.92 |  | 21 | 171 | 1.79 |  | 41 | 200 | 2.09 |
| 2 | 156 | 1.63 |  | 22 | 203 | 2.12 |  | 42 | 177 | 1.85 |
| 3 | 186 | 1.95 |  | 23 | 184 | 1.92 |  | 43 | 196 | 2.05 |
| 4 | 143 | 1.5 |  | 24 | 173 | 1.81 |  | 44 | 177 | 1.85 |
| 5 | 177 | 1.85 |  | 25 | 156 | 1.63 |  | 45 | 173 | 1.81 |
| 6 | 142 | 1.49 |  | 26 | 165 | 1.73 |  | 46 | 180 | 1.88 |
| 7 | 154 | 1.61 |  | 27 | 158 | 1.65 |  | 47 | 174 | 1.82 |
| 8 | 189 | 1.98 |  | 28 | 157 | 1.64 |  | 48 | 185 | 1.93 |
| 9 | 188 | 1.97 |  | 29 | 187 | 1.96 |  | 49 | 170 | 1.78 |
| 10 | 162 | 1.69 |  | 30 | 159 | 1.66 |  | 50 | 174 | 1.82 |
| 11 | 177 | 1.85 |  | 31 | 182 | 1.9 |  | 51 | 193 | 2.02 |
| 12 | 179 | 1.87 |  | 32 | 184 | 1.92 |  | 52 | 177 | 1.85 |
| 13 | 170 | 1.78 |  | 33 | 173 | 1.81 |  | 53 | 186 | 1.95 |
| 14 | 173 | 1.81 |  | 34 | 195 | 2.04 |  | 54 | 165 | 1.73 |
| 15 | 163 | 1.7 |  | 35 | 168 | 1.76 |  | 55 | 174 | 1.82 |
| 16 | 171 | 1.79 |  | 36 | 165 | 1.73 |  |  |  |  |
| 17 | 157 | 1.64 |  | 37 | 156 | 1.63 |  |  |  |  |
| 18 | 173 | 1.81 |  | 38 | 168 | 1.76 |  |  |  |  |
| 19 | 171 | 1.79 |  | 39 | 167 | 1.75 |  |  |  |  |
| 20 | 185 | 1.93 |  | 40 | 189 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 4.4 |  | 24 | 2 | 2.2 |  | 45 | 1 | 1.1 |
| 2 | 2 | 2.2 |  | 26 | 1 | 1.1 |  | 46 | 4 | 4.4 |
| 3 | 2 | 2.2 |  | 27 | 1 | 1.1 |  | 47 | 2 | 2.2 |
| 4 | 2 | 2.2 |  | 28 | 5 | 5.49 |  | 48 | 1 | 1.1 |
| 5 | 4 | 4.4 |  | 29 | 1 | 1.1 |  | 49 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 52 | 2 | 2.2 |
| 7 | 2 | 2.2 |  | 31 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 8 | 4 | 4.4 |  | 32 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 11 | 2 | 2.2 |  | 33 | 1 | 1.1 |  | 55 | 1 | 1.1 |
| 13 | 2 | 2.2 |  | 34 | 2 | 2.2 |  |  |  |  |
| 14 | 2 | 2.2 |  | 35 | 2 | 2.2 |  |  |  |  |
| 15 | 1 | 1.1 |  | 36 | 2 | 2.2 |  |  |  |  |
| 16 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 17 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 39 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 40 | 3 | 3.3 |  |  |  |  |
| 20 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 22 | 1 | 1.1 |  | 43 | 2 | 2.2 |  |  |  |  |
| 23 | 4 | 4.4 |  | 44 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.3 |  | 22 | 3 | 1.65 |  | 42 | 4 | 2.2 |
| 2 | 4 | 2.2 |  | 23 | 5 | 2.75 |  | 43 | 2 | 1.1 |
| 3 | 5 | 2.75 |  | 24 | 3 | 1.65 |  | 44 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 3 | 1.65 |  | 45 | 3 | 1.65 |
| 5 | 5 | 2.75 |  | 26 | 3 | 1.65 |  | 46 | 6 | 3.3 |
| 6 | 2 | 1.1 |  | 27 | 2 | 1.1 |  | 47 | 4 | 2.2 |
| 7 | 2 | 1.1 |  | 28 | 7 | 3.85 |  | 48 | 3 | 1.65 |
| 8 | 8 | 4.4 |  | 29 | 2 | 1.1 |  | 49 | 3 | 1.65 |
| 10 | 1 | 0.55 |  | 30 | 2 | 1.1 |  | 50 | 4 | 2.2 |
| 11 | 4 | 2.2 |  | 31 | 3 | 1.65 |  | 51 | 1 | 0.55 |
| 12 | 1 | 0.55 |  | 32 | 5 | 2.75 |  | 52 | 2 | 1.1 |
| 13 | 3 | 1.65 |  | 33 | 2 | 1.1 |  | 53 | 3 | 1.65 |
| 14 | 4 | 2.2 |  | 34 | 4 | 2.2 |  | 54 | 2 | 1.1 |
| 15 | 3 | 1.65 |  | 35 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 16 | 5 | 2.75 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 3 | 1.65 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 3 | 1.65 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 5 | 2.75 |  |  |  |  |
| 20 | 3 | 1.65 |  | 40 | 5 | 2.75 |  |  |  |  |
| 21 | 4 | 2.2 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 2.63 |  | 21 | 6 | 2.26 |  | 41 | 5 | 1.88 |
| 2 | 5 | 1.88 |  | 22 | 8 | 3.01 |  | 42 | 4 | 1.5 |
| 3 | 5 | 1.88 |  | 23 | 6 | 2.26 |  | 43 | 3 | 1.13 |
| 4 | 4 | 1.5 |  | 24 | 5 | 1.88 |  | 44 | 4 | 1.5 |
| 5 | 6 | 2.26 |  | 25 | 5 | 1.88 |  | 45 | 3 | 1.13 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 7 | 2.63 |
| 7 | 5 | 1.88 |  | 27 | 2 | 0.75 |  | 47 | 6 | 2.26 |
| 8 | 10 | 3.76 |  | 28 | 9 | 3.38 |  | 48 | 3 | 1.13 |
| 9 | 3 | 1.13 |  | 29 | 6 | 2.26 |  | 49 | 4 | 1.5 |
| 10 | 2 | 0.75 |  | 30 | 3 | 1.13 |  | 50 | 6 | 2.26 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 3 | 1.13 |
| 12 | 1 | 0.38 |  | 32 | 6 | 2.26 |  | 52 | 4 | 1.5 |
| 13 | 5 | 1.88 |  | 33 | 4 | 1.5 |  | 53 | 9 | 3.38 |
| 14 | 4 | 1.5 |  | 34 | 5 | 1.88 |  | 54 | 2 | 0.75 |
| 15 | 6 | 2.26 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 9 | 3.38 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 5 | 1.88 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 9 | 2026-05-02 | 61 |
| 10 | 2026-05-09 | 54 |
| 50 | 2026-05-16 | 47 |
| 12 | 2026-05-19 | 44 |
| 25 | 2026-05-30 | 33 |
| 51 | 2026-06-02 | 30 |
| 45 | 2026-06-04 | 28 |
| 29 | 2026-06-04 | 28 |
| 39 | 2026-06-06 | 26 |
| 37 | 2026-06-06 | 26 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 7 |
| 2 | 2026-06-16 | 16 |
| 3 | 2026-06-25 | 7 |
| 4 | 2026-06-18 | 14 |
| 5 | 2026-07-02 | 0 |
| 6 | 2026-06-09 | 23 |
| 7 | 2026-06-27 | 5 |
| 8 | 2026-06-25 | 7 |
| 9 | 2026-05-02 | 61 |
| 10 | 2026-05-09 | 54 |
| 11 | 2026-07-02 | 0 |
| 12 | 2026-05-19 | 44 |
| 13 | 2026-06-30 | 2 |
| 14 | 2026-06-18 | 14 |
| 15 | 2026-06-25 | 7 |
| 16 | 2026-06-27 | 5 |
| 17 | 2026-06-11 | 21 |
| 18 | 2026-06-30 | 2 |
| 19 | 2026-06-13 | 19 |
| 20 | 2026-06-18 | 14 |
| 21 | 2026-06-27 | 5 |
| 22 | 2026-06-30 | 2 |
| 23 | 2026-06-27 | 5 |
| 24 | 2026-06-11 | 21 |
| 25 | 2026-05-30 | 33 |
| 26 | 2026-06-20 | 12 |
| 27 | 2026-06-09 | 23 |
| 28 | 2026-07-02 | 0 |
| 29 | 2026-06-04 | 28 |
| 30 | 2026-06-20 | 12 |
| 31 | 2026-06-16 | 16 |
| 32 | 2026-06-09 | 23 |
| 33 | 2026-06-13 | 19 |
| 34 | 2026-07-02 | 0 |
| 35 | 2026-06-25 | 7 |
| 36 | 2026-06-18 | 14 |
| 37 | 2026-06-06 | 26 |
| 38 | 2026-06-23 | 9 |
| 39 | 2026-06-06 | 26 |
| 40 | 2026-06-23 | 9 |
| 41 | 2026-07-02 | 0 |
| 42 | 2026-07-02 | 0 |
| 43 | 2026-06-30 | 2 |
| 44 | 2026-06-30 | 2 |
| 45 | 2026-06-04 | 28 |
| 46 | 2026-06-23 | 9 |
| 47 | 2026-06-30 | 2 |
| 48 | 2026-06-11 | 21 |
| 49 | 2026-07-02 | 0 |
| 50 | 2026-05-16 | 47 |
| 51 | 2026-06-02 | 30 |
| 52 | 2026-06-27 | 5 |
| 53 | 2026-06-20 | 12 |
| 54 | 2026-06-27 | 5 |
| 55 | 2026-06-25 | 7 |



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

