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
- [📊 Data Statistics](#-data-statistics)
- [🔮 Prediction Models](#-prediction-models)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [📈 Power 5/35 Analysis](#-power-535-analysis)
  - [📅 Recent Results](#-recent-results-1)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time-1)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period-1)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## 📊 Data Statistics

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1262 | 2017-08-01   | 2025-10-30 |            1262 | 00001      | 01262       |
| Power 645 |          1228 | 2017-10-25   | 2025-10-29 |            1228 | 00198      | 01425       |
| Power 535 |           100 | 2025-06-29   | 2025-10-30 |             200 | 00001      | 00248       |
| Keno      |           356 | 2022-12-04   | 2025-10-30 |           46493 | #0110271   | #0257778    |
| 3D        |           992 | 2019-04-22   | 2025-10-29 |             992 | 00001      | 00996       |
| 3D Pro    |           639 | 2021-09-14   | 2025-10-30 |             639 | 00001      | 00643       |
| Bingo18   |           332 | 2024-12-03   | 2025-10-30 |           51544 | 0083123    | 0135809     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

No significant matches found in backtest period.



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date                |    id | result                 | process_time               |
|:--------------------|------:|:-----------------------|:---------------------------|
| 2025-10-30 00:00:00 | 01262 | [20 23 35 41 47 55 37] | 2025-10-31T00:00:51.288093 |
| 2025-10-28 00:00:00 | 01261 | [ 6  8 10 22 25 54  9] | 2025-10-29T00:00:48.613372 |
| 2025-10-25 00:00:00 | 01260 | [ 3  5 11 13 24 27 45] | 2025-10-26T00:00:45.744914 |
| 2025-10-23 00:00:00 | 01259 | [ 8 10 21 48 49 50 40] | 2025-10-24T18:00:52.094824 |
| 2025-10-21 00:00:00 | 01258 | [ 3 11 12 14 22 40 41] | 2025-10-21T21:48:33.658764 |
| 2025-10-18 00:00:00 | 01257 | [ 5 16 19 21 38 43 50] | 2025-10-21T21:48:33.658800 |
| 2025-10-16 00:00:00 | 01256 | [14 15 24 26 27 45 36] | 2025-10-17 21:15:55.017468 |
| 2025-10-14 00:00:00 | 01255 | [ 8  9 16 26 37 55 12] | 2025-10-17 21:15:55.017590 |
| 2025-10-11 00:00:00 | 01254 | [ 3  7 26 43 44 46 25] | 2025-10-17 21:15:55.017694 |
| 2025-10-09 00:00:00 | 01253 | [ 7 11 21 22 39 42 40] | 2025-10-17 21:15:55.017805 |

### 🎲 Number Frequency (All Time)
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.81 |       33 |     160 |      |       20 | 1.49 |         4 |      132 |      | 40.0     | 1.81 | 14        | 160      |
|       1 | 1.7  |       15 |     150 |      |       21 | 1.7  |        16 |      150 |      | 41.0     | 1.68 | 26        | 148      |
|       2 | 1.83 |       45 |     162 |      |       22 | 1.7  |        10 |      150 |      | 42.0     | 1.83 | 5         | 162      |
|       3 | 1.89 |       12 |     167 |      |       23 | 1.56 |         7 |      138 |      | 43.0     | 1.88 | 11        | 166      |
|       4 | 1.86 |       42 |     164 |      |       24 | 1.8  |        55 |      159 |      | 44.0     | 1.66 | 2         | 147      |
|       5 | 1.55 |        6 |     137 |      |       25 | 1.62 |        25 |      143 |      | 45.0     | 1.97 | 8         | 174      |
|       6 | 1.85 |       18 |     163 |      |       26 | 1.87 |        46 |      165 |      | 46.0     | 1.68 | 17        | 148      |
|       7 | 1.96 |        3 |     173 |      |       27 | 1.89 |        31 |      167 |      | 47.0     | 1.91 | 20        | 169      |
|       8 | 1.61 |       30 |     142 |      |       28 | 1.83 |        49 |      162 |      | 48.0     | 1.79 | 35        | 158      |
|       9 | 1.73 |       39 |     153 |      |       29 | 1.87 |        52 |      165 |      | 49.0     | 2.14 | 41        | 189      |
|      10 | 1.68 |       27 |     148 |      |       30 | 2.05 |        34 |      181 |      | 50.0     | 1.91 | 53        | 169      |
|      11 | 1.7  |       36 |     150 |      |       31 | 1.58 |        28 |      140 |      | 51.0     | 1.83 | 47        | 162      |
|      12 | 1.75 |       21 |     155 |      |       32 | 2.07 |        22 |      183 |      | 52.0     | 1.7  | 38        | 150      |
|      13 | 1.94 |       48 |     171 |      |       33 | 1.65 |        37 |      146 |      | 53.0     | 1.9  | 44        | 168      |
|      14 | 2.02 |        9 |     178 |      |       34 | 1.99 |        40 |      176 |      | 54.0     | 1.82 | 50        | 161      |
|      15 | 1.87 |       24 |     165 |      |       35 | 1.85 |        19 |      163 |      |          |      |           |          |
|      16 | 1.7  |       54 |     150 |      |       36 | 2.06 |        43 |      182 |      |          |      |           |          |
|      17 | 2.07 |       51 |     183 |      |       37 | 1.96 |        23 |      173 |      |          |      |           |          |
|      18 | 1.95 |        1 |     172 |      |       38 | 1.89 |        29 |      167 |      |          |      |           |          |
|      19 | 1.73 |       13 |     153 |      |       39 | 1.86 |        32 |      164 |      |          |      |           |          |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   index |   % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 2.6 |       12 |       2 |      |       20 |  2.6 |        27 |        2 |      | 40.0     | 5.19 | 22        | 4        |
|       1 | 1.3 |       23 |       1 |      |       21 |  2.6 |        50 |        2 |      |          |      |           |          |
|       2 | 1.3 |        6 |       1 |      |       22 |  1.3 |        42 |        1 |      |          |      |           |          |
|       3 | 1.3 |       20 |       1 |      |       23 |  2.6 |        19 |        2 |      |          |      |           |          |
|       4 | 3.9 |       26 |       3 |      |       24 |  1.3 |        44 |        1 |      |          |      |           |          |
|       5 | 3.9 |        8 |       3 |      |       25 |  3.9 |        45 |        3 |      |          |      |           |          |
|       6 | 2.6 |       41 |       2 |      |       26 |  3.9 |        43 |        3 |      |          |      |           |          |
|       7 | 2.6 |       16 |       2 |      |       27 |  2.6 |        25 |        2 |      |          |      |           |          |
|       8 | 2.6 |       55 |       2 |      |       28 |  1.3 |        36 |        1 |      |          |      |           |          |
|       9 | 2.6 |       14 |       2 |      |       29 |  3.9 |        40 |        3 |      |          |      |           |          |
|      10 | 1.3 |       54 |       1 |      |       30 |  1.3 |        47 |        1 |      |          |      |           |          |
|      11 | 3.9 |       37 |       3 |      |       31 |  1.3 |        29 |        1 |      |          |      |           |          |
|      12 | 3.9 |       21 |       3 |      |       32 |  1.3 |        13 |        1 |      |          |      |           |          |
|      13 | 2.6 |        9 |       2 |      |       33 |  3.9 |         3 |        3 |      |          |      |           |          |
|      14 | 3.9 |       11 |       3 |      |       34 |  2.6 |         7 |        2 |      |          |      |           |          |
|      15 | 2.6 |       35 |       2 |      |       35 |  1.3 |        48 |        1 |      |          |      |           |          |
|      16 | 1.3 |       38 |       1 |      |       36 |  2.6 |        10 |        2 |      |          |      |           |          |
|      17 | 1.3 |       49 |       1 |      |       37 |  2.6 |         5 |        2 |      |          |      |           |          |
|      18 | 2.6 |       24 |       2 |      |       38 |  1.3 |        39 |        1 |      |          |      |           |          |
|      19 | 1.3 |       15 |       1 |      |       39 |  1.3 |        46 |        1 |      |          |      |           |          |

#### Last 60 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.24 |       53 |       2 |      |       20 | 0.62 |        47 |        1 |      | 40.0     | 1.86 | 42        | 3        |
|       1 | 1.86 |       17 |       3 |      |       21 | 0.62 |        51 |        1 |      | 41.0     | 3.11 | 27        | 5        |
|       2 | 3.11 |       38 |       5 |      |       22 | 2.48 |        39 |        4 |      | 42.0     | 1.24 | 31        | 2        |
|       3 | 0.62 |       54 |       1 |      |       23 | 2.48 |        21 |        4 |      | 43.0     | 5.59 | 8         | 9        |
|       4 | 1.86 |       26 |       3 |      |       24 | 3.73 |        19 |        6 |      | 44.0     | 1.24 | 15        | 2        |
|       5 | 2.48 |        3 |       4 |      |       25 | 1.86 |        14 |        3 |      | 45.0     | 3.73 | 43        | 6        |
|       6 | 1.24 |        1 |       2 |      |       26 | 0.62 |        44 |        1 |      | 46.0     | 3.11 | 46        | 5        |
|       7 | 3.11 |       22 |       5 |      |       27 | 2.48 |        55 |        4 |      | 47.0     | 1.86 | 35        | 3        |
|       8 | 1.24 |       50 |       2 |      |       28 | 1.24 |        12 |        2 |      | 48.0     | 0.62 | 48        | 1        |
|       9 | 1.86 |       36 |       3 |      |       29 | 1.24 |        34 |        2 |      | 49.0     | 1.24 | 18        | 2        |
|      10 | 2.48 |       16 |       4 |      |       30 | 3.11 |        40 |        5 |      | 50.0     | 2.48 | 2         | 4        |
|      11 | 1.24 |       10 |       2 |      |       31 | 1.86 |        13 |        3 |      | 51.0     | 2.48 | 7         | 4        |
|      12 | 3.11 |       24 |       5 |      |       32 | 2.48 |        45 |        4 |      | 52.0     | 1.24 | 52        | 2        |
|      13 | 0.62 |       29 |       1 |      |       33 | 1.86 |        11 |        3 |      |          |      |           |          |
|      14 | 2.48 |       20 |       4 |      |       34 | 1.86 |         5 |        3 |      |          |      |           |          |
|      15 | 1.24 |       23 |       2 |      |       35 | 1.24 |         6 |        2 |      |          |      |           |          |
|      16 | 1.86 |       41 |       3 |      |       36 | 1.24 |        30 |        2 |      |          |      |           |          |
|      17 | 0.62 |       28 |       1 |      |       37 | 1.24 |         9 |        2 |      |          |      |           |          |
|      18 | 1.24 |       33 |       2 |      |       38 | 1.24 |        25 |        2 |      |          |      |           |          |
|      19 | 1.86 |       37 |       3 |      |       39 | 1.24 |        49 |        2 |      |          |      |           |          |

#### Last 90 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 2.38 |       16 |       6 |      |       20 | 3.57 |        43 |        9 |      | 40.0     | 0.79 | 32        | 2        |
|       1 | 1.19 |       49 |       3 |      |       21 | 1.19 |        51 |        3 |      | 41.0     | 3.17 | 22        | 8        |
|       2 | 3.17 |       40 |       8 |      |       22 | 1.98 |        45 |        5 |      | 42.0     | 2.38 | 38        | 6        |
|       3 | 1.98 |       27 |       5 |      |       23 | 1.98 |        46 |        5 |      | 43.0     | 0.79 | 33        | 2        |
|       4 | 1.59 |       13 |       4 |      |       24 | 1.59 |         7 |        4 |      | 44.0     | 1.19 | 47        | 3        |
|       5 | 1.98 |       14 |       5 |      |       25 | 3.97 |        19 |       10 |      | 45.0     | 0.4  | 54        | 1        |
|       6 | 3.57 |        8 |       9 |      |       26 | 2.38 |        55 |        6 |      | 46.0     | 2.38 | 34        | 6        |
|       7 | 0.79 |       12 |       2 |      |       27 | 2.38 |        35 |        6 |      | 47.0     | 1.19 | 25        | 3        |
|       8 | 2.38 |       17 |       6 |      |       28 | 1.98 |         6 |        5 |      | 48.0     | 2.78 | 5         | 7        |
|       9 | 1.59 |       11 |       4 |      |       29 | 2.78 |        24 |        7 |      | 49.0     | 1.59 | 53        | 4        |
|      10 | 1.59 |       42 |       4 |      |       30 | 1.98 |         2 |        5 |      | 50.0     | 2.38 | 30        | 6        |
|      11 | 1.19 |       18 |       3 |      |       31 | 1.98 |         1 |        5 |      | 51.0     | 0.79 | 15        | 2        |
|      12 | 0.79 |       28 |       2 |      |       32 | 1.59 |        23 |        4 |      | 52.0     | 1.59 | 10        | 4        |
|      13 | 1.59 |       37 |       4 |      |       33 | 1.59 |         3 |        4 |      | 53.0     | 1.19 | 48        | 3        |
|      14 | 1.59 |       21 |       4 |      |       34 | 1.59 |        31 |        4 |      |          |      |           |          |
|      15 | 1.98 |       44 |       5 |      |       35 | 1.59 |        20 |        4 |      |          |      |           |          |
|      16 | 3.17 |        9 |       8 |      |       36 | 1.59 |        41 |        4 |      |          |      |           |          |
|      17 | 2.38 |       36 |       6 |      |       37 | 1.59 |        50 |        4 |      |          |      |           |          |
|      18 | 0.4  |       29 |       1 |      |       38 | 1.59 |        26 |        4 |      |          |      |           |          |
|      19 | 1.59 |       39 |       4 |      |       39 | 1.59 |        52 |        4 |      |          |      |           |          |



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
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
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
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>

