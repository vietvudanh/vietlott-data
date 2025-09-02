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
| Power 655 |          1236 | 2017-08-01   | 2025-08-30 |            1236 |      00001 |       01236 |
| Power 645 |          1203 | 2017-10-25   | 2025-08-31 |            1203 |      00198 |       01400 |
| Power 535 |            65 | 2025-06-29   | 2025-09-01 |             130 |      00001 |       00130 |
| 3D        |           971 | 2019-04-22   | 2025-09-01 |             971 |      00001 |       00971 |
| 3D Pro    |           617 | 2021-09-14   | 2025-08-30 |             617 |      00001 |       00617 |
| Bingo18   |           274 | 2024-12-03   | 2025-09-02 |           43318 |    0083123 |     0126488 |

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
| date       |    id | result                      |   page | process_time               |
|:-----------|------:|:----------------------------|-------:|:---------------------------|
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34] |      0 | 2025-08-31 00:00:28.809014 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-29 00:00:35.379419 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-27 00:00:31.403856 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-23 18:50:23.222577 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]  |      0 | 2025-08-23 18:50:23.223490 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45] |      0 | 2025-08-20 16:02:22.840570 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5] |      0 | 2025-08-20 16:02:22.840628 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53] |      0 | 2025-08-20 16:02:22.840684 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]  |      0 | 2025-08-20 16:02:22.840737 |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51, 19]  |      0 | 2025-08-20 16:02:22.840791 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.97 |     |       21 |     151 | 1.75 |     | 41       | 186     | 2.15 |
|        2 |     143 | 1.65 |     |       22 |     176 | 2.03 |     | 42       | 160     | 1.85 |
|        3 |     169 | 1.95 |     |       23 |     170 | 1.97 |     | 43       | 174     | 2.01 |
|        4 |     132 | 1.53 |     |       24 |     160 | 1.85 |     | 44       | 167     | 1.93 |
|        5 |     159 | 1.84 |     |       25 |     140 | 1.62 |     | 45       | 158     | 1.83 |
|        6 |     135 | 1.56 |     |       26 |     145 | 1.68 |     | 46       | 160     | 1.85 |
|        7 |     134 | 1.55 |     |       27 |     143 | 1.65 |     | 47       | 161     | 1.86 |
|        8 |     165 | 1.91 |     |       28 |     139 | 1.61 |     | 48       | 170     | 1.97 |
|        9 |     173 | 2    |     |       29 |     166 | 1.92 |     | 49       | 159     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     139 | 1.61 |     | 50       | 159     | 1.84 |
|       11 |     162 | 1.87 |     |       31 |     164 | 1.9  |     | 51       | 181     | 2.09 |
|       12 |     165 | 1.91 |     |       32 |     164 | 1.9  |     | 52       | 163     | 1.88 |
|       13 |     150 | 1.73 |     |       33 |     158 | 1.83 |     | 53       | 166     | 1.92 |
|       14 |     157 | 1.81 |     |       34 |     178 | 2.06 |     | 54       | 149     | 1.72 |
|       15 |     148 | 1.71 |     |       35 |     155 | 1.79 |     | 55       | 155     | 1.79 |
|       16 |     145 | 1.68 |     |       36 |     147 | 1.7  |     |          |         |      |
|       17 |     145 | 1.68 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     161 | 1.86 |     |       38 |     145 | 1.68 |     |          |         |      |
|       19 |     155 | 1.79 |     |       39 |     149 | 1.72 |     |          |         |      |
|       20 |     165 | 1.91 |     |       40 |     170 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 3.57 |     | 32       | 3       | 3.57 |
|        2 |       1 | 1.19 |     | 34       | 3       | 3.57 |
|        5 |       4 | 4.76 |     | 35       | 3       | 3.57 |
|        6 |       4 | 4.76 |     | 36       | 3       | 3.57 |
|        8 |       1 | 1.19 |     | 37       | 1       | 1.19 |
|        9 |       3 | 3.57 |     | 38       | 1       | 1.19 |
|       10 |       2 | 2.38 |     | 39       | 1       | 1.19 |
|       13 |       1 | 1.19 |     | 40       | 2       | 2.38 |
|       14 |       2 | 2.38 |     | 41       | 2       | 2.38 |
|       16 |       1 | 1.19 |     | 43       | 1       | 1.19 |
|       17 |       3 | 3.57 |     | 44       | 4       | 4.76 |
|       18 |       1 | 1.19 |     | 45       | 2       | 2.38 |
|       19 |       2 | 2.38 |     | 47       | 2       | 2.38 |
|       22 |       1 | 1.19 |     | 48       | 3       | 3.57 |
|       23 |       1 | 1.19 |     | 50       | 2       | 2.38 |
|       24 |       3 | 3.57 |     | 51       | 2       | 2.38 |
|       26 |       1 | 1.19 |     | 52       | 4       | 4.76 |
|       28 |       1 | 1.19 |     | 53       | 2       | 2.38 |
|       30 |       3 | 3.57 |     | 55       | 2       | 2.38 |
|       31 |       3 | 3.57 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.71 |     |       24 |       6 | 3.43 |     | 46       | 1       | 0.57 |
|        2 |       2 | 1.14 |     |       26 |       3 | 1.71 |     | 47       | 3       | 1.71 |
|        3 |       2 | 1.14 |     |       28 |       4 | 2.29 |     | 48       | 7       | 4.0  |
|        4 |       1 | 0.57 |     |       29 |       3 | 1.71 |     | 49       | 1       | 0.57 |
|        5 |       7 | 4    |     |       30 |       5 | 2.86 |     | 50       | 3       | 1.71 |
|        6 |       4 | 2.29 |     |       31 |       6 | 3.43 |     | 51       | 5       | 2.86 |
|        8 |       3 | 1.71 |     |       32 |       5 | 2.86 |     | 52       | 5       | 2.86 |
|        9 |       5 | 2.86 |     |       33 |       5 | 2.86 |     | 53       | 4       | 2.29 |
|       10 |       4 | 2.29 |     |       34 |       8 | 4.57 |     | 54       | 3       | 1.71 |
|       12 |       2 | 1.14 |     |       35 |       4 | 2.29 |     | 55       | 3       | 1.71 |
|       13 |       2 | 1.14 |     |       36 |       5 | 2.86 |     |          |         |      |
|       14 |       2 | 1.14 |     |       37 |       2 | 1.14 |     |          |         |      |
|       15 |       2 | 1.14 |     |       38 |       1 | 0.57 |     |          |         |      |
|       16 |       1 | 0.57 |     |       39 |       3 | 1.71 |     |          |         |      |
|       17 |       4 | 2.29 |     |       40 |       3 | 1.71 |     |          |         |      |
|       18 |       3 | 1.71 |     |       41 |       3 | 1.71 |     |          |         |      |
|       19 |       2 | 1.14 |     |       42 |       3 | 1.71 |     |          |         |      |
|       20 |       1 | 0.57 |     |       43 |       2 | 1.14 |     |          |         |      |
|       22 |       3 | 1.71 |     |       44 |       7 | 4    |     |          |         |      |
|       23 |       3 | 1.71 |     |       45 |       6 | 3.43 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.5  |     |       21 |       3 | 1.13 |     | 41       | 5       | 1.88 |
|        2 |       3 | 1.13 |     |       22 |       5 | 1.88 |     | 42       | 3       | 1.13 |
|        3 |       6 | 2.26 |     |       23 |       3 | 1.13 |     | 43       | 4       | 1.5  |
|        4 |       1 | 0.38 |     |       24 |       7 | 2.63 |     | 44       | 10      | 3.76 |
|        5 |       8 | 3.01 |     |       25 |       1 | 0.38 |     | 45       | 9       | 3.38 |
|        6 |       7 | 2.63 |     |       26 |       4 | 1.5  |     | 46       | 3       | 1.13 |
|        7 |       1 | 0.38 |     |       27 |       3 | 1.13 |     | 47       | 5       | 1.88 |
|        8 |       5 | 1.88 |     |       28 |       4 | 1.5  |     | 48       | 9       | 3.38 |
|        9 |       7 | 2.63 |     |       29 |       5 | 1.88 |     | 49       | 2       | 0.75 |
|       10 |       6 | 2.26 |     |       30 |       6 | 2.26 |     | 50       | 4       | 1.5  |
|       11 |       3 | 1.13 |     |       31 |       7 | 2.63 |     | 51       | 6       | 2.26 |
|       12 |       5 | 1.88 |     |       32 |       7 | 2.63 |     | 52       | 6       | 2.26 |
|       13 |       4 | 1.5  |     |       33 |       7 | 2.63 |     | 53       | 6       | 2.26 |
|       14 |       5 | 1.88 |     |       34 |      11 | 4.14 |     | 54       | 4       | 1.5  |
|       15 |       4 | 1.5  |     |       35 |       4 | 1.5  |     | 55       | 3       | 1.13 |
|       16 |       4 | 1.5  |     |       36 |       5 | 1.88 |     |          |         |      |
|       17 |       6 | 2.26 |     |       37 |       4 | 1.5  |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       1 | 0.38 |     |          |         |      |
|       19 |       3 | 1.13 |     |       39 |       3 | 1.13 |     |          |         |      |
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

