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
| Power 655 | 1305 | 2017-08-01 | 2026-02-07 | 1305 | 00001 | 01305 |
| Power 645 | 1271 | 2017-10-25 | 2026-02-06 | 1271 | 00198 | 01468 |
| Power 535 | 200 | 2025-06-29 | 2026-02-07 | 400 | 00001 | 00448 |
| Keno | 455 | 2022-12-04 | 2026-02-07 | 58145 | #0110271 | #0269678 |
| 3D | 1035 | 2019-04-22 | 2026-02-06 | 1035 | 00001 | 01039 |
| 3D Pro | 682 | 2021-09-14 | 2026-02-07 | 682 | 00001 | 00686 |
| Bingo18 | 430 | 2024-12-03 | 2026-02-07 | 53877 | 0083123 | 0151709 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-02-07 | 01305 | [3, 5, 13, 15, 29, 46, 1] | 2026-02-08T00:00:56.025450 |
| 2026-02-05 | 01304 | [7, 13, 16, 25, 26, 55, 9] | 2026-02-06T00:00:56.250864 |
| 2026-02-03 | 01303 | [12, 15, 18, 22, 48, 53, 45] | 2026-02-04T00:00:54.536676 |
| 2026-01-31 | 01302 | [10, 11, 14, 17, 49, 53, 4] | 2026-02-01T00:00:57.771831 |
| 2026-01-29 | 01301 | [11, 15, 22, 32, 34, 54, 28] | 2026-01-30T00:00:53.319224 |
| 2026-01-27 | 01300 | [13, 22, 32, 42, 53, 54, 29] | 2026-01-29T00:00:55.774585 |
| 2026-01-24 | 01299 | [14, 24, 25, 30, 35, 53, 18] | 2026-01-25T00:01:03.898700 |
| 2026-01-22 | 01298 | [2, 20, 21, 29, 36, 50, 5] | 2026-01-23T00:00:55.759522 |
| 2026-01-20 | 01297 | [4, 20, 26, 28, 37, 41, 32] | 2026-01-21T00:00:50.678079 |
| 2026-01-17 | 01296 | [14, 21, 23, 25, 46, 48, 54] | 2026-01-19T21:35:27.120844 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 174 | 1.9 |  | 21 | 161 | 1.76 |  | 41 | 193 | 2.11 |
| 2 | 150 | 1.64 |  | 22 | 191 | 2.09 |  | 42 | 171 | 1.87 |
| 3 | 177 | 1.94 |  | 23 | 177 | 1.94 |  | 43 | 187 | 2.05 |
| 4 | 138 | 1.51 |  | 24 | 168 | 1.84 |  | 44 | 170 | 1.86 |
| 5 | 168 | 1.84 |  | 25 | 148 | 1.62 |  | 45 | 166 | 1.82 |
| 6 | 139 | 1.52 |  | 26 | 152 | 1.66 |  | 46 | 170 | 1.86 |
| 7 | 142 | 1.55 |  | 27 | 153 | 1.68 |  | 47 | 165 | 1.81 |
| 8 | 177 | 1.94 |  | 28 | 146 | 1.6 |  | 48 | 179 | 1.96 |
| 9 | 182 | 1.99 |  | 29 | 178 | 1.95 |  | 49 | 166 | 1.82 |
| 10 | 157 | 1.72 |  | 30 | 151 | 1.65 |  | 50 | 165 | 1.81 |
| 11 | 172 | 1.88 |  | 31 | 174 | 1.9 |  | 51 | 185 | 2.03 |
| 12 | 174 | 1.9 |  | 32 | 172 | 1.88 |  | 52 | 169 | 1.85 |
| 13 | 161 | 1.76 |  | 33 | 168 | 1.84 |  | 53 | 174 | 1.9 |
| 14 | 168 | 1.84 |  | 34 | 187 | 2.05 |  | 54 | 157 | 1.72 |
| 15 | 156 | 1.71 |  | 35 | 163 | 1.78 |  | 55 | 166 | 1.82 |
| 16 | 159 | 1.74 |  | 36 | 157 | 1.72 |  |  |  |  |
| 17 | 150 | 1.64 |  | 37 | 151 | 1.65 |  |  |  |  |
| 18 | 168 | 1.84 |  | 38 | 160 | 1.75 |  |  |  |  |
| 19 | 166 | 1.82 |  | 39 | 156 | 1.71 |  |  |  |  |
| 20 | 179 | 1.96 |  | 40 | 181 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 24 | 1 | 1.1 |  | 48 | 3 | 3.3 |
| 2 | 1 | 1.1 |  | 25 | 4 | 4.4 |  | 49 | 2 | 2.2 |
| 3 | 2 | 2.2 |  | 26 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 4 | 2 | 2.2 |  | 27 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 29 | 3 | 3.3 |  | 53 | 4 | 4.4 |
| 9 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 54 | 3 | 3.3 |
| 10 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 55 | 3 | 3.3 |
| 11 | 2 | 2.2 |  | 32 | 3 | 3.3 |  |  |  |  |
| 12 | 2 | 2.2 |  | 33 | 1 | 1.1 |  |  |  |  |
| 13 | 4 | 4.4 |  | 34 | 3 | 3.3 |  |  |  |  |
| 14 | 3 | 3.3 |  | 35 | 1 | 1.1 |  |  |  |  |
| 15 | 3 | 3.3 |  | 36 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 17 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 18 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 1 | 1.1 |  |  |  |  |
| 21 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 3 | 3.3 |  | 45 | 1 | 1.1 |  |  |  |  |
| 23 | 1 | 1.1 |  | 46 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 22 | 6 | 3.3 |  | 42 | 3 | 1.65 |
| 2 | 2 | 1.1 |  | 23 | 3 | 1.65 |  | 43 | 2 | 1.1 |
| 3 | 3 | 1.65 |  | 24 | 1 | 0.55 |  | 45 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 5 | 2.75 |  | 46 | 3 | 1.65 |
| 5 | 4 | 2.2 |  | 26 | 2 | 1.1 |  | 47 | 2 | 1.1 |
| 6 | 1 | 0.55 |  | 27 | 1 | 0.55 |  | 48 | 6 | 3.3 |
| 7 | 2 | 1.1 |  | 28 | 3 | 1.65 |  | 49 | 2 | 1.1 |
| 8 | 1 | 0.55 |  | 29 | 6 | 3.3 |  | 50 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 30 | 6 | 3.3 |  | 51 | 1 | 0.55 |
| 10 | 3 | 1.65 |  | 31 | 1 | 0.55 |  | 52 | 3 | 1.65 |
| 11 | 3 | 1.65 |  | 32 | 6 | 3.3 |  | 53 | 4 | 2.2 |
| 12 | 4 | 2.2 |  | 33 | 4 | 2.2 |  | 54 | 4 | 2.2 |
| 13 | 6 | 3.3 |  | 34 | 4 | 2.2 |  | 55 | 7 | 3.85 |
| 14 | 4 | 2.2 |  | 35 | 3 | 1.65 |  |  |  |  |
| 15 | 3 | 1.65 |  | 36 | 4 | 2.2 |  |  |  |  |
| 16 | 6 | 3.3 |  | 37 | 4 | 2.2 |  |  |  |  |
| 17 | 2 | 1.1 |  | 38 | 7 | 3.85 |  |  |  |  |
| 18 | 3 | 1.65 |  | 39 | 3 | 1.65 |  |  |  |  |
| 20 | 5 | 2.75 |  | 40 | 3 | 1.65 |  |  |  |  |
| 21 | 5 | 2.75 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 0.73 |  | 21 | 6 | 2.2 |  | 41 | 4 | 1.47 |
| 2 | 3 | 1.1 |  | 22 | 7 | 2.56 |  | 42 | 7 | 2.56 |
| 3 | 4 | 1.47 |  | 23 | 4 | 1.47 |  | 43 | 4 | 1.47 |
| 4 | 6 | 2.2 |  | 24 | 3 | 1.1 |  | 44 | 1 | 0.37 |
| 5 | 6 | 2.2 |  | 25 | 5 | 1.83 |  | 45 | 4 | 1.47 |
| 6 | 1 | 0.37 |  | 26 | 4 | 1.47 |  | 46 | 5 | 1.83 |
| 7 | 3 | 1.1 |  | 27 | 3 | 1.1 |  | 47 | 3 | 1.1 |
| 8 | 2 | 0.73 |  | 28 | 5 | 1.83 |  | 48 | 8 | 2.93 |
| 9 | 4 | 1.47 |  | 29 | 8 | 2.93 |  | 49 | 3 | 1.1 |
| 10 | 7 | 2.56 |  | 30 | 9 | 3.3 |  | 50 | 4 | 1.47 |
| 11 | 5 | 1.83 |  | 31 | 5 | 1.83 |  | 51 | 2 | 0.73 |
| 12 | 7 | 2.56 |  | 32 | 8 | 2.93 |  | 52 | 4 | 1.47 |
| 13 | 8 | 2.93 |  | 33 | 6 | 2.2 |  | 53 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 34 | 6 | 2.2 |  | 54 | 7 | 2.56 |
| 15 | 5 | 1.83 |  | 35 | 5 | 1.83 |  | 55 | 7 | 2.56 |
| 16 | 7 | 2.56 |  | 36 | 5 | 1.83 |  |  |  |  |
| 17 | 2 | 0.73 |  | 37 | 5 | 1.83 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 9 | 3.3 |  |  |  |  |
| 19 | 2 | 0.73 |  | 39 | 3 | 1.1 |  |  |  |  |
| 20 | 9 | 3.3 |  | 40 | 5 | 1.83 |  |  |  |  |



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

