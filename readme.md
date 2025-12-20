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
| Power 655 | 1284 | 2017-08-01 | 2025-12-20 | 1284 | 00001 | 01284 |
| Power 645 | 1250 | 2017-10-25 | 2025-12-19 | 1250 | 00198 | 01447 |
| Power 535 | 151 | 2025-06-29 | 2025-12-20 | 302 | 00001 | 00350 |
| Keno | 407 | 2022-12-04 | 2025-12-20 | 52487 | #0110271 | #0263772 |
| 3D | 1014 | 2019-04-22 | 2025-12-19 | 1014 | 00001 | 01018 |
| 3D Pro | 661 | 2021-09-14 | 2025-12-20 | 661 | 00001 | 00665 |
| Bingo18 | 383 | 2024-12-03 | 2025-12-20 | 52788 | 0083123 | 0143918 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] | 2025-12-21T00:00:50.783917 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] | 2025-12-19T00:00:54.542458 |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46] | 2025-12-17T00:00:57.950930 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52] | 2025-12-14T00:00:57.940661 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43, 42] | 2025-12-10T00:00:51.279107 |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52, 15] | 2025-12-07T00:00:57.664427 |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53, 14] | 2025-12-05T00:00:49.739433 |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54, 10] | 2025-12-03T00:00:48.323884 |
| 2025-11-29 | 01275 | [4, 20, 24, 27, 40, 48, 9] | 2025-11-30T00:00:57.885215 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.93 |  | 21 | 157 | 1.75 |  | 41 | 191 | 2.13 |
| 2 | 148 | 1.65 |  | 22 | 186 | 2.07 |  | 42 | 168 | 1.87 |
| 3 | 174 | 1.94 |  | 23 | 175 | 1.95 |  | 43 | 185 | 2.06 |
| 4 | 135 | 1.5 |  | 24 | 167 | 1.86 |  | 44 | 170 | 1.89 |
| 5 | 165 | 1.84 |  | 25 | 143 | 1.59 |  | 45 | 164 | 1.82 |
| 6 | 138 | 1.54 |  | 26 | 150 | 1.67 |  | 46 | 168 | 1.87 |
| 7 | 141 | 1.57 |  | 27 | 152 | 1.69 |  | 47 | 163 | 1.81 |
| 8 | 177 | 1.97 |  | 28 | 143 | 1.59 |  | 48 | 174 | 1.94 |
| 9 | 180 | 2.0 |  | 29 | 173 | 1.93 |  | 49 | 164 | 1.82 |
| 10 | 154 | 1.71 |  | 30 | 146 | 1.62 |  | 50 | 163 | 1.81 |
| 11 | 169 | 1.88 |  | 31 | 173 | 1.93 |  | 51 | 184 | 2.05 |
| 12 | 172 | 1.91 |  | 32 | 167 | 1.86 |  | 52 | 168 | 1.87 |
| 13 | 156 | 1.74 |  | 33 | 165 | 1.84 |  | 53 | 170 | 1.89 |
| 14 | 165 | 1.84 |  | 34 | 183 | 2.04 |  | 54 | 153 | 1.7 |
| 15 | 153 | 1.7 |  | 35 | 161 | 1.79 |  | 55 | 162 | 1.8 |
| 16 | 153 | 1.7 |  | 36 | 154 | 1.71 |  |  |  |  |
| 17 | 148 | 1.65 |  | 37 | 148 | 1.65 |  |  |  |  |
| 18 | 166 | 1.85 |  | 38 | 156 | 1.74 |  |  |  |  |
| 19 | 166 | 1.85 |  | 39 | 154 | 1.71 |  |  |  |  |
| 20 | 175 | 1.95 |  | 40 | 179 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 48 | 3 | 3.3 |
| 5 | 2 | 2.2 |  | 28 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 7 | 1 | 1.1 |  | 29 | 3 | 3.3 |  | 51 | 1 | 1.1 |
| 8 | 2 | 2.2 |  | 30 | 1 | 1.1 |  | 52 | 3 | 3.3 |
| 9 | 2 | 2.2 |  | 31 | 2 | 2.2 |  | 53 | 1 | 1.1 |
| 10 | 4 | 4.4 |  | 32 | 3 | 3.3 |  | 54 | 1 | 1.1 |
| 11 | 1 | 1.1 |  | 33 | 2 | 2.2 |  | 55 | 3 | 3.3 |
| 12 | 3 | 3.3 |  | 34 | 2 | 2.2 |  |  |  |  |
| 13 | 1 | 1.1 |  | 35 | 2 | 2.2 |  |  |  |  |
| 14 | 4 | 4.4 |  | 36 | 2 | 2.2 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 1 | 1.1 |  | 38 | 4 | 4.4 |  |  |  |  |
| 18 | 1 | 1.1 |  | 39 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 20 | 3 | 3.3 |  | 41 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 42 | 2 | 2.2 |  |  |  |  |
| 22 | 1 | 1.1 |  | 43 | 1 | 1.1 |  |  |  |  |
| 23 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |
| 24 | 2 | 2.2 |  | 45 | 1 | 1.1 |  |  |  |  |
| 26 | 2 | 2.2 |  | 46 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 22 | 4 | 2.2 |  | 42 | 4 | 2.2 |
| 2 | 1 | 0.55 |  | 23 | 3 | 1.65 |  | 43 | 3 | 1.65 |
| 3 | 2 | 1.1 |  | 24 | 3 | 1.65 |  | 44 | 2 | 1.1 |
| 4 | 3 | 1.65 |  | 25 | 1 | 0.55 |  | 45 | 3 | 1.65 |
| 5 | 4 | 2.2 |  | 26 | 2 | 1.1 |  | 46 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 27 | 5 | 2.75 |  | 47 | 2 | 1.1 |
| 7 | 3 | 1.65 |  | 28 | 3 | 1.65 |  | 48 | 4 | 2.2 |
| 8 | 5 | 2.75 |  | 29 | 6 | 3.3 |  | 49 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 30 | 4 | 2.2 |  | 50 | 3 | 1.65 |
| 10 | 6 | 3.3 |  | 31 | 6 | 3.3 |  | 51 | 1 | 0.55 |
| 11 | 4 | 2.2 |  | 32 | 3 | 1.65 |  | 52 | 3 | 1.65 |
| 12 | 5 | 2.75 |  | 33 | 5 | 2.75 |  | 53 | 1 | 0.55 |
| 13 | 4 | 2.2 |  | 34 | 2 | 1.1 |  | 54 | 4 | 2.2 |
| 14 | 5 | 2.75 |  | 35 | 4 | 2.2 |  | 55 | 4 | 2.2 |
| 15 | 3 | 1.65 |  | 36 | 4 | 2.2 |  |  |  |  |
| 16 | 3 | 1.65 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 6 | 3.3 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 1 | 0.55 |  |  |  |  |
| 20 | 7 | 3.85 |  | 40 | 4 | 2.2 |  |  |  |  |
| 21 | 3 | 1.65 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.1 |  | 21 | 5 | 1.83 |  | 41 | 5 | 1.83 |
| 2 | 2 | 0.73 |  | 22 | 8 | 2.93 |  | 42 | 6 | 2.2 |
| 3 | 4 | 1.47 |  | 23 | 4 | 1.47 |  | 43 | 7 | 2.56 |
| 4 | 3 | 1.1 |  | 24 | 6 | 2.2 |  | 44 | 3 | 1.1 |
| 5 | 6 | 2.2 |  | 25 | 2 | 0.73 |  | 45 | 5 | 1.83 |
| 6 | 2 | 0.73 |  | 26 | 5 | 1.83 |  | 46 | 7 | 2.56 |
| 7 | 6 | 2.2 |  | 27 | 7 | 2.56 |  | 47 | 2 | 0.73 |
| 8 | 10 | 3.66 |  | 28 | 3 | 1.1 |  | 48 | 4 | 1.47 |
| 9 | 4 | 1.47 |  | 29 | 7 | 2.56 |  | 49 | 3 | 1.1 |
| 10 | 6 | 2.2 |  | 30 | 5 | 1.83 |  | 50 | 4 | 1.47 |
| 11 | 6 | 2.2 |  | 31 | 7 | 2.56 |  | 51 | 1 | 0.37 |
| 12 | 7 | 2.56 |  | 32 | 3 | 1.1 |  | 52 | 4 | 1.47 |
| 13 | 5 | 1.83 |  | 33 | 6 | 2.2 |  | 53 | 2 | 0.73 |
| 14 | 7 | 2.56 |  | 34 | 4 | 1.47 |  | 54 | 4 | 1.47 |
| 15 | 4 | 1.47 |  | 35 | 6 | 2.2 |  | 55 | 5 | 1.83 |
| 16 | 5 | 1.83 |  | 36 | 6 | 2.2 |  |  |  |  |
| 17 | 2 | 0.73 |  | 37 | 5 | 1.83 |  |  |  |  |
| 18 | 4 | 1.47 |  | 38 | 10 | 3.66 |  |  |  |  |
| 19 | 7 | 2.56 |  | 39 | 4 | 1.47 |  |  |  |  |
| 20 | 8 | 2.93 |  | 40 | 7 | 2.56 |  |  |  |  |



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

