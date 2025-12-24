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
| Power 655 | 1285 | 2017-08-01 | 2025-12-23 | 1285 | 00001 | 01285 |
| Power 645 | 1252 | 2017-10-25 | 2025-12-24 | 1252 | 00198 | 01449 |
| Power 535 | 155 | 2025-06-29 | 2025-12-24 | 310 | 00001 | 00358 |
| Keno | 411 | 2022-12-04 | 2025-12-24 | 53038 | #0110271 | #0264323 |
| 3D | 1016 | 2019-04-22 | 2025-12-24 | 1016 | 00001 | 01020 |
| 3D Pro | 662 | 2021-09-14 | 2025-12-23 | 662 | 00001 | 00666 |
| Bingo18 | 387 | 2024-12-03 | 2025-12-24 | 52884 | 0083123 | 0144554 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38, 3] | 2025-12-24T00:00:51.363924 |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] | 2025-12-21T00:00:50.783917 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] | 2025-12-19T00:00:54.542458 |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46] | 2025-12-17T00:00:57.950930 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52] | 2025-12-14T00:00:57.940661 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43, 42] | 2025-12-10T00:00:51.279107 |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52, 15] | 2025-12-07T00:00:57.664427 |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53, 14] | 2025-12-05T00:00:49.739433 |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54, 10] | 2025-12-03T00:00:48.323884 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.92 |  | 21 | 157 | 1.75 |  | 41 | 191 | 2.12 |
| 2 | 149 | 1.66 |  | 22 | 186 | 2.07 |  | 42 | 168 | 1.87 |
| 3 | 175 | 1.95 |  | 23 | 175 | 1.95 |  | 43 | 185 | 2.06 |
| 4 | 135 | 1.5 |  | 24 | 167 | 1.86 |  | 44 | 170 | 1.89 |
| 5 | 165 | 1.83 |  | 25 | 144 | 1.6 |  | 45 | 164 | 1.82 |
| 6 | 138 | 1.53 |  | 26 | 150 | 1.67 |  | 46 | 168 | 1.87 |
| 7 | 141 | 1.57 |  | 27 | 152 | 1.69 |  | 47 | 163 | 1.81 |
| 8 | 177 | 1.97 |  | 28 | 143 | 1.59 |  | 48 | 174 | 1.93 |
| 9 | 180 | 2.0 |  | 29 | 173 | 1.92 |  | 49 | 164 | 1.82 |
| 10 | 155 | 1.72 |  | 30 | 146 | 1.62 |  | 50 | 163 | 1.81 |
| 11 | 169 | 1.88 |  | 31 | 173 | 1.92 |  | 51 | 184 | 2.05 |
| 12 | 172 | 1.91 |  | 32 | 168 | 1.87 |  | 52 | 168 | 1.87 |
| 13 | 156 | 1.73 |  | 33 | 165 | 1.83 |  | 53 | 170 | 1.89 |
| 14 | 165 | 1.83 |  | 34 | 183 | 2.03 |  | 54 | 153 | 1.7 |
| 15 | 153 | 1.7 |  | 35 | 161 | 1.79 |  | 55 | 162 | 1.8 |
| 16 | 154 | 1.71 |  | 36 | 154 | 1.71 |  |  |  |  |
| 17 | 148 | 1.65 |  | 37 | 148 | 1.65 |  |  |  |  |
| 18 | 166 | 1.85 |  | 38 | 157 | 1.75 |  |  |  |  |
| 19 | 166 | 1.85 |  | 39 | 154 | 1.71 |  |  |  |  |
| 20 | 175 | 1.95 |  | 40 | 179 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 45 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 46 | 2 | 2.2 |
| 4 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 48 | 3 | 3.3 |
| 5 | 2 | 2.2 |  | 28 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 7 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 8 | 1 | 1.1 |  | 30 | 1 | 1.1 |  | 52 | 3 | 3.3 |
| 9 | 2 | 2.2 |  | 31 | 2 | 2.2 |  | 53 | 1 | 1.1 |
| 10 | 4 | 4.4 |  | 32 | 4 | 4.4 |  | 54 | 1 | 1.1 |
| 11 | 1 | 1.1 |  | 33 | 2 | 2.2 |  | 55 | 3 | 3.3 |
| 12 | 3 | 3.3 |  | 34 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 35 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 36 | 2 | 2.2 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 38 | 5 | 5.49 |  |  |  |  |
| 18 | 1 | 1.1 |  | 39 | 1 | 1.1 |  |  |  |  |
| 20 | 3 | 3.3 |  | 40 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 23 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 24 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.57 |  | 22 | 4 | 2.29 |  | 42 | 4 | 2.29 |
| 2 | 2 | 1.14 |  | 23 | 3 | 1.71 |  | 43 | 3 | 1.71 |
| 3 | 2 | 1.14 |  | 24 | 2 | 1.14 |  | 44 | 2 | 1.14 |
| 4 | 3 | 1.71 |  | 25 | 2 | 1.14 |  | 45 | 2 | 1.14 |
| 5 | 3 | 1.71 |  | 26 | 2 | 1.14 |  | 46 | 3 | 1.71 |
| 6 | 2 | 1.14 |  | 27 | 4 | 2.29 |  | 47 | 2 | 1.14 |
| 7 | 3 | 1.71 |  | 28 | 3 | 1.71 |  | 48 | 3 | 1.71 |
| 8 | 4 | 2.29 |  | 29 | 6 | 3.43 |  | 49 | 2 | 1.14 |
| 9 | 3 | 1.71 |  | 30 | 4 | 2.29 |  | 50 | 2 | 1.14 |
| 10 | 6 | 3.43 |  | 31 | 6 | 3.43 |  | 51 | 1 | 0.57 |
| 11 | 3 | 1.71 |  | 32 | 4 | 2.29 |  | 52 | 3 | 1.71 |
| 12 | 5 | 2.86 |  | 33 | 5 | 2.86 |  | 53 | 1 | 0.57 |
| 13 | 3 | 1.71 |  | 34 | 2 | 1.14 |  | 54 | 4 | 2.29 |
| 14 | 5 | 2.86 |  | 35 | 4 | 2.29 |  | 55 | 4 | 2.29 |
| 15 | 3 | 1.71 |  | 36 | 4 | 2.29 |  |  |  |  |
| 16 | 4 | 2.29 |  | 37 | 3 | 1.71 |  |  |  |  |
| 18 | 3 | 1.71 |  | 38 | 7 | 4.0 |  |  |  |  |
| 19 | 3 | 1.71 |  | 39 | 1 | 0.57 |  |  |  |  |
| 20 | 7 | 4.0 |  | 40 | 3 | 1.71 |  |  |  |  |
| 21 | 2 | 1.14 |  | 41 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.13 |  | 21 | 5 | 1.88 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 8 | 3.01 |  | 42 | 6 | 2.26 |
| 3 | 5 | 1.88 |  | 23 | 4 | 1.5 |  | 43 | 7 | 2.63 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 3 | 1.13 |
| 5 | 5 | 1.88 |  | 25 | 3 | 1.13 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 6 | 2.26 |
| 7 | 6 | 2.26 |  | 27 | 7 | 2.63 |  | 47 | 2 | 0.75 |
| 8 | 8 | 3.01 |  | 28 | 3 | 1.13 |  | 48 | 4 | 1.5 |
| 9 | 4 | 1.5 |  | 29 | 7 | 2.63 |  | 49 | 3 | 1.13 |
| 10 | 7 | 2.63 |  | 30 | 4 | 1.5 |  | 50 | 4 | 1.5 |
| 11 | 6 | 2.26 |  | 31 | 6 | 2.26 |  | 51 | 1 | 0.38 |
| 12 | 7 | 2.63 |  | 32 | 4 | 1.5 |  | 52 | 4 | 1.5 |
| 13 | 5 | 1.88 |  | 33 | 6 | 2.26 |  | 53 | 1 | 0.38 |
| 14 | 7 | 2.63 |  | 34 | 3 | 1.13 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 6 | 2.26 |  | 55 | 5 | 1.88 |
| 16 | 6 | 2.26 |  | 36 | 6 | 2.26 |  |  |  |  |
| 17 | 1 | 0.38 |  | 37 | 5 | 1.88 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 9 | 3.38 |  |  |  |  |
| 19 | 6 | 2.26 |  | 39 | 4 | 1.5 |  |  |  |  |
| 20 | 8 | 3.01 |  | 40 | 7 | 2.63 |  |  |  |  |



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

