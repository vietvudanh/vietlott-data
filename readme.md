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
| Power 645 |          1202 | 2017-10-25   | 2025-08-29 |            1202 |      00198 |       01399 |
| Power 535 |            63 | 2025-06-29   | 2025-08-30 |             126 |      00001 |       00126 |
| 3D        |           970 | 2019-04-22   | 2025-08-29 |             970 |      00001 |       00970 |
| 3D Pro    |           617 | 2021-09-14   | 2025-08-30 |             617 |      00001 |       00617 |
| Bingo18   |           271 | 2024-12-03   | 2025-08-30 |           42961 |    0083123 |     0126110 |

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
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3 |     |       30 |       3 | 3.3 |     | 53       | 2       | 2.2 |
|        2 |       1 | 1.1 |     |       31 |       3 | 3.3 |     | 55       | 2       | 2.2 |
|        5 |       4 | 4.4 |     |       32 |       3 | 3.3 |     |          |         |     |
|        6 |       4 | 4.4 |     |       33 |       1 | 1.1 |     |          |         |     |
|        8 |       1 | 1.1 |     |       34 |       4 | 4.4 |     |          |         |     |
|        9 |       3 | 3.3 |     |       35 |       4 | 4.4 |     |          |         |     |
|       10 |       2 | 2.2 |     |       36 |       3 | 3.3 |     |          |         |     |
|       12 |       1 | 1.1 |     |       37 |       1 | 1.1 |     |          |         |     |
|       13 |       1 | 1.1 |     |       38 |       1 | 1.1 |     |          |         |     |
|       14 |       2 | 2.2 |     |       39 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1 |     |       40 |       2 | 2.2 |     |          |         |     |
|       17 |       3 | 3.3 |     |       41 |       2 | 2.2 |     |          |         |     |
|       18 |       1 | 1.1 |     |       43 |       1 | 1.1 |     |          |         |     |
|       19 |       2 | 2.2 |     |       44 |       4 | 4.4 |     |          |         |     |
|       22 |       1 | 1.1 |     |       45 |       2 | 2.2 |     |          |         |     |
|       23 |       1 | 1.1 |     |       47 |       3 | 3.3 |     |          |         |     |
|       24 |       4 | 4.4 |     |       48 |       3 | 3.3 |     |          |         |     |
|       26 |       1 | 1.1 |     |       50 |       2 | 2.2 |     |          |         |     |
|       28 |       1 | 1.1 |     |       51 |       2 | 2.2 |     |          |         |     |
|       29 |       1 | 1.1 |     |       52 |       4 | 4.4 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       24 |       6 | 3.3  |     | 45       | 7       | 3.85 |
|        2 |       2 | 1.1  |     |       26 |       3 | 1.65 |     | 46       | 1       | 0.55 |
|        3 |       2 | 1.1  |     |       27 |       1 | 0.55 |     | 47       | 3       | 1.65 |
|        4 |       1 | 0.55 |     |       28 |       4 | 2.2  |     | 48       | 7       | 3.85 |
|        5 |       7 | 3.85 |     |       29 |       4 | 2.2  |     | 49       | 1       | 0.55 |
|        6 |       4 | 2.2  |     |       30 |       5 | 2.75 |     | 50       | 3       | 1.65 |
|        8 |       3 | 1.65 |     |       31 |       7 | 3.85 |     | 51       | 5       | 2.75 |
|        9 |       5 | 2.75 |     |       32 |       5 | 2.75 |     | 52       | 5       | 2.75 |
|       10 |       4 | 2.2  |     |       33 |       5 | 2.75 |     | 53       | 4       | 2.2  |
|       12 |       2 | 1.1  |     |       34 |       8 | 4.4  |     | 54       | 4       | 2.2  |
|       13 |       2 | 1.1  |     |       35 |       4 | 2.2  |     | 55       | 3       | 1.65 |
|       14 |       2 | 1.1  |     |       36 |       5 | 2.75 |     |          |         |      |
|       15 |       2 | 1.1  |     |       37 |       2 | 1.1  |     |          |         |      |
|       16 |       1 | 0.55 |     |       38 |       1 | 0.55 |     |          |         |      |
|       17 |       4 | 2.2  |     |       39 |       3 | 1.65 |     |          |         |      |
|       18 |       4 | 2.2  |     |       40 |       3 | 1.65 |     |          |         |      |
|       19 |       3 | 1.65 |     |       41 |       3 | 1.65 |     |          |         |      |
|       20 |       1 | 0.55 |     |       42 |       3 | 1.65 |     |          |         |      |
|       22 |       3 | 1.65 |     |       43 |       2 | 1.1  |     |          |         |      |
|       23 |       3 | 1.65 |     |       44 |       7 | 3.85 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       3 | 1.1  |     | 41       | 5       | 1.83 |
|        2 |       4 | 1.47 |     |       22 |       5 | 1.83 |     | 42       | 3       | 1.1  |
|        3 |       6 | 2.2  |     |       23 |       3 | 1.1  |     | 43       | 4       | 1.47 |
|        4 |       1 | 0.37 |     |       24 |       7 | 2.56 |     | 44       | 10      | 3.66 |
|        5 |       8 | 2.93 |     |       25 |       1 | 0.37 |     | 45       | 9       | 3.3  |
|        6 |       7 | 2.56 |     |       26 |       4 | 1.47 |     | 46       | 3       | 1.1  |
|        7 |       1 | 0.37 |     |       27 |       4 | 1.47 |     | 47       | 5       | 1.83 |
|        8 |       5 | 1.83 |     |       28 |       4 | 1.47 |     | 48       | 9       | 3.3  |
|        9 |       7 | 2.56 |     |       29 |       5 | 1.83 |     | 49       | 2       | 0.73 |
|       10 |       6 | 2.2  |     |       30 |       6 | 2.2  |     | 50       | 4       | 1.47 |
|       11 |       4 | 1.47 |     |       31 |       7 | 2.56 |     | 51       | 7       | 2.56 |
|       12 |       5 | 1.83 |     |       32 |       7 | 2.56 |     | 52       | 6       | 2.2  |
|       13 |       4 | 1.47 |     |       33 |       7 | 2.56 |     | 53       | 6       | 2.2  |
|       14 |       6 | 2.2  |     |       34 |      11 | 4.03 |     | 54       | 4       | 1.47 |
|       15 |       4 | 1.47 |     |       35 |       4 | 1.47 |     | 55       | 3       | 1.1  |
|       16 |       5 | 1.83 |     |       36 |       5 | 1.83 |     |          |         |      |
|       17 |       6 | 2.2  |     |       37 |       4 | 1.47 |     |          |         |      |
|       18 |       7 | 2.56 |     |       38 |       2 | 0.73 |     |          |         |      |
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

