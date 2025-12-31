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
| Power 655 | 1288 | 2017-08-01 | 2025-12-30 | 1288 | 00001 | 01288 |
| Power 645 | 1255 | 2017-10-25 | 2025-12-31 | 1255 | 00198 | 01452 |
| Power 535 | 162 | 2025-06-29 | 2025-12-31 | 324 | 00001 | 00372 |
| Keno | 418 | 2022-12-04 | 2025-12-31 | 53871 | #0110271 | #0265156 |
| 3D | 1019 | 2019-04-22 | 2025-12-31 | 1019 | 00001 | 01023 |
| 3D Pro | 665 | 2021-09-14 | 2025-12-30 | 665 | 00001 | 00669 |
| Bingo18 | 394 | 2024-12-03 | 2025-12-31 | 53052 | 0083123 | 0145667 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55, 38] | 2025-12-31T00:00:53.630435 |
| 2025-12-27 | 01287 | [16, 21, 30, 37, 39, 40, 13] | 2025-12-28T00:00:52.930719 |
| 2025-12-25 | 01286 | [4, 6, 32, 37, 40, 48, 38] | 2025-12-26T00:00:59.517363 |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38, 3] | 2025-12-24T00:00:51.363924 |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] | 2025-12-21T00:00:50.783917 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] | 2025-12-19T00:00:54.542458 |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46] | 2025-12-17T00:00:57.950930 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52] | 2025-12-14T00:00:57.940661 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43, 42] | 2025-12-10T00:00:51.279107 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.92 |  | 21 | 158 | 1.75 |  | 41 | 192 | 2.13 |
| 2 | 149 | 1.65 |  | 22 | 186 | 2.06 |  | 42 | 168 | 1.86 |
| 3 | 175 | 1.94 |  | 23 | 175 | 1.94 |  | 43 | 185 | 2.05 |
| 4 | 136 | 1.51 |  | 24 | 167 | 1.85 |  | 44 | 170 | 1.89 |
| 5 | 165 | 1.83 |  | 25 | 144 | 1.6 |  | 45 | 164 | 1.82 |
| 6 | 139 | 1.54 |  | 26 | 150 | 1.66 |  | 46 | 168 | 1.86 |
| 7 | 141 | 1.56 |  | 27 | 152 | 1.69 |  | 47 | 163 | 1.81 |
| 8 | 177 | 1.96 |  | 28 | 143 | 1.59 |  | 48 | 176 | 1.95 |
| 9 | 180 | 2.0 |  | 29 | 173 | 1.92 |  | 49 | 164 | 1.82 |
| 10 | 155 | 1.72 |  | 30 | 148 | 1.64 |  | 50 | 163 | 1.81 |
| 11 | 170 | 1.89 |  | 31 | 173 | 1.92 |  | 51 | 184 | 2.04 |
| 12 | 172 | 1.91 |  | 32 | 169 | 1.87 |  | 52 | 168 | 1.86 |
| 13 | 157 | 1.74 |  | 33 | 165 | 1.83 |  | 53 | 170 | 1.89 |
| 14 | 165 | 1.83 |  | 34 | 183 | 2.03 |  | 54 | 153 | 1.7 |
| 15 | 153 | 1.7 |  | 35 | 162 | 1.8 |  | 55 | 163 | 1.81 |
| 16 | 155 | 1.72 |  | 36 | 154 | 1.71 |  |  |  |  |
| 17 | 148 | 1.64 |  | 37 | 150 | 1.66 |  |  |  |  |
| 18 | 166 | 1.84 |  | 38 | 159 | 1.76 |  |  |  |  |
| 19 | 166 | 1.84 |  | 39 | 155 | 1.72 |  |  |  |  |
| 20 | 175 | 1.94 |  | 40 | 181 | 2.01 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 24 | 1 | 1.1 |  | 45 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 46 | 1 | 1.1 |
| 4 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 48 | 3 | 3.3 |
| 5 | 1 | 1.1 |  | 27 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 30 | 3 | 3.3 |  | 52 | 3 | 3.3 |
| 8 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 9 | 1 | 1.1 |  | 32 | 4 | 4.4 |  | 54 | 1 | 1.1 |
| 10 | 3 | 3.3 |  | 33 | 2 | 2.2 |  | 55 | 4 | 4.4 |
| 11 | 1 | 1.1 |  | 34 | 1 | 1.1 |  |  |  |  |
| 12 | 3 | 3.3 |  | 35 | 2 | 2.2 |  |  |  |  |
| 13 | 2 | 2.2 |  | 36 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 37 | 4 | 4.4 |  |  |  |  |
| 15 | 1 | 1.1 |  | 38 | 6 | 6.59 |  |  |  |  |
| 16 | 3 | 3.3 |  | 39 | 2 | 2.2 |  |  |  |  |
| 18 | 1 | 1.1 |  | 40 | 3 | 3.3 |  |  |  |  |
| 20 | 2 | 2.2 |  | 41 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 42 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 43 | 1 | 1.1 |  |  |  |  |
| 23 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.57 |  | 22 | 3 | 1.71 |  | 42 | 4 | 2.29 |
| 2 | 2 | 1.14 |  | 23 | 2 | 1.14 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 24 | 2 | 1.14 |  | 44 | 2 | 1.14 |
| 4 | 4 | 2.29 |  | 25 | 1 | 0.57 |  | 45 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 26 | 2 | 1.14 |  | 46 | 3 | 1.71 |
| 6 | 2 | 1.14 |  | 27 | 4 | 2.29 |  | 47 | 1 | 0.57 |
| 7 | 2 | 1.14 |  | 28 | 2 | 1.14 |  | 48 | 5 | 2.86 |
| 8 | 2 | 1.14 |  | 29 | 5 | 2.86 |  | 49 | 2 | 1.14 |
| 9 | 2 | 1.14 |  | 30 | 6 | 3.43 |  | 50 | 2 | 1.14 |
| 10 | 5 | 2.86 |  | 31 | 5 | 2.86 |  | 51 | 1 | 0.57 |
| 11 | 3 | 1.71 |  | 32 | 5 | 2.86 |  | 52 | 3 | 1.71 |
| 12 | 5 | 2.86 |  | 33 | 4 | 2.29 |  | 53 | 1 | 0.57 |
| 13 | 4 | 2.29 |  | 34 | 2 | 1.14 |  | 54 | 3 | 1.71 |
| 14 | 5 | 2.86 |  | 35 | 4 | 2.29 |  | 55 | 4 | 2.29 |
| 15 | 3 | 1.71 |  | 36 | 4 | 2.29 |  |  |  |  |
| 16 | 5 | 2.86 |  | 37 | 4 | 2.29 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 9 | 5.14 |  |  |  |  |
| 19 | 3 | 1.71 |  | 39 | 2 | 1.14 |  |  |  |  |
| 20 | 6 | 3.43 |  | 40 | 5 | 2.86 |  |  |  |  |
| 21 | 3 | 1.71 |  | 41 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.38 |  | 22 | 8 | 3.01 |  | 42 | 5 | 1.88 |
| 2 | 2 | 0.75 |  | 23 | 3 | 1.13 |  | 43 | 6 | 2.26 |
| 3 | 5 | 1.88 |  | 24 | 4 | 1.5 |  | 44 | 3 | 1.13 |
| 4 | 4 | 1.5 |  | 25 | 3 | 1.13 |  | 45 | 5 | 1.88 |
| 5 | 5 | 1.88 |  | 26 | 5 | 1.88 |  | 46 | 4 | 1.5 |
| 6 | 3 | 1.13 |  | 27 | 6 | 2.26 |  | 47 | 2 | 0.75 |
| 7 | 6 | 2.26 |  | 28 | 3 | 1.13 |  | 48 | 6 | 2.26 |
| 8 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 3 | 1.13 |
| 9 | 4 | 1.5 |  | 30 | 6 | 2.26 |  | 50 | 4 | 1.5 |
| 10 | 7 | 2.63 |  | 31 | 6 | 2.26 |  | 51 | 1 | 0.38 |
| 11 | 7 | 2.63 |  | 32 | 5 | 1.88 |  | 52 | 3 | 1.13 |
| 12 | 7 | 2.63 |  | 33 | 6 | 2.26 |  | 53 | 1 | 0.38 |
| 13 | 5 | 1.88 |  | 34 | 2 | 0.75 |  | 54 | 4 | 1.5 |
| 14 | 7 | 2.63 |  | 35 | 7 | 2.63 |  | 55 | 6 | 2.26 |
| 15 | 4 | 1.5 |  | 36 | 6 | 2.26 |  |  |  |  |
| 16 | 7 | 2.63 |  | 37 | 7 | 2.63 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 11 | 4.14 |  |  |  |  |
| 19 | 5 | 1.88 |  | 39 | 3 | 1.13 |  |  |  |  |
| 20 | 7 | 2.63 |  | 40 | 9 | 3.38 |  |  |  |  |
| 21 | 6 | 2.26 |  | 41 | 5 | 1.88 |  |  |  |  |



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

