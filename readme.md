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
| Power 655 | 1333 | 2017-08-01 | 2026-04-16 | 1333 | 00001 | 01333 |
| Power 645 | 1301 | 2017-10-25 | 2026-04-17 | 1301 | 00198 | 01498 |
| Power 535 | 258 | 2025-06-29 | 2026-04-17 | 516 | 00001 | 00586 |
| Keno | 526 | 2022-12-04 | 2026-04-17 | 66800 | #0110271 | #0277885 |
| 3D | 1064 | 2019-04-22 | 2026-04-17 | 1064 | 00001 | 01068 |
| 3D Pro | 710 | 2021-09-14 | 2026-04-16 | 710 | 00001 | 00714 |
| Bingo18 | 476 | 2024-12-03 | 2026-04-17 | 56220 | 0083123 | 0162665 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-04-16 | 01333 | [2, 7, 15, 22, 47, 52, 55] | 2026-04-17T21:50:28.270537 |
| 2026-04-14 | 01332 | [8, 16, 22, 35, 39, 47, 28] | 2026-04-17T21:50:28.272159 |
| 2026-04-11 | 01331 | [13, 26, 29, 38, 49, 53, 7] | 2026-04-17T21:50:28.273700 |
| 2026-04-09 | 01330 | [16, 18, 22, 29, 41, 53, 38] | 2026-04-17T21:50:28.275303 |
| 2026-04-07 | 01329 | [1, 13, 23, 31, 44, 53, 32] | 2026-04-17T21:50:28.276955 |
| 2026-04-04 | 01328 | [5, 7, 10, 23, 30, 54, 40] | 2026-04-17T21:50:28.278567 |
| 2026-04-02 | 01327 | [9, 21, 32, 34, 52, 53, 22] | 2026-04-17T21:50:28.280228 |
| 2026-03-31 | 01326 | [15, 16, 22, 38, 43, 48, 11] | 2026-04-17T21:50:28.281789 |
| 2026-03-28 | 01325 | [7, 13, 21, 30, 33, 42, 39] | 2026-03-29T00:00:55.768670 |
| 2026-03-26 | 01324 | [3, 9, 10, 34, 38, 44, 51] | 2026-03-27T00:01:03.257686 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 1.91 |  | 21 | 165 | 1.77 |  | 41 | 196 | 2.1 |
| 2 | 152 | 1.63 |  | 22 | 198 | 2.12 |  | 42 | 173 | 1.85 |
| 3 | 181 | 1.94 |  | 23 | 179 | 1.92 |  | 43 | 193 | 2.07 |
| 4 | 139 | 1.49 |  | 24 | 168 | 1.8 |  | 44 | 174 | 1.86 |
| 5 | 171 | 1.83 |  | 25 | 151 | 1.62 |  | 45 | 170 | 1.82 |
| 6 | 140 | 1.5 |  | 26 | 161 | 1.73 |  | 46 | 173 | 1.85 |
| 7 | 151 | 1.62 |  | 27 | 156 | 1.67 |  | 47 | 170 | 1.82 |
| 8 | 180 | 1.93 |  | 28 | 149 | 1.6 |  | 48 | 182 | 1.95 |
| 9 | 185 | 1.98 |  | 29 | 183 | 1.96 |  | 49 | 167 | 1.79 |
| 10 | 160 | 1.71 |  | 30 | 156 | 1.67 |  | 50 | 168 | 1.8 |
| 11 | 173 | 1.85 |  | 31 | 179 | 1.92 |  | 51 | 190 | 2.04 |
| 12 | 178 | 1.91 |  | 32 | 179 | 1.92 |  | 52 | 174 | 1.86 |
| 13 | 167 | 1.79 |  | 33 | 169 | 1.81 |  | 53 | 180 | 1.93 |
| 14 | 169 | 1.81 |  | 34 | 190 | 2.04 |  | 54 | 163 | 1.75 |
| 15 | 158 | 1.69 |  | 35 | 165 | 1.77 |  | 55 | 170 | 1.82 |
| 16 | 164 | 1.76 |  | 36 | 161 | 1.73 |  |  |  |  |
| 17 | 152 | 1.63 |  | 37 | 152 | 1.63 |  |  |  |  |
| 18 | 170 | 1.82 |  | 38 | 165 | 1.77 |  |  |  |  |
| 19 | 168 | 1.8 |  | 39 | 160 | 1.71 |  |  |  |  |
| 20 | 181 | 1.94 |  | 40 | 184 | 1.97 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 2.2 |  | 25 | 1 | 1.1 |  | 48 | 1 | 1.1 |
| 2 | 1 | 1.1 |  | 26 | 2 | 2.2 |  | 49 | 1 | 1.1 |
| 3 | 3 | 3.3 |  | 28 | 1 | 1.1 |  | 51 | 1 | 1.1 |
| 5 | 1 | 1.1 |  | 29 | 2 | 2.2 |  | 52 | 2 | 2.2 |
| 6 | 1 | 1.1 |  | 30 | 2 | 2.2 |  | 53 | 5 | 5.49 |
| 7 | 5 | 5.49 |  | 31 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 8 | 1 | 1.1 |  | 32 | 3 | 3.3 |  | 55 | 2 | 2.2 |
| 9 | 3 | 3.3 |  | 33 | 1 | 1.1 |  |  |  |  |
| 10 | 2 | 2.2 |  | 34 | 3 | 3.3 |  |  |  |  |
| 11 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 12 | 1 | 1.1 |  | 36 | 1 | 1.1 |  |  |  |  |
| 13 | 3 | 3.3 |  | 38 | 4 | 4.4 |  |  |  |  |
| 15 | 2 | 2.2 |  | 39 | 2 | 2.2 |  |  |  |  |
| 16 | 3 | 3.3 |  | 40 | 2 | 2.2 |  |  |  |  |
| 17 | 1 | 1.1 |  | 41 | 1 | 1.1 |  |  |  |  |
| 18 | 1 | 1.1 |  | 42 | 1 | 1.1 |  |  |  |  |
| 19 | 1 | 1.1 |  | 43 | 2 | 2.2 |  |  |  |  |
| 21 | 2 | 2.2 |  | 44 | 2 | 2.2 |  |  |  |  |
| 22 | 5 | 5.49 |  | 45 | 1 | 1.1 |  |  |  |  |
| 23 | 2 | 2.2 |  | 47 | 3 | 3.3 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2.29 |  | 21 | 3 | 1.71 |  | 42 | 1 | 0.57 |
| 2 | 1 | 0.57 |  | 22 | 6 | 3.43 |  | 43 | 6 | 3.43 |
| 3 | 4 | 2.29 |  | 23 | 2 | 1.14 |  | 44 | 4 | 2.29 |
| 4 | 1 | 0.57 |  | 25 | 3 | 1.71 |  | 45 | 4 | 2.29 |
| 5 | 3 | 1.71 |  | 26 | 6 | 3.43 |  | 46 | 2 | 1.14 |
| 6 | 1 | 0.57 |  | 27 | 3 | 1.71 |  | 47 | 5 | 2.86 |
| 7 | 9 | 5.14 |  | 28 | 3 | 1.71 |  | 48 | 2 | 1.14 |
| 8 | 2 | 1.14 |  | 29 | 5 | 2.86 |  | 49 | 1 | 0.57 |
| 9 | 3 | 1.71 |  | 30 | 5 | 2.86 |  | 50 | 3 | 1.71 |
| 10 | 3 | 1.71 |  | 31 | 4 | 2.29 |  | 51 | 5 | 2.86 |
| 11 | 1 | 0.57 |  | 32 | 4 | 2.29 |  | 52 | 5 | 2.86 |
| 12 | 4 | 2.29 |  | 33 | 1 | 0.57 |  | 53 | 6 | 3.43 |
| 13 | 4 | 2.29 |  | 34 | 3 | 1.71 |  | 54 | 6 | 3.43 |
| 14 | 1 | 0.57 |  | 35 | 2 | 1.14 |  | 55 | 3 | 1.71 |
| 15 | 2 | 1.14 |  | 36 | 3 | 1.71 |  |  |  |  |
| 16 | 5 | 2.86 |  | 37 | 1 | 0.57 |  |  |  |  |
| 17 | 1 | 0.57 |  | 38 | 5 | 2.86 |  |  |  |  |
| 18 | 2 | 1.14 |  | 39 | 4 | 2.29 |  |  |  |  |
| 19 | 1 | 0.57 |  | 40 | 3 | 1.71 |  |  |  |  |
| 20 | 1 | 0.57 |  | 41 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 1.88 |  | 21 | 6 | 2.26 |  | 41 | 4 | 1.5 |
| 2 | 3 | 1.13 |  | 22 | 10 | 3.76 |  | 42 | 3 | 1.13 |
| 3 | 5 | 1.88 |  | 23 | 3 | 1.13 |  | 43 | 6 | 2.26 |
| 4 | 3 | 1.13 |  | 24 | 1 | 0.38 |  | 44 | 4 | 1.5 |
| 5 | 5 | 1.88 |  | 25 | 6 | 2.26 |  | 45 | 5 | 1.88 |
| 6 | 1 | 0.38 |  | 26 | 11 | 4.14 |  | 46 | 5 | 1.88 |
| 7 | 10 | 3.76 |  | 27 | 3 | 1.13 |  | 47 | 5 | 1.88 |
| 8 | 3 | 1.13 |  | 28 | 5 | 1.88 |  | 48 | 5 | 1.88 |
| 9 | 4 | 1.5 |  | 29 | 8 | 3.01 |  | 49 | 2 | 0.75 |
| 10 | 4 | 1.5 |  | 30 | 6 | 2.26 |  | 50 | 4 | 1.5 |
| 11 | 3 | 1.13 |  | 31 | 5 | 1.88 |  | 51 | 5 | 1.88 |
| 12 | 5 | 1.88 |  | 32 | 10 | 3.76 |  | 52 | 5 | 1.88 |
| 13 | 9 | 3.38 |  | 33 | 1 | 0.38 |  | 53 | 10 | 3.76 |
| 14 | 4 | 1.5 |  | 34 | 4 | 1.5 |  | 54 | 9 | 3.38 |
| 15 | 5 | 1.88 |  | 35 | 3 | 1.13 |  | 55 | 5 | 1.88 |
| 16 | 6 | 2.26 |  | 36 | 5 | 1.88 |  |  |  |  |
| 17 | 3 | 1.13 |  | 37 | 2 | 0.75 |  |  |  |  |
| 18 | 4 | 1.5 |  | 38 | 5 | 1.88 |  |  |  |  |
| 19 | 2 | 0.75 |  | 39 | 4 | 1.5 |  |  |  |  |
| 20 | 4 | 1.5 |  | 40 | 3 | 1.13 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 24 | 2026-01-24 | 82 |
| 46 | 2026-02-26 | 49 |
| 37 | 2026-03-05 | 42 |
| 14 | 2026-03-05 | 42 |
| 4 | 2026-03-07 | 40 |
| 20 | 2026-03-10 | 37 |
| 27 | 2026-03-14 | 33 |
| 50 | 2026-03-17 | 30 |
| 36 | 2026-03-19 | 28 |
| 17 | 2026-03-19 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-04-07 | 9 |
| 2 | 2026-04-16 | 0 |
| 3 | 2026-03-26 | 21 |
| 4 | 2026-03-07 | 40 |
| 5 | 2026-04-04 | 12 |
| 6 | 2026-03-21 | 26 |
| 7 | 2026-04-16 | 0 |
| 8 | 2026-04-14 | 2 |
| 9 | 2026-04-02 | 14 |
| 10 | 2026-04-04 | 12 |
| 11 | 2026-03-31 | 16 |
| 12 | 2026-03-24 | 23 |
| 13 | 2026-04-11 | 5 |
| 14 | 2026-03-05 | 42 |
| 15 | 2026-04-16 | 0 |
| 16 | 2026-04-14 | 2 |
| 17 | 2026-03-19 | 28 |
| 18 | 2026-04-09 | 7 |
| 19 | 2026-03-24 | 23 |
| 20 | 2026-03-10 | 37 |
| 21 | 2026-04-02 | 14 |
| 22 | 2026-04-16 | 0 |
| 23 | 2026-04-07 | 9 |
| 24 | 2026-01-24 | 82 |
| 25 | 2026-03-24 | 23 |
| 26 | 2026-04-11 | 5 |
| 27 | 2026-03-14 | 33 |
| 28 | 2026-04-14 | 2 |
| 29 | 2026-04-11 | 5 |
| 30 | 2026-04-04 | 12 |
| 31 | 2026-04-07 | 9 |
| 32 | 2026-04-07 | 9 |
| 33 | 2026-03-28 | 19 |
| 34 | 2026-04-02 | 14 |
| 35 | 2026-04-14 | 2 |
| 36 | 2026-03-19 | 28 |
| 37 | 2026-03-05 | 42 |
| 38 | 2026-04-11 | 5 |
| 39 | 2026-04-14 | 2 |
| 40 | 2026-04-04 | 12 |
| 41 | 2026-04-09 | 7 |
| 42 | 2026-03-28 | 19 |
| 43 | 2026-03-31 | 16 |
| 44 | 2026-04-07 | 9 |
| 45 | 2026-03-24 | 23 |
| 46 | 2026-02-26 | 49 |
| 47 | 2026-04-16 | 0 |
| 48 | 2026-03-31 | 16 |
| 49 | 2026-04-11 | 5 |
| 50 | 2026-03-17 | 30 |
| 51 | 2026-03-26 | 21 |
| 52 | 2026-04-16 | 0 |
| 53 | 2026-04-11 | 5 |
| 54 | 2026-04-04 | 12 |
| 55 | 2026-04-16 | 0 |



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

