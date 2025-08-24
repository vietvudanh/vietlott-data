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
| Power 655 |          1233 | 2017-08-01   | 2025-08-23 |            1233 |      00001 |       01233 |
| Power 645 |          1199 | 2017-10-25   | 2025-08-22 |            1199 |      00198 |       01396 |
| Power 535 |            56 | 2025-06-29   | 2025-08-23 |             112 |      00001 |       00112 |
| 3D        |           967 | 2019-04-22   | 2025-08-22 |             967 |      00001 |       00967 |
| 3D Pro    |           614 | 2021-09-14   | 2025-08-23 |             614 |      00001 |       00614 |
| Bingo18   |           265 | 2024-12-03   | 2025-08-24 |           41887 |    0083123 |     0125050 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                       | predicted                |
|:-----------|:-----------------------------|:-------------------------|
| 2023-02-16 | [1, 5, 7, 8, 20, 22, 33]     | [1, 33, 20, 8, 37, 5]    |
| 2022-10-08 | [11, 17, 23, 34, 41, 51, 40] | [41, 11, 34, 40, 20, 51] |
| 2021-09-16 | [10, 16, 40, 43, 45, 46, 22] | [16, 45, 46, 27, 40, 22] |
| 2017-12-14 | [11, 12, 22, 28, 46, 50, 7]  | [11, 46, 52, 28, 7, 22]  |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]   |      0 | 2025-08-23 18:50:23.222577 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]   |      0 | 2025-08-23 18:50:23.223490 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45]  |      0 | 2025-08-20 16:02:22.840570 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5]  |      0 | 2025-08-20 16:02:22.840628 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53]  |      0 | 2025-08-20 16:02:22.840684 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]   |      0 | 2025-08-20 16:02:22.840737 |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51, 19]   |      0 | 2025-08-20 16:02:22.840791 |
| 2025-08-07 | 01226 | [6, 24, 31, 32, 39, 48, 52]  |      0 | 2025-08-20 16:02:22.840845 |
| 2025-08-05 | 01225 | [8, 41, 45, 51, 52, 53, 31]  |      0 | 2025-08-20 16:02:22.840894 |
| 2025-08-02 | 01224 | [12, 24, 29, 33, 34, 35, 47] |      0 | 2025-08-20 16:02:22.840946 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.97 |     |       21 |     151 | 1.75 |     | 41       | 186     | 2.16 |
|        2 |     142 | 1.65 |     |       22 |     175 | 2.03 |     | 42       | 160     | 1.85 |
|        3 |     169 | 1.96 |     |       23 |     170 | 1.97 |     | 43       | 174     | 2.02 |
|        4 |     132 | 1.53 |     |       24 |     159 | 1.84 |     | 44       | 165     | 1.91 |
|        5 |     158 | 1.83 |     |       25 |     140 | 1.62 |     | 45       | 158     | 1.83 |
|        6 |     134 | 1.55 |     |       26 |     145 | 1.68 |     | 46       | 160     | 1.85 |
|        7 |     134 | 1.55 |     |       27 |     143 | 1.66 |     | 47       | 161     | 1.87 |
|        8 |     165 | 1.91 |     |       28 |     138 | 1.6  |     | 48       | 169     | 1.96 |
|        9 |     173 | 2    |     |       29 |     166 | 1.92 |     | 49       | 159     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     136 | 1.58 |     | 50       | 158     | 1.83 |
|       11 |     162 | 1.88 |     |       31 |     164 | 1.9  |     | 51       | 181     | 2.1  |
|       12 |     165 | 1.91 |     |       32 |     164 | 1.9  |     | 52       | 162     | 1.88 |
|       13 |     149 | 1.73 |     |       33 |     158 | 1.83 |     | 53       | 166     | 1.92 |
|       14 |     157 | 1.82 |     |       34 |     177 | 2.05 |     | 54       | 149     | 1.73 |
|       15 |     148 | 1.71 |     |       35 |     154 | 1.78 |     | 55       | 154     | 1.78 |
|       16 |     145 | 1.68 |     |       36 |     147 | 1.7  |     |          |         |      |
|       17 |     144 | 1.67 |     |       37 |     143 | 1.66 |     |          |         |      |
|       18 |     161 | 1.87 |     |       38 |     144 | 1.67 |     |          |         |      |
|       19 |     154 | 1.78 |     |       39 |     149 | 1.73 |     |          |         |      |
|       20 |     165 | 1.91 |     |       40 |     170 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3  |     |       33 |       2 | 2.2 |     | 54       | 1       | 1.1 |
|        4 |       1 | 1.1  |     |       34 |       4 | 4.4 |     | 55       | 1       | 1.1 |
|        5 |       5 | 5.49 |     |       35 |       3 | 3.3 |     |          |         |     |
|        6 |       3 | 3.3  |     |       36 |       3 | 3.3 |     |          |         |     |
|        8 |       2 | 2.2  |     |       37 |       2 | 2.2 |     |          |         |     |
|        9 |       3 | 3.3  |     |       39 |       1 | 1.1 |     |          |         |     |
|       10 |       2 | 2.2  |     |       40 |       2 | 2.2 |     |          |         |     |
|       12 |       1 | 1.1  |     |       41 |       2 | 2.2 |     |          |         |     |
|       14 |       2 | 2.2  |     |       42 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1  |     |       43 |       2 | 2.2 |     |          |         |     |
|       17 |       3 | 3.3  |     |       44 |       2 | 2.2 |     |          |         |     |
|       18 |       1 | 1.1  |     |       45 |       3 | 3.3 |     |          |         |     |
|       19 |       1 | 1.1  |     |       46 |       1 | 1.1 |     |          |         |     |
|       23 |       2 | 2.2  |     |       47 |       3 | 3.3 |     |          |         |     |
|       24 |       3 | 3.3  |     |       48 |       3 | 3.3 |     |          |         |     |
|       26 |       2 | 2.2  |     |       49 |       1 | 1.1 |     |          |         |     |
|       28 |       1 | 1.1  |     |       50 |       1 | 1.1 |     |          |         |     |
|       29 |       2 | 2.2  |     |       51 |       3 | 3.3 |     |          |         |     |
|       31 |       4 | 4.4  |     |       52 |       3 | 3.3 |     |          |         |     |
|       32 |       3 | 3.3  |     |       53 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.2  |     |       23 |       3 | 1.65 |     | 44       | 5       | 2.75 |
|        2 |       2 | 1.1  |     |       24 |       5 | 2.75 |     | 45       | 8       | 4.4  |
|        3 |       3 | 1.65 |     |       25 |       1 | 0.55 |     | 46       | 1       | 0.55 |
|        4 |       1 | 0.55 |     |       26 |       3 | 1.65 |     | 47       | 3       | 1.65 |
|        5 |       6 | 3.3  |     |       27 |       3 | 1.65 |     | 48       | 6       | 3.3  |
|        6 |       3 | 1.65 |     |       28 |       3 | 1.65 |     | 49       | 1       | 0.55 |
|        8 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 50       | 3       | 1.65 |
|        9 |       5 | 2.75 |     |       30 |       2 | 1.1  |     | 51       | 6       | 3.3  |
|       10 |       4 | 2.2  |     |       31 |       7 | 3.85 |     | 52       | 4       | 2.2  |
|       11 |       2 | 1.1  |     |       32 |       5 | 2.75 |     | 53       | 4       | 2.2  |
|       12 |       3 | 1.65 |     |       33 |       6 | 3.3  |     | 54       | 4       | 2.2  |
|       13 |       2 | 1.1  |     |       34 |       7 | 3.85 |     | 55       | 2       | 1.1  |
|       14 |       4 | 2.2  |     |       35 |       3 | 1.65 |     |          |         |      |
|       15 |       3 | 1.65 |     |       36 |       5 | 2.75 |     |          |         |      |
|       16 |       2 | 1.1  |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       3 | 1.65 |     |       39 |       3 | 1.65 |     |          |         |      |
|       18 |       4 | 2.2  |     |       40 |       4 | 2.2  |     |          |         |      |
|       19 |       2 | 1.1  |     |       41 |       3 | 1.65 |     |          |         |      |
|       20 |       2 | 1.1  |     |       42 |       3 | 1.65 |     |          |         |      |
|       22 |       2 | 1.1  |     |       43 |       2 | 1.1  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       3 | 1.1  |     | 41       | 6       | 2.2  |
|        2 |       3 | 1.1  |     |       22 |       4 | 1.47 |     | 42       | 5       | 1.83 |
|        3 |       6 | 2.2  |     |       23 |       3 | 1.1  |     | 43       | 4       | 1.47 |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 9       | 3.3  |
|        5 |       7 | 2.56 |     |       25 |       1 | 0.37 |     | 45       | 11      | 4.03 |
|        6 |       7 | 2.56 |     |       26 |       4 | 1.47 |     | 46       | 4       | 1.47 |
|        7 |       1 | 0.37 |     |       27 |       4 | 1.47 |     | 47       | 5       | 1.83 |
|        8 |       6 | 2.2  |     |       28 |       3 | 1.1  |     | 48       | 9       | 3.3  |
|        9 |       8 | 2.93 |     |       29 |       5 | 1.83 |     | 49       | 3       | 1.1  |
|       10 |       6 | 2.2  |     |       30 |       3 | 1.1  |     | 50       | 4       | 1.47 |
|       11 |       4 | 1.47 |     |       31 |       7 | 2.56 |     | 51       | 7       | 2.56 |
|       12 |       6 | 2.2  |     |       32 |       7 | 2.56 |     | 52       | 5       | 1.83 |
|       13 |       3 | 1.1  |     |       33 |       7 | 2.56 |     | 53       | 6       | 2.2  |
|       14 |       7 | 2.56 |     |       34 |      10 | 3.66 |     | 54       | 4       | 1.47 |
|       15 |       4 | 1.47 |     |       35 |       3 | 1.1  |     | 55       | 3       | 1.1  |
|       16 |       5 | 1.83 |     |       36 |       5 | 1.83 |     |          |         |      |
|       17 |       5 | 1.83 |     |       37 |       5 | 1.83 |     |          |         |      |
|       18 |       8 | 2.93 |     |       38 |       1 | 0.37 |     |          |         |      |
|       19 |       3 | 1.1  |     |       39 |       3 | 1.1  |     |          |         |      |
|       20 |       3 | 1.1  |     |       40 |       5 | 1.83 |     |          |         |      |



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

