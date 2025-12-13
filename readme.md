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
| Power 655 | 1280 | 2017-08-01 | 2025-12-11 | 1280 | 00001 | 01280 |
| Power 645 | 1247 | 2017-10-25 | 2025-12-12 | 1247 | 00198 | 01444 |
| Power 535 | 143 | 2025-06-29 | 2025-12-12 | 286 | 00001 | 00334 |
| Keno | 400 | 2022-12-04 | 2025-12-13 | 51654 | #0110271 | #0262939 |
| 3D | 1011 | 2019-04-22 | 2025-12-12 | 1011 | 00001 | 01015 |
| 3D Pro | 657 | 2021-09-14 | 2025-12-11 | 657 | 00001 | 00661 |
| Bingo18 | 376 | 2024-12-03 | 2025-12-13 | 52608 | 0083123 | 0142706 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43, 42] | 2025-12-10T00:00:51.279107 |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52, 15] | 2025-12-07T00:00:57.664427 |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53, 14] | 2025-12-05T00:00:49.739433 |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54, 10] | 2025-12-03T00:00:48.323884 |
| 2025-11-29 | 01275 | [4, 20, 24, 27, 40, 48, 9] | 2025-11-30T00:00:57.885215 |
| 2025-11-27 | 01274 | [4, 5, 10, 11, 28, 35, 38] | 2025-11-28T00:00:53.620470 |
| 2025-11-25 | 01273 | [23, 31, 32, 42, 46, 48, 4] | 2025-11-26T00:00:52.128543 |
| 2025-11-22 | 01272 | [8, 10, 19, 29, 34, 46, 14] | 2025-11-23T00:00:55.277843 |
| 2025-11-20 | 01271 | [3, 12, 19, 20, 31, 42, 13] | 2025-11-21T00:00:55.461521 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.93 |  | 21 | 157 | 1.75 |  | 41 | 190 | 2.12 |
| 2 | 148 | 1.65 |  | 22 | 185 | 2.06 |  | 42 | 168 | 1.88 |
| 3 | 174 | 1.94 |  | 23 | 174 | 1.94 |  | 43 | 185 | 2.06 |
| 4 | 135 | 1.51 |  | 24 | 167 | 1.86 |  | 44 | 170 | 1.9 |
| 5 | 164 | 1.83 |  | 25 | 143 | 1.6 |  | 45 | 164 | 1.83 |
| 6 | 138 | 1.54 |  | 26 | 150 | 1.67 |  | 46 | 167 | 1.86 |
| 7 | 140 | 1.56 |  | 27 | 152 | 1.7 |  | 47 | 163 | 1.82 |
| 8 | 176 | 1.96 |  | 28 | 143 | 1.6 |  | 48 | 174 | 1.94 |
| 9 | 180 | 2.01 |  | 29 | 172 | 1.92 |  | 49 | 164 | 1.83 |
| 10 | 154 | 1.72 |  | 30 | 145 | 1.62 |  | 50 | 162 | 1.81 |
| 11 | 169 | 1.89 |  | 31 | 173 | 1.93 |  | 51 | 184 | 2.05 |
| 12 | 170 | 1.9 |  | 32 | 166 | 1.85 |  | 52 | 166 | 1.85 |
| 13 | 156 | 1.74 |  | 33 | 164 | 1.83 |  | 53 | 170 | 1.9 |
| 14 | 164 | 1.83 |  | 34 | 183 | 2.04 |  | 54 | 153 | 1.71 |
| 15 | 153 | 1.71 |  | 35 | 160 | 1.79 |  | 55 | 160 | 1.79 |
| 16 | 153 | 1.71 |  | 36 | 153 | 1.71 |  |  |  |  |
| 17 | 148 | 1.65 |  | 37 | 147 | 1.64 |  |  |  |  |
| 18 | 165 | 1.84 |  | 38 | 154 | 1.72 |  |  |  |  |
| 19 | 166 | 1.85 |  | 39 | 153 | 1.71 |  |  |  |  |
| 20 | 174 | 1.94 |  | 40 | 178 | 1.99 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.1 |  | 23 | 1 | 1.1 |  | 46 | 2 | 2.2 |
| 2 | 1 | 1.1 |  | 24 | 2 | 2.2 |  | 48 | 3 | 3.3 |
| 3 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 4 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 50 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 28 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 8 | 1 | 1.1 |  | 30 | 3 | 3.3 |  | 53 | 1 | 1.1 |
| 9 | 2 | 2.2 |  | 31 | 3 | 3.3 |  | 54 | 2 | 2.2 |
| 10 | 4 | 4.4 |  | 32 | 2 | 2.2 |  | 55 | 1 | 1.1 |
| 11 | 1 | 1.1 |  | 33 | 2 | 2.2 |  |  |  |  |
| 12 | 3 | 3.3 |  | 34 | 2 | 2.2 |  |  |  |  |
| 13 | 3 | 3.3 |  | 35 | 2 | 2.2 |  |  |  |  |
| 14 | 3 | 3.3 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 2 | 2.2 |  | 37 | 1 | 1.1 |  |  |  |  |
| 16 | 1 | 1.1 |  | 38 | 3 | 3.3 |  |  |  |  |
| 18 | 1 | 1.1 |  | 40 | 2 | 2.2 |  |  |  |  |
| 19 | 2 | 2.2 |  | 42 | 4 | 4.4 |  |  |  |  |
| 20 | 3 | 3.3 |  | 43 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 22 | 4 | 2.2 |  | 43 | 4 | 2.2 |
| 2 | 1 | 0.55 |  | 23 | 2 | 1.1 |  | 44 | 2 | 1.1 |
| 3 | 3 | 1.65 |  | 24 | 4 | 2.2 |  | 45 | 4 | 2.2 |
| 4 | 3 | 1.65 |  | 25 | 1 | 0.55 |  | 46 | 2 | 1.1 |
| 5 | 4 | 2.2 |  | 26 | 4 | 2.2 |  | 47 | 2 | 1.1 |
| 6 | 2 | 1.1 |  | 27 | 6 | 3.3 |  | 48 | 4 | 2.2 |
| 7 | 2 | 1.1 |  | 28 | 3 | 1.65 |  | 49 | 3 | 1.65 |
| 8 | 5 | 2.75 |  | 29 | 5 | 2.75 |  | 50 | 3 | 1.65 |
| 9 | 4 | 2.2 |  | 30 | 3 | 1.65 |  | 51 | 1 | 0.55 |
| 10 | 6 | 3.3 |  | 31 | 6 | 3.3 |  | 52 | 1 | 0.55 |
| 11 | 5 | 2.75 |  | 32 | 2 | 1.1 |  | 53 | 1 | 0.55 |
| 12 | 5 | 2.75 |  | 33 | 4 | 2.2 |  | 54 | 4 | 2.2 |
| 13 | 4 | 2.2 |  | 34 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 14 | 6 | 3.3 |  | 35 | 3 | 1.65 |  |  |  |  |
| 15 | 4 | 2.2 |  | 36 | 4 | 2.2 |  |  |  |  |
| 16 | 5 | 2.75 |  | 37 | 3 | 1.65 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 5 | 2.75 |  |  |  |  |
| 19 | 4 | 2.2 |  | 40 | 4 | 2.2 |  |  |  |  |
| 20 | 6 | 3.3 |  | 41 | 3 | 1.65 |  |  |  |  |
| 21 | 4 | 2.2 |  | 42 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.13 |  | 21 | 5 | 1.88 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 7 | 2.63 |  | 42 | 6 | 2.26 |
| 3 | 5 | 1.88 |  | 23 | 3 | 1.13 |  | 43 | 9 | 3.38 |
| 4 | 3 | 1.13 |  | 24 | 6 | 2.26 |  | 44 | 3 | 1.13 |
| 5 | 5 | 1.88 |  | 25 | 2 | 0.75 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 5 | 1.88 |  | 46 | 6 | 2.26 |
| 7 | 5 | 1.88 |  | 27 | 8 | 3.01 |  | 47 | 2 | 0.75 |
| 8 | 11 | 4.14 |  | 28 | 4 | 1.5 |  | 48 | 4 | 1.5 |
| 9 | 4 | 1.5 |  | 29 | 6 | 2.26 |  | 49 | 3 | 1.13 |
| 10 | 6 | 2.26 |  | 30 | 5 | 1.88 |  | 50 | 3 | 1.13 |
| 11 | 6 | 2.26 |  | 31 | 7 | 2.63 |  | 51 | 1 | 0.38 |
| 12 | 5 | 1.88 |  | 32 | 2 | 0.75 |  | 52 | 2 | 0.75 |
| 13 | 6 | 2.26 |  | 33 | 6 | 2.26 |  | 53 | 3 | 1.13 |
| 14 | 7 | 2.63 |  | 34 | 4 | 1.5 |  | 54 | 4 | 1.5 |
| 15 | 4 | 1.5 |  | 35 | 5 | 1.88 |  | 55 | 4 | 1.5 |
| 16 | 5 | 1.88 |  | 36 | 6 | 2.26 |  |  |  |  |
| 17 | 3 | 1.13 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 9 | 3.38 |  |  |  |  |
| 19 | 9 | 3.38 |  | 39 | 4 | 1.5 |  |  |  |  |
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

