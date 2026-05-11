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
| Power 655 | 1343 | 2017-08-01 | 2026-05-09 | 1343 | 00001 | 01343 |
| Power 645 | 1311 | 2017-10-25 | 2026-05-10 | 1311 | 00198 | 01508 |
| Power 535 | 280 | 2025-06-29 | 2026-05-10 | 559 | 00001 | 00632 |
| Keno | 547 | 2022-12-04 | 2026-05-11 | 69216 | #0110271 | #0280667 |
| 3D | 1073 | 2019-04-22 | 2026-05-08 | 1073 | 00001 | 01077 |
| 3D Pro | 720 | 2021-09-14 | 2026-05-09 | 720 | 00001 | 00724 |
| Bingo18 | 523 | 2024-12-03 | 2026-05-11 | 70469 | 0083123 | 0166383 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-09 | 01343 | [3, 10, 32, 37, 45, 55, 46] | 2026-05-10T00:01:08.118122 |
| 2026-05-07 | 01342 | [13, 14, 33, 44, 46, 50, 47] | 2026-05-08T12:04:58.259525 |
| 2026-05-05 | 01341 | [4, 6, 8, 17, 30, 50, 32] | 2026-05-08T12:04:58.261267 |
| 2026-05-02 | 01340 | [9, 21, 22, 26, 33, 51, 17] | 2026-05-02T18:53:23.258397 |
| 2026-04-30 | 01339 | [9, 15, 21, 25, 29, 50, 16] | 2026-05-02T18:53:23.260631 |
| 2026-04-28 | 01338 | [24, 25, 34, 51, 52, 53, 35] | 2026-05-02T18:53:23.263066 |
| 2026-04-25 | 01337 | [4, 7, 10, 29, 41, 46, 43] | 2026-05-02T18:53:23.265527 |
| 2026-04-23 | 01336 | [5, 16, 17, 22, 33, 53, 55] | 2026-05-02T18:53:23.268125 |
| 2026-04-21 | 01335 | [8, 30, 36, 39, 50, 53, 15] | 2026-05-02T18:53:23.270378 |
| 2026-04-18 | 01334 | [9, 19, 20, 28, 37, 39, 24] | 2026-05-02T18:53:23.273130 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 1.89 |  | 21 | 167 | 1.78 |  | 41 | 197 | 2.1 |
| 2 | 152 | 1.62 |  | 22 | 200 | 2.13 |  | 42 | 173 | 1.84 |
| 3 | 182 | 1.94 |  | 23 | 179 | 1.9 |  | 43 | 194 | 2.06 |
| 4 | 141 | 1.5 |  | 24 | 170 | 1.81 |  | 44 | 175 | 1.86 |
| 5 | 172 | 1.83 |  | 25 | 153 | 1.63 |  | 45 | 171 | 1.82 |
| 6 | 141 | 1.5 |  | 26 | 162 | 1.72 |  | 46 | 176 | 1.87 |
| 7 | 152 | 1.62 |  | 27 | 156 | 1.66 |  | 47 | 171 | 1.82 |
| 8 | 182 | 1.94 |  | 28 | 150 | 1.6 |  | 48 | 182 | 1.94 |
| 9 | 188 | 2.0 |  | 29 | 185 | 1.97 |  | 49 | 167 | 1.78 |
| 10 | 162 | 1.72 |  | 30 | 158 | 1.68 |  | 50 | 172 | 1.83 |
| 11 | 173 | 1.84 |  | 31 | 179 | 1.9 |  | 51 | 192 | 2.04 |
| 12 | 178 | 1.89 |  | 32 | 181 | 1.93 |  | 52 | 175 | 1.86 |
| 13 | 168 | 1.79 |  | 33 | 172 | 1.83 |  | 53 | 183 | 1.95 |
| 14 | 170 | 1.81 |  | 34 | 191 | 2.03 |  | 54 | 163 | 1.73 |
| 15 | 160 | 1.7 |  | 35 | 166 | 1.77 |  | 55 | 172 | 1.83 |
| 16 | 166 | 1.77 |  | 36 | 162 | 1.72 |  |  |  |  |
| 17 | 155 | 1.65 |  | 37 | 154 | 1.64 |  |  |  |  |
| 18 | 170 | 1.81 |  | 38 | 165 | 1.76 |  |  |  |  |
| 19 | 169 | 1.8 |  | 39 | 162 | 1.72 |  |  |  |  |
| 20 | 182 | 1.94 |  | 40 | 184 | 1.96 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 51 | 2 | 2.2 |
| 3 | 1 | 1.1 |  | 28 | 2 | 2.2 |  | 52 | 2 | 2.2 |
| 4 | 2 | 2.2 |  | 29 | 3 | 3.3 |  | 53 | 4 | 4.4 |
| 5 | 1 | 1.1 |  | 30 | 2 | 2.2 |  | 55 | 3 | 3.3 |
| 6 | 1 | 1.1 |  | 32 | 2 | 2.2 |  |  |  |  |
| 7 | 3 | 3.3 |  | 33 | 3 | 3.3 |  |  |  |  |
| 8 | 3 | 3.3 |  | 34 | 1 | 1.1 |  |  |  |  |
| 9 | 3 | 3.3 |  | 35 | 2 | 2.2 |  |  |  |  |
| 10 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 2 | 2.2 |  | 37 | 2 | 2.2 |  |  |  |  |
| 14 | 1 | 1.1 |  | 38 | 1 | 1.1 |  |  |  |  |
| 15 | 3 | 3.3 |  | 39 | 3 | 3.3 |  |  |  |  |
| 16 | 3 | 3.3 |  | 41 | 1 | 1.1 |  |  |  |  |
| 17 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |
| 20 | 1 | 1.1 |  | 45 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 46 | 3 | 3.3 |  |  |  |  |
| 22 | 4 | 4.4 |  | 47 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 49 | 1 | 1.1 |  |  |  |  |
| 25 | 2 | 2.2 |  | 50 | 4 | 4.4 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.1 |  | 21 | 4 | 2.2 |  | 41 | 2 | 1.1 |
| 2 | 1 | 0.55 |  | 22 | 7 | 3.85 |  | 42 | 1 | 0.55 |
| 3 | 4 | 2.2 |  | 23 | 2 | 1.1 |  | 43 | 4 | 2.2 |
| 4 | 2 | 1.1 |  | 24 | 2 | 1.1 |  | 44 | 3 | 1.65 |
| 5 | 2 | 1.1 |  | 25 | 3 | 1.65 |  | 45 | 2 | 1.1 |
| 6 | 2 | 1.1 |  | 26 | 5 | 2.75 |  | 46 | 3 | 1.65 |
| 7 | 7 | 3.85 |  | 27 | 1 | 0.55 |  | 47 | 5 | 2.75 |
| 8 | 3 | 1.65 |  | 28 | 4 | 2.2 |  | 48 | 1 | 0.55 |
| 9 | 6 | 3.3 |  | 29 | 5 | 2.75 |  | 49 | 1 | 0.55 |
| 10 | 4 | 2.2 |  | 30 | 4 | 2.2 |  | 50 | 5 | 2.75 |
| 11 | 1 | 0.55 |  | 31 | 2 | 1.1 |  | 51 | 3 | 1.65 |
| 12 | 3 | 1.65 |  | 32 | 5 | 2.75 |  | 52 | 5 | 2.75 |
| 13 | 4 | 2.2 |  | 33 | 4 | 2.2 |  | 53 | 9 | 4.95 |
| 14 | 1 | 0.55 |  | 34 | 4 | 2.2 |  | 54 | 3 | 1.65 |
| 15 | 4 | 2.2 |  | 35 | 2 | 1.1 |  | 55 | 5 | 2.75 |
| 16 | 6 | 3.3 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 4 | 2.2 |  | 37 | 2 | 1.1 |  |  |  |  |
| 18 | 1 | 0.55 |  | 38 | 4 | 2.2 |  |  |  |  |
| 19 | 2 | 1.1 |  | 39 | 4 | 2.2 |  |  |  |  |
| 20 | 1 | 0.55 |  | 40 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.5 |  | 21 | 6 | 2.26 |  | 41 | 4 | 1.5 |
| 2 | 2 | 0.75 |  | 22 | 9 | 3.38 |  | 42 | 2 | 0.75 |
| 3 | 5 | 1.88 |  | 23 | 2 | 0.75 |  | 43 | 7 | 2.63 |
| 4 | 3 | 1.13 |  | 24 | 2 | 0.75 |  | 44 | 5 | 1.88 |
| 5 | 4 | 1.5 |  | 25 | 5 | 1.88 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 10 | 3.76 |  | 46 | 6 | 2.26 |
| 7 | 10 | 3.76 |  | 27 | 3 | 1.13 |  | 47 | 6 | 2.26 |
| 8 | 5 | 1.88 |  | 28 | 4 | 1.5 |  | 48 | 3 | 1.13 |
| 9 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 1 | 0.38 |
| 10 | 5 | 1.88 |  | 30 | 7 | 2.63 |  | 50 | 7 | 2.63 |
| 11 | 1 | 0.38 |  | 31 | 5 | 1.88 |  | 51 | 7 | 2.63 |
| 12 | 4 | 1.5 |  | 32 | 9 | 3.38 |  | 52 | 6 | 2.26 |
| 13 | 7 | 2.63 |  | 33 | 4 | 1.5 |  | 53 | 9 | 3.38 |
| 14 | 2 | 0.75 |  | 34 | 4 | 1.5 |  | 54 | 6 | 2.26 |
| 15 | 4 | 1.5 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 7 | 2.63 |  | 36 | 5 | 1.88 |  |  |  |  |
| 17 | 5 | 1.88 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 2 | 0.75 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 3 | 1.13 |  | 39 | 6 | 2.26 |  |  |  |  |
| 20 | 3 | 1.13 |  | 40 | 3 | 1.13 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 27 | 2026-03-14 | 56 |
| 12 | 2026-03-24 | 46 |
| 42 | 2026-03-28 | 42 |
| 48 | 2026-03-31 | 39 |
| 11 | 2026-03-31 | 39 |
| 54 | 2026-04-04 | 35 |
| 40 | 2026-04-04 | 35 |
| 31 | 2026-04-07 | 32 |
| 1 | 2026-04-07 | 32 |
| 23 | 2026-04-07 | 32 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-04-07 | 32 |
| 2 | 2026-04-16 | 23 |
| 3 | 2026-05-09 | 0 |
| 4 | 2026-05-05 | 4 |
| 5 | 2026-04-23 | 16 |
| 6 | 2026-05-05 | 4 |
| 7 | 2026-04-25 | 14 |
| 8 | 2026-05-05 | 4 |
| 9 | 2026-05-02 | 7 |
| 10 | 2026-05-09 | 0 |
| 11 | 2026-03-31 | 39 |
| 12 | 2026-03-24 | 46 |
| 13 | 2026-05-07 | 2 |
| 14 | 2026-05-07 | 2 |
| 15 | 2026-04-30 | 9 |
| 16 | 2026-04-30 | 9 |
| 17 | 2026-05-05 | 4 |
| 18 | 2026-04-09 | 30 |
| 19 | 2026-04-18 | 21 |
| 20 | 2026-04-18 | 21 |
| 21 | 2026-05-02 | 7 |
| 22 | 2026-05-02 | 7 |
| 23 | 2026-04-07 | 32 |
| 24 | 2026-04-28 | 11 |
| 25 | 2026-04-30 | 9 |
| 26 | 2026-05-02 | 7 |
| 27 | 2026-03-14 | 56 |
| 28 | 2026-04-18 | 21 |
| 29 | 2026-04-30 | 9 |
| 30 | 2026-05-05 | 4 |
| 31 | 2026-04-07 | 32 |
| 32 | 2026-05-09 | 0 |
| 33 | 2026-05-07 | 2 |
| 34 | 2026-04-28 | 11 |
| 35 | 2026-04-28 | 11 |
| 36 | 2026-04-21 | 18 |
| 37 | 2026-05-09 | 0 |
| 38 | 2026-04-11 | 28 |
| 39 | 2026-04-21 | 18 |
| 40 | 2026-04-04 | 35 |
| 41 | 2026-04-25 | 14 |
| 42 | 2026-03-28 | 42 |
| 43 | 2026-04-25 | 14 |
| 44 | 2026-05-07 | 2 |
| 45 | 2026-05-09 | 0 |
| 46 | 2026-05-09 | 0 |
| 47 | 2026-05-07 | 2 |
| 48 | 2026-03-31 | 39 |
| 49 | 2026-04-11 | 28 |
| 50 | 2026-05-07 | 2 |
| 51 | 2026-05-02 | 7 |
| 52 | 2026-04-28 | 11 |
| 53 | 2026-04-28 | 11 |
| 54 | 2026-04-04 | 35 |
| 55 | 2026-05-09 | 0 |



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

