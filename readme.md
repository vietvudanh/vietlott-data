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
| Power 655 |          1235 | 2017-08-01   | 2025-08-28 |            1235 |      00001 |       01235 |
| Power 645 |          1202 | 2017-10-25   | 2025-08-29 |            1202 |      00198 |       01399 |
| Power 535 |            62 | 2025-06-29   | 2025-08-29 |             124 |      00001 |       00124 |
| 3D        |           970 | 2019-04-22   | 2025-08-29 |             970 |      00001 |       00970 |
| 3D Pro    |           616 | 2021-09-14   | 2025-08-28 |             616 |      00001 |       00616 |
| Bingo18   |           271 | 2024-12-03   | 2025-08-30 |           42841 |    0083123 |     0126011 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2021-11-04 | [5, 10, 15, 31, 32, 50, 28] | [31, 28, 32, 15, 50, 9] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                      |   page | process_time               |
|:-----------|------:|:----------------------------|-------:|:---------------------------|
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-29 00:00:35.379419 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-27 00:00:31.403856 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-23 18:50:23.222577 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]  |      0 | 2025-08-23 18:50:23.223490 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45] |      0 | 2025-08-20 16:02:22.840570 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5] |      0 | 2025-08-20 16:02:22.840628 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53] |      0 | 2025-08-20 16:02:22.840684 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]  |      0 | 2025-08-20 16:02:22.840737 |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51, 19]  |      0 | 2025-08-20 16:02:22.840791 |
| 2025-08-07 | 01226 | [6, 24, 31, 32, 39, 48, 52] |      0 | 2025-08-20 16:02:22.840845 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.97 |     |       21 |     151 | 1.75 |     | 41       | 186     | 2.15 |
|        2 |     142 | 1.64 |     |       22 |     176 | 2.04 |     | 42       | 160     | 1.85 |
|        3 |     169 | 1.96 |     |       23 |     170 | 1.97 |     | 43       | 174     | 2.01 |
|        4 |     132 | 1.53 |     |       24 |     159 | 1.84 |     | 44       | 166     | 1.92 |
|        5 |     159 | 1.84 |     |       25 |     140 | 1.62 |     | 45       | 158     | 1.83 |
|        6 |     135 | 1.56 |     |       26 |     145 | 1.68 |     | 46       | 160     | 1.85 |
|        7 |     134 | 1.55 |     |       27 |     143 | 1.65 |     | 47       | 161     | 1.86 |
|        8 |     165 | 1.91 |     |       28 |     139 | 1.61 |     | 48       | 170     | 1.97 |
|        9 |     173 | 2    |     |       29 |     166 | 1.92 |     | 49       | 159     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     138 | 1.6  |     | 50       | 159     | 1.84 |
|       11 |     162 | 1.87 |     |       31 |     164 | 1.9  |     | 51       | 181     | 2.09 |
|       12 |     165 | 1.91 |     |       32 |     164 | 1.9  |     | 52       | 163     | 1.89 |
|       13 |     150 | 1.74 |     |       33 |     158 | 1.83 |     | 53       | 166     | 1.92 |
|       14 |     157 | 1.82 |     |       34 |     177 | 2.05 |     | 54       | 149     | 1.72 |
|       15 |     148 | 1.71 |     |       35 |     155 | 1.79 |     | 55       | 155     | 1.79 |
|       16 |     145 | 1.68 |     |       36 |     147 | 1.7  |     |          |         |      |
|       17 |     144 | 1.67 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     161 | 1.86 |     |       38 |     145 | 1.68 |     |          |         |      |
|       19 |     154 | 1.78 |     |       39 |     149 | 1.72 |     |          |         |      |
|       20 |     165 | 1.91 |     |       40 |     170 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3  |     |       31 |       4 | 4.4 |     | 51       | 2       | 2.2 |
|        5 |       5 | 5.49 |     |       32 |       3 | 3.3 |     | 52       | 4       | 4.4 |
|        6 |       4 | 4.4  |     |       33 |       1 | 1.1 |     | 53       | 2       | 2.2 |
|        8 |       1 | 1.1  |     |       34 |       3 | 3.3 |     | 55       | 2       | 2.2 |
|        9 |       3 | 3.3  |     |       35 |       4 | 4.4 |     |          |         |     |
|       10 |       2 | 2.2  |     |       36 |       3 | 3.3 |     |          |         |     |
|       12 |       1 | 1.1  |     |       37 |       2 | 2.2 |     |          |         |     |
|       13 |       1 | 1.1  |     |       38 |       1 | 1.1 |     |          |         |     |
|       14 |       2 | 2.2  |     |       39 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1  |     |       40 |       2 | 2.2 |     |          |         |     |
|       17 |       3 | 3.3  |     |       41 |       2 | 2.2 |     |          |         |     |
|       18 |       1 | 1.1  |     |       42 |       1 | 1.1 |     |          |         |     |
|       19 |       1 | 1.1  |     |       43 |       1 | 1.1 |     |          |         |     |
|       22 |       1 | 1.1  |     |       44 |       3 | 3.3 |     |          |         |     |
|       23 |       1 | 1.1  |     |       45 |       2 | 2.2 |     |          |         |     |
|       24 |       3 | 3.3  |     |       46 |       1 | 1.1 |     |          |         |     |
|       26 |       1 | 1.1  |     |       47 |       3 | 3.3 |     |          |         |     |
|       28 |       1 | 1.1  |     |       48 |       3 | 3.3 |     |          |         |     |
|       29 |       1 | 1.1  |     |       49 |       1 | 1.1 |     |          |         |     |
|       30 |       2 | 2.2  |     |       50 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       23 |       3 | 1.65 |     | 44       | 6       | 3.3  |
|        2 |       1 | 0.55 |     |       24 |       5 | 2.75 |     | 45       | 7       | 3.85 |
|        3 |       3 | 1.65 |     |       26 |       3 | 1.65 |     | 46       | 1       | 0.55 |
|        4 |       1 | 0.55 |     |       27 |       2 | 1.1  |     | 47       | 3       | 1.65 |
|        5 |       7 | 3.85 |     |       28 |       4 | 2.2  |     | 48       | 7       | 3.85 |
|        6 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 49       | 1       | 0.55 |
|        8 |       3 | 1.65 |     |       30 |       4 | 2.2  |     | 50       | 3       | 1.65 |
|        9 |       5 | 2.75 |     |       31 |       7 | 3.85 |     | 51       | 5       | 2.75 |
|       10 |       4 | 2.2  |     |       32 |       5 | 2.75 |     | 52       | 5       | 2.75 |
|       11 |       1 | 0.55 |     |       33 |       6 | 3.3  |     | 53       | 4       | 2.2  |
|       12 |       3 | 1.65 |     |       34 |       7 | 3.85 |     | 54       | 4       | 2.2  |
|       13 |       2 | 1.1  |     |       35 |       4 | 2.2  |     | 55       | 3       | 1.65 |
|       14 |       3 | 1.65 |     |       36 |       5 | 2.75 |     |          |         |      |
|       15 |       3 | 1.65 |     |       37 |       2 | 1.1  |     |          |         |      |
|       16 |       1 | 0.55 |     |       38 |       1 | 0.55 |     |          |         |      |
|       17 |       3 | 1.65 |     |       39 |       3 | 1.65 |     |          |         |      |
|       18 |       4 | 2.2  |     |       40 |       3 | 1.65 |     |          |         |      |
|       19 |       2 | 1.1  |     |       41 |       3 | 1.65 |     |          |         |      |
|       20 |       1 | 0.55 |     |       42 |       3 | 1.65 |     |          |         |      |
|       22 |       3 | 1.65 |     |       43 |       2 | 1.1  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.5  |     |       21 |       3 | 1.13 |     | 41       | 5       | 1.88 |
|        2 |       3 | 1.13 |     |       22 |       5 | 1.88 |     | 42       | 3       | 1.13 |
|        3 |       6 | 2.26 |     |       23 |       3 | 1.13 |     | 43       | 4       | 1.5  |
|        4 |       1 | 0.38 |     |       24 |       6 | 2.26 |     | 44       | 9       | 3.38 |
|        5 |       8 | 3.01 |     |       25 |       1 | 0.38 |     | 45       | 9       | 3.38 |
|        6 |       7 | 2.63 |     |       26 |       4 | 1.5  |     | 46       | 3       | 1.13 |
|        7 |       1 | 0.38 |     |       27 |       4 | 1.5  |     | 47       | 5       | 1.88 |
|        8 |       5 | 1.88 |     |       28 |       4 | 1.5  |     | 48       | 9       | 3.38 |
|        9 |       7 | 2.63 |     |       29 |       5 | 1.88 |     | 49       | 2       | 0.75 |
|       10 |       6 | 2.26 |     |       30 |       5 | 1.88 |     | 50       | 4       | 1.5  |
|       11 |       4 | 1.5  |     |       31 |       7 | 2.63 |     | 51       | 7       | 2.63 |
|       12 |       5 | 1.88 |     |       32 |       7 | 2.63 |     | 52       | 6       | 2.26 |
|       13 |       4 | 1.5  |     |       33 |       7 | 2.63 |     | 53       | 6       | 2.26 |
|       14 |       6 | 2.26 |     |       34 |      10 | 3.76 |     | 54       | 4       | 1.5  |
|       15 |       4 | 1.5  |     |       35 |       4 | 1.5  |     | 55       | 3       | 1.13 |
|       16 |       5 | 1.88 |     |       36 |       5 | 1.88 |     |          |         |      |
|       17 |       5 | 1.88 |     |       37 |       4 | 1.5  |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       2 | 0.75 |     |          |         |      |
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

