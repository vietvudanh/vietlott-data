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
| Power 655 | 1373 | 2017-08-01 | 2026-07-18 | 1373 | 00001 | 01373 |
| Power 645 | 1341 | 2017-10-25 | 2026-07-19 | 1341 | 00198 | 01538 |
| Power 535 | 350 | 2025-06-29 | 2026-07-20 | 698 | 00001 | 00774 |
| Keno | 618 | 2022-12-04 | 2026-07-21 | 77609 | #0110271 | #0289116 |
| 3D | 1104 | 2019-04-22 | 2026-07-20 | 1104 | 00001 | 01108 |
| 3D Pro | 750 | 2021-09-14 | 2026-07-18 | 750 | 00001 | 00754 |
| Bingo18 | 594 | 2024-12-03 | 2026-07-21 | 81790 | 0083123 | 0177672 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] | 2026-07-19T00:01:43.344602 |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] | 2026-07-17T00:01:22.153181 |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] | 2026-07-15T00:01:11.127525 |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40] | 2026-07-12T18:49:36.892797 |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45] | 2026-07-12T18:49:36.894485 |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8] | 2026-07-12T18:49:36.896159 |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] | 2026-07-05T00:01:16.742550 |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49] | 2026-07-04T17:51:54.277165 |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47] | 2026-07-04T17:51:54.284547 |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54] | 2026-07-04T17:51:54.286368 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 184 | 1.91 |  | 21 | 172 | 1.79 |  | 41 | 203 | 2.11 |
| 2 | 157 | 1.63 |  | 22 | 204 | 2.12 |  | 42 | 178 | 1.85 |
| 3 | 186 | 1.94 |  | 23 | 185 | 1.93 |  | 43 | 197 | 2.05 |
| 4 | 144 | 1.5 |  | 24 | 174 | 1.81 |  | 44 | 178 | 1.85 |
| 5 | 177 | 1.84 |  | 25 | 157 | 1.63 |  | 45 | 177 | 1.84 |
| 6 | 143 | 1.49 |  | 26 | 165 | 1.72 |  | 46 | 180 | 1.87 |
| 7 | 154 | 1.6 |  | 27 | 158 | 1.64 |  | 47 | 174 | 1.81 |
| 8 | 190 | 1.98 |  | 28 | 157 | 1.63 |  | 48 | 187 | 1.95 |
| 9 | 190 | 1.98 |  | 29 | 187 | 1.95 |  | 49 | 171 | 1.78 |
| 10 | 164 | 1.71 |  | 30 | 160 | 1.66 |  | 50 | 174 | 1.81 |
| 11 | 177 | 1.84 |  | 31 | 183 | 1.9 |  | 51 | 194 | 2.02 |
| 12 | 179 | 1.86 |  | 32 | 185 | 1.93 |  | 52 | 177 | 1.84 |
| 13 | 171 | 1.78 |  | 33 | 177 | 1.84 |  | 53 | 187 | 1.95 |
| 14 | 174 | 1.81 |  | 34 | 195 | 2.03 |  | 54 | 166 | 1.73 |
| 15 | 164 | 1.71 |  | 35 | 169 | 1.76 |  | 55 | 175 | 1.82 |
| 16 | 172 | 1.79 |  | 36 | 165 | 1.72 |  |  |  |  |
| 17 | 159 | 1.65 |  | 37 | 156 | 1.62 |  |  |  |  |
| 18 | 174 | 1.81 |  | 38 | 168 | 1.75 |  |  |  |  |
| 19 | 172 | 1.79 |  | 39 | 167 | 1.74 |  |  |  |  |
| 20 | 187 | 1.95 |  | 40 | 190 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.38 |  | 22 | 2 | 2.38 |  | 48 | 2 | 2.38 |
| 2 | 1 | 1.19 |  | 23 | 3 | 3.57 |  | 49 | 2 | 2.38 |
| 3 | 1 | 1.19 |  | 24 | 1 | 1.19 |  | 51 | 1 | 1.19 |
| 4 | 1 | 1.19 |  | 25 | 1 | 1.19 |  | 52 | 1 | 1.19 |
| 5 | 3 | 3.57 |  | 28 | 3 | 3.57 |  | 53 | 1 | 1.19 |
| 6 | 1 | 1.19 |  | 30 | 1 | 1.19 |  | 54 | 2 | 2.38 |
| 7 | 1 | 1.19 |  | 31 | 1 | 1.19 |  | 55 | 2 | 2.38 |
| 8 | 2 | 2.38 |  | 32 | 1 | 1.19 |  |  |  |  |
| 9 | 2 | 2.38 |  | 33 | 4 | 4.76 |  |  |  |  |
| 10 | 2 | 2.38 |  | 34 | 1 | 1.19 |  |  |  |  |
| 11 | 1 | 1.19 |  | 35 | 2 | 2.38 |  |  |  |  |
| 13 | 3 | 3.57 |  | 38 | 1 | 1.19 |  |  |  |  |
| 14 | 1 | 1.19 |  | 40 | 2 | 2.38 |  |  |  |  |
| 15 | 2 | 2.38 |  | 41 | 4 | 4.76 |  |  |  |  |
| 16 | 2 | 2.38 |  | 42 | 2 | 2.38 |  |  |  |  |
| 17 | 2 | 2.38 |  | 43 | 2 | 2.38 |  |  |  |  |
| 18 | 2 | 2.38 |  | 44 | 2 | 2.38 |  |  |  |  |
| 19 | 1 | 1.19 |  | 45 | 4 | 4.76 |  |  |  |  |
| 20 | 2 | 2.38 |  | 46 | 1 | 1.19 |  |  |  |  |
| 21 | 2 | 2.38 |  | 47 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3.43 |  | 22 | 3 | 1.71 |  | 42 | 5 | 2.86 |
| 2 | 4 | 2.29 |  | 23 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 3 | 4 | 2.29 |  | 24 | 4 | 2.29 |  | 44 | 3 | 1.71 |
| 4 | 3 | 1.71 |  | 25 | 3 | 1.71 |  | 45 | 5 | 2.86 |
| 5 | 5 | 2.86 |  | 26 | 1 | 0.57 |  | 46 | 4 | 2.29 |
| 6 | 2 | 1.14 |  | 27 | 2 | 1.14 |  | 47 | 2 | 1.14 |
| 7 | 2 | 1.14 |  | 28 | 5 | 2.86 |  | 48 | 3 | 1.71 |
| 8 | 7 | 4.0 |  | 29 | 2 | 1.14 |  | 49 | 4 | 2.29 |
| 9 | 2 | 1.14 |  | 30 | 2 | 1.14 |  | 51 | 2 | 1.14 |
| 10 | 2 | 1.14 |  | 31 | 3 | 1.71 |  | 52 | 2 | 1.14 |
| 11 | 3 | 1.71 |  | 32 | 2 | 1.14 |  | 53 | 3 | 1.71 |
| 13 | 3 | 1.71 |  | 33 | 5 | 2.86 |  | 54 | 3 | 1.71 |
| 14 | 4 | 2.29 |  | 34 | 3 | 1.71 |  | 55 | 2 | 1.14 |
| 15 | 3 | 1.71 |  | 35 | 3 | 1.71 |  |  |  |  |
| 16 | 5 | 2.86 |  | 36 | 2 | 1.14 |  |  |  |  |
| 17 | 4 | 2.29 |  | 37 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 3 | 1.71 |  | 39 | 2 | 1.14 |  |  |  |  |
| 20 | 4 | 2.29 |  | 40 | 4 | 2.29 |  |  |  |  |
| 21 | 4 | 2.29 |  | 41 | 5 | 2.86 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 2.26 |  | 21 | 7 | 2.63 |  | 41 | 7 | 2.63 |
| 2 | 5 | 1.88 |  | 22 | 6 | 2.26 |  | 42 | 5 | 1.88 |
| 3 | 5 | 1.88 |  | 23 | 6 | 2.26 |  | 43 | 4 | 1.5 |
| 4 | 5 | 1.88 |  | 24 | 5 | 1.88 |  | 44 | 4 | 1.5 |
| 5 | 6 | 2.26 |  | 25 | 6 | 2.26 |  | 45 | 7 | 2.63 |
| 6 | 3 | 1.13 |  | 26 | 4 | 1.5 |  | 46 | 7 | 2.63 |
| 7 | 3 | 1.13 |  | 27 | 2 | 0.75 |  | 47 | 4 | 1.5 |
| 8 | 9 | 3.38 |  | 28 | 7 | 2.63 |  | 48 | 5 | 1.88 |
| 9 | 4 | 1.5 |  | 29 | 4 | 1.5 |  | 49 | 4 | 1.5 |
| 10 | 4 | 1.5 |  | 30 | 3 | 1.13 |  | 50 | 5 | 1.88 |
| 11 | 4 | 1.5 |  | 31 | 4 | 1.5 |  | 51 | 4 | 1.5 |
| 12 | 1 | 0.38 |  | 32 | 6 | 2.26 |  | 52 | 3 | 1.13 |
| 13 | 4 | 1.5 |  | 33 | 8 | 3.01 |  | 53 | 6 | 2.26 |
| 14 | 5 | 1.88 |  | 34 | 5 | 1.88 |  | 54 | 3 | 1.13 |
| 15 | 5 | 1.88 |  | 35 | 4 | 1.5 |  | 55 | 5 | 1.88 |
| 16 | 8 | 3.01 |  | 36 | 3 | 1.13 |  |  |  |  |
| 17 | 7 | 2.63 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 3 | 1.13 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 5 | 1.88 |  |  |  |  |
| 20 | 5 | 1.88 |  | 40 | 6 | 2.26 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 50 | 2026-05-16 | 63 |
| 12 | 2026-05-19 | 60 |
| 29 | 2026-06-04 | 44 |
| 39 | 2026-06-06 | 42 |
| 37 | 2026-06-06 | 42 |
| 27 | 2026-06-09 | 39 |
| 36 | 2026-06-18 | 30 |
| 26 | 2026-06-20 | 28 |
| 46 | 2026-06-23 | 25 |
| 38 | 2026-06-23 | 25 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-25 | 23 |
| 2 | 2026-07-09 | 9 |
| 3 | 2026-06-25 | 23 |
| 4 | 2026-07-07 | 11 |
| 5 | 2026-07-02 | 16 |
| 6 | 2026-07-07 | 11 |
| 7 | 2026-06-27 | 21 |
| 8 | 2026-07-07 | 11 |
| 9 | 2026-07-11 | 7 |
| 10 | 2026-07-14 | 4 |
| 11 | 2026-07-02 | 16 |
| 12 | 2026-05-19 | 60 |
| 13 | 2026-07-04 | 14 |
| 14 | 2026-07-09 | 9 |
| 15 | 2026-07-04 | 14 |
| 16 | 2026-07-18 | 0 |
| 17 | 2026-07-11 | 7 |
| 18 | 2026-07-04 | 14 |
| 19 | 2026-07-16 | 2 |
| 20 | 2026-07-16 | 2 |
| 21 | 2026-07-16 | 2 |
| 22 | 2026-07-18 | 0 |
| 23 | 2026-07-04 | 14 |
| 24 | 2026-07-14 | 4 |
| 25 | 2026-07-07 | 11 |
| 26 | 2026-06-20 | 28 |
| 27 | 2026-06-09 | 39 |
| 28 | 2026-07-02 | 16 |
| 29 | 2026-06-04 | 44 |
| 30 | 2026-07-14 | 4 |
| 31 | 2026-07-04 | 14 |
| 32 | 2026-07-07 | 11 |
| 33 | 2026-07-16 | 2 |
| 34 | 2026-07-02 | 16 |
| 35 | 2026-07-14 | 4 |
| 36 | 2026-06-18 | 30 |
| 37 | 2026-06-06 | 42 |
| 38 | 2026-06-23 | 25 |
| 39 | 2026-06-06 | 42 |
| 40 | 2026-07-11 | 7 |
| 41 | 2026-07-18 | 0 |
| 42 | 2026-07-11 | 7 |
| 43 | 2026-07-04 | 14 |
| 44 | 2026-07-07 | 11 |
| 45 | 2026-07-18 | 0 |
| 46 | 2026-06-23 | 25 |
| 47 | 2026-06-30 | 18 |
| 48 | 2026-07-18 | 0 |
| 49 | 2026-07-09 | 9 |
| 50 | 2026-05-16 | 63 |
| 51 | 2026-07-14 | 4 |
| 52 | 2026-06-27 | 21 |
| 53 | 2026-07-16 | 2 |
| 54 | 2026-07-18 | 0 |
| 55 | 2026-07-18 | 0 |



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

