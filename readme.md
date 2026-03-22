# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

## 🔗 Links

- 🌐 [Website](https://vietvudanh.github.io/vietlott-data/) - Interactive data visualization
- 📝 [Blog Post](https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the) - About this project

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

- [🔗 Links](#-links)
- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [Predictions](#-predictions)
- [📊 Data Statistics](#-data-statistics)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
  - [⏳ Top 10 Numbers by Days Since Last Appearance](#-top-10-số-lâu-chưa-xuất-hiện-top-10-numbers-by-days-since-last-appearance)
  - [📆 Days Since Last Appearance - All Numbers](#-số-ngày-từ-lần-xuất-hiện-cuối-cùng-days-since-last-appearance---all-numbers)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## Predictions

Predicitons models are at [/src/predictions](./src/machine_learning/).

For background on these models, see the [Machine Learning README](./src/machine_learning/).

## 📊 Data Statistics

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 1322 | 2017-08-01 | 2026-03-21 | 1322 | 00001 | 01322 |
| Power 645 | 1290 | 2017-10-25 | 2026-03-22 | 1290 | 00198 | 01487 |
| Power 535 | 242 | 2025-06-29 | 2026-03-22 | 484 | 00001 | 00534 |
| Keno | 492 | 2022-12-04 | 2026-03-22 | 62253 | #0110271 | #0274795 |
| 3D | 1052 | 2019-04-22 | 2026-03-20 | 1052 | 00001 | 01056 |
| 3D Pro | 699 | 2021-09-14 | 2026-03-21 | 699 | 00001 | 00703 |
| Bingo18 | 466 | 2024-12-03 | 2026-03-22 | 54655 | 0083123 | 0158546 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-03-21 | 01322 | [1, 6, 40, 43, 47, 53, 3] | 2026-03-22T00:00:58.677766 |
| 2026-03-19 | 01321 | [7, 9, 17, 31, 34, 36, 55] | 2026-03-20T00:00:58.910179 |
| 2026-03-17 | 01320 | [12, 26, 28, 43, 50, 54, 52] | 2026-03-18T00:00:56.999640 |
| 2026-03-14 | 01319 | [7, 16, 27, 29, 47, 52, 26] | 2026-03-15T00:00:52.883799 |
| 2026-03-12 | 01318 | [12, 28, 36, 40, 53, 55, 54] | 2026-03-13T00:00:57.770966 |
| 2026-03-10 | 01317 | [3, 26, 31, 39, 47, 54, 20] | 2026-03-12T00:00:58.996922 |
| 2026-03-07 | 01316 | [4, 32, 41, 45, 50, 52, 29] | 2026-03-08T00:01:04.043596 |
| 2026-03-05 | 01315 | [14, 16, 35, 38, 43, 51, 37] | 2026-03-06T00:01:02.441420 |
| 2026-03-03 | 01314 | [7, 13, 27, 29, 43, 50, 25] | 2026-03-04T00:00:55.331151 |
| 2026-02-28 | 01313 | [22, 25, 31, 44, 51, 54, 36] | 2026-03-01T00:00:58.241470 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 177 | 1.91 |  | 21 | 163 | 1.76 |  | 41 | 195 | 2.11 |
| 2 | 151 | 1.63 |  | 22 | 193 | 2.09 |  | 42 | 172 | 1.86 |
| 3 | 179 | 1.93 |  | 23 | 177 | 1.91 |  | 43 | 192 | 2.08 |
| 4 | 139 | 1.5 |  | 24 | 168 | 1.82 |  | 44 | 172 | 1.86 |
| 5 | 170 | 1.84 |  | 25 | 150 | 1.62 |  | 45 | 169 | 1.83 |
| 6 | 140 | 1.51 |  | 26 | 159 | 1.72 |  | 46 | 173 | 1.87 |
| 7 | 147 | 1.59 |  | 27 | 156 | 1.69 |  | 47 | 168 | 1.82 |
| 8 | 179 | 1.93 |  | 28 | 148 | 1.6 |  | 48 | 181 | 1.96 |
| 9 | 183 | 1.98 |  | 29 | 181 | 1.96 |  | 49 | 166 | 1.79 |
| 10 | 158 | 1.71 |  | 30 | 154 | 1.66 |  | 50 | 168 | 1.82 |
| 11 | 172 | 1.86 |  | 31 | 178 | 1.92 |  | 51 | 189 | 2.04 |
| 12 | 177 | 1.91 |  | 32 | 176 | 1.9 |  | 52 | 172 | 1.86 |
| 13 | 164 | 1.77 |  | 33 | 168 | 1.82 |  | 53 | 176 | 1.9 |
| 14 | 169 | 1.83 |  | 34 | 188 | 2.03 |  | 54 | 162 | 1.75 |
| 15 | 156 | 1.69 |  | 35 | 164 | 1.77 |  | 55 | 169 | 1.83 |
| 16 | 161 | 1.74 |  | 36 | 161 | 1.74 |  |  |  |  |
| 17 | 152 | 1.64 |  | 37 | 152 | 1.64 |  |  |  |  |
| 18 | 169 | 1.83 |  | 38 | 161 | 1.74 |  |  |  |  |
| 19 | 167 | 1.8 |  | 39 | 158 | 1.71 |  |  |  |  |
| 20 | 181 | 1.96 |  | 40 | 183 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 27 | 2 | 2.2 |  | 51 | 4 | 4.4 |
| 3 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 52 | 3 | 3.3 |
| 4 | 1 | 1.1 |  | 29 | 3 | 3.3 |  | 53 | 2 | 2.2 |
| 5 | 2 | 2.2 |  | 30 | 2 | 2.2 |  | 54 | 5 | 5.49 |
| 6 | 1 | 1.1 |  | 31 | 3 | 3.3 |  | 55 | 2 | 2.2 |
| 7 | 5 | 5.49 |  | 32 | 1 | 1.1 |  |  |  |  |
| 8 | 1 | 1.1 |  | 34 | 1 | 1.1 |  |  |  |  |
| 9 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 10 | 1 | 1.1 |  | 36 | 3 | 3.3 |  |  |  |  |
| 12 | 3 | 3.3 |  | 37 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 14 | 1 | 1.1 |  | 39 | 2 | 2.2 |  |  |  |  |
| 16 | 2 | 2.2 |  | 40 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 41 | 2 | 2.2 |  |  |  |  |
| 18 | 1 | 1.1 |  | 43 | 4 | 4.4 |  |  |  |  |
| 20 | 1 | 1.1 |  | 44 | 2 | 2.2 |  |  |  |  |
| 21 | 1 | 1.1 |  | 45 | 2 | 2.2 |  |  |  |  |
| 22 | 1 | 1.1 |  | 46 | 1 | 1.1 |  |  |  |  |
| 25 | 2 | 2.2 |  | 47 | 3 | 3.3 |  |  |  |  |
| 26 | 4 | 4.4 |  | 50 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.29 |  | 21 | 3 | 1.71 |  | 43 | 5 | 2.86 |
| 2 | 2 | 1.14 |  | 22 | 5 | 2.86 |  | 44 | 2 | 1.14 |
| 3 | 3 | 1.71 |  | 24 | 1 | 0.57 |  | 45 | 4 | 2.29 |
| 4 | 2 | 1.14 |  | 25 | 4 | 2.29 |  | 46 | 4 | 2.29 |
| 5 | 4 | 2.29 |  | 26 | 8 | 4.57 |  | 47 | 3 | 1.71 |
| 6 | 1 | 0.57 |  | 27 | 3 | 1.71 |  | 48 | 3 | 1.71 |
| 7 | 6 | 3.43 |  | 28 | 3 | 1.71 |  | 49 | 1 | 0.57 |
| 8 | 2 | 1.14 |  | 29 | 6 | 3.43 |  | 50 | 4 | 2.29 |
| 9 | 2 | 1.14 |  | 30 | 4 | 2.29 |  | 51 | 4 | 2.29 |
| 10 | 2 | 1.14 |  | 31 | 4 | 2.29 |  | 52 | 3 | 1.71 |
| 11 | 2 | 1.14 |  | 32 | 6 | 3.43 |  | 53 | 6 | 3.43 |
| 12 | 4 | 2.29 |  | 34 | 2 | 1.14 |  | 54 | 7 | 4.0 |
| 13 | 6 | 3.43 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 14 | 3 | 1.71 |  | 36 | 5 | 2.86 |  |  |  |  |
| 15 | 3 | 1.71 |  | 37 | 1 | 0.57 |  |  |  |  |
| 16 | 3 | 1.71 |  | 38 | 1 | 0.57 |  |  |  |  |
| 17 | 3 | 1.71 |  | 39 | 2 | 1.14 |  |  |  |  |
| 18 | 3 | 1.71 |  | 40 | 2 | 1.14 |  |  |  |  |
| 19 | 1 | 0.57 |  | 41 | 2 | 1.14 |  |  |  |  |
| 20 | 3 | 1.71 |  | 42 | 2 | 1.14 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.5 |  | 21 | 6 | 2.26 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 7 | 2.63 |  | 42 | 4 | 1.5 |
| 3 | 5 | 1.88 |  | 23 | 2 | 0.75 |  | 43 | 7 | 2.63 |
| 4 | 4 | 1.5 |  | 24 | 1 | 0.38 |  | 44 | 2 | 0.75 |
| 5 | 5 | 1.88 |  | 25 | 7 | 2.63 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 9 | 3.38 |  | 46 | 5 | 1.88 |
| 7 | 6 | 2.26 |  | 27 | 4 | 1.5 |  | 47 | 5 | 1.88 |
| 8 | 2 | 0.75 |  | 28 | 5 | 1.88 |  | 48 | 7 | 2.63 |
| 9 | 3 | 1.13 |  | 29 | 8 | 3.01 |  | 49 | 2 | 0.75 |
| 10 | 4 | 1.5 |  | 30 | 8 | 3.01 |  | 50 | 5 | 1.88 |
| 11 | 3 | 1.13 |  | 31 | 5 | 1.88 |  | 51 | 5 | 1.88 |
| 12 | 5 | 1.88 |  | 32 | 9 | 3.38 |  | 52 | 4 | 1.5 |
| 13 | 8 | 3.01 |  | 33 | 3 | 1.13 |  | 53 | 6 | 2.26 |
| 14 | 4 | 1.5 |  | 34 | 5 | 1.88 |  | 54 | 9 | 3.38 |
| 15 | 3 | 1.13 |  | 35 | 3 | 1.13 |  | 55 | 7 | 2.63 |
| 16 | 8 | 3.01 |  | 36 | 7 | 2.63 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 4 | 1.5 |  |  |  |  |
| 18 | 3 | 1.13 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 1 | 0.38 |  | 39 | 4 | 1.5 |  |  |  |  |
| 20 | 6 | 2.26 |  | 40 | 4 | 1.5 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 33 | 2026-01-10 | 70 |
| 23 | 2026-01-17 | 63 |
| 24 | 2026-01-24 | 56 |
| 49 | 2026-01-31 | 49 |
| 11 | 2026-01-31 | 49 |
| 15 | 2026-02-07 | 42 |
| 19 | 2026-02-12 | 37 |
| 42 | 2026-02-14 | 35 |
| 2 | 2026-02-14 | 35 |
| 48 | 2026-02-19 | 30 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-03-21 | 0 |
| 2 | 2026-02-14 | 35 |
| 3 | 2026-03-21 | 0 |
| 4 | 2026-03-07 | 14 |
| 5 | 2026-02-24 | 25 |
| 6 | 2026-03-21 | 0 |
| 7 | 2026-03-19 | 2 |
| 8 | 2026-02-24 | 25 |
| 9 | 2026-03-19 | 2 |
| 10 | 2026-02-26 | 23 |
| 11 | 2026-01-31 | 49 |
| 12 | 2026-03-17 | 4 |
| 13 | 2026-03-03 | 18 |
| 14 | 2026-03-05 | 16 |
| 15 | 2026-02-07 | 42 |
| 16 | 2026-03-14 | 7 |
| 17 | 2026-03-19 | 2 |
| 18 | 2026-02-24 | 25 |
| 19 | 2026-02-12 | 37 |
| 20 | 2026-03-10 | 11 |
| 21 | 2026-02-26 | 23 |
| 22 | 2026-02-28 | 21 |
| 23 | 2026-01-17 | 63 |
| 24 | 2026-01-24 | 56 |
| 25 | 2026-03-03 | 18 |
| 26 | 2026-03-17 | 4 |
| 27 | 2026-03-14 | 7 |
| 28 | 2026-03-17 | 4 |
| 29 | 2026-03-14 | 7 |
| 30 | 2026-02-24 | 25 |
| 31 | 2026-03-19 | 2 |
| 32 | 2026-03-07 | 14 |
| 33 | 2026-01-10 | 70 |
| 34 | 2026-03-19 | 2 |
| 35 | 2026-03-05 | 16 |
| 36 | 2026-03-19 | 2 |
| 37 | 2026-03-05 | 16 |
| 38 | 2026-03-05 | 16 |
| 39 | 2026-03-10 | 11 |
| 40 | 2026-03-21 | 0 |
| 41 | 2026-03-07 | 14 |
| 42 | 2026-02-14 | 35 |
| 43 | 2026-03-21 | 0 |
| 44 | 2026-02-28 | 21 |
| 45 | 2026-03-07 | 14 |
| 46 | 2026-02-26 | 23 |
| 47 | 2026-03-21 | 0 |
| 48 | 2026-02-19 | 30 |
| 49 | 2026-01-31 | 49 |
| 50 | 2026-03-17 | 4 |
| 51 | 2026-03-05 | 16 |
| 52 | 2026-03-17 | 4 |
| 53 | 2026-03-21 | 0 |
| 54 | 2026-03-17 | 4 |
| 55 | 2026-03-19 | 2 |



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

