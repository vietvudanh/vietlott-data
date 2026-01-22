# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

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

- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [Predictions](#-predictions)
- [📊 Data Statistics](#-data-statistics)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## Predictions

Predicitons models are at [/src/predictions](./src/machine_learning/prediction_summary.md)

## 📊 Data Statistics

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 1297 | 2017-08-01 | 2026-01-20 | 1297 | 00001 | 01297 |
| Power 645 | 1264 | 2017-10-25 | 2026-01-21 | 1264 | 00198 | 01461 |
| Power 535 | 183 | 2025-06-29 | 2026-01-21 | 366 | 00001 | 00414 |
| Keno | 439 | 2022-12-04 | 2026-01-22 | 56210 | #0110271 | #0267699 |
| 3D | 1028 | 2019-04-22 | 2026-01-21 | 1028 | 00001 | 01032 |
| 3D Pro | 674 | 2021-09-14 | 2026-01-20 | 674 | 00001 | 00678 |
| Bingo18 | 414 | 2024-12-03 | 2026-01-22 | 53517 | 0083123 | 0149066 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-01-20 | 01297 | [4, 20, 26, 28, 37, 41, 32] | 2026-01-21T00:00:50.678079 |
| 2026-01-17 | 01296 | [14, 21, 23, 25, 46, 48, 54] | 2026-01-19T21:35:27.120844 |
| 2026-01-15 | 01295 | [13, 21, 31, 34, 48, 55, 27] | 2026-01-16T00:00:56.117552 |
| 2026-01-13 | 01294 | [3, 12, 25, 51, 52, 55, 43] | 2026-01-14T00:00:52.922646 |
| 2026-01-10 | 01293 | [9, 16, 30, 33, 34, 38, 49] | 2026-01-11T00:00:48.139236 |
| 2026-01-08 | 01292 | [20, 22, 36, 43, 45, 50, 47] | 2026-01-09T00:00:54.645813 |
| 2026-01-06 | 01291 | [22, 28, 29, 30, 34, 47, 20] | 2026-01-07T00:00:54.634335 |
| 2026-01-03 | 01290 | [10, 16, 17, 23, 33, 36, 42] | 2026-01-04T00:00:56.590991 |
| 2026-01-01 | 01289 | [5, 16, 29, 33, 39, 42, 54] | 2026-01-02T00:00:56.179609 |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55, 38] | 2025-12-31T00:00:53.630435 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.91 |  | 21 | 160 | 1.76 |  | 41 | 193 | 2.13 |
| 2 | 149 | 1.64 |  | 22 | 188 | 2.07 |  | 42 | 170 | 1.87 |
| 3 | 176 | 1.94 |  | 23 | 177 | 1.95 |  | 43 | 187 | 2.06 |
| 4 | 137 | 1.51 |  | 24 | 167 | 1.84 |  | 44 | 170 | 1.87 |
| 5 | 166 | 1.83 |  | 25 | 146 | 1.61 |  | 45 | 165 | 1.82 |
| 6 | 139 | 1.53 |  | 26 | 151 | 1.66 |  | 46 | 169 | 1.86 |
| 7 | 141 | 1.55 |  | 27 | 153 | 1.69 |  | 47 | 165 | 1.82 |
| 8 | 177 | 1.95 |  | 28 | 145 | 1.6 |  | 48 | 178 | 1.96 |
| 9 | 181 | 1.99 |  | 29 | 175 | 1.93 |  | 49 | 165 | 1.82 |
| 10 | 156 | 1.72 |  | 30 | 150 | 1.65 |  | 50 | 164 | 1.81 |
| 11 | 170 | 1.87 |  | 31 | 174 | 1.92 |  | 51 | 185 | 2.04 |
| 12 | 173 | 1.91 |  | 32 | 170 | 1.87 |  | 52 | 169 | 1.86 |
| 13 | 158 | 1.74 |  | 33 | 168 | 1.85 |  | 53 | 170 | 1.87 |
| 14 | 166 | 1.83 |  | 34 | 186 | 2.05 |  | 54 | 155 | 1.71 |
| 15 | 153 | 1.69 |  | 35 | 162 | 1.78 |  | 55 | 165 | 1.82 |
| 16 | 158 | 1.74 |  | 36 | 156 | 1.72 |  |  |  |  |
| 17 | 149 | 1.64 |  | 37 | 151 | 1.66 |  |  |  |  |
| 18 | 166 | 1.83 |  | 38 | 160 | 1.76 |  |  |  |  |
| 19 | 166 | 1.83 |  | 39 | 156 | 1.72 |  |  |  |  |
| 20 | 178 | 1.96 |  | 40 | 181 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 28 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 3 | 2 | 2.2 |  | 29 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 4 | 2 | 2.2 |  | 30 | 4 | 4.4 |  | 51 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 52 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 32 | 3 | 3.3 |  | 54 | 2 | 2.2 |
| 9 | 1 | 1.1 |  | 33 | 3 | 3.3 |  | 55 | 3 | 3.3 |
| 10 | 2 | 2.2 |  | 34 | 3 | 3.3 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 36 | 2 | 2.2 |  |  |  |  |
| 13 | 2 | 2.2 |  | 37 | 3 | 3.3 |  |  |  |  |
| 14 | 1 | 1.1 |  | 38 | 4 | 4.4 |  |  |  |  |
| 16 | 5 | 5.49 |  | 39 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 20 | 3 | 3.3 |  | 41 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 42 | 2 | 2.2 |  |  |  |  |
| 22 | 2 | 2.2 |  | 43 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 45 | 1 | 1.1 |  |  |  |  |
| 25 | 3 | 3.3 |  | 46 | 1 | 1.1 |  |  |  |  |
| 26 | 1 | 1.1 |  | 47 | 2 | 2.2 |  |  |  |  |
| 27 | 1 | 1.1 |  | 48 | 4 | 4.4 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 0.57 |  | 23 | 4 | 2.29 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 24 | 2 | 1.14 |  | 44 | 1 | 0.57 |
| 4 | 5 | 2.86 |  | 25 | 3 | 1.71 |  | 45 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 26 | 3 | 1.71 |  | 46 | 3 | 1.71 |
| 6 | 1 | 0.57 |  | 27 | 3 | 1.71 |  | 47 | 2 | 1.14 |
| 7 | 1 | 0.57 |  | 28 | 3 | 1.71 |  | 48 | 7 | 4.0 |
| 8 | 1 | 0.57 |  | 29 | 4 | 2.29 |  | 49 | 1 | 0.57 |
| 9 | 3 | 1.71 |  | 30 | 5 | 2.86 |  | 50 | 3 | 1.71 |
| 10 | 5 | 2.86 |  | 31 | 3 | 1.71 |  | 51 | 2 | 1.14 |
| 11 | 2 | 1.14 |  | 32 | 6 | 3.43 |  | 52 | 4 | 2.29 |
| 12 | 4 | 2.29 |  | 33 | 5 | 2.86 |  | 53 | 1 | 0.57 |
| 13 | 3 | 1.71 |  | 34 | 4 | 2.29 |  | 54 | 3 | 1.71 |
| 14 | 4 | 2.29 |  | 35 | 3 | 1.71 |  | 55 | 6 | 3.43 |
| 15 | 1 | 0.57 |  | 36 | 4 | 2.29 |  |  |  |  |
| 16 | 6 | 3.43 |  | 37 | 5 | 2.86 |  |  |  |  |
| 17 | 1 | 0.57 |  | 38 | 8 | 4.57 |  |  |  |  |
| 18 | 1 | 0.57 |  | 39 | 3 | 1.71 |  |  |  |  |
| 20 | 6 | 3.43 |  | 40 | 4 | 2.29 |  |  |  |  |
| 21 | 5 | 2.86 |  | 41 | 3 | 1.71 |  |  |  |  |
| 22 | 3 | 1.71 |  | 42 | 4 | 2.29 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.38 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 2 | 0.75 |  | 22 | 6 | 2.26 |  | 42 | 6 | 2.26 |
| 3 | 4 | 1.5 |  | 23 | 5 | 1.88 |  | 43 | 5 | 1.88 |
| 4 | 5 | 1.88 |  | 24 | 3 | 1.13 |  | 44 | 2 | 0.75 |
| 5 | 5 | 1.88 |  | 25 | 4 | 1.5 |  | 45 | 4 | 1.5 |
| 6 | 3 | 1.13 |  | 26 | 3 | 1.13 |  | 46 | 4 | 1.5 |
| 7 | 3 | 1.13 |  | 27 | 6 | 2.26 |  | 47 | 4 | 1.5 |
| 8 | 4 | 1.5 |  | 28 | 5 | 1.88 |  | 48 | 7 | 2.63 |
| 9 | 4 | 1.5 |  | 29 | 8 | 3.01 |  | 49 | 3 | 1.13 |
| 10 | 7 | 2.63 |  | 30 | 8 | 3.01 |  | 50 | 3 | 1.13 |
| 11 | 5 | 1.88 |  | 31 | 7 | 2.63 |  | 51 | 2 | 0.75 |
| 12 | 6 | 2.26 |  | 32 | 6 | 2.26 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 8 | 3.01 |  | 53 | 1 | 0.38 |
| 14 | 6 | 2.26 |  | 34 | 5 | 1.88 |  | 54 | 6 | 2.26 |
| 15 | 3 | 1.13 |  | 35 | 5 | 1.88 |  | 55 | 7 | 2.63 |
| 16 | 8 | 3.01 |  | 36 | 6 | 2.26 |  |  |  |  |
| 17 | 1 | 0.38 |  | 37 | 6 | 2.26 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 10 | 3.76 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 3 | 1.13 |  |  |  |  |
| 20 | 10 | 3.76 |  | 40 | 5 | 1.88 |  |  |  |  |



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

