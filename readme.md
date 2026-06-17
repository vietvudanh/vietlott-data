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
| Power 655 | 1359 | 2017-08-01 | 2026-06-16 | 1359 | 00001 | 01359 |
| Power 645 | 1326 | 2017-10-25 | 2026-06-14 | 1326 | 00198 | 01523 |
| Power 535 | 317 | 2025-06-29 | 2026-06-16 | 633 | 00001 | 00706 |
| Keno | 586 | 2022-12-04 | 2026-06-17 | 73852 | #0110271 | #0285070 |
| 3D | 1089 | 2019-04-22 | 2026-06-15 | 1089 | 00001 | 01093 |
| 3D Pro | 736 | 2021-09-14 | 2026-06-16 | 736 | 00001 | 00740 |
| Bingo18 | 560 | 2024-12-03 | 2026-06-17 | 76366 | 0083123 | 0172266 |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-06-16 | 01359 | [2, 4, 5, 7, 31, 40, 14] | 2026-06-17T00:01:06.923555 |
| 2026-06-13 | 01358 | [2, 8, 19, 33, 36, 47, 42] | 2026-06-14T00:01:35.675726 |
| 2026-06-11 | 01357 | [1, 8, 17, 24, 40, 48, 46] | 2026-06-12T00:01:08.901627 |
| 2026-06-09 | 01356 | [6, 8, 18, 27, 32, 34, 35] | 2026-06-10T00:01:14.808665 |
| 2026-06-06 | 01355 | [3, 11, 16, 37, 39, 41, 28] | 2026-06-09T00:01:21.410974 |
| 2026-06-04 | 01354 | [23, 24, 28, 29, 39, 43, 45] | 2026-06-05T00:01:07.859417 |
| 2026-06-02 | 01353 | [1, 3, 5, 16, 37, 51, 42] | 2026-06-03T00:01:21.144685 |
| 2026-05-30 | 01352 | [2, 8, 20, 24, 25, 42, 44] | 2026-06-01T00:01:26.268124 |
| 2026-05-28 | 01351 | [8, 11, 21, 25, 31, 53, 54] | 2026-05-29T00:01:21.691058 |
| 2026-05-26 | 01350 | [1, 14, 15, 19, 23, 34, 29] | 2026-05-27T00:01:07.369677 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 181 | 1.9 |  | 21 | 170 | 1.79 |  | 41 | 199 | 2.09 |
| 2 | 156 | 1.64 |  | 22 | 202 | 2.12 |  | 42 | 176 | 1.85 |
| 3 | 185 | 1.94 |  | 23 | 181 | 1.9 |  | 43 | 195 | 2.05 |
| 4 | 142 | 1.49 |  | 24 | 173 | 1.82 |  | 44 | 176 | 1.85 |
| 5 | 174 | 1.83 |  | 25 | 156 | 1.64 |  | 45 | 173 | 1.82 |
| 6 | 142 | 1.49 |  | 26 | 164 | 1.72 |  | 46 | 177 | 1.86 |
| 7 | 153 | 1.61 |  | 27 | 158 | 1.66 |  | 47 | 173 | 1.82 |
| 8 | 188 | 1.98 |  | 28 | 154 | 1.62 |  | 48 | 185 | 1.94 |
| 9 | 188 | 1.98 |  | 29 | 187 | 1.97 |  | 49 | 168 | 1.77 |
| 10 | 162 | 1.7 |  | 30 | 158 | 1.66 |  | 50 | 174 | 1.83 |
| 11 | 176 | 1.85 |  | 31 | 182 | 1.91 |  | 51 | 193 | 2.03 |
| 12 | 179 | 1.88 |  | 32 | 184 | 1.93 |  | 52 | 175 | 1.84 |
| 13 | 168 | 1.77 |  | 33 | 173 | 1.82 |  | 53 | 185 | 1.94 |
| 14 | 172 | 1.81 |  | 34 | 194 | 2.04 |  | 54 | 164 | 1.72 |
| 15 | 162 | 1.7 |  | 35 | 167 | 1.76 |  | 55 | 173 | 1.82 |
| 16 | 169 | 1.78 |  | 36 | 164 | 1.72 |  |  |  |  |
| 17 | 157 | 1.65 |  | 37 | 156 | 1.64 |  |  |  |  |
| 18 | 172 | 1.81 |  | 38 | 167 | 1.76 |  |  |  |  |
| 19 | 171 | 1.8 |  | 39 | 167 | 1.76 |  |  |  |  |
| 20 | 184 | 1.93 |  | 40 | 188 | 1.98 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3.3 |  | 24 | 3 | 3.3 |  | 46 | 1 | 1.1 |
| 2 | 3 | 3.3 |  | 25 | 2 | 2.2 |  | 47 | 1 | 1.1 |
| 3 | 3 | 3.3 |  | 27 | 2 | 2.2 |  | 48 | 2 | 2.2 |
| 4 | 1 | 1.1 |  | 28 | 3 | 3.3 |  | 49 | 1 | 1.1 |
| 5 | 2 | 2.2 |  | 29 | 2 | 2.2 |  | 51 | 1 | 1.1 |
| 6 | 1 | 1.1 |  | 31 | 2 | 2.2 |  | 53 | 2 | 2.2 |
| 7 | 1 | 1.1 |  | 32 | 2 | 2.2 |  | 54 | 1 | 1.1 |
| 8 | 5 | 5.49 |  | 33 | 1 | 1.1 |  |  |  |  |
| 11 | 2 | 2.2 |  | 34 | 3 | 3.3 |  |  |  |  |
| 12 | 1 | 1.1 |  | 35 | 1 | 1.1 |  |  |  |  |
| 14 | 2 | 2.2 |  | 36 | 1 | 1.1 |  |  |  |  |
| 15 | 1 | 1.1 |  | 37 | 2 | 2.2 |  |  |  |  |
| 16 | 3 | 3.3 |  | 38 | 1 | 1.1 |  |  |  |  |
| 17 | 2 | 2.2 |  | 39 | 3 | 3.3 |  |  |  |  |
| 18 | 2 | 2.2 |  | 40 | 4 | 4.4 |  |  |  |  |
| 19 | 2 | 2.2 |  | 41 | 1 | 1.1 |  |  |  |  |
| 20 | 2 | 2.2 |  | 42 | 3 | 3.3 |  |  |  |  |
| 21 | 3 | 3.3 |  | 43 | 1 | 1.1 |  |  |  |  |
| 22 | 1 | 1.1 |  | 44 | 1 | 1.1 |  |  |  |  |
| 23 | 2 | 2.2 |  | 45 | 2 | 2.2 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1.65 |  | 21 | 5 | 2.75 |  | 41 | 3 | 1.65 |
| 2 | 4 | 2.2 |  | 22 | 4 | 2.2 |  | 42 | 3 | 1.65 |
| 3 | 4 | 2.2 |  | 23 | 2 | 1.1 |  | 43 | 2 | 1.1 |
| 4 | 3 | 1.65 |  | 24 | 5 | 2.75 |  | 44 | 2 | 1.1 |
| 5 | 3 | 1.65 |  | 25 | 5 | 2.75 |  | 45 | 3 | 1.65 |
| 6 | 2 | 1.1 |  | 26 | 3 | 1.65 |  | 46 | 4 | 2.2 |
| 7 | 2 | 1.1 |  | 27 | 2 | 1.1 |  | 47 | 3 | 1.65 |
| 8 | 8 | 4.4 |  | 28 | 5 | 2.75 |  | 48 | 3 | 1.65 |
| 9 | 3 | 1.65 |  | 29 | 4 | 2.2 |  | 49 | 1 | 0.55 |
| 10 | 2 | 1.1 |  | 30 | 2 | 1.1 |  | 50 | 6 | 3.3 |
| 11 | 3 | 1.65 |  | 31 | 3 | 1.65 |  | 51 | 3 | 1.65 |
| 12 | 1 | 0.55 |  | 32 | 5 | 2.75 |  | 52 | 1 | 0.55 |
| 13 | 1 | 0.55 |  | 33 | 4 | 2.2 |  | 53 | 5 | 2.75 |
| 14 | 3 | 1.65 |  | 34 | 4 | 2.2 |  | 54 | 1 | 0.55 |
| 15 | 4 | 2.2 |  | 35 | 2 | 1.1 |  | 55 | 3 | 1.65 |
| 16 | 5 | 2.75 |  | 36 | 3 | 1.65 |  |  |  |  |
| 17 | 5 | 2.75 |  | 37 | 4 | 2.2 |  |  |  |  |
| 18 | 2 | 1.1 |  | 38 | 2 | 1.1 |  |  |  |  |
| 19 | 3 | 1.65 |  | 39 | 7 | 3.85 |  |  |  |  |
| 20 | 3 | 1.65 |  | 40 | 4 | 2.2 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | 1.83 |  | 21 | 7 | 2.56 |  | 41 | 4 | 1.47 |
| 2 | 5 | 1.83 |  | 22 | 9 | 3.3 |  | 42 | 4 | 1.47 |
| 3 | 7 | 2.56 |  | 23 | 4 | 1.47 |  | 43 | 4 | 1.47 |
| 4 | 3 | 1.1 |  | 24 | 5 | 1.83 |  | 44 | 4 | 1.47 |
| 5 | 4 | 1.47 |  | 25 | 6 | 2.2 |  | 45 | 4 | 1.47 |
| 6 | 3 | 1.1 |  | 26 | 5 | 1.83 |  | 46 | 4 | 1.47 |
| 7 | 7 | 2.56 |  | 27 | 2 | 0.73 |  | 47 | 6 | 2.2 |
| 8 | 9 | 3.3 |  | 28 | 6 | 2.2 |  | 48 | 4 | 1.47 |
| 9 | 6 | 2.2 |  | 29 | 6 | 2.2 |  | 49 | 2 | 0.73 |
| 10 | 4 | 1.47 |  | 30 | 4 | 1.47 |  | 50 | 6 | 2.2 |
| 11 | 4 | 1.47 |  | 31 | 5 | 1.83 |  | 51 | 4 | 1.47 |
| 12 | 2 | 0.73 |  | 32 | 8 | 2.93 |  | 52 | 3 | 1.1 |
| 13 | 4 | 1.47 |  | 33 | 5 | 1.83 |  | 53 | 10 | 3.66 |
| 14 | 3 | 1.1 |  | 34 | 7 | 2.56 |  | 54 | 2 | 0.73 |
| 15 | 6 | 2.2 |  | 35 | 3 | 1.1 |  | 55 | 5 | 1.83 |
| 16 | 8 | 2.93 |  | 36 | 4 | 1.47 |  |  |  |  |
| 17 | 6 | 2.2 |  | 37 | 4 | 1.47 |  |  |  |  |
| 18 | 3 | 1.1 |  | 38 | 6 | 2.2 |  |  |  |  |
| 19 | 4 | 1.47 |  | 39 | 9 | 3.3 |  |  |  |  |
| 20 | 3 | 1.1 |  | 40 | 6 | 2.2 |  |  |  |  |

### ⏳ Top 10 số lâu chưa xuất hiện (Top 10 Numbers by Days Since Last Appearance)
| result | last_date | days_since |
| --- | --- | --- |
| 52 | 2026-04-28 | 49 |
| 9 | 2026-05-02 | 45 |
| 30 | 2026-05-05 | 42 |
| 13 | 2026-05-07 | 40 |
| 10 | 2026-05-09 | 38 |
| 55 | 2026-05-14 | 33 |
| 26 | 2026-05-14 | 33 |
| 50 | 2026-05-16 | 31 |
| 12 | 2026-05-19 | 28 |
| 22 | 2026-05-23 | 24 |

### 📆 Số ngày từ lần xuất hiện cuối cùng (Days Since Last Appearance - All Numbers)
| result | last_date | days_since |
| --- | --- | --- |
| 1 | 2026-06-11 | 5 |
| 2 | 2026-06-16 | 0 |
| 3 | 2026-06-06 | 10 |
| 4 | 2026-06-16 | 0 |
| 5 | 2026-06-16 | 0 |
| 6 | 2026-06-09 | 7 |
| 7 | 2026-06-16 | 0 |
| 8 | 2026-06-13 | 3 |
| 9 | 2026-05-02 | 45 |
| 10 | 2026-05-09 | 38 |
| 11 | 2026-06-06 | 10 |
| 12 | 2026-05-19 | 28 |
| 13 | 2026-05-07 | 40 |
| 14 | 2026-06-16 | 0 |
| 15 | 2026-05-26 | 21 |
| 16 | 2026-06-06 | 10 |
| 17 | 2026-06-11 | 5 |
| 18 | 2026-06-09 | 7 |
| 19 | 2026-06-13 | 3 |
| 20 | 2026-05-30 | 17 |
| 21 | 2026-05-28 | 19 |
| 22 | 2026-05-23 | 24 |
| 23 | 2026-06-04 | 12 |
| 24 | 2026-06-11 | 5 |
| 25 | 2026-05-30 | 17 |
| 26 | 2026-05-14 | 33 |
| 27 | 2026-06-09 | 7 |
| 28 | 2026-06-06 | 10 |
| 29 | 2026-06-04 | 12 |
| 30 | 2026-05-05 | 42 |
| 31 | 2026-06-16 | 0 |
| 32 | 2026-06-09 | 7 |
| 33 | 2026-06-13 | 3 |
| 34 | 2026-06-09 | 7 |
| 35 | 2026-06-09 | 7 |
| 36 | 2026-06-13 | 3 |
| 37 | 2026-06-06 | 10 |
| 38 | 2026-05-23 | 24 |
| 39 | 2026-06-06 | 10 |
| 40 | 2026-06-16 | 0 |
| 41 | 2026-06-06 | 10 |
| 42 | 2026-06-13 | 3 |
| 43 | 2026-06-04 | 12 |
| 44 | 2026-05-30 | 17 |
| 45 | 2026-06-04 | 12 |
| 46 | 2026-06-11 | 5 |
| 47 | 2026-06-13 | 3 |
| 48 | 2026-06-11 | 5 |
| 49 | 2026-05-23 | 24 |
| 50 | 2026-05-16 | 31 |
| 51 | 2026-06-02 | 14 |
| 52 | 2026-04-28 | 49 |
| 53 | 2026-05-28 | 19 |
| 54 | 2026-05-28 | 19 |
| 55 | 2026-05-14 | 33 |



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

