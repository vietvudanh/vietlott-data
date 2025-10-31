# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)

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
| Power 655 |          1261 | 2017-08-01   | 2025-10-28 |            1261 | 00001      | 01261       |
| Power 645 |          1228 | 2017-10-25   | 2025-10-29 |            1228 | 00198      | 01425       |
| Power 535 |            99 | 2025-06-29   | 2025-10-29 |             198 | 00001      | 00246       |
| Keno      |           356 | 2022-12-04   | 2025-10-30 |           46418 | #0110271   | #0257703    |
| 3D        |           992 | 2019-04-22   | 2025-10-29 |             992 | 00001      | 00996       |
| 3D Pro    |           638 | 2021-09-14   | 2025-10-28 |             638 | 00001      | 00642       |
| Bingo18   |           332 | 2024-12-03   | 2025-10-30 |           51520 | 0083123    | 0135710     |

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
| 2025-10-28 00:00:00 | 01261 | [ 6  8 10 22 25 54  9] | 2025-10-29T00:00:48.613372 |
| 2025-10-25 00:00:00 | 01260 | [ 3  5 11 13 24 27 45] | 2025-10-26T00:00:45.744914 |
| 2025-10-23 00:00:00 | 01259 | [ 8 10 21 48 49 50 40] | 2025-10-24T18:00:52.094824 |
| 2025-10-21 00:00:00 | 01258 | [ 3 11 12 14 22 40 41] | 2025-10-21T21:48:33.658764 |
| 2025-10-18 00:00:00 | 01257 | [ 5 16 19 21 38 43 50] | 2025-10-21T21:48:33.658800 |
| 2025-10-16 00:00:00 | 01256 | [14 15 24 26 27 45 36] | 2025-10-17 21:15:55.017468 |
| 2025-10-14 00:00:00 | 01255 | [ 8  9 16 26 37 55 12] | 2025-10-17 21:15:55.017590 |
| 2025-10-11 00:00:00 | 01254 | [ 3  7 26 43 44 46 25] | 2025-10-17 21:15:55.017694 |
| 2025-10-09 00:00:00 | 01253 | [ 7 11 21 22 39 42 40] | 2025-10-17 21:15:55.017805 |
| 2025-10-07 00:00:00 | 01252 | [19 22 35 37 43 45 29] | 2025-10-17 21:15:55.017899 |

### 🎲 Number Frequency (All Time)
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.94 |       48 |     171 |      |       20 | 1.5  |         4 |      132 |      | 40.0     | 1.88 | 11        | 166      |
|       1 | 1.86 |       42 |     164 |      |       21 | 1.7  |        10 |      150 |      | 41.0     | 1.86 | 32        | 164      |
|       2 | 2.02 |        9 |     178 |      |       22 | 1.95 |         1 |      172 |      | 42.0     | 1.95 | 23        | 172      |
|       3 | 1.68 |       27 |     148 |      |       23 | 1.73 |        13 |      153 |      | 43.0     | 1.81 | 14        | 160      |
|       4 | 1.76 |       21 |     155 |      |       24 | 1.79 |        55 |      158 |      | 44.0     | 1.68 | 17        | 148      |
|       5 | 1.61 |       30 |     142 |      |       25 | 1.99 |        40 |      176 |      | 45.0     | 1.9  | 20        | 168      |
|       6 | 1.7  |       15 |     150 |      |       26 | 1.87 |        46 |      165 |      | 46.0     | 1.89 | 29        | 167      |
|       7 | 1.85 |       18 |     163 |      |       27 | 1.59 |        28 |      140 |      | 47.0     | 1.67 | 2         | 147      |
|       8 | 1.55 |        6 |     137 |      |       28 | 2.07 |        22 |      183 |      | 48.0     | 1.91 | 53        | 169      |
|       9 | 1.96 |        3 |     173 |      |       29 | 2.05 |        34 |      181 |      | 49.0     | 1.82 | 47        | 161      |
|      10 | 1.7  |       36 |     150 |      |       30 | 1.85 |        19 |      163 |      | 50.0     | 1.7  | 38        | 150      |
|      11 | 1.81 |       33 |     160 |      |       31 | 1.64 |        37 |      145 |      | 51.0     | 1.78 | 35        | 157      |
|      12 | 1.84 |       45 |     162 |      |       32 | 1.89 |        31 |      167 |      | 52.0     | 1.82 | 50        | 161      |
|      13 | 1.87 |       24 |     165 |      |       33 | 1.62 |        25 |      143 |      | 53.0     | 2.13 | 41        | 188      |
|      14 | 1.89 |       12 |     167 |      |       34 | 1.84 |        49 |      162 |      | 54.0     | 1.9  | 44        | 168      |
|      15 | 1.73 |       39 |     153 |      |       35 | 2.06 |        43 |      182 |      |          |      |           |          |
|      16 | 2.07 |       51 |     183 |      |       36 | 1.87 |        52 |      165 |      |          |      |           |          |
|      17 | 1.7  |       54 |     150 |      |       37 | 1.97 |         8 |      174 |      |          |      |           |          |
|      18 | 1.7  |       16 |     150 |      |       38 | 1.84 |         5 |      162 |      |          |      |           |          |
|      19 | 1.56 |        7 |     138 |      |       39 | 1.68 |        26 |      148 |      |          |      |           |          |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.1  |        1 |       1 |      |       20 |  3.3 |         7 |        3 |      | 40.0     | 1.1  | 23        | 1        |
|       1 | 5.49 |       22 |       5 |      |       21 |  2.2 |         9 |        2 |      | 41.0     | 1.1  | 48        | 1        |
|       2 | 1.1  |       15 |       1 |      |       22 |  2.2 |        16 |        2 |      | 42.0     | 2.2  | 25        | 2        |
|       3 | 4.4  |       43 |       4 |      |       23 |  2.2 |        36 |        2 |      | 43.0     | 2.2  | 12        | 2        |
|       4 | 1.1  |       54 |       1 |      |       24 |  1.1 |        49 |        1 |      | 44.0     | 3.3  | 21        | 3        |
|       5 | 1.1  |       34 |       1 |      |       25 |  4.4 |         8 |        4 |      | 45.0     | 1.1  | 13        | 1        |
|       6 | 3.3  |        3 |       3 |      |       26 |  1.1 |        29 |        1 |      |          |      |           |          |
|       7 | 2.2  |       19 |       2 |      |       27 |  2.2 |        46 |        2 |      |          |      |           |          |
|       8 | 2.2  |       10 |       2 |      |       28 |  1.1 |        17 |        1 |      |          |      |           |          |
|       9 | 1.1  |       20 |       1 |      |       29 |  1.1 |        41 |        1 |      |          |      |           |          |
|      10 | 2.2  |       35 |       2 |      |       30 |  3.3 |        26 |        3 |      |          |      |           |          |
|      11 | 3.3  |       45 |       3 |      |       31 |  1.1 |        33 |        1 |      |          |      |           |          |
|      12 | 1.1  |       52 |       1 |      |       32 |  1.1 |        55 |        1 |      |          |      |           |          |
|      13 | 2.2  |       50 |       2 |      |       33 |  2.2 |        14 |        2 |      |          |      |           |          |
|      14 | 3.3  |       11 |       3 |      |       34 |  2.2 |        38 |        2 |      |          |      |           |          |
|      15 | 2.2  |        5 |       2 |      |       35 |  2.2 |        39 |        2 |      |          |      |           |          |
|      16 | 2.2  |       37 |       2 |      |       36 |  1.1 |         6 |        1 |      |          |      |           |          |
|      17 | 3.3  |       27 |       3 |      |       37 |  1.1 |        44 |        1 |      |          |      |           |          |
|      18 | 2.2  |       42 |       2 |      |       38 |  1.1 |         2 |        1 |      |          |      |           |          |
|      19 | 3.3  |       24 |       3 |      |       39 |  4.4 |        40 |        4 |      |          |      |           |          |

#### Last 60 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 1.14 |       12 |       2 |      |       20 | 1.71 |        13 |        3 |      | 40.0     | 1.71 | 36        | 3        |
|       1 | 2.29 |        3 |       4 |      |       21 | 1.14 |        18 |        2 |      | 41.0     | 1.71 | 31        | 3        |
|       2 | 1.71 |       25 |       3 |      |       22 | 1.71 |         5 |        3 |      | 42.0     | 1.14 | 51        | 2        |
|       3 | 2.86 |       46 |       5 |      |       23 | 2.29 |         2 |        4 |      | 43.0     | 1.71 | 26        | 3        |
|       4 | 1.14 |       52 |       2 |      |       24 | 1.71 |        30 |        3 |      | 44.0     | 4.57 | 19        | 8        |
|       5 | 3.43 |       40 |       6 |      |       25 | 2.29 |         7 |        4 |      | 45.0     | 1.14 | 15        | 2        |
|       6 | 1.71 |       20 |       3 |      |       26 | 1.71 |        55 |        3 |      | 46.0     | 1.14 | 6         | 2        |
|       7 | 1.71 |       17 |       3 |      |       27 | 2.86 |        38 |        5 |      | 47.0     | 2.29 | 21        | 4        |
|       8 | 1.14 |       10 |       2 |      |       28 | 1.14 |        37 |        2 |      | 48.0     | 2.29 | 11        | 4        |
|       9 | 1.14 |        1 |       2 |      |       29 | 0.57 |        48 |        1 |      | 49.0     | 2.86 | 24        | 5        |
|      10 | 2.86 |       16 |       5 |      |       30 | 1.71 |        53 |        3 |      | 50.0     | 1.14 | 50        | 2        |
|      11 | 2.29 |       42 |       4 |      |       31 | 0.57 |        44 |        1 |      | 51.0     | 0.57 | 28        | 1        |
|      12 | 4    |       22 |       7 |      |       32 | 2.86 |         9 |        5 |      |          |      |           |          |
|      13 | 0.57 |       54 |       1 |      |       33 | 5.14 |         8 |        9 |      |          |      |           |          |
|      14 | 1.71 |       14 |       3 |      |       34 | 1.14 |        41 |        2 |      |          |      |           |          |
|      15 | 2.86 |       27 |       5 |      |       35 | 1.14 |        23 |        2 |      |          |      |           |          |
|      16 | 1.71 |       49 |       3 |      |       36 | 2.29 |        45 |        4 |      |          |      |           |          |
|      17 | 1.14 |       35 |       2 |      |       37 | 1.71 |        34 |        3 |      |          |      |           |          |
|      18 | 4.57 |       43 |       8 |      |       38 | 1.14 |        33 |        2 |      |          |      |           |          |
|      19 | 2.29 |       39 |       4 |      |       39 | 0.57 |        29 |        1 |      |          |      |           |          |

#### Last 90 Days
|   index |    % |   result |   count | 1-   |   1index |   1% |   1result |   1count | 2-   | 2index   | 2%   | 2result   | 2count   |
|--------:|-----:|---------:|--------:|:-----|---------:|-----:|----------:|---------:|:-----|:---------|:-----|:----------|:---------|
|       0 | 3.01 |       22 |       8 |      |       20 | 1.13 |        37 |        3 |      | 40.0     | 1.13 | 32        | 3        |
|       1 | 1.88 |        1 |       5 |      |       21 | 1.5  |        50 |        4 |      | 41.0     | 2.26 | 30        | 6        |
|       2 | 0.75 |       15 |       2 |      |       22 | 1.88 |         2 |        5 |      | 42.0     | 1.88 | 27        | 5        |
|       3 | 1.5  |       10 |       4 |      |       23 | 1.5  |        11 |        4 |      | 43.0     | 2.63 | 34        | 7        |
|       4 | 1.13 |       49 |       3 |      |       24 | 1.5  |         3 |        4 |      | 44.0     | 1.13 | 20        | 3        |
|       5 | 1.88 |       39 |       5 |      |       25 | 1.88 |        44 |        5 |      | 45.0     | 1.5  | 7         | 4        |
|       6 | 1.5  |       41 |       4 |      |       26 | 1.5  |        42 |        4 |      | 46.0     | 2.26 | 45        | 6        |
|       7 | 1.88 |       46 |       5 |      |       27 | 1.13 |        12 |        3 |      | 47.0     | 1.13 | 23        | 3        |
|       8 | 2.26 |       17 |       6 |      |       28 | 3.38 |        43 |        9 |      | 48.0     | 3.01 | 40        | 8        |
|       9 | 1.88 |       14 |       5 |      |       29 | 0.38 |        54 |        1 |      | 49.0     | 0.75 | 29        | 2        |
|      10 | 2.26 |       38 |       6 |      |       30 | 1.5  |        26 |        4 |      | 50.0     | 1.5  | 51        | 4        |
|      11 | 2.26 |       52 |       6 |      |       31 | 2.26 |        35 |        6 |      | 51.0     | 1.88 | 55        | 5        |
|      12 | 1.13 |       25 |       3 |      |       32 | 2.26 |        36 |        6 |      | 52.0     | 1.13 | 18        | 3        |
|      13 | 2.26 |       31 |       6 |      |       33 | 1.13 |        33 |        3 |      | 53.0     | 1.5  | 13        | 4        |
|      14 | 2.26 |       16 |       6 |      |       34 | 0.75 |        28 |        2 |      |          |      |           |          |
|      15 | 3.76 |       19 |      10 |      |       35 | 1.5  |        21 |        4 |      |          |      |           |          |
|      16 | 3.01 |        9 |       8 |      |       36 | 3.76 |         8 |       10 |      |          |      |           |          |
|      17 | 1.88 |       53 |       5 |      |       37 | 1.13 |        47 |        3 |      |          |      |           |          |
|      18 | 2.26 |        6 |       6 |      |       38 | 2.63 |         5 |        7 |      |          |      |           |          |
|      19 | 1.5  |       48 |       4 |      |       39 | 3.38 |        24 |        9 |      |          |      |           |          |



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
#   --run-date TEXT       Specific date to crawl
#   --index_from INTEGER  Starting page index
#   --index_to INTEGER    Ending page index
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process
#   --help          Show help message
```

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

