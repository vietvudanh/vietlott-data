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
| Power 655 |          1242 | 2017-08-01   | 2025-09-13 |            1242 |      00001 |       01242 |
| Power 645 |          1208 | 2017-10-25   | 2025-09-12 |            1208 |      00198 |       01405 |
| Power 535 |            77 | 2025-06-29   | 2025-09-13 |             154 |      00001 |       00154 |
| 3D        |           976 | 2019-04-22   | 2025-09-12 |             976 |      00001 |       00976 |
| 3D Pro    |           623 | 2021-09-14   | 2025-09-13 |             623 |      00001 |       00623 |
| Bingo18   |           285 | 2024-12-03   | 2025-09-13 |           45187 |    0083123 |     0128336 |

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
| 2025-09-13 | 01242 | [2, 7, 15, 18, 24, 27, 45]  |      0 | 2025-09-14 00:00:29.018121 |
| 2025-09-11 | 01241 | [6, 16, 46, 49, 51, 55, 42] |      0 | 2025-09-12 00:00:34.372685 |
| 2025-09-09 | 01240 | [16, 20, 21, 31, 40, 52, 2] |      0 | 2025-09-04 12:00:40.054941 |
| 2025-09-06 | 01239 | [9, 11, 19, 22, 34, 43, 31] |      0 | 2025-09-04 12:00:40.056040 |
| 2025-09-04 | 01238 | [9, 19, 23, 42, 49, 53, 40] |      0 | 2025-09-04 12:00:40.056931 |
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43] |      0 | 2025-09-03 00:00:31.255648 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34] |      0 | 2025-08-31 00:00:28.809014 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-29 00:00:35.379419 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-27 00:00:31.403856 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-23 18:50:23.222577 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.96 |     |       21 |     152 | 1.75 |     | 41       | 186     | 2.14 |
|        2 |     145 | 1.67 |     |       22 |     178 | 2.05 |     | 42       | 162     | 1.86 |
|        3 |     169 | 1.94 |     |       23 |     171 | 1.97 |     | 43       | 176     | 2.02 |
|        4 |     132 | 1.52 |     |       24 |     161 | 1.85 |     | 44       | 167     | 1.92 |
|        5 |     159 | 1.83 |     |       25 |     141 | 1.62 |     | 45       | 159     | 1.83 |
|        6 |     136 | 1.56 |     |       26 |     145 | 1.67 |     | 46       | 161     | 1.85 |
|        7 |     135 | 1.55 |     |       27 |     144 | 1.66 |     | 47       | 161     | 1.85 |
|        8 |     165 | 1.9  |     |       28 |     139 | 1.6  |     | 48       | 170     | 1.96 |
|        9 |     176 | 2.02 |     |       29 |     166 | 1.91 |     | 49       | 161     | 1.85 |
|       10 |     148 | 1.7  |     |       30 |     140 | 1.61 |     | 50       | 159     | 1.83 |
|       11 |     163 | 1.88 |     |       31 |     166 | 1.91 |     | 51       | 183     | 2.11 |
|       12 |     165 | 1.9  |     |       32 |     164 | 1.89 |     | 52       | 164     | 1.89 |
|       13 |     150 | 1.73 |     |       33 |     158 | 1.82 |     | 53       | 167     | 1.92 |
|       14 |     157 | 1.81 |     |       34 |     179 | 2.06 |     | 54       | 149     | 1.71 |
|       15 |     149 | 1.71 |     |       35 |     155 | 1.78 |     | 55       | 156     | 1.79 |
|       16 |     148 | 1.7  |     |       36 |     147 | 1.69 |     |          |         |      |
|       17 |     145 | 1.67 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     162 | 1.86 |     |       38 |     145 | 1.67 |     |          |         |      |
|       19 |     157 | 1.81 |     |       39 |     149 | 1.71 |     |          |         |      |
|       20 |     166 | 1.91 |     |       40 |     172 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.2  |     |       26 |       1 | 1.1 |     | 50       | 2       | 2.2 |
|        2 |       3 | 3.3  |     |       27 |       1 | 1.1 |     | 51       | 2       | 2.2 |
|        5 |       3 | 3.3  |     |       28 |       1 | 1.1 |     | 52       | 3       | 3.3 |
|        6 |       2 | 2.2  |     |       30 |       4 | 4.4 |     | 53       | 1       | 1.1 |
|        7 |       1 | 1.1  |     |       31 |       3 | 3.3 |     | 55       | 2       | 2.2 |
|        9 |       5 | 5.49 |     |       32 |       1 | 1.1 |     |          |         |     |
|       11 |       1 | 1.1  |     |       34 |       4 | 4.4 |     |          |         |     |
|       13 |       1 | 1.1  |     |       35 |       2 | 2.2 |     |          |         |     |
|       14 |       2 | 2.2  |     |       36 |       2 | 2.2 |     |          |         |     |
|       15 |       1 | 1.1  |     |       38 |       1 | 1.1 |     |          |         |     |
|       16 |       3 | 3.3  |     |       40 |       3 | 3.3 |     |          |         |     |
|       17 |       2 | 2.2  |     |       41 |       1 | 1.1 |     |          |         |     |
|       18 |       1 | 1.1  |     |       42 |       2 | 2.2 |     |          |         |     |
|       19 |       3 | 3.3  |     |       43 |       2 | 2.2 |     |          |         |     |
|       20 |       1 | 1.1  |     |       44 |       4 | 4.4 |     |          |         |     |
|       21 |       1 | 1.1  |     |       45 |       2 | 2.2 |     |          |         |     |
|       22 |       3 | 3.3  |     |       46 |       1 | 1.1 |     |          |         |     |
|       23 |       2 | 2.2  |     |       47 |       2 | 2.2 |     |          |         |     |
|       24 |       2 | 2.2  |     |       48 |       2 | 2.2 |     |          |         |     |
|       25 |       1 | 1.1  |     |       49 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.65 |     |       22 |       4 | 2.2  |     | 42       | 3       | 1.65 |
|        2 |       3 | 1.65 |     |       23 |       3 | 1.65 |     | 43       | 4       | 2.2  |
|        4 |       1 | 0.55 |     |       24 |       6 | 3.3  |     | 44       | 6       | 3.3  |
|        5 |       7 | 3.85 |     |       25 |       1 | 0.55 |     | 45       | 5       | 2.75 |
|        6 |       5 | 2.75 |     |       26 |       2 | 1.1  |     | 46       | 2       | 1.1  |
|        7 |       1 | 0.55 |     |       27 |       1 | 0.55 |     | 47       | 3       | 1.65 |
|        8 |       3 | 1.65 |     |       28 |       4 | 2.2  |     | 48       | 5       | 2.75 |
|        9 |       8 | 4.4  |     |       29 |       3 | 1.65 |     | 49       | 3       | 1.65 |
|       10 |       4 | 2.2  |     |       30 |       5 | 2.75 |     | 50       | 2       | 1.1  |
|       11 |       1 | 0.55 |     |       31 |       6 | 3.3  |     | 51       | 5       | 2.75 |
|       12 |       1 | 0.55 |     |       32 |       3 | 1.65 |     | 52       | 5       | 2.75 |
|       13 |       2 | 1.1  |     |       33 |       4 | 2.2  |     | 53       | 4       | 2.2  |
|       14 |       2 | 1.1  |     |       34 |       7 | 3.85 |     | 54       | 2       | 1.1  |
|       15 |       2 | 1.1  |     |       35 |       4 | 2.2  |     | 55       | 3       | 1.65 |
|       16 |       4 | 2.2  |     |       36 |       4 | 2.2  |     |          |         |      |
|       17 |       4 | 2.2  |     |       37 |       2 | 1.1  |     |          |         |      |
|       18 |       3 | 1.65 |     |       38 |       1 | 0.55 |     |          |         |      |
|       19 |       4 | 2.2  |     |       39 |       2 | 1.1  |     |          |         |      |
|       20 |       2 | 1.1  |     |       40 |       5 | 2.75 |     |          |         |      |
|       21 |       1 | 0.55 |     |       41 |       2 | 1.1  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       1 | 0.37 |     | 41       | 3       | 1.1  |
|        2 |       5 | 1.83 |     |       22 |       6 | 2.2  |     | 42       | 5       | 1.83 |
|        3 |       5 | 1.83 |     |       23 |       4 | 1.47 |     | 43       | 6       | 2.2  |
|        4 |       1 | 0.37 |     |       24 |       7 | 2.56 |     | 44       | 9       | 3.3  |
|        5 |       8 | 2.93 |     |       25 |       2 | 0.73 |     | 45       | 9       | 3.3  |
|        6 |       6 | 2.2  |     |       26 |       3 | 1.1  |     | 46       | 2       | 0.73 |
|        7 |       2 | 0.73 |     |       27 |       4 | 1.47 |     | 47       | 4       | 1.47 |
|        8 |       4 | 1.47 |     |       28 |       4 | 1.47 |     | 48       | 8       | 2.93 |
|        9 |      10 | 3.66 |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       6 | 2.2  |     |       30 |       7 | 2.56 |     | 50       | 4       | 1.47 |
|       11 |       3 | 1.1  |     |       31 |       9 | 3.3  |     | 51       | 8       | 2.93 |
|       12 |       3 | 1.1  |     |       32 |       7 | 2.56 |     | 52       | 6       | 2.2  |
|       13 |       4 | 1.47 |     |       33 |       6 | 2.2  |     | 53       | 7       | 2.56 |
|       14 |       4 | 1.47 |     |       34 |      10 | 3.66 |     | 54       | 4       | 1.47 |
|       15 |       5 | 1.83 |     |       35 |       4 | 1.47 |     | 55       | 4       | 1.47 |
|       16 |       6 | 2.2  |     |       36 |       5 | 1.83 |     |          |         |      |
|       17 |       4 | 1.47 |     |       37 |       2 | 0.73 |     |          |         |      |
|       18 |       7 | 2.56 |     |       38 |       1 | 0.37 |     |          |         |      |
|       19 |       5 | 1.83 |     |       39 |       3 | 1.1  |     |          |         |      |
|       20 |       4 | 1.47 |     |       40 |       6 | 2.2  |     |          |         |      |



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

