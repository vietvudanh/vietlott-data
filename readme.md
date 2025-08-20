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
| Power 655 |          1231 | 2017-08-01   | 2025-08-19 |            1231 |      00001 |       01231 |
| Power 645 |          1197 | 2017-10-25   | 2025-08-17 |            1197 |      00198 |       01394 |
| Power 535 |            53 | 2025-06-29   | 2025-08-20 |             105 |      00001 |       00105 |
| 3D        |           965 | 2019-04-22   | 2025-08-18 |             965 |      00001 |       00965 |
| 3D Pro    |           612 | 2021-09-14   | 2025-08-19 |             612 |      00001 |       00612 |
| Bingo18   |           243 | 2024-12-03   | 2025-08-20 |           38323 |    0083123 |     0124461 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2023-05-30 | [1, 14, 24, 28, 40, 46, 34] | [34, 46, 28, 40, 44, 1] |
| 2022-10-04 | [5, 11, 12, 22, 43, 45, 42] | [5, 11, 42, 43, 12, 15] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45]  |      0 | 2025-08-20 16:02:22.840570 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5]  |      0 | 2025-08-20 16:02:22.840628 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53]  |      0 | 2025-08-20 16:02:22.840684 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]   |      0 | 2025-08-20 16:02:22.840737 |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51, 19]   |      0 | 2025-08-20 16:02:22.840791 |
| 2025-08-07 | 01226 | [6, 24, 31, 32, 39, 48, 52]  |      0 | 2025-08-20 16:02:22.840845 |
| 2025-08-05 | 01225 | [8, 41, 45, 51, 52, 53, 31]  |      0 | 2025-08-20 16:02:22.840894 |
| 2025-08-02 | 01224 | [12, 24, 29, 33, 34, 35, 47] |      0 | 2025-08-20 16:02:22.840946 |
| 2025-07-31 | 01223 | [5, 17, 31, 42, 46, 49, 37]  |      0 | 2025-08-01 00:00:35.635172 |
| 2025-07-29 | 01222 | [4, 8, 23, 43, 45, 51, 48]   |      0 | 2025-07-30 00:00:36.365372 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     169 | 1.96 |     |       21 |     151 | 1.75 |     | 41       | 185     | 2.15 |
|        2 |     142 | 1.65 |     |       22 |     175 | 2.03 |     | 42       | 160     | 1.86 |
|        3 |     169 | 1.96 |     |       23 |     170 | 1.97 |     | 43       | 174     | 2.02 |
|        4 |     132 | 1.53 |     |       24 |     159 | 1.85 |     | 44       | 163     | 1.89 |
|        5 |     157 | 1.82 |     |       25 |     140 | 1.62 |     | 45       | 158     | 1.83 |
|        6 |     134 | 1.56 |     |       26 |     144 | 1.67 |     | 46       | 160     | 1.86 |
|        7 |     134 | 1.56 |     |       27 |     143 | 1.66 |     | 47       | 161     | 1.87 |
|        8 |     165 | 1.92 |     |       28 |     138 | 1.6  |     | 48       | 169     | 1.96 |
|        9 |     171 | 1.98 |     |       29 |     166 | 1.93 |     | 49       | 159     | 1.85 |
|       10 |     148 | 1.72 |     |       30 |     136 | 1.58 |     | 50       | 157     | 1.82 |
|       11 |     162 | 1.88 |     |       31 |     164 | 1.9  |     | 51       | 181     | 2.1  |
|       12 |     165 | 1.92 |     |       32 |     164 | 1.9  |     | 52       | 161     | 1.87 |
|       13 |     149 | 1.73 |     |       33 |     158 | 1.83 |     | 53       | 166     | 1.93 |
|       14 |     157 | 1.82 |     |       34 |     176 | 2.04 |     | 54       | 149     | 1.73 |
|       15 |     148 | 1.72 |     |       35 |     153 | 1.78 |     | 55       | 154     | 1.79 |
|       16 |     145 | 1.68 |     |       36 |     147 | 1.71 |     |          |         |      |
|       17 |     143 | 1.66 |     |       37 |     143 | 1.66 |     |          |         |      |
|       18 |     161 | 1.87 |     |       38 |     144 | 1.67 |     |          |         |      |
|       19 |     154 | 1.79 |     |       39 |     149 | 1.73 |     |          |         |      |
|       20 |     165 | 1.92 |     |       40 |     169 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.2  |     |       30 |       1 | 1.1 |     | 52       | 2       | 2.2 |
|        4 |       1 | 1.1  |     |       31 |       4 | 4.4 |     | 53       | 2       | 2.2 |
|        5 |       5 | 5.49 |     |       32 |       3 | 3.3 |     | 54       | 1       | 1.1 |
|        6 |       3 | 3.3  |     |       33 |       3 | 3.3 |     | 55       | 1       | 1.1 |
|        8 |       2 | 2.2  |     |       34 |       4 | 4.4 |     |          |         |     |
|        9 |       2 | 2.2  |     |       35 |       2 | 2.2 |     |          |         |     |
|       10 |       4 | 4.4  |     |       36 |       3 | 3.3 |     |          |         |     |
|       12 |       1 | 1.1  |     |       37 |       2 | 2.2 |     |          |         |     |
|       14 |       2 | 2.2  |     |       39 |       1 | 1.1 |     |          |         |     |
|       15 |       1 | 1.1  |     |       40 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1  |     |       41 |       1 | 1.1 |     |          |         |     |
|       17 |       2 | 2.2  |     |       42 |       1 | 1.1 |     |          |         |     |
|       18 |       1 | 1.1  |     |       43 |       2 | 2.2 |     |          |         |     |
|       19 |       1 | 1.1  |     |       44 |       1 | 1.1 |     |          |         |     |
|       22 |       1 | 1.1  |     |       45 |       4 | 4.4 |     |          |         |     |
|       23 |       2 | 2.2  |     |       46 |       1 | 1.1 |     |          |         |     |
|       24 |       4 | 4.4  |     |       47 |       3 | 3.3 |     |          |         |     |
|       26 |       1 | 1.1  |     |       48 |       3 | 3.3 |     |          |         |     |
|       28 |       2 | 2.2  |     |       49 |       1 | 1.1 |     |          |         |     |
|       29 |       3 | 3.3  |     |       51 |       3 | 3.3 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       23 |       3 | 1.65 |     | 44       | 4       | 2.2  |
|        2 |       2 | 1.1  |     |       24 |       5 | 2.75 |     | 45       | 8       | 4.4  |
|        3 |       4 | 2.2  |     |       25 |       1 | 0.55 |     | 46       | 1       | 0.55 |
|        4 |       1 | 0.55 |     |       26 |       2 | 1.1  |     | 47       | 3       | 1.65 |
|        5 |       5 | 2.75 |     |       27 |       3 | 1.65 |     | 48       | 7       | 3.85 |
|        6 |       4 | 2.2  |     |       28 |       3 | 1.65 |     | 49       | 1       | 0.55 |
|        8 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 50       | 2       | 1.1  |
|        9 |       4 | 2.2  |     |       30 |       3 | 1.65 |     | 51       | 6       | 3.3  |
|       10 |       5 | 2.75 |     |       31 |       7 | 3.85 |     | 52       | 3       | 1.65 |
|       11 |       2 | 1.1  |     |       32 |       6 | 3.3  |     | 53       | 6       | 3.3  |
|       12 |       3 | 1.65 |     |       33 |       6 | 3.3  |     | 54       | 4       | 2.2  |
|       13 |       2 | 1.1  |     |       34 |       6 | 3.3  |     | 55       | 2       | 1.1  |
|       14 |       4 | 2.2  |     |       35 |       2 | 1.1  |     |          |         |      |
|       15 |       4 | 2.2  |     |       36 |       5 | 2.75 |     |          |         |      |
|       16 |       2 | 1.1  |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       2 | 1.1  |     |       39 |       3 | 1.65 |     |          |         |      |
|       18 |       5 | 2.75 |     |       40 |       3 | 1.65 |     |          |         |      |
|       19 |       2 | 1.1  |     |       41 |       2 | 1.1  |     |          |         |      |
|       20 |       3 | 1.65 |     |       42 |       3 | 1.65 |     |          |         |      |
|       22 |       2 | 1.1  |     |       43 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       3 | 1.1  |     | 41       | 6       | 2.2  |
|        2 |       3 | 1.1  |     |       22 |       5 | 1.83 |     | 42       | 5       | 1.83 |
|        3 |       7 | 2.56 |     |       23 |       3 | 1.1  |     | 43       | 4       | 1.47 |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 7       | 2.56 |
|        5 |       6 | 2.2  |     |       25 |       1 | 0.37 |     | 45       | 12      | 4.4  |
|        6 |       7 | 2.56 |     |       26 |       3 | 1.1  |     | 46       | 4       | 1.47 |
|        7 |       1 | 0.37 |     |       27 |       5 | 1.83 |     | 47       | 6       | 2.2  |
|        8 |       6 | 2.2  |     |       28 |       3 | 1.1  |     | 48       | 9       | 3.3  |
|        9 |       7 | 2.56 |     |       29 |       5 | 1.83 |     | 49       | 3       | 1.1  |
|       10 |       6 | 2.2  |     |       30 |       4 | 1.47 |     | 50       | 3       | 1.1  |
|       11 |       4 | 1.47 |     |       31 |       7 | 2.56 |     | 51       | 7       | 2.56 |
|       12 |       6 | 2.2  |     |       32 |       7 | 2.56 |     | 52       | 4       | 1.47 |
|       13 |       3 | 1.1  |     |       33 |       7 | 2.56 |     | 53       | 6       | 2.2  |
|       14 |       8 | 2.93 |     |       34 |       9 | 3.3  |     | 54       | 4       | 1.47 |
|       15 |       5 | 1.83 |     |       35 |       2 | 0.73 |     | 55       | 5       | 1.83 |
|       16 |       5 | 1.83 |     |       36 |       5 | 1.83 |     |          |         |      |
|       17 |       4 | 1.47 |     |       37 |       5 | 1.83 |     |          |         |      |
|       18 |       8 | 2.93 |     |       38 |       1 | 0.37 |     |          |         |      |
|       19 |       4 | 1.47 |     |       39 |       3 | 1.1  |     |          |         |      |
|       20 |       4 | 1.47 |     |       40 |       4 | 1.47 |     |          |         |      |



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

