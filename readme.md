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
| Power 655 | 1312 | 2017-08-01 | 2026-02-26 | 1312 | 00001 | 01312 |
| Power 645 | 1280 | 2017-10-25 | 2026-02-27 | 1280 | 00198 | 01477 |
| Power 535 | 219 | 2025-06-29 | 2026-02-27 | 438 | 00001 | 00488 |
| Keno | 470 | 2022-12-04 | 2026-02-28 | 59648 | #0110271 | #0272102 |
| 3D | 1043 | 2019-04-22 | 2026-02-27 | 1043 | 00001 | 01047 |
| 3D Pro | 689 | 2021-09-14 | 2026-02-26 | 689 | 00001 | 00693 |
| Bingo18 | 444 | 2024-12-03 | 2026-02-28 | 54156 | 0083123 | 0154949 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-02-26 | 01312 | [1, 7, 10, 21, 44, 51, 46] | 2026-02-27T00:00:58.514222 |
| 2026-02-24 | 01311 | [5, 8, 18, 30, 39, 54, 51] | 2026-02-25T09:14:17.252048 |
| 2026-02-21 | 01310 | [5, 7, 26, 30, 41, 45, 12] | 2026-02-23T00:01:21.197262 |
| 2026-02-19 | 01309 | [1, 27, 30, 43, 45, 46, 48] | 2026-02-21T00:00:56.973082 |
| 2026-02-14 | 01308 | [2, 13, 26, 32, 36, 42, 48] | 2026-02-21T00:00:56.975209 |
| 2026-02-12 | 01307 | [8, 17, 19, 31, 32, 46, 26] | 2026-02-21T00:00:56.982362 |
| 2026-02-10 | 01306 | [13, 21, 22, 26, 32, 55, 20] | 2026-02-11T00:00:56.086988 |
| 2026-02-07 | 01305 | [3, 5, 13, 15, 29, 46, 1] | 2026-02-08T00:00:56.025450 |
| 2026-02-05 | 01304 | [7, 13, 16, 25, 26, 55, 9] | 2026-02-06T00:00:56.250864 |
| 2026-02-03 | 01303 | [12, 15, 18, 22, 48, 53, 45] | 2026-02-04T00:00:54.536676 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 176 | 1.92 |  | 21 | 163 | 1.78 |  | 41 | 194 | 2.11 |
| 2 | 151 | 1.64 |  | 22 | 192 | 2.09 |  | 42 | 172 | 1.87 |
| 3 | 177 | 1.93 |  | 23 | 177 | 1.93 |  | 43 | 188 | 2.05 |
| 4 | 138 | 1.5 |  | 24 | 168 | 1.83 |  | 44 | 171 | 1.86 |
| 5 | 170 | 1.85 |  | 25 | 148 | 1.61 |  | 45 | 168 | 1.83 |
| 6 | 139 | 1.51 |  | 26 | 156 | 1.7 |  | 46 | 173 | 1.88 |
| 7 | 144 | 1.57 |  | 27 | 154 | 1.68 |  | 47 | 165 | 1.8 |
| 8 | 179 | 1.95 |  | 28 | 146 | 1.59 |  | 48 | 181 | 1.97 |
| 9 | 182 | 1.98 |  | 29 | 178 | 1.94 |  | 49 | 166 | 1.81 |
| 10 | 158 | 1.72 |  | 30 | 154 | 1.68 |  | 50 | 165 | 1.8 |
| 11 | 172 | 1.87 |  | 31 | 175 | 1.91 |  | 51 | 187 | 2.04 |
| 12 | 175 | 1.91 |  | 32 | 175 | 1.91 |  | 52 | 169 | 1.84 |
| 13 | 163 | 1.78 |  | 33 | 168 | 1.83 |  | 53 | 174 | 1.89 |
| 14 | 168 | 1.83 |  | 34 | 187 | 2.04 |  | 54 | 158 | 1.72 |
| 15 | 156 | 1.7 |  | 35 | 163 | 1.78 |  | 55 | 167 | 1.82 |
| 16 | 159 | 1.73 |  | 36 | 158 | 1.72 |  |  |  |  |
| 17 | 151 | 1.64 |  | 37 | 151 | 1.64 |  |  |  |  |
| 18 | 169 | 1.84 |  | 38 | 160 | 1.74 |  |  |  |  |
| 19 | 167 | 1.82 |  | 39 | 157 | 1.71 |  |  |  |  |
| 20 | 180 | 1.96 |  | 40 | 181 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.57 |  | 22 | 3 | 3.57 |  | 51 | 2 | 2.38 |
| 2 | 1 | 1.19 |  | 25 | 1 | 1.19 |  | 53 | 2 | 2.38 |
| 3 | 1 | 1.19 |  | 26 | 5 | 5.95 |  | 54 | 2 | 2.38 |
| 4 | 1 | 1.19 |  | 27 | 1 | 1.19 |  | 55 | 2 | 2.38 |
| 5 | 3 | 3.57 |  | 28 | 1 | 1.19 |  |  |  |  |
| 7 | 3 | 3.57 |  | 29 | 1 | 1.19 |  |  |  |  |
| 8 | 2 | 2.38 |  | 30 | 3 | 3.57 |  |  |  |  |
| 9 | 1 | 1.19 |  | 31 | 1 | 1.19 |  |  |  |  |
| 10 | 2 | 2.38 |  | 32 | 4 | 4.76 |  |  |  |  |
| 11 | 2 | 2.38 |  | 34 | 1 | 1.19 |  |  |  |  |
| 12 | 2 | 2.38 |  | 36 | 1 | 1.19 |  |  |  |  |
| 13 | 4 | 4.76 |  | 39 | 1 | 1.19 |  |  |  |  |
| 14 | 1 | 1.19 |  | 41 | 1 | 1.19 |  |  |  |  |
| 15 | 3 | 3.57 |  | 42 | 1 | 1.19 |  |  |  |  |
| 16 | 1 | 1.19 |  | 43 | 1 | 1.19 |  |  |  |  |
| 17 | 2 | 2.38 |  | 44 | 1 | 1.19 |  |  |  |  |
| 18 | 2 | 2.38 |  | 45 | 3 | 3.57 |  |  |  |  |
| 19 | 1 | 1.19 |  | 46 | 4 | 4.76 |  |  |  |  |
| 20 | 1 | 1.19 |  | 48 | 3 | 3.57 |  |  |  |  |
| 21 | 2 | 2.38 |  | 49 | 1 | 1.19 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.71 |  | 22 | 6 | 3.43 |  | 43 | 3 | 1.71 |
| 2 | 2 | 1.14 |  | 23 | 2 | 1.14 |  | 44 | 1 | 0.57 |
| 3 | 2 | 1.14 |  | 24 | 1 | 0.57 |  | 45 | 4 | 2.29 |
| 4 | 2 | 1.14 |  | 25 | 4 | 2.29 |  | 46 | 5 | 2.86 |
| 5 | 5 | 2.86 |  | 26 | 6 | 3.43 |  | 47 | 2 | 1.14 |
| 7 | 3 | 1.71 |  | 27 | 2 | 1.14 |  | 48 | 6 | 3.43 |
| 8 | 2 | 1.14 |  | 28 | 3 | 1.71 |  | 49 | 2 | 1.14 |
| 9 | 2 | 1.14 |  | 29 | 5 | 2.86 |  | 50 | 2 | 1.14 |
| 10 | 3 | 1.71 |  | 30 | 7 | 4.0 |  | 51 | 3 | 1.71 |
| 11 | 3 | 1.71 |  | 31 | 2 | 1.14 |  | 52 | 1 | 0.57 |
| 12 | 3 | 1.71 |  | 32 | 6 | 3.43 |  | 53 | 4 | 2.29 |
| 13 | 6 | 3.43 |  | 33 | 3 | 1.71 |  | 54 | 5 | 2.86 |
| 14 | 3 | 1.71 |  | 34 | 4 | 2.29 |  | 55 | 5 | 2.86 |
| 15 | 3 | 1.71 |  | 35 | 2 | 1.14 |  |  |  |  |
| 16 | 4 | 2.29 |  | 36 | 4 | 2.29 |  |  |  |  |
| 17 | 3 | 1.71 |  | 37 | 1 | 0.57 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 2 | 1.14 |  |  |  |  |
| 19 | 1 | 0.57 |  | 39 | 2 | 1.14 |  |  |  |  |
| 20 | 5 | 2.86 |  | 41 | 3 | 1.71 |  |  |  |  |
| 21 | 5 | 2.86 |  | 42 | 4 | 2.29 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.16 |  | 21 | 8 | 3.09 |  | 41 | 4 | 1.54 |
| 2 | 3 | 1.16 |  | 22 | 7 | 2.7 |  | 42 | 5 | 1.93 |
| 3 | 3 | 1.16 |  | 23 | 3 | 1.16 |  | 43 | 4 | 1.54 |
| 4 | 3 | 1.16 |  | 24 | 2 | 0.77 |  | 44 | 2 | 0.77 |
| 5 | 6 | 2.32 |  | 25 | 5 | 1.93 |  | 45 | 5 | 1.93 |
| 6 | 1 | 0.39 |  | 26 | 8 | 3.09 |  | 46 | 6 | 2.32 |
| 7 | 4 | 1.54 |  | 27 | 3 | 1.16 |  | 47 | 2 | 0.77 |
| 8 | 3 | 1.16 |  | 28 | 3 | 1.16 |  | 48 | 8 | 3.09 |
| 9 | 3 | 1.16 |  | 29 | 7 | 2.7 |  | 49 | 2 | 0.77 |
| 10 | 6 | 2.32 |  | 30 | 9 | 3.47 |  | 50 | 4 | 1.54 |
| 11 | 3 | 1.16 |  | 31 | 3 | 1.16 |  | 51 | 4 | 1.54 |
| 12 | 6 | 2.32 |  | 32 | 10 | 3.86 |  | 52 | 4 | 1.54 |
| 13 | 8 | 3.09 |  | 33 | 5 | 1.93 |  | 53 | 5 | 1.93 |
| 14 | 6 | 2.32 |  | 34 | 5 | 1.93 |  | 54 | 6 | 2.32 |
| 15 | 4 | 1.54 |  | 35 | 3 | 1.16 |  | 55 | 8 | 3.09 |
| 16 | 7 | 2.7 |  | 36 | 6 | 2.32 |  |  |  |  |
| 17 | 3 | 1.16 |  | 37 | 5 | 1.93 |  |  |  |  |
| 18 | 4 | 1.54 |  | 38 | 7 | 2.7 |  |  |  |  |
| 19 | 1 | 0.39 |  | 39 | 4 | 1.54 |  |  |  |  |
| 20 | 7 | 2.7 |  | 40 | 3 | 1.16 |  |  |  |  |



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

