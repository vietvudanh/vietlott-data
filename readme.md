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
| Power 655 | 1289 | 2017-08-01 | 2026-01-01 | 1289 | 00001 | 01289 |
| Power 645 | 1255 | 2017-10-25 | 2025-12-31 | 1255 | 00198 | 01452 |
| Power 535 | 163 | 2025-06-29 | 2026-01-01 | 326 | 00001 | 00374 |
| Keno | 420 | 2022-12-04 | 2026-01-02 | 54034 | #0110271 | #0265319 |
| 3D | 1019 | 2019-04-22 | 2025-12-31 | 1019 | 00001 | 01023 |
| 3D Pro | 666 | 2021-09-14 | 2026-01-01 | 666 | 00001 | 00670 |
| Bingo18 | 396 | 2024-12-03 | 2026-01-02 | 53088 | 0083123 | 0145886 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-01-01 | 01289 | [5, 16, 29, 33, 39, 42, 54] | 2026-01-02T00:00:56.179609 |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55, 38] | 2025-12-31T00:00:53.630435 |
| 2025-12-27 | 01287 | [16, 21, 30, 37, 39, 40, 13] | 2025-12-28T00:00:52.930719 |
| 2025-12-25 | 01286 | [4, 6, 32, 37, 40, 48, 38] | 2025-12-26T00:00:59.517363 |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38, 3] | 2025-12-24T00:00:51.363924 |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] | 2025-12-21T00:00:50.783917 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] | 2025-12-19T00:00:54.542458 |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55, 46] | 2025-12-17T00:00:57.950930 |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38, 52] | 2025-12-14T00:00:57.940661 |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55, 38] | 2025-12-12T00:01:16.182376 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 173 | 1.92 |  | 21 | 158 | 1.75 |  | 41 | 192 | 2.13 |
| 2 | 149 | 1.65 |  | 22 | 186 | 2.06 |  | 42 | 169 | 1.87 |
| 3 | 175 | 1.94 |  | 23 | 175 | 1.94 |  | 43 | 185 | 2.05 |
| 4 | 136 | 1.51 |  | 24 | 167 | 1.85 |  | 44 | 170 | 1.88 |
| 5 | 166 | 1.84 |  | 25 | 144 | 1.6 |  | 45 | 164 | 1.82 |
| 6 | 139 | 1.54 |  | 26 | 150 | 1.66 |  | 46 | 168 | 1.86 |
| 7 | 141 | 1.56 |  | 27 | 152 | 1.68 |  | 47 | 163 | 1.81 |
| 8 | 177 | 1.96 |  | 28 | 143 | 1.59 |  | 48 | 176 | 1.95 |
| 9 | 180 | 2.0 |  | 29 | 174 | 1.93 |  | 49 | 164 | 1.82 |
| 10 | 155 | 1.72 |  | 30 | 148 | 1.64 |  | 50 | 163 | 1.81 |
| 11 | 170 | 1.88 |  | 31 | 173 | 1.92 |  | 51 | 184 | 2.04 |
| 12 | 172 | 1.91 |  | 32 | 169 | 1.87 |  | 52 | 168 | 1.86 |
| 13 | 157 | 1.74 |  | 33 | 166 | 1.84 |  | 53 | 170 | 1.88 |
| 14 | 165 | 1.83 |  | 34 | 183 | 2.03 |  | 54 | 154 | 1.71 |
| 15 | 153 | 1.7 |  | 35 | 162 | 1.8 |  | 55 | 163 | 1.81 |
| 16 | 156 | 1.73 |  | 36 | 154 | 1.71 |  |  |  |  |
| 17 | 148 | 1.64 |  | 37 | 150 | 1.66 |  |  |  |  |
| 18 | 166 | 1.84 |  | 38 | 159 | 1.76 |  |  |  |  |
| 19 | 166 | 1.84 |  | 39 | 156 | 1.73 |  |  |  |  |
| 20 | 175 | 1.94 |  | 40 | 181 | 2.01 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 25 | 1 | 1.1 |  | 46 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 48 | 3 | 3.3 |
| 4 | 1 | 1.1 |  | 27 | 1 | 1.1 |  | 50 | 2 | 2.2 |
| 5 | 2 | 2.2 |  | 29 | 3 | 3.3 |  | 52 | 3 | 3.3 |
| 6 | 1 | 1.1 |  | 30 | 3 | 3.3 |  | 53 | 1 | 1.1 |
| 7 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 54 | 1 | 1.1 |
| 8 | 1 | 1.1 |  | 32 | 4 | 4.4 |  | 55 | 4 | 4.4 |
| 9 | 1 | 1.1 |  | 33 | 3 | 3.3 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 2 | 2.2 |  |  |  |  |
| 12 | 3 | 3.3 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 2 | 2.2 |  | 37 | 4 | 4.4 |  |  |  |  |
| 14 | 3 | 3.3 |  | 38 | 6 | 6.59 |  |  |  |  |
| 15 | 1 | 1.1 |  | 39 | 3 | 3.3 |  |  |  |  |
| 16 | 3 | 3.3 |  | 40 | 3 | 3.3 |  |  |  |  |
| 18 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 20 | 1 | 1.1 |  | 42 | 2 | 2.2 |  |  |  |  |
| 21 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |
| 23 | 1 | 1.1 |  | 45 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.55 |  | 22 | 3 | 1.65 |  | 42 | 5 | 2.75 |
| 2 | 2 | 1.1 |  | 23 | 2 | 1.1 |  | 43 | 3 | 1.65 |
| 3 | 2 | 1.1 |  | 24 | 2 | 1.1 |  | 44 | 2 | 1.1 |
| 4 | 4 | 2.2 |  | 25 | 1 | 0.55 |  | 45 | 2 | 1.1 |
| 5 | 4 | 2.2 |  | 26 | 2 | 1.1 |  | 46 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 27 | 4 | 2.2 |  | 47 | 1 | 0.55 |
| 7 | 2 | 1.1 |  | 28 | 2 | 1.1 |  | 48 | 5 | 2.75 |
| 8 | 2 | 1.1 |  | 29 | 6 | 3.3 |  | 49 | 2 | 1.1 |
| 9 | 2 | 1.1 |  | 30 | 6 | 3.3 |  | 50 | 2 | 1.1 |
| 10 | 5 | 2.75 |  | 31 | 5 | 2.75 |  | 51 | 1 | 0.55 |
| 11 | 3 | 1.65 |  | 32 | 5 | 2.75 |  | 52 | 3 | 1.65 |
| 12 | 5 | 2.75 |  | 33 | 5 | 2.75 |  | 53 | 1 | 0.55 |
| 13 | 4 | 2.2 |  | 34 | 2 | 1.1 |  | 54 | 4 | 2.2 |
| 14 | 5 | 2.75 |  | 35 | 4 | 2.2 |  | 55 | 4 | 2.2 |
| 15 | 3 | 1.65 |  | 36 | 4 | 2.2 |  |  |  |  |
| 16 | 6 | 3.3 |  | 37 | 4 | 2.2 |  |  |  |  |
| 18 | 3 | 1.65 |  | 38 | 9 | 4.95 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 3 | 1.65 |  |  |  |  |
| 20 | 6 | 3.3 |  | 40 | 5 | 2.75 |  |  |  |  |
| 21 | 3 | 1.65 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0.37 |  | 22 | 8 | 2.93 |  | 42 | 6 | 2.2 |
| 2 | 2 | 0.73 |  | 23 | 3 | 1.1 |  | 43 | 6 | 2.2 |
| 3 | 5 | 1.83 |  | 24 | 4 | 1.47 |  | 44 | 3 | 1.1 |
| 4 | 4 | 1.47 |  | 25 | 3 | 1.1 |  | 45 | 5 | 1.83 |
| 5 | 6 | 2.2 |  | 26 | 5 | 1.83 |  | 46 | 4 | 1.47 |
| 6 | 3 | 1.1 |  | 27 | 6 | 2.2 |  | 47 | 2 | 0.73 |
| 7 | 6 | 2.2 |  | 28 | 3 | 1.1 |  | 48 | 6 | 2.2 |
| 8 | 6 | 2.2 |  | 29 | 8 | 2.93 |  | 49 | 3 | 1.1 |
| 9 | 4 | 1.47 |  | 30 | 6 | 2.2 |  | 50 | 4 | 1.47 |
| 10 | 7 | 2.56 |  | 31 | 6 | 2.2 |  | 51 | 1 | 0.37 |
| 11 | 7 | 2.56 |  | 32 | 5 | 1.83 |  | 52 | 3 | 1.1 |
| 12 | 7 | 2.56 |  | 33 | 7 | 2.56 |  | 53 | 1 | 0.37 |
| 13 | 5 | 1.83 |  | 34 | 2 | 0.73 |  | 54 | 5 | 1.83 |
| 14 | 7 | 2.56 |  | 35 | 7 | 2.56 |  | 55 | 6 | 2.2 |
| 15 | 4 | 1.47 |  | 36 | 6 | 2.2 |  |  |  |  |
| 16 | 8 | 2.93 |  | 37 | 7 | 2.56 |  |  |  |  |
| 18 | 3 | 1.1 |  | 38 | 11 | 4.03 |  |  |  |  |
| 19 | 5 | 1.83 |  | 39 | 4 | 1.47 |  |  |  |  |
| 20 | 7 | 2.56 |  | 40 | 9 | 3.3 |  |  |  |  |
| 21 | 6 | 2.2 |  | 41 | 5 | 1.83 |  |  |  |  |



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

