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
| Power 655 | 1362 | 2017-08-01 | 2026-06-23 | 1362 | 00001 | 01362 |
| Power 645 | 1330 | 2017-10-25 | 2026-06-24 | 1330 | 00198 | 01527 |
| Power 535 | 325 | 2025-06-29 | 2026-06-24 | 649 | 00001 | 00722 |
| Keno | 594 | 2022-12-04 | 2026-06-25 | 74804 | #0110271 | #0286022 |
| 3D | 1093 | 2019-04-22 | 2026-06-24 | 1093 | 00001 | 01097 |
| 3D Pro | 739 | 2021-09-14 | 2026-06-23 | 739 | 00001 | 00743 |
| Bingo18 | 568 | 2024-12-03 | 2026-06-25 | 77638 | 0083123 | 0173538 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5] | 2026-06-24T00:01:16.333044 |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53, 46] | 2026-06-21T00:01:15.642578 |
| 2026-06-18 | 01360 | [1, 4, 14, 20, 46, 49, 36] | 2026-06-19T00:01:20.356025 |
| 2026-06-16 | 01359 | [2, 4, 5, 7, 31, 40, 14] | 2026-06-17T00:01:06.923555 |
| 2026-06-13 | 01358 | [2, 8, 19, 33, 36, 47, 42] | 2026-06-14T00:01:35.675726 |
| 2026-06-11 | 01357 | [1, 8, 17, 24, 40, 48, 46] | 2026-06-12T00:01:08.901627 |
| 2026-06-09 | 01356 | [6, 8, 18, 27, 32, 34, 35] | 2026-06-10T00:01:14.808665 |
| 2026-06-06 | 01355 | [3, 11, 16, 37, 39, 41, 28] | 2026-06-09T00:01:21.410974 |
| 2026-06-04 | 01354 | [23, 24, 28, 29, 39, 43, 45] | 2026-06-05T00:01:07.859417 |
| 2026-06-02 | 01353 | [1, 3, 5, 16, 37, 51, 42] | 2026-06-03T00:01:21.144685 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 183 | 1.92 |  | 21 | 170 | 1.78 |  | 41 | 199 | 2.09 |
| 2 | 156 | 1.64 |  | 22 | 202 | 2.12 |  | 42 | 176 | 1.85 |
| 3 | 185 | 1.94 |  | 23 | 182 | 1.91 |  | 43 | 195 | 2.05 |
| 4 | 143 | 1.5 |  | 24 | 173 | 1.81 |  | 44 | 176 | 1.85 |
| 5 | 175 | 1.84 |  | 25 | 156 | 1.64 |  | 45 | 173 | 1.81 |
| 6 | 142 | 1.49 |  | 26 | 165 | 1.73 |  | 46 | 180 | 1.89 |
| 7 | 153 | 1.6 |  | 27 | 158 | 1.66 |  | 47 | 173 | 1.81 |
| 8 | 188 | 1.97 |  | 28 | 155 | 1.63 |  | 48 | 185 | 1.94 |
| 9 | 188 | 1.97 |  | 29 | 187 | 1.96 |  | 49 | 169 | 1.77 |
| 10 | 162 | 1.7 |  | 30 | 159 | 1.67 |  | 50 | 174 | 1.83 |
| 11 | 176 | 1.85 |  | 31 | 182 | 1.91 |  | 51 | 193 | 2.02 |
| 12 | 179 | 1.88 |  | 32 | 184 | 1.93 |  | 52 | 176 | 1.85 |
| 13 | 169 | 1.77 |  | 33 | 173 | 1.81 |  | 53 | 186 | 1.95 |
| 14 | 173 | 1.81 |  | 34 | 194 | 2.04 |  | 54 | 164 | 1.72 |
| 15 | 162 | 1.7 |  | 35 | 167 | 1.75 |  | 55 | 173 | 1.81 |
| 16 | 170 | 1.78 |  | 36 | 165 | 1.73 |  |  |  |  |
| 17 | 157 | 1.65 |  | 37 | 156 | 1.64 |  |  |  |  |
| 18 | 172 | 1.8 |  | 38 | 168 | 1.76 |  |  |  |  |
| 19 | 171 | 1.79 |  | 39 | 167 | 1.75 |  |  |  |  |
| 20 | 185 | 1.94 |  | 40 | 189 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 5.49 |  | 25 | 2 | 2.2 |  | 45 | 1 | 1.1 |
| 2 | 3 | 3.3 |  | 26 | 1 | 1.1 |  | 46 | 4 | 4.4 |
| 3 | 2 | 2.2 |  | 27 | 1 | 1.1 |  | 47 | 1 | 1.1 |
| 4 | 2 | 2.2 |  | 28 | 3 | 3.3 |  | 48 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 29 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 31 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 8 | 5 | 5.49 |  | 32 | 1 | 1.1 |  | 53 | 2 | 2.2 |
| 11 | 2 | 2.2 |  | 33 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 13 | 1 | 1.1 |  | 34 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 35 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 36 | 2 | 2.2 |  |  |  |  |
| 16 | 3 | 3.3 |  | 37 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 18 | 1 | 1.1 |  | 39 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 40 | 3 | 3.3 |  |  |  |  |
| 20 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 21 | 1 | 1.1 |  | 42 | 3 | 3.3 |  |  |  |  |
| 23 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 24 | 3 | 3.3 |  | 44 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 2.86 |  | 21 | 5 | 2.86 |  | 41 | 2 | 1.14 |
| 2 | 4 | 2.29 |  | 22 | 3 | 1.71 |  | 42 | 3 | 1.71 |
| 3 | 4 | 2.29 |  | 23 | 3 | 1.71 |  | 43 | 1 | 0.57 |
| 4 | 3 | 1.71 |  | 24 | 4 | 2.29 |  | 44 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 25 | 5 | 2.86 |  | 45 | 3 | 1.71 |
| 6 | 2 | 1.14 |  | 26 | 4 | 2.29 |  | 46 | 6 | 3.43 |
| 7 | 1 | 0.57 |  | 27 | 2 | 1.14 |  | 47 | 3 | 1.71 |
| 8 | 7 | 4.0 |  | 28 | 5 | 2.86 |  | 48 | 3 | 1.71 |
| 9 | 2 | 1.14 |  | 29 | 3 | 1.71 |  | 49 | 2 | 1.14 |
| 10 | 1 | 0.57 |  | 30 | 2 | 1.14 |  | 50 | 5 | 2.86 |
| 11 | 3 | 1.71 |  | 31 | 3 | 1.71 |  | 51 | 3 | 1.71 |
| 12 | 1 | 0.57 |  | 32 | 5 | 2.86 |  | 52 | 2 | 1.14 |
| 13 | 2 | 1.14 |  | 33 | 3 | 1.71 |  | 53 | 4 | 2.29 |
| 14 | 4 | 2.29 |  | 34 | 4 | 2.29 |  | 54 | 1 | 0.57 |
| 15 | 3 | 1.71 |  | 35 | 2 | 1.14 |  | 55 | 2 | 1.14 |
| 16 | 5 | 2.86 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 2 | 1.14 |  | 38 | 3 | 1.71 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 5 | 2.86 |  |  |  |  |
| 20 | 3 | 1.71 |  | 40 | 5 | 2.86 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.26 |  | 21 | 7 | 2.63 |  | 41 | 4 | 1.5 |
| 2 | 5 | 1.88 |  | 22 | 9 | 3.38 |  | 42 | 4 | 1.5 |
| 3 | 4 | 1.5 |  | 23 | 5 | 1.88 |  | 43 | 3 | 1.13 |
| 4 | 4 | 1.5 |  | 24 | 5 | 1.88 |  | 44 | 3 | 1.13 |
| 5 | 5 | 1.88 |  | 25 | 5 | 1.88 |  | 45 | 3 | 1.13 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 7 | 2.63 |
| 7 | 6 | 2.26 |  | 27 | 2 | 0.75 |  | 47 | 5 | 1.88 |
| 8 | 9 | 3.38 |  | 28 | 7 | 2.63 |  | 48 | 4 | 1.5 |
| 9 | 4 | 1.5 |  | 29 | 6 | 2.26 |  | 49 | 3 | 1.13 |
| 10 | 3 | 1.13 |  | 30 | 5 | 1.88 |  | 50 | 6 | 2.26 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 3 | 1.13 |
| 12 | 1 | 0.38 |  | 32 | 7 | 2.63 |  | 52 | 4 | 1.5 |
| 13 | 5 | 1.88 |  | 33 | 5 | 1.88 |  | 53 | 10 | 3.76 |
| 14 | 4 | 1.5 |  | 34 | 5 | 1.88 |  | 54 | 2 | 0.75 |
| 15 | 6 | 2.26 |  | 35 | 3 | 1.13 |  | 55 | 4 | 1.5 |
| 16 | 9 | 3.38 |  | 36 | 4 | 1.5 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 9 | 3.38 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 6 | 2.26 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 9 | 2026-05-02 | 52 |
| 10 | 2026-05-09 | 45 |
| 55 | 2026-05-14 | 40 |
| 50 | 2026-05-16 | 38 |
| 12 | 2026-05-19 | 35 |
| 22 | 2026-05-23 | 31 |
| 15 | 2026-05-26 | 28 |
| 54 | 2026-05-28 | 26 |
| 21 | 2026-05-28 | 26 |
| 25 | 2026-05-30 | 24 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-23 | 0 |
| 2 | 2026-06-16 | 7 |
| 3 | 2026-06-06 | 17 |
| 4 | 2026-06-18 | 5 |
| 5 | 2026-06-23 | 0 |
| 6 | 2026-06-09 | 14 |
| 7 | 2026-06-16 | 7 |
| 8 | 2026-06-13 | 10 |
| 9 | 2026-05-02 | 52 |
| 10 | 2026-05-09 | 45 |
| 11 | 2026-06-06 | 17 |
| 12 | 2026-05-19 | 35 |
| 13 | 2026-06-23 | 0 |
| 14 | 2026-06-18 | 5 |
| 15 | 2026-05-26 | 28 |
| 16 | 2026-06-20 | 3 |
| 17 | 2026-06-11 | 12 |
| 18 | 2026-06-09 | 14 |
| 19 | 2026-06-13 | 10 |
| 20 | 2026-06-18 | 5 |
| 21 | 2026-05-28 | 26 |
| 22 | 2026-05-23 | 31 |
| 23 | 2026-06-20 | 3 |
| 24 | 2026-06-11 | 12 |
| 25 | 2026-05-30 | 24 |
| 26 | 2026-06-20 | 3 |
| 27 | 2026-06-09 | 14 |
| 28 | 2026-06-23 | 0 |
| 29 | 2026-06-04 | 19 |
| 30 | 2026-06-20 | 3 |
| 31 | 2026-06-16 | 7 |
| 32 | 2026-06-09 | 14 |
| 33 | 2026-06-13 | 10 |
| 34 | 2026-06-09 | 14 |
| 35 | 2026-06-09 | 14 |
| 36 | 2026-06-18 | 5 |
| 37 | 2026-06-06 | 17 |
| 38 | 2026-06-23 | 0 |
| 39 | 2026-06-06 | 17 |
| 40 | 2026-06-23 | 0 |
| 41 | 2026-06-06 | 17 |
| 42 | 2026-06-13 | 10 |
| 43 | 2026-06-04 | 19 |
| 44 | 2026-05-30 | 24 |
| 45 | 2026-06-04 | 19 |
| 46 | 2026-06-23 | 0 |
| 47 | 2026-06-13 | 10 |
| 48 | 2026-06-11 | 12 |
| 49 | 2026-06-18 | 5 |
| 50 | 2026-05-16 | 38 |
| 51 | 2026-06-02 | 21 |
| 52 | 2026-06-20 | 3 |
| 53 | 2026-06-20 | 3 |
| 54 | 2026-05-28 | 26 |
| 55 | 2026-05-14 | 40 |



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

