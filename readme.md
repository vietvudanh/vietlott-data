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
| Power 655 | 1278 | 2017-08-01 | 2025-12-06 | 1278 | 00001 | 01278 |
| Power 645 | 1245 | 2017-10-25 | 2025-12-07 | 1245 | 00198 | 01442 |
| Power 535 | 138 | 2025-06-29 | 2025-12-07 | 276 | 00001 | 00324 |
| Keno | 395 | 2022-12-04 | 2025-12-08 | 51059 | #0110271 | #0262344 |
| 3D | 1008 | 2019-04-22 | 2025-12-05 | 1008 | 00001 | 01012 |
| 3D Pro | 655 | 2021-09-14 | 2025-12-06 | 655 | 00001 | 00659 |
| Bingo18 | 371 | 2024-12-03 | 2025-12-08 | 52488 | 0083123 | 0141911 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52, 15] | 2025-12-07T00:00:57.664427 |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53, 14] | 2025-12-05T00:00:49.739433 |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54, 10] | 2025-12-03T00:00:48.323884 |
| 2025-11-29 | 01275 | [4, 20, 24, 27, 40, 48, 9] | 2025-11-30T00:00:57.885215 |
| 2025-11-27 | 01274 | [4, 5, 10, 11, 28, 35, 38] | 2025-11-28T00:00:53.620470 |
| 2025-11-25 | 01273 | [23, 31, 32, 42, 46, 48, 4] | 2025-11-26T00:00:52.128543 |
| 2025-11-22 | 01272 | [8, 10, 19, 29, 34, 46, 14] | 2025-11-23T00:00:55.277843 |
| 2025-11-20 | 01271 | [3, 12, 19, 20, 31, 42, 13] | 2025-11-21T00:00:55.461521 |
| 2025-11-18 | 01270 | [7, 12, 18, 22, 30, 49, 5] | 2025-11-19T00:00:50.139294 |
| 2025-11-15 | 01269 | [2, 30, 33, 35, 42, 54, 45] | 2025-11-16T00:00:51.177522 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.93 |  | 21 | 155 | 1.73 |  | 41 | 190 | 2.12 |
| 2 | 148 | 1.65 |  | 22 | 185 | 2.07 |  | 42 | 167 | 1.87 |
| 3 | 174 | 1.95 |  | 23 | 174 | 1.95 |  | 43 | 184 | 2.06 |
| 4 | 135 | 1.51 |  | 24 | 167 | 1.87 |  | 44 | 170 | 1.9 |
| 5 | 164 | 1.83 |  | 25 | 143 | 1.6 |  | 45 | 163 | 1.82 |
| 6 | 138 | 1.54 |  | 26 | 149 | 1.67 |  | 46 | 167 | 1.87 |
| 7 | 140 | 1.57 |  | 27 | 151 | 1.69 |  | 47 | 163 | 1.82 |
| 8 | 176 | 1.97 |  | 28 | 143 | 1.6 |  | 48 | 173 | 1.93 |
| 9 | 179 | 2.0 |  | 29 | 172 | 1.92 |  | 49 | 164 | 1.83 |
| 10 | 154 | 1.72 |  | 30 | 145 | 1.62 |  | 50 | 162 | 1.81 |
| 11 | 169 | 1.89 |  | 31 | 172 | 1.92 |  | 51 | 184 | 2.06 |
| 12 | 170 | 1.9 |  | 32 | 166 | 1.86 |  | 52 | 166 | 1.86 |
| 13 | 155 | 1.73 |  | 33 | 164 | 1.83 |  | 53 | 170 | 1.9 |
| 14 | 163 | 1.82 |  | 34 | 183 | 2.05 |  | 54 | 153 | 1.71 |
| 15 | 153 | 1.71 |  | 35 | 160 | 1.79 |  | 55 | 159 | 1.78 |
| 16 | 153 | 1.71 |  | 36 | 153 | 1.71 |  |  |  |  |
| 17 | 148 | 1.65 |  | 37 | 147 | 1.64 |  |  |  |  |
| 18 | 165 | 1.84 |  | 38 | 153 | 1.71 |  |  |  |  |
| 19 | 166 | 1.86 |  | 39 | 153 | 1.71 |  |  |  |  |
| 20 | 174 | 1.95 |  | 40 | 178 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 46 | 2 | 2.2 |
| 2 | 1 | 1.1 |  | 26 | 1 | 1.1 |  | 47 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 27 | 2 | 2.2 |  | 48 | 2 | 2.2 |
| 4 | 3 | 3.3 |  | 28 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 29 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 30 | 3 | 3.3 |  | 51 | 1 | 1.1 |
| 8 | 1 | 1.1 |  | 31 | 3 | 3.3 |  | 52 | 1 | 1.1 |
| 9 | 1 | 1.1 |  | 32 | 2 | 2.2 |  | 53 | 1 | 1.1 |
| 10 | 4 | 4.4 |  | 33 | 2 | 2.2 |  | 54 | 3 | 3.3 |
| 11 | 2 | 2.2 |  | 34 | 2 | 2.2 |  |  |  |  |
| 12 | 3 | 3.3 |  | 35 | 2 | 2.2 |  |  |  |  |
| 13 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 38 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 18 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 19 | 3 | 3.3 |  | 42 | 3 | 3.3 |  |  |  |  |
| 20 | 4 | 4.4 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 23 | 1 | 1.1 |  | 45 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 22 | 5 | 2.75 |  | 42 | 4 | 2.2 |
| 2 | 1 | 0.55 |  | 23 | 2 | 1.1 |  | 43 | 4 | 2.2 |
| 3 | 4 | 2.2 |  | 24 | 4 | 2.2 |  | 44 | 3 | 1.65 |
| 4 | 3 | 1.65 |  | 25 | 2 | 1.1 |  | 45 | 3 | 1.65 |
| 5 | 4 | 2.2 |  | 26 | 4 | 2.2 |  | 46 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 27 | 5 | 2.75 |  | 47 | 2 | 1.1 |
| 7 | 4 | 2.2 |  | 28 | 3 | 1.65 |  | 48 | 3 | 1.65 |
| 8 | 5 | 2.75 |  | 29 | 5 | 2.75 |  | 49 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 30 | 3 | 1.65 |  | 50 | 3 | 1.65 |
| 10 | 6 | 3.3 |  | 31 | 5 | 2.75 |  | 51 | 1 | 0.55 |
| 11 | 6 | 3.3 |  | 32 | 2 | 1.1 |  | 52 | 1 | 0.55 |
| 12 | 5 | 2.75 |  | 33 | 4 | 2.2 |  | 53 | 1 | 0.55 |
| 13 | 3 | 1.65 |  | 34 | 2 | 1.1 |  | 54 | 4 | 2.2 |
| 14 | 5 | 2.75 |  | 35 | 3 | 1.65 |  | 55 | 2 | 1.1 |
| 15 | 4 | 2.2 |  | 36 | 4 | 2.2 |  |  |  |  |
| 16 | 5 | 2.75 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 4 | 2.2 |  | 39 | 1 | 0.55 |  |  |  |  |
| 20 | 6 | 3.3 |  | 40 | 5 | 2.75 |  |  |  |  |
| 21 | 3 | 1.65 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.1 |  | 21 | 4 | 1.47 |  | 41 | 4 | 1.47 |
| 2 | 5 | 1.83 |  | 22 | 7 | 2.56 |  | 42 | 6 | 2.2 |
| 3 | 5 | 1.83 |  | 23 | 3 | 1.1 |  | 43 | 8 | 2.93 |
| 4 | 3 | 1.1 |  | 24 | 7 | 2.56 |  | 44 | 3 | 1.1 |
| 5 | 5 | 1.83 |  | 25 | 2 | 0.73 |  | 45 | 5 | 1.83 |
| 6 | 3 | 1.1 |  | 26 | 4 | 1.47 |  | 46 | 7 | 2.56 |
| 7 | 6 | 2.2 |  | 27 | 8 | 2.93 |  | 47 | 2 | 0.73 |
| 8 | 11 | 4.03 |  | 28 | 4 | 1.47 |  | 48 | 3 | 1.1 |
| 9 | 3 | 1.1 |  | 29 | 6 | 2.2 |  | 49 | 4 | 1.47 |
| 10 | 6 | 2.2 |  | 30 | 5 | 1.83 |  | 50 | 3 | 1.1 |
| 11 | 6 | 2.2 |  | 31 | 7 | 2.56 |  | 51 | 2 | 0.73 |
| 12 | 5 | 1.83 |  | 32 | 2 | 0.73 |  | 52 | 3 | 1.1 |
| 13 | 5 | 1.83 |  | 33 | 6 | 2.2 |  | 53 | 3 | 1.1 |
| 14 | 6 | 2.2 |  | 34 | 4 | 1.47 |  | 54 | 4 | 1.47 |
| 15 | 5 | 1.83 |  | 35 | 5 | 1.83 |  | 55 | 4 | 1.47 |
| 16 | 7 | 2.56 |  | 36 | 6 | 2.2 |  |  |  |  |
| 17 | 3 | 1.1 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 8 | 2.93 |  |  |  |  |
| 19 | 9 | 3.3 |  | 39 | 4 | 1.47 |  |  |  |  |
| 20 | 9 | 3.3 |  | 40 | 7 | 2.56 |  |  |  |  |



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

