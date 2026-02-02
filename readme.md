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
| Power 655 | 1302 | 2017-08-01 | 2026-01-31 | 1302 | 00001 | 01302 |
| Power 645 | 1269 | 2017-10-25 | 2026-02-01 | 1269 | 00198 | 01466 |
| Power 535 | 195 | 2025-06-29 | 2026-02-02 | 390 | 00001 | 00438 |
| Keno | 450 | 2022-12-04 | 2026-02-02 | 57550 | #0110271 | #0269083 |
| 3D | 1033 | 2019-04-22 | 2026-02-02 | 1033 | 00001 | 01037 |
| 3D Pro | 679 | 2021-09-14 | 2026-01-31 | 679 | 00001 | 00683 |
| Bingo18 | 425 | 2024-12-03 | 2026-02-02 | 53757 | 0083123 | 0150914 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-01-31 | 01302 | [10, 11, 14, 17, 49, 53, 4] | 2026-02-01T00:00:57.771831 |
| 2026-01-29 | 01301 | [11, 15, 22, 32, 34, 54, 28] | 2026-01-30T00:00:53.319224 |
| 2026-01-27 | 01300 | [13, 22, 32, 42, 53, 54, 29] | 2026-01-29T00:00:55.774585 |
| 2026-01-24 | 01299 | [14, 24, 25, 30, 35, 53, 18] | 2026-01-25T00:01:03.898700 |
| 2026-01-22 | 01298 | [2, 20, 21, 29, 36, 50, 5] | 2026-01-23T00:00:55.759522 |
| 2026-01-20 | 01297 | [4, 20, 26, 28, 37, 41, 32] | 2026-01-21T00:00:50.678079 |
| 2026-01-17 | 01296 | [14, 21, 23, 25, 46, 48, 54] | 2026-01-19T21:35:27.120844 |
| 2026-01-15 | 01295 | [13, 21, 31, 34, 48, 55, 27] | 2026-01-16T00:00:56.117552 |
| 2026-01-13 | 01294 | [3, 12, 25, 51, 52, 55, 43] | 2026-01-14T00:00:52.922646 |
| 2026-01-10 | 01293 | [9, 16, 30, 33, 34, 38, 49] | 2026-01-11T00:00:48.139236 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.9 |  | 21 | 161 | 1.77 |  | 41 | 193 | 2.12 |
| 2 | 150 | 1.65 |  | 22 | 190 | 2.08 |  | 42 | 171 | 1.88 |
| 3 | 176 | 1.93 |  | 23 | 177 | 1.94 |  | 43 | 187 | 2.05 |
| 4 | 138 | 1.51 |  | 24 | 168 | 1.84 |  | 44 | 170 | 1.87 |
| 5 | 167 | 1.83 |  | 25 | 147 | 1.61 |  | 45 | 165 | 1.81 |
| 6 | 139 | 1.53 |  | 26 | 151 | 1.66 |  | 46 | 169 | 1.85 |
| 7 | 141 | 1.55 |  | 27 | 153 | 1.68 |  | 47 | 165 | 1.81 |
| 8 | 177 | 1.94 |  | 28 | 146 | 1.6 |  | 48 | 178 | 1.95 |
| 9 | 181 | 1.99 |  | 29 | 177 | 1.94 |  | 49 | 166 | 1.82 |
| 10 | 157 | 1.72 |  | 30 | 151 | 1.66 |  | 50 | 165 | 1.81 |
| 11 | 172 | 1.89 |  | 31 | 174 | 1.91 |  | 51 | 185 | 2.03 |
| 12 | 173 | 1.9 |  | 32 | 172 | 1.89 |  | 52 | 169 | 1.85 |
| 13 | 159 | 1.74 |  | 33 | 168 | 1.84 |  | 53 | 173 | 1.9 |
| 14 | 168 | 1.84 |  | 34 | 187 | 2.05 |  | 54 | 157 | 1.72 |
| 15 | 154 | 1.69 |  | 35 | 163 | 1.79 |  | 55 | 165 | 1.81 |
| 16 | 158 | 1.73 |  | 36 | 157 | 1.72 |  |  |  |  |
| 17 | 150 | 1.65 |  | 37 | 151 | 1.66 |  |  |  |  |
| 18 | 167 | 1.83 |  | 38 | 160 | 1.76 |  |  |  |  |
| 19 | 166 | 1.82 |  | 39 | 156 | 1.71 |  |  |  |  |
| 20 | 179 | 1.96 |  | 40 | 181 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.19 |  | 26 | 1 | 1.19 |  | 49 | 2 | 2.38 |
| 3 | 1 | 1.19 |  | 27 | 1 | 1.19 |  | 50 | 2 | 2.38 |
| 4 | 2 | 2.38 |  | 28 | 3 | 3.57 |  | 51 | 1 | 1.19 |
| 5 | 1 | 1.19 |  | 29 | 3 | 3.57 |  | 52 | 1 | 1.19 |
| 9 | 1 | 1.19 |  | 30 | 3 | 3.57 |  | 53 | 3 | 3.57 |
| 10 | 1 | 1.19 |  | 31 | 1 | 1.19 |  | 54 | 3 | 3.57 |
| 11 | 2 | 2.38 |  | 32 | 3 | 3.57 |  | 55 | 2 | 2.38 |
| 12 | 1 | 1.19 |  | 33 | 1 | 1.19 |  |  |  |  |
| 13 | 2 | 2.38 |  | 34 | 4 | 4.76 |  |  |  |  |
| 14 | 3 | 3.57 |  | 35 | 1 | 1.19 |  |  |  |  |
| 15 | 1 | 1.19 |  | 36 | 2 | 2.38 |  |  |  |  |
| 16 | 1 | 1.19 |  | 37 | 1 | 1.19 |  |  |  |  |
| 17 | 1 | 1.19 |  | 38 | 1 | 1.19 |  |  |  |  |
| 18 | 1 | 1.19 |  | 41 | 1 | 1.19 |  |  |  |  |
| 20 | 4 | 4.76 |  | 42 | 1 | 1.19 |  |  |  |  |
| 21 | 3 | 3.57 |  | 43 | 2 | 2.38 |  |  |  |  |
| 22 | 4 | 4.76 |  | 45 | 1 | 1.19 |  |  |  |  |
| 23 | 1 | 1.19 |  | 46 | 1 | 1.19 |  |  |  |  |
| 24 | 1 | 1.19 |  | 47 | 2 | 2.38 |  |  |  |  |
| 25 | 3 | 3.57 |  | 48 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2 | 1.14 |  | 23 | 3 | 1.71 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 24 | 1 | 0.57 |  | 45 | 2 | 1.14 |
| 4 | 3 | 1.71 |  | 25 | 4 | 2.29 |  | 46 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 26 | 3 | 1.71 |  | 47 | 2 | 1.14 |
| 6 | 1 | 0.57 |  | 27 | 2 | 1.14 |  | 48 | 5 | 2.86 |
| 7 | 1 | 0.57 |  | 28 | 3 | 1.71 |  | 49 | 2 | 1.14 |
| 8 | 1 | 0.57 |  | 29 | 5 | 2.86 |  | 50 | 4 | 2.29 |
| 9 | 2 | 1.14 |  | 30 | 6 | 3.43 |  | 51 | 1 | 0.57 |
| 10 | 3 | 1.71 |  | 31 | 2 | 1.14 |  | 52 | 4 | 2.29 |
| 11 | 3 | 1.71 |  | 32 | 6 | 3.43 |  | 53 | 3 | 1.71 |
| 12 | 4 | 2.29 |  | 33 | 4 | 2.29 |  | 54 | 4 | 2.29 |
| 13 | 4 | 2.29 |  | 34 | 5 | 2.86 |  | 55 | 6 | 3.43 |
| 14 | 5 | 2.86 |  | 35 | 3 | 1.71 |  |  |  |  |
| 15 | 2 | 1.14 |  | 36 | 4 | 2.29 |  |  |  |  |
| 16 | 5 | 2.86 |  | 37 | 5 | 2.86 |  |  |  |  |
| 17 | 2 | 1.14 |  | 38 | 7 | 4.0 |  |  |  |  |
| 18 | 2 | 1.14 |  | 39 | 3 | 1.71 |  |  |  |  |
| 20 | 5 | 2.86 |  | 40 | 3 | 1.71 |  |  |  |  |
| 21 | 6 | 3.43 |  | 41 | 3 | 1.71 |  |  |  |  |
| 22 | 5 | 2.86 |  | 42 | 4 | 2.29 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.38 |  | 21 | 6 | 2.26 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 7 | 2.63 |  | 42 | 7 | 2.63 |
| 3 | 3 | 1.13 |  | 23 | 4 | 1.5 |  | 43 | 4 | 1.5 |
| 4 | 6 | 2.26 |  | 24 | 3 | 1.13 |  | 44 | 2 | 0.75 |
| 5 | 5 | 1.88 |  | 25 | 4 | 1.5 |  | 45 | 3 | 1.13 |
| 6 | 2 | 0.75 |  | 26 | 3 | 1.13 |  | 46 | 4 | 1.5 |
| 7 | 2 | 0.75 |  | 27 | 4 | 1.5 |  | 47 | 3 | 1.13 |
| 8 | 2 | 0.75 |  | 28 | 5 | 1.88 |  | 48 | 7 | 2.63 |
| 9 | 3 | 1.13 |  | 29 | 8 | 3.01 |  | 49 | 4 | 1.5 |
| 10 | 7 | 2.63 |  | 30 | 9 | 3.38 |  | 50 | 4 | 1.5 |
| 11 | 5 | 1.88 |  | 31 | 5 | 1.88 |  | 51 | 2 | 0.75 |
| 12 | 6 | 2.26 |  | 32 | 8 | 3.01 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 7 | 2.63 |  | 53 | 4 | 1.5 |
| 14 | 8 | 3.01 |  | 34 | 6 | 2.26 |  | 54 | 7 | 2.63 |
| 15 | 3 | 1.13 |  | 35 | 5 | 1.88 |  | 55 | 6 | 2.26 |
| 16 | 8 | 3.01 |  | 36 | 6 | 2.26 |  |  |  |  |
| 17 | 2 | 0.75 |  | 37 | 5 | 1.88 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 9 | 3.38 |  |  |  |  |
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

