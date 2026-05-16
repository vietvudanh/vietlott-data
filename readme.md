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
| Power 655 | 1346 | 2017-08-01 | 2026-05-16 | 1346 | 00001 | 01346 |
| Power 645 | 1313 | 2017-10-25 | 2026-05-15 | 1313 | 00198 | 01510 |
| Power 535 | 286 | 2025-06-29 | 2026-05-16 | 571 | 00001 | 00644 |
| Keno | 552 | 2022-12-04 | 2026-05-16 | 69886 | #0110271 | #0281337 |
| 3D | 1076 | 2019-04-22 | 2026-05-15 | 1076 | 00001 | 01080 |
| 3D Pro | 723 | 2021-09-14 | 2026-05-16 | 723 | 00001 | 00727 |
| Bingo18 | 528 | 2024-12-03 | 2026-05-16 | 71324 | 0083123 | 0167277 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-16 | 01346 | [8, 25, 32, 36, 39, 47, 50] | 2026-05-17T00:01:14.316887 |
| 2026-05-14 | 01345 | [26, 28, 39, 41, 48, 55, 50] | 2026-05-15T00:01:10.822513 |
| 2026-05-12 | 01344 | [2, 11, 22, 26, 31, 38, 15] | 2026-05-12T18:58:07.963930 |
| 2026-05-09 | 01343 | [3, 10, 32, 37, 45, 55, 46] | 2026-05-10T00:01:08.118122 |
| 2026-05-07 | 01342 | [13, 14, 33, 44, 46, 50, 47] | 2026-05-08T12:04:58.259525 |
| 2026-05-05 | 01341 | [4, 6, 8, 17, 30, 50, 32] | 2026-05-08T12:04:58.261267 |
| 2026-05-02 | 01340 | [9, 21, 22, 26, 33, 51, 17] | 2026-05-02T18:53:23.258397 |
| 2026-04-30 | 01339 | [9, 15, 21, 25, 29, 50, 16] | 2026-05-02T18:53:23.260631 |
| 2026-04-28 | 01338 | [24, 25, 34, 51, 52, 53, 35] | 2026-05-02T18:53:23.263066 |
| 2026-04-25 | 01337 | [4, 7, 10, 29, 41, 46, 43] | 2026-05-02T18:53:23.265527 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 1.89 |  | 21 | 167 | 1.77 |  | 41 | 198 | 2.1 |
| 2 | 153 | 1.62 |  | 22 | 201 | 2.13 |  | 42 | 173 | 1.84 |
| 3 | 182 | 1.93 |  | 23 | 179 | 1.9 |  | 43 | 194 | 2.06 |
| 4 | 141 | 1.5 |  | 24 | 170 | 1.8 |  | 44 | 175 | 1.86 |
| 5 | 172 | 1.83 |  | 25 | 154 | 1.63 |  | 45 | 171 | 1.82 |
| 6 | 141 | 1.5 |  | 26 | 164 | 1.74 |  | 46 | 176 | 1.87 |
| 7 | 152 | 1.61 |  | 27 | 156 | 1.66 |  | 47 | 172 | 1.83 |
| 8 | 183 | 1.94 |  | 28 | 151 | 1.6 |  | 48 | 183 | 1.94 |
| 9 | 188 | 2.0 |  | 29 | 185 | 1.96 |  | 49 | 167 | 1.77 |
| 10 | 162 | 1.72 |  | 30 | 158 | 1.68 |  | 50 | 174 | 1.85 |
| 11 | 174 | 1.85 |  | 31 | 180 | 1.91 |  | 51 | 192 | 2.04 |
| 12 | 178 | 1.89 |  | 32 | 182 | 1.93 |  | 52 | 175 | 1.86 |
| 13 | 168 | 1.78 |  | 33 | 172 | 1.83 |  | 53 | 183 | 1.94 |
| 14 | 170 | 1.8 |  | 34 | 191 | 2.03 |  | 54 | 163 | 1.73 |
| 15 | 161 | 1.71 |  | 35 | 166 | 1.76 |  | 55 | 173 | 1.84 |
| 16 | 166 | 1.76 |  | 36 | 163 | 1.73 |  |  |  |  |
| 17 | 155 | 1.65 |  | 37 | 154 | 1.63 |  |  |  |  |
| 18 | 170 | 1.8 |  | 38 | 166 | 1.76 |  |  |  |  |
| 19 | 169 | 1.79 |  | 39 | 164 | 1.74 |  |  |  |  |
| 20 | 182 | 1.93 |  | 40 | 184 | 1.95 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 1.1 |  | 25 | 3 | 3.3 |  | 48 | 1 | 1.1 |
| 3 | 1 | 1.1 |  | 26 | 3 | 3.3 |  | 50 | 6 | 6.59 |
| 4 | 2 | 2.2 |  | 28 | 2 | 2.2 |  | 51 | 2 | 2.2 |
| 5 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 52 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 30 | 2 | 2.2 |  | 53 | 3 | 3.3 |
| 7 | 1 | 1.1 |  | 31 | 1 | 1.1 |  | 55 | 3 | 3.3 |
| 8 | 3 | 3.3 |  | 32 | 3 | 3.3 |  |  |  |  |
| 9 | 3 | 3.3 |  | 33 | 3 | 3.3 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 13 | 1 | 1.1 |  | 36 | 2 | 2.2 |  |  |  |  |
| 14 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 15 | 3 | 3.3 |  | 38 | 1 | 1.1 |  |  |  |  |
| 16 | 2 | 2.2 |  | 39 | 4 | 4.4 |  |  |  |  |
| 17 | 3 | 3.3 |  | 41 | 2 | 2.2 |  |  |  |  |
| 19 | 1 | 1.1 |  | 43 | 1 | 1.1 |  |  |  |  |
| 20 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 45 | 1 | 1.1 |  |  |  |  |
| 22 | 3 | 3.3 |  | 46 | 3 | 3.3 |  |  |  |  |
| 24 | 2 | 2.2 |  | 47 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.1 |  | 21 | 4 | 2.2 |  | 42 | 1 | 0.55 |
| 2 | 2 | 1.1 |  | 22 | 8 | 4.4 |  | 43 | 3 | 1.65 |
| 3 | 4 | 2.2 |  | 23 | 2 | 1.1 |  | 44 | 3 | 1.65 |
| 4 | 2 | 1.1 |  | 24 | 2 | 1.1 |  | 45 | 2 | 1.1 |
| 5 | 2 | 1.1 |  | 25 | 4 | 2.2 |  | 46 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 26 | 5 | 2.75 |  | 47 | 5 | 2.75 |
| 7 | 6 | 3.3 |  | 28 | 3 | 1.65 |  | 48 | 2 | 1.1 |
| 8 | 4 | 2.2 |  | 29 | 4 | 2.2 |  | 49 | 1 | 0.55 |
| 9 | 6 | 3.3 |  | 30 | 4 | 2.2 |  | 50 | 6 | 3.3 |
| 10 | 4 | 2.2 |  | 31 | 3 | 1.65 |  | 51 | 3 | 1.65 |
| 11 | 2 | 1.1 |  | 32 | 6 | 3.3 |  | 52 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 33 | 4 | 2.2 |  | 53 | 8 | 4.4 |
| 13 | 4 | 2.2 |  | 34 | 4 | 2.2 |  | 54 | 1 | 0.55 |
| 14 | 1 | 0.55 |  | 35 | 2 | 1.1 |  | 55 | 5 | 2.75 |
| 15 | 5 | 2.75 |  | 36 | 3 | 1.65 |  |  |  |  |
| 16 | 5 | 2.75 |  | 37 | 2 | 1.1 |  |  |  |  |
| 17 | 4 | 2.2 |  | 38 | 5 | 2.75 |  |  |  |  |
| 18 | 1 | 0.55 |  | 39 | 6 | 3.3 |  |  |  |  |
| 19 | 2 | 1.1 |  | 40 | 2 | 1.1 |  |  |  |  |
| 20 | 1 | 0.55 |  | 41 | 3 | 1.65 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1.5 |  | 21 | 5 | 1.88 |  | 41 | 5 | 1.88 |
| 2 | 2 | 0.75 |  | 22 | 9 | 3.38 |  | 42 | 1 | 0.38 |
| 3 | 5 | 1.88 |  | 23 | 2 | 0.75 |  | 43 | 7 | 2.63 |
| 4 | 3 | 1.13 |  | 24 | 2 | 0.75 |  | 44 | 5 | 1.88 |
| 5 | 4 | 1.5 |  | 25 | 6 | 2.26 |  | 45 | 5 | 1.88 |
| 6 | 2 | 0.75 |  | 26 | 9 | 3.38 |  | 46 | 5 | 1.88 |
| 7 | 10 | 3.76 |  | 27 | 3 | 1.13 |  | 47 | 7 | 2.63 |
| 8 | 5 | 1.88 |  | 28 | 5 | 1.88 |  | 48 | 3 | 1.13 |
| 9 | 6 | 2.26 |  | 29 | 7 | 2.63 |  | 49 | 1 | 0.38 |
| 10 | 5 | 1.88 |  | 30 | 7 | 2.63 |  | 50 | 9 | 3.38 |
| 11 | 2 | 0.75 |  | 31 | 5 | 1.88 |  | 51 | 7 | 2.63 |
| 12 | 4 | 1.5 |  | 32 | 7 | 2.63 |  | 52 | 6 | 2.26 |
| 13 | 5 | 1.88 |  | 33 | 4 | 1.5 |  | 53 | 9 | 3.38 |
| 14 | 2 | 0.75 |  | 34 | 4 | 1.5 |  | 54 | 6 | 2.26 |
| 15 | 5 | 1.88 |  | 35 | 3 | 1.13 |  | 55 | 6 | 2.26 |
| 16 | 7 | 2.63 |  | 36 | 5 | 1.88 |  |  |  |  |
| 17 | 4 | 1.5 |  | 37 | 3 | 1.13 |  |  |  |  |
| 18 | 2 | 0.75 |  | 38 | 6 | 2.26 |  |  |  |  |
| 19 | 2 | 0.75 |  | 39 | 8 | 3.01 |  |  |  |  |
| 20 | 2 | 0.75 |  | 40 | 3 | 1.13 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 27 | 2026-03-14 | 63 |
| 12 | 2026-03-24 | 53 |
| 42 | 2026-03-28 | 49 |
| 54 | 2026-04-04 | 42 |
| 40 | 2026-04-04 | 42 |
| 1 | 2026-04-07 | 39 |
| 23 | 2026-04-07 | 39 |
| 18 | 2026-04-09 | 37 |
| 49 | 2026-04-11 | 35 |
| 19 | 2026-04-18 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-04-07 | 39 |
| 2 | 2026-05-12 | 4 |
| 3 | 2026-05-09 | 7 |
| 4 | 2026-05-05 | 11 |
| 5 | 2026-04-23 | 23 |
| 6 | 2026-05-05 | 11 |
| 7 | 2026-04-25 | 21 |
| 8 | 2026-05-16 | 0 |
| 9 | 2026-05-02 | 14 |
| 10 | 2026-05-09 | 7 |
| 11 | 2026-05-12 | 4 |
| 12 | 2026-03-24 | 53 |
| 13 | 2026-05-07 | 9 |
| 14 | 2026-05-07 | 9 |
| 15 | 2026-05-12 | 4 |
| 16 | 2026-04-30 | 16 |
| 17 | 2026-05-05 | 11 |
| 18 | 2026-04-09 | 37 |
| 19 | 2026-04-18 | 28 |
| 20 | 2026-04-18 | 28 |
| 21 | 2026-05-02 | 14 |
| 22 | 2026-05-12 | 4 |
| 23 | 2026-04-07 | 39 |
| 24 | 2026-04-28 | 18 |
| 25 | 2026-05-16 | 0 |
| 26 | 2026-05-14 | 2 |
| 27 | 2026-03-14 | 63 |
| 28 | 2026-05-14 | 2 |
| 29 | 2026-04-30 | 16 |
| 30 | 2026-05-05 | 11 |
| 31 | 2026-05-12 | 4 |
| 32 | 2026-05-16 | 0 |
| 33 | 2026-05-07 | 9 |
| 34 | 2026-04-28 | 18 |
| 35 | 2026-04-28 | 18 |
| 36 | 2026-05-16 | 0 |
| 37 | 2026-05-09 | 7 |
| 38 | 2026-05-12 | 4 |
| 39 | 2026-05-16 | 0 |
| 40 | 2026-04-04 | 42 |
| 41 | 2026-05-14 | 2 |
| 42 | 2026-03-28 | 49 |
| 43 | 2026-04-25 | 21 |
| 44 | 2026-05-07 | 9 |
| 45 | 2026-05-09 | 7 |
| 46 | 2026-05-09 | 7 |
| 47 | 2026-05-16 | 0 |
| 48 | 2026-05-14 | 2 |
| 49 | 2026-04-11 | 35 |
| 50 | 2026-05-16 | 0 |
| 51 | 2026-05-02 | 14 |
| 52 | 2026-04-28 | 18 |
| 53 | 2026-04-28 | 18 |
| 54 | 2026-04-04 | 42 |
| 55 | 2026-05-14 | 2 |



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

