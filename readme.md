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
| Power 655 | 1340 | 2017-08-01 | 2026-05-02 | 1340 | 00001 | 01340 |
| Power 645 | 1307 | 2017-10-25 | 2026-05-01 | 1307 | 00198 | 01504 |
| Power 535 | 272 | 2025-06-29 | 2026-05-02 | 543 | 00001 | 00616 |
| Keno | 529 | 2022-12-04 | 2026-05-03 | 67096 | #0110271 | #0279715 |
| 3D | 1070 | 2019-04-22 | 2026-05-01 | 1070 | 00001 | 01074 |
| 3D Pro | 717 | 2021-09-14 | 2026-05-02 | 717 | 00001 | 00721 |
| Bingo18 | 515 | 2024-12-03 | 2026-05-03 | 66702 | 0083123 | 0165111 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-05-02 | 01340 | [9, 21, 22, 26, 33, 51, 17] | 2026-05-02T18:53:23.258397 |
| 2026-04-30 | 01339 | [9, 15, 21, 25, 29, 50, 16] | 2026-05-02T18:53:23.260631 |
| 2026-04-28 | 01338 | [24, 25, 34, 51, 52, 53, 35] | 2026-05-02T18:53:23.263066 |
| 2026-04-25 | 01337 | [4, 7, 10, 29, 41, 46, 43] | 2026-05-02T18:53:23.265527 |
| 2026-04-23 | 01336 | [5, 16, 17, 22, 33, 53, 55] | 2026-05-02T18:53:23.268125 |
| 2026-04-21 | 01335 | [8, 30, 36, 39, 50, 53, 15] | 2026-05-02T18:53:23.270378 |
| 2026-04-18 | 01334 | [9, 19, 20, 28, 37, 39, 24] | 2026-05-02T18:53:23.273130 |
| 2026-04-16 | 01333 | [2, 7, 15, 22, 47, 52, 55] | 2026-04-17T21:50:28.270537 |
| 2026-04-14 | 01332 | [8, 16, 22, 35, 39, 47, 28] | 2026-04-17T21:50:28.272159 |
| 2026-04-11 | 01331 | [13, 26, 29, 38, 49, 53, 7] | 2026-04-17T21:50:28.273700 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 178 | 1.9 |  | 21 | 167 | 1.78 |  | 41 | 197 | 2.1 |
| 2 | 152 | 1.62 |  | 22 | 200 | 2.13 |  | 42 | 173 | 1.84 |
| 3 | 181 | 1.93 |  | 23 | 179 | 1.91 |  | 43 | 194 | 2.07 |
| 4 | 140 | 1.49 |  | 24 | 170 | 1.81 |  | 44 | 174 | 1.86 |
| 5 | 172 | 1.83 |  | 25 | 153 | 1.63 |  | 45 | 170 | 1.81 |
| 6 | 140 | 1.49 |  | 26 | 162 | 1.73 |  | 46 | 174 | 1.86 |
| 7 | 152 | 1.62 |  | 27 | 156 | 1.66 |  | 47 | 170 | 1.81 |
| 8 | 181 | 1.93 |  | 28 | 150 | 1.6 |  | 48 | 182 | 1.94 |
| 9 | 188 | 2.0 |  | 29 | 185 | 1.97 |  | 49 | 167 | 1.78 |
| 10 | 161 | 1.72 |  | 30 | 157 | 1.67 |  | 50 | 170 | 1.81 |
| 11 | 173 | 1.84 |  | 31 | 179 | 1.91 |  | 51 | 192 | 2.05 |
| 12 | 178 | 1.9 |  | 32 | 179 | 1.91 |  | 52 | 175 | 1.87 |
| 13 | 167 | 1.78 |  | 33 | 171 | 1.82 |  | 53 | 183 | 1.95 |
| 14 | 169 | 1.8 |  | 34 | 191 | 2.04 |  | 54 | 163 | 1.74 |
| 15 | 160 | 1.71 |  | 35 | 166 | 1.77 |  | 55 | 171 | 1.82 |
| 16 | 166 | 1.77 |  | 36 | 162 | 1.73 |  |  |  |  |
| 17 | 154 | 1.64 |  | 37 | 153 | 1.63 |  |  |  |  |
| 18 | 170 | 1.81 |  | 38 | 165 | 1.76 |  |  |  |  |
| 19 | 169 | 1.8 |  | 39 | 162 | 1.73 |  |  |  |  |
| 20 | 182 | 1.94 |  | 40 | 184 | 1.96 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1.19 |  | 26 | 2 | 2.38 |  | 51 | 2 | 2.38 |
| 2 | 1 | 1.19 |  | 28 | 2 | 2.38 |  | 52 | 2 | 2.38 |
| 4 | 1 | 1.19 |  | 29 | 4 | 4.76 |  | 53 | 6 | 7.14 |
| 5 | 1 | 1.19 |  | 30 | 1 | 1.19 |  | 55 | 2 | 2.38 |
| 7 | 3 | 3.57 |  | 31 | 1 | 1.19 |  |  |  |  |
| 8 | 2 | 2.38 |  | 32 | 1 | 1.19 |  |  |  |  |
| 9 | 3 | 3.57 |  | 33 | 2 | 2.38 |  |  |  |  |
| 10 | 1 | 1.19 |  | 34 | 1 | 1.19 |  |  |  |  |
| 13 | 2 | 2.38 |  | 35 | 2 | 2.38 |  |  |  |  |
| 15 | 3 | 3.57 |  | 36 | 1 | 1.19 |  |  |  |  |
| 16 | 4 | 4.76 |  | 37 | 1 | 1.19 |  |  |  |  |
| 17 | 2 | 2.38 |  | 38 | 2 | 2.38 |  |  |  |  |
| 18 | 1 | 1.19 |  | 39 | 3 | 3.57 |  |  |  |  |
| 19 | 1 | 1.19 |  | 41 | 2 | 2.38 |  |  |  |  |
| 20 | 1 | 1.19 |  | 43 | 1 | 1.19 |  |  |  |  |
| 21 | 2 | 2.38 |  | 44 | 1 | 1.19 |  |  |  |  |
| 22 | 5 | 5.95 |  | 46 | 1 | 1.19 |  |  |  |  |
| 23 | 1 | 1.19 |  | 47 | 2 | 2.38 |  |  |  |  |
| 24 | 2 | 2.38 |  | 49 | 1 | 1.19 |  |  |  |  |
| 25 | 2 | 2.38 |  | 50 | 2 | 2.38 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1.14 |  | 22 | 7 | 4.0 |  | 42 | 1 | 0.57 |
| 2 | 1 | 0.57 |  | 23 | 2 | 1.14 |  | 43 | 4 | 2.29 |
| 3 | 4 | 2.29 |  | 24 | 2 | 1.14 |  | 44 | 2 | 1.14 |
| 4 | 2 | 1.14 |  | 25 | 3 | 1.71 |  | 45 | 2 | 1.14 |
| 5 | 2 | 1.14 |  | 26 | 6 | 3.43 |  | 46 | 1 | 0.57 |
| 6 | 1 | 0.57 |  | 27 | 1 | 0.57 |  | 47 | 5 | 2.86 |
| 7 | 7 | 4.0 |  | 28 | 4 | 2.29 |  | 48 | 1 | 0.57 |
| 8 | 2 | 1.14 |  | 29 | 6 | 3.43 |  | 49 | 1 | 0.57 |
| 9 | 6 | 3.43 |  | 30 | 3 | 1.71 |  | 50 | 4 | 2.29 |
| 10 | 3 | 1.71 |  | 31 | 3 | 1.71 |  | 51 | 3 | 1.71 |
| 11 | 1 | 0.57 |  | 32 | 4 | 2.29 |  | 52 | 6 | 3.43 |
| 12 | 3 | 1.71 |  | 33 | 3 | 1.71 |  | 53 | 9 | 5.14 |
| 13 | 3 | 1.71 |  | 34 | 4 | 2.29 |  | 54 | 4 | 2.29 |
| 15 | 4 | 2.29 |  | 35 | 2 | 1.14 |  | 55 | 4 | 2.29 |
| 16 | 6 | 3.43 |  | 36 | 3 | 1.71 |  |  |  |  |
| 17 | 3 | 1.71 |  | 37 | 1 | 0.57 |  |  |  |  |
| 18 | 1 | 0.57 |  | 38 | 4 | 2.29 |  |  |  |  |
| 19 | 2 | 1.14 |  | 39 | 5 | 2.86 |  |  |  |  |
| 20 | 2 | 1.14 |  | 40 | 3 | 1.71 |  |  |  |  |
| 21 | 4 | 2.29 |  | 41 | 3 | 1.71 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 1.93 |  | 21 | 6 | 2.32 |  | 41 | 4 | 1.54 |
| 2 | 2 | 0.77 |  | 22 | 9 | 3.47 |  | 42 | 2 | 0.77 |
| 3 | 5 | 1.93 |  | 23 | 2 | 0.77 |  | 43 | 7 | 2.7 |
| 4 | 2 | 0.77 |  | 24 | 2 | 0.77 |  | 44 | 4 | 1.54 |
| 5 | 5 | 1.93 |  | 25 | 6 | 2.32 |  | 45 | 4 | 1.54 |
| 6 | 1 | 0.39 |  | 26 | 11 | 4.25 |  | 46 | 5 | 1.93 |
| 7 | 11 | 4.25 |  | 27 | 3 | 1.16 |  | 47 | 5 | 1.93 |
| 8 | 4 | 1.54 |  | 28 | 4 | 1.54 |  | 48 | 3 | 1.16 |
| 9 | 7 | 2.7 |  | 29 | 8 | 3.09 |  | 49 | 1 | 0.39 |
| 10 | 4 | 1.54 |  | 30 | 6 | 2.32 |  | 50 | 5 | 1.93 |
| 11 | 1 | 0.39 |  | 31 | 5 | 1.93 |  | 51 | 7 | 2.7 |
| 12 | 4 | 1.54 |  | 32 | 7 | 2.7 |  | 52 | 6 | 2.32 |
| 13 | 8 | 3.09 |  | 33 | 3 | 1.16 |  | 53 | 9 | 3.47 |
| 14 | 1 | 0.39 |  | 34 | 4 | 1.54 |  | 54 | 6 | 2.32 |
| 15 | 5 | 1.93 |  | 35 | 3 | 1.16 |  | 55 | 6 | 2.32 |
| 16 | 8 | 3.09 |  | 36 | 5 | 1.93 |  |  |  |  |
| 17 | 4 | 1.54 |  | 37 | 2 | 0.77 |  |  |  |  |
| 18 | 2 | 0.77 |  | 38 | 5 | 1.93 |  |  |  |  |
| 19 | 3 | 1.16 |  | 39 | 6 | 2.32 |  |  |  |  |
| 20 | 3 | 1.16 |  | 40 | 3 | 1.16 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 14 | 2026-03-05 | 58 |
| 27 | 2026-03-14 | 49 |
| 6 | 2026-03-21 | 42 |
| 45 | 2026-03-24 | 39 |
| 12 | 2026-03-24 | 39 |
| 3 | 2026-03-26 | 37 |
| 42 | 2026-03-28 | 35 |
| 48 | 2026-03-31 | 32 |
| 11 | 2026-03-31 | 32 |
| 54 | 2026-04-04 | 28 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-04-07 | 25 |
| 2 | 2026-04-16 | 16 |
| 3 | 2026-03-26 | 37 |
| 4 | 2026-04-25 | 7 |
| 5 | 2026-04-23 | 9 |
| 6 | 2026-03-21 | 42 |
| 7 | 2026-04-25 | 7 |
| 8 | 2026-04-21 | 11 |
| 9 | 2026-05-02 | 0 |
| 10 | 2026-04-25 | 7 |
| 11 | 2026-03-31 | 32 |
| 12 | 2026-03-24 | 39 |
| 13 | 2026-04-11 | 21 |
| 14 | 2026-03-05 | 58 |
| 15 | 2026-04-30 | 2 |
| 16 | 2026-04-30 | 2 |
| 17 | 2026-05-02 | 0 |
| 18 | 2026-04-09 | 23 |
| 19 | 2026-04-18 | 14 |
| 20 | 2026-04-18 | 14 |
| 21 | 2026-05-02 | 0 |
| 22 | 2026-05-02 | 0 |
| 23 | 2026-04-07 | 25 |
| 24 | 2026-04-28 | 4 |
| 25 | 2026-04-30 | 2 |
| 26 | 2026-05-02 | 0 |
| 27 | 2026-03-14 | 49 |
| 28 | 2026-04-18 | 14 |
| 29 | 2026-04-30 | 2 |
| 30 | 2026-04-21 | 11 |
| 31 | 2026-04-07 | 25 |
| 32 | 2026-04-07 | 25 |
| 33 | 2026-05-02 | 0 |
| 34 | 2026-04-28 | 4 |
| 35 | 2026-04-28 | 4 |
| 36 | 2026-04-21 | 11 |
| 37 | 2026-04-18 | 14 |
| 38 | 2026-04-11 | 21 |
| 39 | 2026-04-21 | 11 |
| 40 | 2026-04-04 | 28 |
| 41 | 2026-04-25 | 7 |
| 42 | 2026-03-28 | 35 |
| 43 | 2026-04-25 | 7 |
| 44 | 2026-04-07 | 25 |
| 45 | 2026-03-24 | 39 |
| 46 | 2026-04-25 | 7 |
| 47 | 2026-04-16 | 16 |
| 48 | 2026-03-31 | 32 |
| 49 | 2026-04-11 | 21 |
| 50 | 2026-04-30 | 2 |
| 51 | 2026-05-02 | 0 |
| 52 | 2026-04-28 | 4 |
| 53 | 2026-04-28 | 4 |
| 54 | 2026-04-04 | 28 |
| 55 | 2026-04-23 | 9 |



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

