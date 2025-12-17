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
| Power 655 | 1282 | 2017-08-01 | 2025-12-16 | 1282 | 00001 | 01282 |
| Power 645 | 1249 | 2017-10-25 | 2025-12-17 | 1249 | 00198 | 01446 |
| Power 535 | 148 | 2025-06-29 | 2025-12-17 | 296 | 00001 | 00344 |
| Keno | 404 | 2022-12-04 | 2025-12-17 | 52205 | #0110271 | #0263490 |
| 3D | 1013 | 2019-04-22 | 2025-12-17 | 1013 | 00001 | 01017 |
| 3D Pro | 659 | 2021-09-14 | 2025-12-16 | 659 | 00001 | 00663 |
| Bingo18 | 380 | 2024-12-03 | 2025-12-17 | 52716 | 0083123 | 0143441 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46] | 2025-12-17T00:00:57.950930 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52] | 2025-12-14T00:00:57.940661 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43, 42] | 2025-12-10T00:00:51.279107 |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52, 15] | 2025-12-07T00:00:57.664427 |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53, 14] | 2025-12-05T00:00:49.739433 |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54, 10] | 2025-12-03T00:00:48.323884 |
| 2025-11-29 | 01275 | [4, 20, 24, 27, 40, 48, 9] | 2025-11-30T00:00:57.885215 |
| 2025-11-27 | 01274 | [4, 5, 10, 11, 28, 35, 38] | 2025-11-28T00:00:53.620470 |
| 2025-11-25 | 01273 | [23, 31, 32, 42, 46, 48, 4] | 2025-11-26T00:00:52.128543 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.93 |  | 21 | 157 | 1.75 |  | 41 | 190 | 2.12 |
| 2 | 148 | 1.65 |  | 22 | 185 | 2.06 |  | 42 | 168 | 1.87 |
| 3 | 174 | 1.94 |  | 23 | 174 | 1.94 |  | 43 | 185 | 2.06 |
| 4 | 135 | 1.5 |  | 24 | 167 | 1.86 |  | 44 | 170 | 1.89 |
| 5 | 165 | 1.84 |  | 25 | 143 | 1.59 |  | 45 | 164 | 1.83 |
| 6 | 138 | 1.54 |  | 26 | 150 | 1.67 |  | 46 | 168 | 1.87 |
| 7 | 141 | 1.57 |  | 27 | 152 | 1.69 |  | 47 | 163 | 1.82 |
| 8 | 177 | 1.97 |  | 28 | 143 | 1.59 |  | 48 | 174 | 1.94 |
| 9 | 180 | 2.01 |  | 29 | 172 | 1.92 |  | 49 | 164 | 1.83 |
| 10 | 154 | 1.72 |  | 30 | 145 | 1.62 |  | 50 | 162 | 1.81 |
| 11 | 169 | 1.88 |  | 31 | 173 | 1.93 |  | 51 | 184 | 2.05 |
| 12 | 171 | 1.91 |  | 32 | 166 | 1.85 |  | 52 | 168 | 1.87 |
| 13 | 156 | 1.74 |  | 33 | 164 | 1.83 |  | 53 | 170 | 1.89 |
| 14 | 164 | 1.83 |  | 34 | 183 | 2.04 |  | 54 | 153 | 1.71 |
| 15 | 153 | 1.71 |  | 35 | 160 | 1.78 |  | 55 | 161 | 1.79 |
| 16 | 153 | 1.71 |  | 36 | 154 | 1.72 |  |  |  |  |
| 17 | 148 | 1.65 |  | 37 | 148 | 1.65 |  |  |  |  |
| 18 | 166 | 1.85 |  | 38 | 156 | 1.74 |  |  |  |  |
| 19 | 166 | 1.85 |  | 39 | 153 | 1.71 |  |  |  |  |
| 20 | 175 | 1.95 |  | 40 | 178 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 4 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 5 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 7 | 2 | 2.2 |  | 29 | 2 | 2.2 |  | 52 | 3 | 3.3 |
| 8 | 2 | 2.2 |  | 30 | 1 | 1.1 |  | 53 | 1 | 1.1 |
| 9 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 54 | 1 | 1.1 |
| 10 | 4 | 4.4 |  | 32 | 2 | 2.2 |  | 55 | 2 | 2.2 |
| 11 | 1 | 1.1 |  | 33 | 1 | 1.1 |  |  |  |  |
| 12 | 4 | 4.4 |  | 34 | 2 | 2.2 |  |  |  |  |
| 13 | 2 | 2.2 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 3 | 3.3 |  | 36 | 2 | 2.2 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 38 | 4 | 4.4 |  |  |  |  |
| 18 | 2 | 2.2 |  | 40 | 1 | 1.1 |  |  |  |  |
| 19 | 2 | 2.2 |  | 42 | 3 | 3.3 |  |  |  |  |
| 20 | 4 | 4.4 |  | 43 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 45 | 1 | 1.1 |  |  |  |  |
| 23 | 1 | 1.1 |  | 46 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 48 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.57 |  | 22 | 4 | 2.29 |  | 43 | 3 | 1.71 |
| 2 | 1 | 0.57 |  | 23 | 2 | 1.14 |  | 44 | 2 | 1.14 |
| 3 | 3 | 1.71 |  | 24 | 3 | 1.71 |  | 45 | 3 | 1.71 |
| 4 | 3 | 1.71 |  | 25 | 1 | 0.57 |  | 46 | 3 | 1.71 |
| 5 | 4 | 2.29 |  | 26 | 2 | 1.14 |  | 47 | 2 | 1.14 |
| 6 | 2 | 1.14 |  | 27 | 5 | 2.86 |  | 48 | 4 | 2.29 |
| 7 | 3 | 1.71 |  | 28 | 3 | 1.71 |  | 49 | 3 | 1.71 |
| 8 | 5 | 2.86 |  | 29 | 5 | 2.86 |  | 50 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 30 | 3 | 1.71 |  | 51 | 1 | 0.57 |
| 10 | 6 | 3.43 |  | 31 | 6 | 3.43 |  | 52 | 3 | 1.71 |
| 11 | 5 | 2.86 |  | 32 | 2 | 1.14 |  | 53 | 1 | 0.57 |
| 12 | 5 | 2.86 |  | 33 | 4 | 2.29 |  | 54 | 4 | 2.29 |
| 13 | 4 | 2.29 |  | 34 | 2 | 1.14 |  | 55 | 3 | 1.71 |
| 14 | 5 | 2.86 |  | 35 | 3 | 1.71 |  |  |  |  |
| 15 | 3 | 1.71 |  | 36 | 4 | 2.29 |  |  |  |  |
| 16 | 3 | 1.71 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 6 | 3.43 |  |  |  |  |
| 19 | 3 | 1.71 |  | 40 | 4 | 2.29 |  |  |  |  |
| 20 | 7 | 4.0 |  | 41 | 3 | 1.71 |  |  |  |  |
| 21 | 3 | 1.71 |  | 42 | 4 | 2.29 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.13 |  | 21 | 5 | 1.88 |  | 41 | 4 | 1.5 |
| 2 | 2 | 0.75 |  | 22 | 7 | 2.63 |  | 42 | 6 | 2.26 |
| 3 | 4 | 1.5 |  | 23 | 3 | 1.13 |  | 43 | 8 | 3.01 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 3 | 1.13 |
| 5 | 6 | 2.26 |  | 25 | 2 | 0.75 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 7 | 2.63 |
| 7 | 6 | 2.26 |  | 27 | 7 | 2.63 |  | 47 | 2 | 0.75 |
| 8 | 11 | 4.14 |  | 28 | 3 | 1.13 |  | 48 | 4 | 1.5 |
| 9 | 4 | 1.5 |  | 29 | 6 | 2.26 |  | 49 | 3 | 1.13 |
| 10 | 6 | 2.26 |  | 30 | 5 | 1.88 |  | 50 | 3 | 1.13 |
| 11 | 6 | 2.26 |  | 31 | 7 | 2.63 |  | 51 | 1 | 0.38 |
| 12 | 6 | 2.26 |  | 32 | 2 | 0.75 |  | 52 | 4 | 1.5 |
| 13 | 6 | 2.26 |  | 33 | 5 | 1.88 |  | 53 | 2 | 0.75 |
| 14 | 7 | 2.63 |  | 34 | 4 | 1.5 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 5 | 1.88 |  | 55 | 4 | 1.5 |
| 16 | 5 | 1.88 |  | 36 | 7 | 2.63 |  |  |  |  |
| 17 | 2 | 0.75 |  | 37 | 5 | 1.88 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 10 | 3.76 |  |  |  |  |
| 19 | 8 | 3.01 |  | 39 | 3 | 1.13 |  |  |  |  |
| 20 | 8 | 3.01 |  | 40 | 6 | 2.26 |  |  |  |  |



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

