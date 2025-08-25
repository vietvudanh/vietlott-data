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
| Power 645 |          1200 | 2017-10-25   | 2025-08-24 |            1200 |      00198 |       01397 |
| Power 535 |            58 | 2025-06-29   | 2025-08-25 |             116 |      00001 |       00116 |
| 3D        |           968 | 2019-04-22   | 2025-08-25 |             968 |      00001 |       00968 |
| 3D Pro    |           614 | 2021-09-14   | 2025-08-23 |             614 |      00001 |       00614 |
| Bingo18   |           266 | 2024-12-03   | 2025-08-25 |           42007 |    0083123 |     0125315 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted                |
|:-----------|:----------------------------|:-------------------------|
| 2025-06-21 | [6, 10, 15, 43, 44, 53, 32] | [27, 10, 32, 53, 43, 15] |
| 2020-03-07 | [5, 11, 21, 30, 40, 48, 20] | [21, 13, 5, 30, 20, 11]  |



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
|   result |   count |    % | -   |   result |   count |    % |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|
|        1 |       3 | 3.57 |     |       34 |       3 | 3.57 |
|        4 |       1 | 1.19 |     |       35 |       3 | 3.57 |
|        5 |       4 | 4.76 |     |       36 |       3 | 3.57 |
|        6 |       3 | 3.57 |     |       37 |       2 | 2.38 |
|        8 |       2 | 2.38 |     |       39 |       1 | 1.19 |
|        9 |       3 | 3.57 |     |       40 |       2 | 2.38 |
|       10 |       2 | 2.38 |     |       41 |       2 | 2.38 |
|       12 |       1 | 1.19 |     |       42 |       1 | 1.19 |
|       14 |       2 | 2.38 |     |       43 |       2 | 2.38 |
|       16 |       1 | 1.19 |     |       44 |       2 | 2.38 |
|       17 |       3 | 3.57 |     |       45 |       3 | 3.57 |
|       18 |       1 | 1.19 |     |       46 |       1 | 1.19 |
|       19 |       1 | 1.19 |     |       47 |       3 | 3.57 |
|       23 |       2 | 2.38 |     |       48 |       3 | 3.57 |
|       24 |       3 | 3.57 |     |       49 |       1 | 1.19 |
|       26 |       1 | 1.19 |     |       50 |       1 | 1.19 |
|       29 |       1 | 1.19 |     |       51 |       3 | 3.57 |
|       31 |       4 | 4.76 |     |       52 |       3 | 3.57 |
|       32 |       3 | 3.57 |     |       53 |       2 | 2.38 |
|       33 |       1 | 1.19 |     |       55 |       1 | 1.19 |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.71 |     |       23 |       3 | 1.71 |     | 44       | 5       | 2.86 |
|        2 |       1 | 0.57 |     |       24 |       5 | 2.86 |     | 45       | 8       | 4.57 |
|        3 |       3 | 1.71 |     |       25 |       1 | 0.57 |     | 46       | 1       | 0.57 |
|        4 |       1 | 0.57 |     |       26 |       3 | 1.71 |     | 47       | 3       | 1.71 |
|        5 |       6 | 3.43 |     |       27 |       2 | 1.14 |     | 48       | 6       | 3.43 |
|        6 |       3 | 1.71 |     |       28 |       3 | 1.71 |     | 49       | 1       | 0.57 |
|        8 |       4 | 2.29 |     |       29 |       4 | 2.29 |     | 50       | 3       | 1.71 |
|        9 |       5 | 2.86 |     |       30 |       2 | 1.14 |     | 51       | 5       | 2.86 |
|       10 |       4 | 2.29 |     |       31 |       7 | 4    |     | 52       | 4       | 2.29 |
|       11 |       2 | 1.14 |     |       32 |       5 | 2.86 |     | 53       | 4       | 2.29 |
|       12 |       3 | 1.71 |     |       33 |       6 | 3.43 |     | 54       | 4       | 2.29 |
|       13 |       2 | 1.14 |     |       34 |       7 | 4    |     | 55       | 2       | 1.14 |
|       14 |       3 | 1.71 |     |       35 |       3 | 1.71 |     |          |         |      |
|       15 |       3 | 1.71 |     |       36 |       5 | 2.86 |     |          |         |      |
|       16 |       1 | 0.57 |     |       37 |       2 | 1.14 |     |          |         |      |
|       17 |       3 | 1.71 |     |       39 |       3 | 1.71 |     |          |         |      |
|       18 |       4 | 2.29 |     |       40 |       3 | 1.71 |     |          |         |      |
|       19 |       2 | 1.14 |     |       41 |       3 | 1.71 |     |          |         |      |
|       20 |       2 | 1.14 |     |       42 |       3 | 1.71 |     |          |         |      |
|       22 |       2 | 1.14 |     |       43 |       2 | 1.14 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.5  |     |       21 |       3 | 1.13 |     | 41       | 6       | 2.26 |
|        2 |       3 | 1.13 |     |       22 |       4 | 1.5  |     | 42       | 4       | 1.5  |
|        3 |       6 | 2.26 |     |       23 |       3 | 1.13 |     | 43       | 4       | 1.5  |
|        4 |       1 | 0.38 |     |       24 |       7 | 2.63 |     | 44       | 8       | 3.01 |
|        5 |       7 | 2.63 |     |       25 |       1 | 0.38 |     | 45       | 11      | 4.14 |
|        6 |       7 | 2.63 |     |       26 |       4 | 1.5  |     | 46       | 4       | 1.5  |
|        7 |       1 | 0.38 |     |       27 |       4 | 1.5  |     | 47       | 5       | 1.88 |
|        8 |       6 | 2.26 |     |       28 |       3 | 1.13 |     | 48       | 8       | 3.01 |
|        9 |       8 | 3.01 |     |       29 |       5 | 1.88 |     | 49       | 3       | 1.13 |
|       10 |       6 | 2.26 |     |       30 |       3 | 1.13 |     | 50       | 4       | 1.5  |
|       11 |       4 | 1.5  |     |       31 |       7 | 2.63 |     | 51       | 7       | 2.63 |
|       12 |       5 | 1.88 |     |       32 |       7 | 2.63 |     | 52       | 5       | 1.88 |
|       13 |       3 | 1.13 |     |       33 |       7 | 2.63 |     | 53       | 6       | 2.26 |
|       14 |       7 | 2.63 |     |       34 |      10 | 3.76 |     | 54       | 4       | 1.5  |
|       15 |       4 | 1.5  |     |       35 |       3 | 1.13 |     | 55       | 3       | 1.13 |
|       16 |       5 | 1.88 |     |       36 |       5 | 1.88 |     |          |         |      |
|       17 |       5 | 1.88 |     |       37 |       5 | 1.88 |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       1 | 0.38 |     |          |         |      |
|       19 |       2 | 0.75 |     |       39 |       3 | 1.13 |     |          |         |      |
|       20 |       3 | 1.13 |     |       40 |       5 | 1.88 |     |          |         |      |



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

