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
| Power 655 |          1240 | 2017-08-01   | 2025-09-09 |            1240 |      00001 |       01240 |
| Power 645 |          1207 | 2017-10-25   | 2025-09-10 |            1207 |      00198 |       01404 |
| Power 535 |            75 | 2025-06-29   | 2025-09-11 |             149 |      00001 |       00149 |
| 3D        |           975 | 2019-04-22   | 2025-09-10 |             975 |      00001 |       00975 |
| 3D Pro    |           621 | 2021-09-14   | 2025-09-09 |             621 |      00001 |       00621 |
| Bingo18   |           283 | 2024-12-03   | 2025-09-11 |           44809 |    0083123 |     0127979 |

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
| 2025-09-09 | 01240 | [16, 20, 21, 31, 40, 52, 2] |      0 | 2025-09-04 12:00:40.054941 |
| 2025-09-06 | 01239 | [9, 11, 19, 22, 34, 43, 31] |      0 | 2025-09-04 12:00:40.056040 |
| 2025-09-04 | 01238 | [9, 19, 23, 42, 49, 53, 40] |      0 | 2025-09-04 12:00:40.056931 |
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43] |      0 | 2025-09-03 00:00:31.255648 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34] |      0 | 2025-08-31 00:00:28.809014 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-29 00:00:35.379419 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-27 00:00:31.403856 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-23 18:50:23.222577 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]  |      0 | 2025-08-23 18:50:23.223490 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45] |      0 | 2025-08-20 16:02:22.840570 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.96 |     |       21 |     152 | 1.75 |     | 41       | 186     | 2.14 |
|        2 |     144 | 1.66 |     |       22 |     178 | 2.05 |     | 42       | 161     | 1.86 |
|        3 |     169 | 1.95 |     |       23 |     171 | 1.97 |     | 43       | 176     | 2.03 |
|        4 |     132 | 1.52 |     |       24 |     160 | 1.84 |     | 44       | 167     | 1.92 |
|        5 |     159 | 1.83 |     |       25 |     141 | 1.62 |     | 45       | 158     | 1.82 |
|        6 |     135 | 1.56 |     |       26 |     145 | 1.67 |     | 46       | 160     | 1.84 |
|        7 |     134 | 1.54 |     |       27 |     143 | 1.65 |     | 47       | 161     | 1.86 |
|        8 |     165 | 1.9  |     |       28 |     139 | 1.6  |     | 48       | 170     | 1.96 |
|        9 |     176 | 2.03 |     |       29 |     166 | 1.91 |     | 49       | 160     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     140 | 1.61 |     | 50       | 159     | 1.83 |
|       11 |     163 | 1.88 |     |       31 |     166 | 1.91 |     | 51       | 182     | 2.1  |
|       12 |     165 | 1.9  |     |       32 |     164 | 1.89 |     | 52       | 164     | 1.89 |
|       13 |     150 | 1.73 |     |       33 |     158 | 1.82 |     | 53       | 167     | 1.92 |
|       14 |     157 | 1.81 |     |       34 |     179 | 2.06 |     | 54       | 149     | 1.72 |
|       15 |     148 | 1.71 |     |       35 |     155 | 1.79 |     | 55       | 155     | 1.79 |
|       16 |     147 | 1.69 |     |       36 |     147 | 1.69 |     |          |         |      |
|       17 |     145 | 1.67 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     161 | 1.86 |     |       38 |     145 | 1.67 |     |          |         |      |
|       19 |     157 | 1.81 |     |       39 |     149 | 1.72 |     |          |         |      |
|       20 |     166 | 1.91 |     |       40 |     172 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3  |     |       28 |       1 | 1.1 |     | 52       | 3       | 3.3 |
|        2 |       2 | 2.2  |     |       30 |       4 | 4.4 |     | 53       | 2       | 2.2 |
|        5 |       3 | 3.3  |     |       31 |       3 | 3.3 |     | 55       | 2       | 2.2 |
|        6 |       3 | 3.3  |     |       32 |       2 | 2.2 |     |          |         |     |
|        9 |       5 | 5.49 |     |       34 |       4 | 4.4 |     |          |         |     |
|       10 |       2 | 2.2  |     |       35 |       3 | 3.3 |     |          |         |     |
|       11 |       1 | 1.1  |     |       36 |       2 | 2.2 |     |          |         |     |
|       13 |       1 | 1.1  |     |       37 |       1 | 1.1 |     |          |         |     |
|       14 |       2 | 2.2  |     |       38 |       1 | 1.1 |     |          |         |     |
|       16 |       2 | 2.2  |     |       40 |       4 | 4.4 |     |          |         |     |
|       17 |       3 | 3.3  |     |       41 |       1 | 1.1 |     |          |         |     |
|       18 |       1 | 1.1  |     |       42 |       1 | 1.1 |     |          |         |     |
|       19 |       3 | 3.3  |     |       43 |       2 | 2.2 |     |          |         |     |
|       20 |       1 | 1.1  |     |       44 |       4 | 4.4 |     |          |         |     |
|       21 |       1 | 1.1  |     |       45 |       1 | 1.1 |     |          |         |     |
|       22 |       3 | 3.3  |     |       47 |       2 | 2.2 |     |          |         |     |
|       23 |       2 | 2.2  |     |       48 |       2 | 2.2 |     |          |         |     |
|       24 |       2 | 2.2  |     |       49 |       1 | 1.1 |     |          |         |     |
|       25 |       1 | 1.1  |     |       50 |       2 | 2.2 |     |          |         |     |
|       26 |       1 | 1.1  |     |       51 |       1 | 1.1 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.71 |     |       23 |       3 | 1.71 |     | 44       | 6       | 3.43 |
|        2 |       2 | 1.14 |     |       24 |       5 | 2.86 |     | 45       | 4       | 2.29 |
|        4 |       1 | 0.57 |     |       25 |       1 | 0.57 |     | 46       | 1       | 0.57 |
|        5 |       7 | 4    |     |       26 |       3 | 1.71 |     | 47       | 3       | 1.71 |
|        6 |       4 | 2.29 |     |       28 |       4 | 2.29 |     | 48       | 6       | 3.43 |
|        8 |       3 | 1.71 |     |       29 |       3 | 1.71 |     | 49       | 2       | 1.14 |
|        9 |       8 | 4.57 |     |       30 |       6 | 3.43 |     | 50       | 2       | 1.14 |
|       10 |       4 | 2.29 |     |       31 |       7 | 4    |     | 51       | 4       | 2.29 |
|       11 |       1 | 0.57 |     |       32 |       4 | 2.29 |     | 52       | 5       | 2.86 |
|       12 |       1 | 0.57 |     |       33 |       4 | 2.29 |     | 53       | 4       | 2.29 |
|       13 |       2 | 1.14 |     |       34 |       7 | 4    |     | 54       | 2       | 1.14 |
|       14 |       2 | 1.14 |     |       35 |       4 | 2.29 |     | 55       | 2       | 1.14 |
|       15 |       1 | 0.57 |     |       36 |       5 | 2.86 |     |          |         |      |
|       16 |       3 | 1.71 |     |       37 |       2 | 1.14 |     |          |         |      |
|       17 |       4 | 2.29 |     |       38 |       1 | 0.57 |     |          |         |      |
|       18 |       3 | 1.71 |     |       39 |       2 | 1.14 |     |          |         |      |
|       19 |       4 | 2.29 |     |       40 |       5 | 2.86 |     |          |         |      |
|       20 |       2 | 1.14 |     |       41 |       2 | 1.14 |     |          |         |      |
|       21 |       1 | 0.57 |     |       42 |       2 | 1.14 |     |          |         |      |
|       22 |       4 | 2.29 |     |       43 |       4 | 2.29 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.5  |     |       21 |       1 | 0.38 |     | 41       | 4       | 1.5  |
|        2 |       4 | 1.5  |     |       22 |       7 | 2.63 |     | 42       | 4       | 1.5  |
|        3 |       5 | 1.88 |     |       23 |       4 | 1.5  |     | 43       | 6       | 2.26 |
|        4 |       1 | 0.38 |     |       24 |       7 | 2.63 |     | 44       | 9       | 3.38 |
|        5 |       8 | 3.01 |     |       25 |       2 | 0.75 |     | 45       | 8       | 3.01 |
|        6 |       5 | 1.88 |     |       26 |       4 | 1.5  |     | 46       | 1       | 0.38 |
|        7 |       1 | 0.38 |     |       27 |       3 | 1.13 |     | 47       | 5       | 1.88 |
|        8 |       4 | 1.5  |     |       28 |       4 | 1.5  |     | 48       | 8       | 3.01 |
|        9 |      10 | 3.76 |     |       29 |       4 | 1.5  |     | 49       | 2       | 0.75 |
|       10 |       6 | 2.26 |     |       30 |       7 | 2.63 |     | 50       | 4       | 1.5  |
|       11 |       4 | 1.5  |     |       31 |       9 | 3.38 |     | 51       | 7       | 2.63 |
|       12 |       4 | 1.5  |     |       32 |       7 | 2.63 |     | 52       | 6       | 2.26 |
|       13 |       4 | 1.5  |     |       33 |       6 | 2.26 |     | 53       | 7       | 2.63 |
|       14 |       4 | 1.5  |     |       34 |      10 | 3.76 |     | 54       | 4       | 1.5  |
|       15 |       4 | 1.5  |     |       35 |       4 | 1.5  |     | 55       | 3       | 1.13 |
|       16 |       5 | 1.88 |     |       36 |       5 | 1.88 |     |          |         |      |
|       17 |       4 | 1.5  |     |       37 |       2 | 0.75 |     |          |         |      |
|       18 |       6 | 2.26 |     |       38 |       1 | 0.38 |     |          |         |      |
|       19 |       5 | 1.88 |     |       39 |       3 | 1.13 |     |          |         |      |
|       20 |       4 | 1.5  |     |       40 |       6 | 2.26 |     |          |         |      |



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

