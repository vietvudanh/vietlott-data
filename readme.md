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

| Product   |   Total Draws | Start Date   | End Date   |   Total Records |   First ID |   Latest ID |
|:----------|--------------:|:-------------|:-----------|----------------:|-----------:|------------:|
| Power 655 |          1222 | 2017-08-01   | 2025-07-29 |            1222 |      00001 |       01222 |
| Power 645 |          1188 | 2017-10-25   | 2025-07-27 |            1188 |      00198 |       01385 |
| Power 535 |            10 | 2025-06-29   | 2025-07-08 |              19 |      00001 |       00019 |
| 3D        |           956 | 2019-04-22   | 2025-07-28 |             956 |      00001 |       00956 |
| 3D Pro    |           603 | 2021-09-14   | 2025-07-29 |             603 |      00001 |       00603 |
| Bingo18   |           240 | 2024-12-03   | 2025-07-30 |           37912 |    0083123 |     0121082 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2021-07-13 | [5, 11, 18, 27, 34, 43, 42] | [47, 11, 27, 34, 42, 5] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-07-29 | 01222 | [4, 8, 23, 43, 45, 51, 48]   |      0 | 2025-07-30 00:00:36.365372 |
| 2025-07-26 | 01221 | [5, 26, 28, 29, 33, 54, 34]  |      0 | 2025-07-27 00:00:32.385732 |
| 2025-07-24 | 01220 | [5, 10, 24, 29, 30, 34, 45]  |      0 | 2025-07-25 12:00:38.542614 |
| 2025-07-22 | 01219 | [9, 10, 15, 28, 33, 44, 22]  |      0 | 2025-07-23 00:01:21.445784 |
| 2025-07-19 | 01218 | [8, 9, 20, 36, 39, 44, 28]   |      0 | 2025-07-20 00:01:20.503953 |
| 2025-07-17 | 01217 | [13, 18, 33, 40, 48, 53, 54] |      0 | 2025-07-18 00:01:24.912307 |
| 2025-07-15 | 01216 | [18, 26, 31, 32, 36, 48, 30] |      0 | 2025-07-16 00:01:25.441672 |
| 2025-07-12 | 01215 | [2, 34, 39, 41, 45, 52, 51]  |      0 | 2025-07-14 18:47:06.725228 |
| 2025-07-10 | 01214 | [12, 33, 34, 42, 44, 53, 3]  |      0 | 2025-07-14 18:47:06.726125 |
| 2025-07-08 | 01213 | [23, 24, 32, 42, 48, 50, 31] |      0 | 2025-07-09 00:01:24.568129 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.95 |     |       21 |     151 | 1.77 |     | 41       | 184     | 2.15 |
|        2 |     142 | 1.66 |     |       22 |     175 | 2.05 |     | 42       | 159     | 1.86 |
|        3 |     169 | 1.98 |     |       23 |     169 | 1.98 |     | 43       | 173     | 2.02 |
|        4 |     132 | 1.54 |     |       24 |     156 | 1.82 |     | 44       | 163     | 1.91 |
|        5 |     154 | 1.8  |     |       25 |     140 | 1.64 |     | 45       | 156     | 1.82 |
|        6 |     131 | 1.53 |     |       26 |     144 | 1.68 |     | 46       | 159     | 1.86 |
|        7 |     134 | 1.57 |     |       27 |     143 | 1.67 |     | 47       | 158     | 1.85 |
|        8 |     164 | 1.92 |     |       28 |     138 | 1.61 |     | 48       | 167     | 1.95 |
|        9 |     170 | 1.99 |     |       29 |     165 | 1.93 |     | 49       | 158     | 1.85 |
|       10 |     146 | 1.71 |     |       30 |     136 | 1.59 |     | 50       | 157     | 1.84 |
|       11 |     162 | 1.89 |     |       31 |     160 | 1.87 |     | 51       | 179     | 2.09 |
|       12 |     164 | 1.92 |     |       32 |     161 | 1.88 |     | 52       | 159     | 1.86 |
|       13 |     149 | 1.74 |     |       33 |     157 | 1.84 |     | 53       | 164     | 1.92 |
|       14 |     155 | 1.81 |     |       34 |     174 | 2.03 |     | 54       | 149     | 1.74 |
|       15 |     148 | 1.73 |     |       35 |     151 | 1.77 |     | 55       | 153     | 1.79 |
|       16 |     144 | 1.68 |     |       36 |     144 | 1.68 |     |          |         |      |
|       17 |     141 | 1.65 |     |       37 |     141 | 1.65 |     |          |         |      |
|       18 |     160 | 1.87 |     |       38 |     144 | 1.68 |     |          |         |      |
|       19 |     153 | 1.79 |     |       39 |     148 | 1.73 |     |          |         |      |
|       20 |     165 | 1.93 |     |       40 |     168 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.1 |     |       28 |       3 | 3.3  |     | 54       | 4       | 4.4 |
|        3 |       3 | 3.3 |     |       29 |       3 | 3.3  |     | 55       | 1       | 1.1 |
|        4 |       1 | 1.1 |     |       30 |       2 | 2.2  |     |          |         |     |
|        5 |       2 | 2.2 |     |       31 |       3 | 3.3  |     |          |         |     |
|        8 |       2 | 2.2 |     |       32 |       2 | 2.2  |     |          |         |     |
|        9 |       2 | 2.2 |     |       33 |       5 | 5.49 |     |          |         |     |
|       10 |       2 | 2.2 |     |       34 |       4 | 4.4  |     |          |         |     |
|       11 |       1 | 1.1 |     |       36 |       2 | 2.2  |     |          |         |     |
|       12 |       2 | 2.2 |     |       39 |       2 | 2.2  |     |          |         |     |
|       13 |       1 | 1.1 |     |       40 |       1 | 1.1  |     |          |         |     |
|       14 |       1 | 1.1 |     |       41 |       1 | 1.1  |     |          |         |     |
|       15 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       18 |       3 | 3.3 |     |       43 |       1 | 1.1  |     |          |         |     |
|       19 |       1 | 1.1 |     |       44 |       3 | 3.3  |     |          |         |     |
|       20 |       1 | 1.1 |     |       45 |       5 | 5.49 |     |          |         |     |
|       22 |       2 | 2.2 |     |       48 |       4 | 4.4  |     |          |         |     |
|       23 |       2 | 2.2 |     |       50 |       1 | 1.1  |     |          |         |     |
|       24 |       2 | 2.2 |     |       51 |       3 | 3.3  |     |          |         |     |
|       26 |       2 | 2.2 |     |       52 |       1 | 1.1  |     |          |         |     |
|       27 |       2 | 2.2 |     |       53 |       2 | 2.2  |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.55 |     |       21 |       3 | 1.65 |     | 42       | 2       | 1.1  |
|        2 |       3 | 1.65 |     |       22 |       4 | 2.2  |     | 43       | 3       | 1.65 |
|        3 |       6 | 3.3  |     |       23 |       2 | 1.1  |     | 44       | 6       | 3.3  |
|        4 |       1 | 0.55 |     |       24 |       4 | 2.2  |     | 45       | 8       | 4.4  |
|        5 |       3 | 1.65 |     |       25 |       1 | 0.55 |     | 46       | 2       | 1.1  |
|        6 |       4 | 2.2  |     |       26 |       3 | 1.65 |     | 47       | 2       | 1.1  |
|        7 |       1 | 0.55 |     |       27 |       4 | 2.2  |     | 48       | 6       | 3.3  |
|        8 |       5 | 2.75 |     |       28 |       3 | 1.65 |     | 49       | 2       | 1.1  |
|        9 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 50       | 2       | 1.1  |
|       10 |       4 | 2.2  |     |       30 |       3 | 1.65 |     | 51       | 5       | 2.75 |
|       11 |       4 | 2.2  |     |       31 |       3 | 1.65 |     | 52       | 2       | 1.1  |
|       12 |       4 | 2.2  |     |       32 |       4 | 2.2  |     | 53       | 4       | 2.2  |
|       13 |       3 | 1.65 |     |       33 |       6 | 3.3  |     | 54       | 4       | 2.2  |
|       14 |       4 | 2.2  |     |       34 |       7 | 3.85 |     | 55       | 2       | 1.1  |
|       15 |       4 | 2.2  |     |       36 |       2 | 1.1  |     |          |         |      |
|       16 |       4 | 2.2  |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       2 | 1.1  |     |       38 |       1 | 0.55 |     |          |         |      |
|       18 |       6 | 3.3  |     |       39 |       2 | 1.1  |     |          |         |      |
|       19 |       1 | 0.55 |     |       40 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       41 |       4 | 2.2  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.37 |     |       21 |       5 | 1.83 |     | 42       | 6       | 2.2  |
|        2 |       4 | 1.47 |     |       22 |       5 | 1.83 |     | 43       | 5       | 1.83 |
|        3 |       9 | 3.3  |     |       23 |       2 | 0.73 |     | 44       | 9       | 3.3  |
|        4 |       2 | 0.73 |     |       24 |       5 | 1.83 |     | 45       | 12      | 4.4  |
|        5 |       4 | 1.47 |     |       25 |       2 | 0.73 |     | 46       | 3       | 1.1  |
|        6 |       5 | 1.83 |     |       26 |       5 | 1.83 |     | 47       | 6       | 2.2  |
|        7 |       4 | 1.47 |     |       27 |       6 | 2.2  |     | 48       | 7       | 2.56 |
|        8 |       6 | 2.2  |     |       28 |       5 | 1.83 |     | 49       | 3       | 1.1  |
|        9 |       7 | 2.56 |     |       29 |       6 | 2.2  |     | 50       | 6       | 2.2  |
|       10 |       4 | 1.47 |     |       30 |       5 | 1.83 |     | 51       | 6       | 2.2  |
|       11 |       4 | 1.47 |     |       31 |       3 | 1.1  |     | 52       | 3       | 1.1  |
|       12 |       6 | 2.2  |     |       32 |       4 | 1.47 |     | 53       | 4       | 1.47 |
|       13 |       4 | 1.47 |     |       33 |       6 | 2.2  |     | 54       | 6       | 2.2  |
|       14 |       7 | 2.56 |     |       34 |       8 | 2.93 |     | 55       | 5       | 1.83 |
|       15 |       8 | 2.93 |     |       36 |       2 | 0.73 |     |          |         |      |
|       16 |       6 | 2.2  |     |       37 |       4 | 1.47 |     |          |         |      |
|       17 |       3 | 1.1  |     |       38 |       2 | 0.73 |     |          |         |      |
|       18 |       7 | 2.56 |     |       39 |       5 | 1.83 |     |          |         |      |
|       19 |       7 | 2.56 |     |       40 |       3 | 1.1  |     |          |         |      |
|       20 |       4 | 1.47 |     |       41 |       7 | 2.56 |     |          |         |      |



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

