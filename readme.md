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
| Power 655 |          1275 | 2017-08-01   | 2025-11-29 |            1275 | 00001      | 01275       |
| Power 645 |          1241 | 2017-10-25   | 2025-11-28 |            1241 | 00198      | 01438       |
| Power 535 |           130 | 2025-06-29   | 2025-11-29 |             260 | 00001      | 00308       |
| Keno      |           386 | 2022-12-04   | 2025-11-29 |           49988 | #0110271   | #0261273    |
| 3D        |          1005 | 2019-04-22   | 2025-11-28 |            1005 | 00001      | 01009       |
| 3D Pro    |           652 | 2021-09-14   | 2025-11-29 |             652 | 00001      | 00656       |
| Bingo18   |           362 | 2024-12-03   | 2025-11-29 |           52276 | 0083123    | 0140579     |

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
| 2025-11-29 00:00:00 | 01275 | [ 4 20 24 27 40 48  9] | 2025-11-30T00:00:57.885215 |
| 2025-11-27 00:00:00 | 01274 | [ 4  5 10 11 28 35 38] | 2025-11-28T00:00:53.620470 |
| 2025-11-25 00:00:00 | 01273 | [23 31 32 42 46 48  4] | 2025-11-26T00:00:52.128543 |
| 2025-11-22 00:00:00 | 01272 | [ 8 10 19 29 34 46 14] | 2025-11-23T00:00:55.277843 |
| 2025-11-20 00:00:00 | 01271 | [ 3 12 19 20 31 42 13] | 2025-11-21T00:00:55.461521 |
| 2025-11-18 00:00:00 | 01270 | [ 7 12 18 22 30 49  5] | 2025-11-19T00:00:50.139294 |
| 2025-11-15 00:00:00 | 01269 | [ 2 30 33 35 42 54 45] | 2025-11-16T00:00:51.177522 |
| 2025-11-13 00:00:00 | 01268 | [ 1 15 30 38 40 43 13] | 2025-11-14T00:00:51.765554 |
| 2025-11-11 00:00:00 | 01267 | [11 20 28 41 47 54 31] | 2025-11-12T00:00:54.138665 |
| 2025-11-08 00:00:00 | 01266 | [14 16 19 22 27 44 18] | 2025-11-09T00:00:52.697026 |

### 🎲 Number Frequency (All Time)
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.7  |       36 |     152 |      |       20 | 1.7  |        10 |      152 |      | 40.0     | 1.94 | 20        | 173      |
|       1 | 1.71 |       39 |     153 |      |       21 | 1.74 |        13 |      155 |      | 41.0     | 1.97 | 8         | 176      |
|       2 | 1.95 |        3 |     174 |      |       22 | 1.7  |        16 |      152 |      | 42.0     | 1.92 | 29        | 171      |
|       3 | 1.87 |       42 |     167 |      |       23 | 1.94 |         1 |      173 |      | 43.0     | 1.66 | 26        | 148      |
|       4 | 1.62 |       30 |     145 |      |       24 | 1.87 |        46 |      167 |      | 44.0     | 1.82 | 14        | 162      |
|       5 | 1.83 |       33 |     163 |      |       25 | 1.78 |        55 |      159 |      | 45.0     | 1.85 | 32        | 165      |
|       6 | 1.94 |       48 |     173 |      |       26 | 1.85 |        52 |      165 |      | 46.0     | 1.66 | 2         | 148      |
|       7 | 1.74 |       21 |     155 |      |       27 | 1.99 |        40 |      178 |      | 47.0     | 1.89 | 11        | 169      |
|       8 | 1.83 |       45 |     163 |      |       28 | 1.64 |        37 |      146 |      | 48.0     | 1.89 | 44        | 169      |
|       9 | 1.7  |       15 |     152 |      |       29 | 2.04 |        34 |      182 |      | 49.0     | 1.71 | 38        | 153      |
|      10 | 1.55 |        6 |     138 |      |       30 | 2.06 |        43 |      184 |      | 50.0     | 1.8  | 50        | 161      |
|      11 | 1.85 |       18 |     165 |      |       31 | 1.6  |        25 |      143 |      | 51.0     | 1.79 | 35        | 160      |
|      12 | 1.89 |       12 |     169 |      |       32 | 2.07 |        22 |      185 |      | 52.0     | 2.13 | 41        | 190      |
|      13 | 1.69 |       27 |     151 |      |       33 | 1.6  |        28 |      143 |      | 53.0     | 1.89 | 53        | 169      |
|      14 | 2.01 |        9 |     179 |      |       34 | 1.84 |        49 |      164 |      | 54.0     | 1.83 | 47        | 163      |
|      15 | 1.86 |       24 |     166 |      |       35 | 1.86 |        19 |      166 |      |          |      |           |          |
|      16 | 1.7  |       54 |     152 |      |       36 | 1.93 |        31 |      172 |      |          |      |           |          |
|      17 | 2.05 |       51 |     183 |      |       37 | 1.95 |        23 |      174 |      |          |      |           |          |
|      18 | 1.51 |        4 |     135 |      |       38 | 1.84 |         5 |      164 |      |          |      |           |          |
|      19 | 1.57 |        7 |     140 |      |       39 | 1.66 |        17 |      148 |      |          |      |           |          |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 3.3  |       11 |       3 |      |       20 |  1.1 |        24 |        1 |      | 40.0     | 2.2  | 13        | 2        |
|       1 | 1.1  |        9 |       1 |      |       21 |  3.3 |        30 |        3 |      | 41.0     | 1.1  | 44        | 1        |
|       2 | 4.4  |       20 |       4 |      |       22 |  1.1 |         6 |        1 |      | 42.0     | 2.2  | 5         | 2        |
|       3 | 3.3  |       27 |       3 |      |       23 |  2.2 |        43 |        2 |      | 43.0     | 1.1  | 2         | 1        |
|       4 | 1.1  |       45 |       1 |      |       24 |  2.2 |        35 |        2 |      |          |      |           |          |
|       5 | 2.2  |       14 |       2 |      |       25 |  3.3 |        28 |        3 |      |          |      |           |          |
|       6 | 2.2  |        8 |       2 |      |       26 |  2.2 |        54 |        2 |      |          |      |           |          |
|       7 | 2.2  |       10 |       2 |      |       27 |  1.1 |        47 |        1 |      |          |      |           |          |
|       8 | 1.1  |       32 |       1 |      |       28 |  3.3 |        19 |        3 |      |          |      |           |          |
|       9 | 2.2  |       18 |       2 |      |       29 |  2.2 |        36 |        2 |      |          |      |           |          |
|      10 | 4.4  |       29 |       4 |      |       30 |  1.1 |        23 |        1 |      |          |      |           |          |
|      11 | 2.2  |        7 |       2 |      |       31 |  2.2 |        22 |        2 |      |          |      |           |          |
|      12 | 5.49 |       31 |       5 |      |       32 |  2.2 |        15 |        2 |      |          |      |           |          |
|      13 | 2.2  |       12 |       2 |      |       33 |  3.3 |        42 |        3 |      |          |      |           |          |
|      14 | 2.2  |       49 |       2 |      |       34 |  1.1 |         1 |        1 |      |          |      |           |          |
|      15 | 2.2  |       16 |       2 |      |       35 |  3.3 |         4 |        3 |      |          |      |           |          |
|      16 | 2.2  |       48 |       2 |      |       36 |  2.2 |        46 |        2 |      |          |      |           |          |
|      17 | 3.3  |       33 |       3 |      |       37 |  1.1 |         3 |        1 |      |          |      |           |          |
|      18 | 3.3  |       38 |       3 |      |       38 |  2.2 |        40 |        2 |      |          |      |           |          |
|      19 | 1.1  |       41 |       1 |      |       39 |  1.1 |        34 |        1 |      |          |      |           |          |

#### Last 60 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 2.75 |       31 |       5 |      |       20 | 1.65 |        37 |        3 |      | 40.0     | 2.75 | 35        | 5        |
|       1 | 2.2  |        5 |       4 |      |       21 | 2.2  |         3 |        4 |      | 41.0     | 1.65 | 48        | 3        |
|       2 | 2.2  |       45 |       4 |      |       22 | 2.75 |        38 |        5 |      | 42.0     | 1.1  | 44        | 2        |
|       3 | 1.65 |       28 |       3 |      |       23 | 3.3  |        40 |        6 |      | 43.0     | 3.85 | 22        | 7        |
|       4 | 0.55 |       32 |       1 |      |       24 | 1.1  |        18 |        2 |      | 44.0     | 0.55 | 39        | 1        |
|       5 | 1.1  |       47 |       2 |      |       25 | 2.2  |        33 |        4 |      | 45.0     | 1.1  | 23        | 2        |
|       6 | 0.55 |       34 |       1 |      |       26 | 1.1  |        25 |        2 |      | 46.0     | 2.2  | 16        | 4        |
|       7 | 3.3  |       43 |       6 |      |       27 | 2.75 |        19 |        5 |      | 47.0     | 1.1  | 55        | 2        |
|       8 | 2.2  |       12 |       4 |      |       28 | 2.75 |         8 |        5 |      | 48.0     | 1.65 | 54        | 3        |
|       9 | 3.3  |       27 |       6 |      |       29 | 1.65 |         4 |        3 |      | 49.0     | 1.65 | 26        | 3        |
|      10 | 1.1  |       50 |       2 |      |       30 | 2.2  |        10 |        4 |      | 50.0     | 2.75 | 42        | 5        |
|      11 | 1.65 |       41 |       3 |      |       31 | 2.75 |         7 |        5 |      |          |      |           |          |
|      12 | 3.3  |       20 |       6 |      |       32 | 2.2  |        36 |        4 |      |          |      |           |          |
|      13 | 1.65 |       30 |       3 |      |       33 | 1.65 |        15 |        3 |      |          |      |           |          |
|      14 | 2.2  |       24 |       4 |      |       34 | 1.1  |         1 |        2 |      |          |      |           |          |
|      15 | 1.65 |        9 |       3 |      |       35 | 1.65 |        49 |        3 |      |          |      |           |          |
|      16 | 2.2  |       14 |       4 |      |       36 | 1.1  |         6 |        2 |      |          |      |           |          |
|      17 | 1.1  |        2 |       2 |      |       37 | 3.3  |        11 |        6 |      |          |      |           |          |
|      18 | 1.65 |       13 |       3 |      |       38 | 1.65 |        21 |        3 |      |          |      |           |          |
|      19 | 1.65 |       46 |       3 |      |       39 | 2.75 |        29 |        5 |      |          |      |           |          |

#### Last 90 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.47 |       28 |       4 |      |       20 | 1.83 |         2 |        5 |      | 40.0     | 1.83 | 14        | 5        |
|       1 | 1.47 |       21 |       4 |      |       21 | 2.56 |        11 |        7 |      | 41.0     | 1.47 | 55        | 4        |
|       2 | 1.47 |       18 |       4 |      |       22 | 1.1  |         6 |        3 |      | 42.0     | 2.56 | 46        | 7        |
|       3 | 2.2  |        9 |       6 |      |       23 | 1.1  |        26 |        3 |      | 43.0     | 1.83 | 35        | 5        |
|       4 | 3.3  |       22 |       9 |      |       24 | 0.73 |        52 |        2 |      | 44.0     | 1.1  | 54        | 3        |
|       5 | 2.2  |        7 |       6 |      |       25 | 1.1  |        25 |        3 |      | 45.0     | 1.47 | 23        | 4        |
|       6 | 2.93 |       31 |       8 |      |       26 | 1.1  |        37 |        3 |      | 46.0     | 1.1  | 48        | 3        |
|       7 | 1.1  |        4 |       3 |      |       27 | 2.93 |        27 |        8 |      | 47.0     | 1.83 | 36        | 5        |
|       8 | 1.1  |       53 |       3 |      |       28 | 4.03 |        19 |       11 |      | 48.0     | 1.83 | 49        | 5        |
|       9 | 2.93 |       40 |       8 |      |       29 | 1.1  |         1 |        3 |      | 49.0     | 2.56 | 16        | 7        |
|      10 | 1.83 |        3 |       5 |      |       30 | 2.2  |        30 |        6 |      | 50.0     | 1.47 | 12        | 4        |
|      11 | 3.66 |       43 |      10 |      |       31 | 4.03 |         8 |       11 |      | 51.0     | 2.93 | 20        | 8        |
|      12 | 1.47 |       41 |       4 |      |       32 | 1.47 |        10 |        4 |      | 52.0     | 0.73 | 44        | 2        |
|      13 | 2.56 |       42 |       7 |      |       33 | 0.73 |        51 |        2 |      | 53.0     | 1.1  | 17        | 3        |
|      14 | 1.83 |       33 |       5 |      |       34 | 1.83 |        13 |        5 |      | 54.0     | 0.73 | 47        | 2        |
|      15 | 1.47 |       34 |       4 |      |       35 | 1.47 |        15 |        4 |      |          |      |           |          |
|      16 | 1.83 |       45 |       5 |      |       36 | 1.47 |        39 |        4 |      |          |      |           |          |
|      17 | 1.83 |        5 |       5 |      |       37 | 2.2  |        24 |        6 |      |          |      |           |          |
|      18 | 0.37 |       32 |       1 |      |       38 | 1.83 |        29 |        5 |      |          |      |           |          |
|      19 | 2.93 |       38 |       8 |      |       39 | 0.73 |        50 |        2 |      |          |      |           |          |



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

