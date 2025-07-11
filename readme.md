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
| Power 655 |          1213 | 2017-08-01   | 2025-07-08 |            1213 | 00001      | 01213       |
| Power 645 |          1180 | 2017-10-25   | 2025-07-09 |            1180 | 00198      | 01377       |
| Power 535 |            10 | 2025-06-29   | 2025-07-08 |              19 | 00001      | 00019       |
| Keno      |           946 | 2022-12-04   | 2025-07-10 |          133523 | #0110271   | #0244420    |
| 3D        |           948 | 2019-04-22   | 2025-07-09 |             948 | 00001      | 00948       |
| 3D Pro    |           594 | 2021-09-14   | 2025-07-08 |             594 | 00001      | 00594       |
| Bingo18   |           220 | 2024-12-03   | 2025-07-10 |           34800 | 0083123    | 0117962     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                     | predicted               |
|:-----------|:---------------------------|:------------------------|
| 2020-06-27 | [2, 6, 38, 47, 50, 53, 14] | [50, 53, 14, 54, 47, 2] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-07-08 | 01213 | [23, 24, 32, 42, 48, 50, 31] |      0 | 2025-07-09 00:01:24.568129 |
| 2025-07-05 | 01212 | [3, 15, 22, 45, 51, 55, 54]  |      0 | 2025-07-06 00:01:25.986584 |
| 2025-07-03 | 01211 | [18, 19, 29, 31, 45, 54, 27] |      0 | 2025-07-04 00:01:20.834544 |
| 2025-07-01 | 01210 | [3, 11, 12, 14, 27, 33, 15]  |      0 | 2025-07-02 00:01:16.154567 |
| 2025-06-28 | 01209 | [8, 11, 13, 20, 45, 50, 25]  |      0 | 2025-06-30 15:30:00.150910 |
| 2025-06-26 | 01208 | [1, 14, 16, 27, 40, 51, 2]   |      0 | 2025-06-30 15:30:00.151037 |
| 2025-06-24 | 01207 | [3, 9, 18, 20, 30, 53, 48]   |      0 | 2025-06-30 15:30:00.151131 |
| 2025-06-21 | 01206 | [6, 10, 15, 43, 44, 53, 32]  |      0 | 2025-06-22 19:00:16.907461 |
| 2025-06-19 | 01205 | [3, 5, 9, 10, 16, 47, 34]    |      0 | 2025-06-19 19:00:12.105342 |
| 2025-06-17 | 01204 | [7, 13, 18, 22, 32, 44, 43]  |      0 | 2025-06-17 19:00:14.248629 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.97 |     |       21 |     151 | 1.78 |     | 41       | 183     | 2.16 |
|        2 |     141 | 1.66 |     |       22 |     174 | 2.05 |     | 42       | 158     | 1.86 |
|        3 |     168 | 1.98 |     |       23 |     168 | 1.98 |     | 43       | 172     | 2.03 |
|        4 |     131 | 1.54 |     |       24 |     155 | 1.83 |     | 44       | 160     | 1.88 |
|        5 |     152 | 1.79 |     |       25 |     140 | 1.65 |     | 45       | 153     | 1.8  |
|        6 |     131 | 1.54 |     |       26 |     142 | 1.67 |     | 46       | 159     | 1.87 |
|        7 |     134 | 1.58 |     |       27 |     143 | 1.68 |     | 47       | 158     | 1.86 |
|        8 |     162 | 1.91 |     |       28 |     135 | 1.59 |     | 48       | 164     | 1.93 |
|        9 |     168 | 1.98 |     |       29 |     163 | 1.92 |     | 49       | 158     | 1.86 |
|       10 |     144 | 1.7  |     |       30 |     134 | 1.58 |     | 50       | 157     | 1.85 |
|       11 |     162 | 1.91 |     |       31 |     159 | 1.87 |     | 51       | 177     | 2.08 |
|       12 |     163 | 1.92 |     |       32 |     160 | 1.88 |     | 52       | 158     | 1.86 |
|       13 |     148 | 1.74 |     |       33 |     153 | 1.8  |     | 53       | 162     | 1.91 |
|       14 |     155 | 1.83 |     |       34 |     170 | 2    |     | 54       | 147     | 1.73 |
|       15 |     147 | 1.73 |     |       35 |     151 | 1.78 |     | 55       | 153     | 1.8  |
|       16 |     144 | 1.7  |     |       36 |     142 | 1.67 |     |          |         |      |
|       17 |     141 | 1.66 |     |       37 |     141 | 1.66 |     |          |         |      |
|       18 |     158 | 1.86 |     |       38 |     144 | 1.7  |     |          |         |      |
|       19 |     153 | 1.8  |     |       39 |     146 | 1.72 |     |          |         |      |
|       20 |     164 | 1.93 |     |       40 |     167 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1  |     |       22 |       3 | 3.3 |     | 48       | 2       | 2.2 |
|        2 |       1 | 1.1  |     |       23 |       1 | 1.1 |     | 50       | 2       | 2.2 |
|        3 |       5 | 5.49 |     |       24 |       2 | 2.2 |     | 51       | 2       | 2.2 |
|        5 |       1 | 1.1  |     |       25 |       1 | 1.1 |     | 53       | 2       | 2.2 |
|        6 |       3 | 3.3  |     |       26 |       1 | 1.1 |     | 54       | 2       | 2.2 |
|        7 |       1 | 1.1  |     |       27 |       3 | 3.3 |     | 55       | 1       | 1.1 |
|        8 |       2 | 2.2  |     |       29 |       2 | 2.2 |     |          |         |     |
|        9 |       2 | 2.2  |     |       30 |       1 | 1.1 |     |          |         |     |
|       10 |       2 | 2.2  |     |       31 |       2 | 2.2 |     |          |         |     |
|       11 |       3 | 3.3  |     |       32 |       3 | 3.3 |     |          |         |     |
|       12 |       2 | 2.2  |     |       33 |       1 | 1.1 |     |          |         |     |
|       13 |       2 | 2.2  |     |       34 |       2 | 2.2 |     |          |         |     |
|       14 |       2 | 2.2  |     |       37 |       1 | 1.1 |     |          |         |     |
|       15 |       3 | 3.3  |     |       40 |       2 | 2.2 |     |          |         |     |
|       16 |       3 | 3.3  |     |       41 |       2 | 2.2 |     |          |         |     |
|       17 |       1 | 1.1  |     |       42 |       1 | 1.1 |     |          |         |     |
|       18 |       4 | 4.4  |     |       43 |       2 | 2.2 |     |          |         |     |
|       19 |       1 | 1.1  |     |       44 |       3 | 3.3 |     |          |         |     |
|       20 |       2 | 2.2  |     |       45 |       3 | 3.3 |     |          |         |     |
|       21 |       1 | 1.1  |     |       47 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.57 |     |       21 |       3 | 1.71 |     | 44       | 6       | 3.43 |
|        2 |       3 | 1.71 |     |       22 |       4 | 2.29 |     | 45       | 8       | 4.57 |
|        3 |       7 | 4    |     |       23 |       1 | 0.57 |     | 46       | 3       | 1.71 |
|        4 |       1 | 0.57 |     |       24 |       4 | 2.29 |     | 47       | 5       | 2.86 |
|        5 |       1 | 0.57 |     |       25 |       1 | 0.57 |     | 48       | 4       | 2.29 |
|        6 |       5 | 2.86 |     |       26 |       2 | 1.14 |     | 49       | 3       | 1.71 |
|        7 |       3 | 1.71 |     |       27 |       6 | 3.43 |     | 50       | 4       | 2.29 |
|        8 |       3 | 1.71 |     |       29 |       3 | 1.71 |     | 51       | 3       | 1.71 |
|        9 |       5 | 2.86 |     |       30 |       2 | 1.14 |     | 52       | 2       | 1.14 |
|       10 |       2 | 1.14 |     |       31 |       2 | 1.14 |     | 53       | 2       | 1.14 |
|       11 |       4 | 2.29 |     |       32 |       3 | 1.71 |     | 54       | 4       | 2.29 |
|       12 |       4 | 2.29 |     |       33 |       2 | 1.14 |     | 55       | 5       | 2.86 |
|       13 |       3 | 1.71 |     |       34 |       3 | 1.71 |     |          |         |      |
|       14 |       6 | 3.43 |     |       37 |       3 | 1.71 |     |          |         |      |
|       15 |       5 | 2.86 |     |       38 |       1 | 0.57 |     |          |         |      |
|       16 |       4 | 2.29 |     |       39 |       1 | 0.57 |     |          |         |      |
|       17 |       2 | 1.14 |     |       40 |       2 | 1.14 |     |          |         |      |
|       18 |       5 | 2.86 |     |       41 |       5 | 2.86 |     |          |         |      |
|       19 |       4 | 2.29 |     |       42 |       4 | 2.29 |     |          |         |      |
|       20 |       3 | 1.71 |     |       43 |       3 | 1.71 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.13 |     |       21 |       6 | 2.26 |     | 43       | 5       | 1.88 |
|        2 |       4 | 1.5  |     |       22 |       4 | 1.5  |     | 44       | 6       | 2.26 |
|        3 |      10 | 3.76 |     |       23 |       4 | 1.5  |     | 45       | 9       | 3.38 |
|        4 |       1 | 0.38 |     |       24 |       6 | 2.26 |     | 46       | 3       | 1.13 |
|        5 |       3 | 1.13 |     |       25 |       3 | 1.13 |     | 47       | 7       | 2.63 |
|        6 |       5 | 1.88 |     |       26 |       3 | 1.13 |     | 48       | 6       | 2.26 |
|        7 |       4 | 1.5  |     |       27 |       7 | 2.63 |     | 49       | 5       | 1.88 |
|        8 |       5 | 1.88 |     |       28 |       3 | 1.13 |     | 50       | 6       | 2.26 |
|        9 |       5 | 1.88 |     |       29 |       5 | 1.88 |     | 51       | 4       | 1.5  |
|       10 |       3 | 1.13 |     |       30 |       3 | 1.13 |     | 52       | 4       | 1.5  |
|       11 |       5 | 1.88 |     |       31 |       3 | 1.13 |     | 53       | 2       | 0.75 |
|       12 |       5 | 1.88 |     |       32 |       5 | 1.88 |     | 54       | 4       | 1.5  |
|       13 |       3 | 1.13 |     |       33 |       3 | 1.13 |     | 55       | 6       | 2.26 |
|       14 |      10 | 3.76 |     |       34 |       4 | 1.5  |     |          |         |      |
|       15 |      11 | 4.14 |     |       37 |       6 | 2.26 |     |          |         |      |
|       16 |       7 | 2.63 |     |       38 |       3 | 1.13 |     |          |         |      |
|       17 |       4 | 1.5  |     |       39 |       4 | 1.5  |     |          |         |      |
|       18 |       6 | 2.26 |     |       40 |       4 | 1.5  |     |          |         |      |
|       19 |       8 | 3.01 |     |       41 |       8 | 3.01 |     |          |         |      |
|       20 |       5 | 1.88 |     |       42 |       8 | 3.01 |     |          |         |      |



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

