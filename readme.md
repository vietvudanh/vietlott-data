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
| Power 655 |          1215 | 2017-08-01   | 2025-07-12 |            1215 | 00001      | 01215       |
| Power 645 |          1182 | 2017-10-25   | 2025-07-13 |            1182 | 00198      | 01379       |
| Power 535 |            10 | 2025-06-29   | 2025-07-08 |              19 | 00001      | 00019       |
| Keno      |           952 | 2022-12-04   | 2025-07-14 |          134267 | #0110271   | #0244902    |
| 3D        |           950 | 2019-04-22   | 2025-07-14 |             950 | 00001      | 00950       |
| 3D Pro    |           596 | 2021-09-14   | 2025-07-12 |             596 | 00001      | 00596       |
| Bingo18   |           221 | 2024-12-03   | 2025-07-14 |           34852 | 0083123    | 0118605     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2021-07-15 | [3, 4, 12, 16, 30, 50, 20]  | [16, 12, 20, 53, 4, 50] |
| 2019-02-14 | [8, 15, 26, 41, 43, 53, 46] | [15, 43, 49, 41, 26, 8] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-07-12 | 01215 | [2, 34, 39, 41, 45, 52, 51]  |      0 | 2025-07-14 18:47:06.725228 |
| 2025-07-10 | 01214 | [12, 33, 34, 42, 44, 53, 3]  |      0 | 2025-07-14 18:47:06.726125 |
| 2025-07-08 | 01213 | [23, 24, 32, 42, 48, 50, 31] |      0 | 2025-07-09 00:01:24.568129 |
| 2025-07-05 | 01212 | [3, 15, 22, 45, 51, 55, 54]  |      0 | 2025-07-06 00:01:25.986584 |
| 2025-07-03 | 01211 | [18, 19, 29, 31, 45, 54, 27] |      0 | 2025-07-04 00:01:20.834544 |
| 2025-07-01 | 01210 | [3, 11, 12, 14, 27, 33, 15]  |      0 | 2025-07-02 00:01:16.154567 |
| 2025-06-28 | 01209 | [8, 11, 13, 20, 45, 50, 25]  |      0 | 2025-06-30 15:30:00.150910 |
| 2025-06-26 | 01208 | [1, 14, 16, 27, 40, 51, 2]   |      0 | 2025-06-30 15:30:00.151037 |
| 2025-06-24 | 01207 | [3, 9, 18, 20, 30, 53, 48]   |      0 | 2025-06-30 15:30:00.151131 |
| 2025-06-21 | 01206 | [6, 10, 15, 43, 44, 53, 32]  |      0 | 2025-06-22 19:00:16.907461 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.96 |     |       21 |     151 | 1.78 |     | 41       | 184     | 2.16 |
|        2 |     142 | 1.67 |     |       22 |     174 | 2.05 |     | 42       | 159     | 1.87 |
|        3 |     169 | 1.99 |     |       23 |     168 | 1.98 |     | 43       | 172     | 2.02 |
|        4 |     131 | 1.54 |     |       24 |     155 | 1.82 |     | 44       | 161     | 1.89 |
|        5 |     152 | 1.79 |     |       25 |     140 | 1.65 |     | 45       | 154     | 1.81 |
|        6 |     131 | 1.54 |     |       26 |     142 | 1.67 |     | 46       | 159     | 1.87 |
|        7 |     134 | 1.58 |     |       27 |     143 | 1.68 |     | 47       | 158     | 1.86 |
|        8 |     162 | 1.9  |     |       28 |     135 | 1.59 |     | 48       | 164     | 1.93 |
|        9 |     168 | 1.98 |     |       29 |     163 | 1.92 |     | 49       | 158     | 1.86 |
|       10 |     144 | 1.69 |     |       30 |     134 | 1.58 |     | 50       | 157     | 1.85 |
|       11 |     162 | 1.9  |     |       31 |     159 | 1.87 |     | 51       | 178     | 2.09 |
|       12 |     164 | 1.93 |     |       32 |     160 | 1.88 |     | 52       | 159     | 1.87 |
|       13 |     148 | 1.74 |     |       33 |     154 | 1.81 |     | 53       | 163     | 1.92 |
|       14 |     155 | 1.82 |     |       34 |     172 | 2.02 |     | 54       | 147     | 1.73 |
|       15 |     147 | 1.73 |     |       35 |     151 | 1.78 |     | 55       | 153     | 1.8  |
|       16 |     144 | 1.69 |     |       36 |     142 | 1.67 |     |          |         |      |
|       17 |     141 | 1.66 |     |       37 |     141 | 1.66 |     |          |         |      |
|       18 |     158 | 1.86 |     |       38 |     144 | 1.69 |     |          |         |      |
|       19 |     153 | 1.8  |     |       39 |     147 | 1.73 |     |          |         |      |
|       20 |     164 | 1.93 |     |       40 |     167 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1  |     |       24 |       2 | 2.2 |     | 51       | 3       | 3.3 |
|        2 |       2 | 2.2  |     |       25 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        3 |       5 | 5.49 |     |       26 |       1 | 1.1 |     | 53       | 3       | 3.3 |
|        5 |       1 | 1.1  |     |       27 |       3 | 3.3 |     | 54       | 2       | 2.2 |
|        6 |       1 | 1.1  |     |       29 |       1 | 1.1 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1  |     |       30 |       1 | 1.1 |     |          |         |     |
|        8 |       1 | 1.1  |     |       31 |       2 | 2.2 |     |          |         |     |
|        9 |       2 | 2.2  |     |       32 |       3 | 3.3 |     |          |         |     |
|       10 |       2 | 2.2  |     |       33 |       2 | 2.2 |     |          |         |     |
|       11 |       3 | 3.3  |     |       34 |       3 | 3.3 |     |          |         |     |
|       12 |       3 | 3.3  |     |       39 |       1 | 1.1 |     |          |         |     |
|       13 |       2 | 2.2  |     |       40 |       1 | 1.1 |     |          |         |     |
|       14 |       2 | 2.2  |     |       41 |       2 | 2.2 |     |          |         |     |
|       15 |       3 | 3.3  |     |       42 |       2 | 2.2 |     |          |         |     |
|       16 |       2 | 2.2  |     |       43 |       2 | 2.2 |     |          |         |     |
|       18 |       3 | 3.3  |     |       44 |       3 | 3.3 |     |          |         |     |
|       19 |       1 | 1.1  |     |       45 |       4 | 4.4 |     |          |         |     |
|       20 |       2 | 2.2  |     |       47 |       2 | 2.2 |     |          |         |     |
|       22 |       3 | 3.3  |     |       48 |       2 | 2.2 |     |          |         |     |
|       23 |       1 | 1.1  |     |       50 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.55 |     |       21 |       3 | 1.65 |     | 44       | 7       | 3.85 |
|        2 |       4 | 2.2  |     |       22 |       4 | 2.2  |     | 45       | 9       | 4.95 |
|        3 |       7 | 3.85 |     |       23 |       1 | 0.55 |     | 46       | 3       | 1.65 |
|        4 |       1 | 0.55 |     |       24 |       3 | 1.65 |     | 47       | 5       | 2.75 |
|        5 |       1 | 0.55 |     |       25 |       1 | 0.55 |     | 48       | 4       | 2.2  |
|        6 |       5 | 2.75 |     |       26 |       2 | 1.1  |     | 49       | 3       | 1.65 |
|        7 |       2 | 1.1  |     |       27 |       6 | 3.3  |     | 50       | 4       | 2.2  |
|        8 |       3 | 1.65 |     |       29 |       3 | 1.65 |     | 51       | 4       | 2.2  |
|        9 |       5 | 2.75 |     |       30 |       2 | 1.1  |     | 52       | 3       | 1.65 |
|       10 |       2 | 1.1  |     |       31 |       2 | 1.1  |     | 53       | 3       | 1.65 |
|       11 |       4 | 2.2  |     |       32 |       3 | 1.65 |     | 54       | 3       | 1.65 |
|       12 |       5 | 2.75 |     |       33 |       3 | 1.65 |     | 55       | 4       | 2.2  |
|       13 |       3 | 1.65 |     |       34 |       5 | 2.75 |     |          |         |      |
|       14 |       6 | 3.3  |     |       37 |       3 | 1.65 |     |          |         |      |
|       15 |       5 | 2.75 |     |       38 |       1 | 0.55 |     |          |         |      |
|       16 |       4 | 2.2  |     |       39 |       1 | 0.55 |     |          |         |      |
|       17 |       2 | 1.1  |     |       40 |       2 | 1.1  |     |          |         |      |
|       18 |       5 | 2.75 |     |       41 |       6 | 3.3  |     |          |         |      |
|       19 |       4 | 2.2  |     |       42 |       4 | 2.2  |     |          |         |      |
|       20 |       3 | 1.65 |     |       43 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       6 | 2.2  |     | 43       | 5       | 1.83 |
|        2 |       5 | 1.83 |     |       22 |       4 | 1.47 |     | 44       | 7       | 2.56 |
|        3 |      10 | 3.66 |     |       23 |       3 | 1.1  |     | 45       | 10      | 3.66 |
|        4 |       1 | 0.37 |     |       24 |       6 | 2.2  |     | 46       | 3       | 1.1  |
|        5 |       3 | 1.1  |     |       25 |       3 | 1.1  |     | 47       | 7       | 2.56 |
|        6 |       5 | 1.83 |     |       26 |       3 | 1.1  |     | 48       | 6       | 2.2  |
|        7 |       4 | 1.47 |     |       27 |       7 | 2.56 |     | 49       | 5       | 1.83 |
|        8 |       5 | 1.83 |     |       28 |       3 | 1.1  |     | 50       | 6       | 2.2  |
|        9 |       5 | 1.83 |     |       29 |       5 | 1.83 |     | 51       | 5       | 1.83 |
|       10 |       3 | 1.1  |     |       30 |       3 | 1.1  |     | 52       | 5       | 1.83 |
|       11 |       5 | 1.83 |     |       31 |       3 | 1.1  |     | 53       | 3       | 1.1  |
|       12 |       6 | 2.2  |     |       32 |       5 | 1.83 |     | 54       | 4       | 1.47 |
|       13 |       3 | 1.1  |     |       33 |       4 | 1.47 |     | 55       | 5       | 1.83 |
|       14 |       9 | 3.3  |     |       34 |       6 | 2.2  |     |          |         |      |
|       15 |      11 | 4.03 |     |       37 |       5 | 1.83 |     |          |         |      |
|       16 |       7 | 2.56 |     |       38 |       3 | 1.1  |     |          |         |      |
|       17 |       4 | 1.47 |     |       39 |       5 | 1.83 |     |          |         |      |
|       18 |       6 | 2.2  |     |       40 |       4 | 1.47 |     |          |         |      |
|       19 |       7 | 2.56 |     |       41 |       9 | 3.3  |     |          |         |      |
|       20 |       5 | 1.83 |     |       42 |       8 | 2.93 |     |          |         |      |



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

