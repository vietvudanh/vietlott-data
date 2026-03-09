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
| Power 655 | 1316 | 2017-08-01 | 2026-03-07 | 1316 | 00001 | 01316 |
| Power 645 | 1284 | 2017-10-25 | 2026-03-08 | 1284 | 00198 | 01481 |
| Power 535 | 229 | 2025-06-29 | 2026-03-09 | 458 | 00001 | 00508 |
| Keno | 479 | 2022-12-04 | 2026-03-09 | 60794 | #0110271 | #0273248 |
| 3D | 1047 | 2019-04-22 | 2026-03-09 | 1047 | 00001 | 01051 |
| 3D Pro | 693 | 2021-09-14 | 2026-03-07 | 693 | 00001 | 00697 |
| Bingo18 | 453 | 2024-12-03 | 2026-03-09 | 54384 | 0083123 | 0156479 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-03-07 | 01316 | [4, 32, 41, 45, 50, 52, 29] | 2026-03-08T00:01:04.043596 |
| 2026-03-05 | 01315 | [14, 16, 35, 38, 43, 51, 37] | 2026-03-06T00:01:02.441420 |
| 2026-03-03 | 01314 | [7, 13, 27, 29, 43, 50, 25] | 2026-03-04T00:00:55.331151 |
| 2026-02-28 | 01313 | [22, 25, 31, 44, 51, 54, 36] | 2026-03-01T00:00:58.241470 |
| 2026-02-26 | 01312 | [1, 7, 10, 21, 44, 51, 46] | 2026-02-27T00:00:58.514222 |
| 2026-02-24 | 01311 | [5, 8, 18, 30, 39, 54, 51] | 2026-02-25T09:14:17.252048 |
| 2026-02-21 | 01310 | [5, 7, 26, 30, 41, 45, 12] | 2026-02-23T00:01:21.197262 |
| 2026-02-19 | 01309 | [1, 27, 30, 43, 45, 46, 48] | 2026-02-21T00:00:56.973082 |
| 2026-02-14 | 01308 | [2, 13, 26, 32, 36, 42, 48] | 2026-02-21T00:00:56.975209 |
| 2026-02-12 | 01307 | [8, 17, 19, 31, 32, 46, 26] | 2026-02-21T00:00:56.982362 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 176 | 1.91 |  | 21 | 163 | 1.77 |  | 41 | 195 | 2.12 |
| 2 | 151 | 1.64 |  | 22 | 193 | 2.1 |  | 42 | 172 | 1.87 |
| 3 | 177 | 1.92 |  | 23 | 177 | 1.92 |  | 43 | 190 | 2.06 |
| 4 | 139 | 1.51 |  | 24 | 168 | 1.82 |  | 44 | 172 | 1.87 |
| 5 | 170 | 1.85 |  | 25 | 150 | 1.63 |  | 45 | 169 | 1.83 |
| 6 | 139 | 1.51 |  | 26 | 156 | 1.69 |  | 46 | 173 | 1.88 |
| 7 | 145 | 1.57 |  | 27 | 155 | 1.68 |  | 47 | 165 | 1.79 |
| 8 | 179 | 1.94 |  | 28 | 146 | 1.59 |  | 48 | 181 | 1.97 |
| 9 | 182 | 1.98 |  | 29 | 180 | 1.95 |  | 49 | 166 | 1.8 |
| 10 | 158 | 1.72 |  | 30 | 154 | 1.67 |  | 50 | 167 | 1.81 |
| 11 | 172 | 1.87 |  | 31 | 176 | 1.91 |  | 51 | 189 | 2.05 |
| 12 | 175 | 1.9 |  | 32 | 176 | 1.91 |  | 52 | 170 | 1.85 |
| 13 | 164 | 1.78 |  | 33 | 168 | 1.82 |  | 53 | 174 | 1.89 |
| 14 | 169 | 1.83 |  | 34 | 187 | 2.03 |  | 54 | 159 | 1.73 |
| 15 | 156 | 1.69 |  | 35 | 164 | 1.78 |  | 55 | 167 | 1.81 |
| 16 | 160 | 1.74 |  | 36 | 159 | 1.73 |  |  |  |  |
| 17 | 151 | 1.64 |  | 37 | 152 | 1.65 |  |  |  |  |
| 18 | 169 | 1.83 |  | 38 | 161 | 1.75 |  |  |  |  |
| 19 | 167 | 1.81 |  | 39 | 157 | 1.7 |  |  |  |  |
| 20 | 180 | 1.95 |  | 40 | 181 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.6 |  | 29 | 2 | 2.6 |  | 55 | 1 | 1.3 |
| 2 | 1 | 1.3 |  | 30 | 3 | 3.9 |  |  |  |  |
| 4 | 1 | 1.3 |  | 31 | 2 | 2.6 |  |  |  |  |
| 5 | 2 | 2.6 |  | 32 | 4 | 5.19 |  |  |  |  |
| 7 | 3 | 3.9 |  | 35 | 1 | 1.3 |  |  |  |  |
| 8 | 2 | 2.6 |  | 36 | 2 | 2.6 |  |  |  |  |
| 10 | 1 | 1.3 |  | 37 | 1 | 1.3 |  |  |  |  |
| 12 | 1 | 1.3 |  | 38 | 1 | 1.3 |  |  |  |  |
| 13 | 3 | 3.9 |  | 39 | 1 | 1.3 |  |  |  |  |
| 14 | 1 | 1.3 |  | 41 | 2 | 2.6 |  |  |  |  |
| 16 | 1 | 1.3 |  | 42 | 1 | 1.3 |  |  |  |  |
| 17 | 1 | 1.3 |  | 43 | 3 | 3.9 |  |  |  |  |
| 18 | 1 | 1.3 |  | 44 | 2 | 2.6 |  |  |  |  |
| 19 | 1 | 1.3 |  | 45 | 3 | 3.9 |  |  |  |  |
| 20 | 1 | 1.3 |  | 46 | 3 | 3.9 |  |  |  |  |
| 21 | 2 | 2.6 |  | 48 | 2 | 2.6 |  |  |  |  |
| 22 | 2 | 2.6 |  | 50 | 2 | 2.6 |  |  |  |  |
| 25 | 2 | 2.6 |  | 51 | 4 | 5.19 |  |  |  |  |
| 26 | 4 | 5.19 |  | 52 | 1 | 1.3 |  |  |  |  |
| 27 | 2 | 2.6 |  | 54 | 2 | 2.6 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.79 |  | 22 | 5 | 2.98 |  | 43 | 4 | 2.38 |
| 2 | 2 | 1.19 |  | 23 | 1 | 0.6 |  | 44 | 2 | 1.19 |
| 3 | 2 | 1.19 |  | 24 | 1 | 0.6 |  | 45 | 4 | 2.38 |
| 4 | 3 | 1.79 |  | 25 | 6 | 3.57 |  | 46 | 5 | 2.98 |
| 5 | 4 | 2.38 |  | 26 | 6 | 3.57 |  | 48 | 5 | 2.98 |
| 7 | 4 | 2.38 |  | 27 | 3 | 1.79 |  | 49 | 2 | 1.19 |
| 8 | 2 | 1.19 |  | 28 | 2 | 1.19 |  | 50 | 3 | 1.79 |
| 9 | 2 | 1.19 |  | 29 | 5 | 2.98 |  | 51 | 5 | 2.98 |
| 10 | 2 | 1.19 |  | 30 | 5 | 2.98 |  | 52 | 2 | 1.19 |
| 11 | 2 | 1.19 |  | 31 | 3 | 1.79 |  | 53 | 4 | 2.38 |
| 12 | 3 | 1.79 |  | 32 | 7 | 4.17 |  | 54 | 5 | 2.98 |
| 13 | 7 | 4.17 |  | 33 | 1 | 0.6 |  | 55 | 4 | 2.38 |
| 14 | 4 | 2.38 |  | 34 | 3 | 1.79 |  |  |  |  |
| 15 | 3 | 1.79 |  | 35 | 2 | 1.19 |  |  |  |  |
| 16 | 3 | 1.79 |  | 36 | 3 | 1.79 |  |  |  |  |
| 17 | 2 | 1.19 |  | 37 | 2 | 1.19 |  |  |  |  |
| 18 | 3 | 1.79 |  | 38 | 2 | 1.19 |  |  |  |  |
| 19 | 1 | 0.6 |  | 39 | 1 | 0.6 |  |  |  |  |
| 20 | 3 | 1.79 |  | 41 | 3 | 1.79 |  |  |  |  |
| 21 | 5 | 2.98 |  | 42 | 2 | 1.19 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.16 |  | 21 | 7 | 2.7 |  | 41 | 5 | 1.93 |
| 2 | 3 | 1.16 |  | 22 | 8 | 3.09 |  | 42 | 4 | 1.54 |
| 3 | 3 | 1.16 |  | 23 | 3 | 1.16 |  | 43 | 5 | 1.93 |
| 4 | 4 | 1.54 |  | 24 | 1 | 0.39 |  | 44 | 2 | 0.77 |
| 5 | 6 | 2.32 |  | 25 | 7 | 2.7 |  | 45 | 6 | 2.32 |
| 6 | 1 | 0.39 |  | 26 | 6 | 2.32 |  | 46 | 6 | 2.32 |
| 7 | 5 | 1.93 |  | 27 | 3 | 1.16 |  | 47 | 2 | 0.77 |
| 8 | 3 | 1.16 |  | 28 | 3 | 1.16 |  | 48 | 8 | 3.09 |
| 9 | 3 | 1.16 |  | 29 | 8 | 3.09 |  | 49 | 2 | 0.77 |
| 10 | 4 | 1.54 |  | 30 | 9 | 3.47 |  | 50 | 5 | 1.93 |
| 11 | 3 | 1.16 |  | 31 | 3 | 1.16 |  | 51 | 5 | 1.93 |
| 12 | 5 | 1.93 |  | 32 | 10 | 3.86 |  | 52 | 4 | 1.54 |
| 13 | 9 | 3.47 |  | 33 | 4 | 1.54 |  | 53 | 4 | 1.54 |
| 14 | 5 | 1.93 |  | 34 | 4 | 1.54 |  | 54 | 6 | 2.32 |
| 15 | 3 | 1.16 |  | 35 | 4 | 1.54 |  | 55 | 8 | 3.09 |
| 16 | 7 | 2.7 |  | 36 | 6 | 2.32 |  |  |  |  |
| 17 | 3 | 1.16 |  | 37 | 5 | 1.93 |  |  |  |  |
| 18 | 4 | 1.54 |  | 38 | 8 | 3.09 |  |  |  |  |
| 19 | 1 | 0.39 |  | 39 | 4 | 1.54 |  |  |  |  |
| 20 | 6 | 2.32 |  | 40 | 3 | 1.16 |  |  |  |  |



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

