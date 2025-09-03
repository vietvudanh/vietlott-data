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
| Power 655 |          1237 | 2017-08-01   | 2025-09-02 |            1237 |      00001 |       01237 |
| Power 645 |          1204 | 2017-10-25   | 2025-09-03 |            1204 |      00198 |       01401 |
| Power 535 |            67 | 2025-06-29   | 2025-09-03 |             134 |      00001 |       00134 |
| 3D        |           972 | 2019-04-22   | 2025-09-03 |             972 |      00001 |       00972 |
| 3D Pro    |           618 | 2021-09-14   | 2025-09-02 |             618 |      00001 |       00618 |
| Bingo18   |           275 | 2024-12-03   | 2025-09-03 |           43597 |    0083123 |     0126746 |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                      | predicted               |
|:-----------|:----------------------------|:------------------------|
| 2024-02-06 | [8, 19, 27, 34, 46, 51, 24] | [8, 24, 51, 27, 19, 46] |
| 2023-11-16 | [3, 5, 10, 18, 44, 49, 28]  | [5, 31, 44, 3, 28, 18]  |
| 2023-03-30 | [6, 11, 14, 21, 30, 32, 22] | [14, 30, 32, 11, 4, 6]  |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                      |   page | process_time               |
|:-----------|------:|:----------------------------|-------:|:---------------------------|
| 2025-09-02 | 01237 | [9, 16, 22, 25, 30, 51, 43] |      0 | 2025-09-03 00:00:31.255648 |
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44, 34] |      0 | 2025-08-31 00:00:28.809014 |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52, 50] |      0 | 2025-08-29 00:00:35.379419 |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55, 5] |      0 | 2025-08-27 00:00:31.403856 |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50, 52]  |      0 | 2025-08-23 18:50:23.222577 |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41, 44]  |      0 | 2025-08-23 18:50:23.223490 |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47, 45] |      0 | 2025-08-20 16:02:22.840570 |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48, 5] |      0 | 2025-08-20 16:02:22.840628 |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35, 53] |      0 | 2025-08-20 16:02:22.840684 |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55, 10]  |      0 | 2025-08-20 16:02:22.840737 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     170 | 1.96 |     |       21 |     151 | 1.74 |     | 41       | 186     | 2.15 |
|        2 |     143 | 1.65 |     |       22 |     177 | 2.04 |     | 42       | 160     | 1.85 |
|        3 |     169 | 1.95 |     |       23 |     170 | 1.96 |     | 43       | 175     | 2.02 |
|        4 |     132 | 1.52 |     |       24 |     160 | 1.85 |     | 44       | 167     | 1.93 |
|        5 |     159 | 1.84 |     |       25 |     141 | 1.63 |     | 45       | 158     | 1.82 |
|        6 |     135 | 1.56 |     |       26 |     145 | 1.67 |     | 46       | 160     | 1.85 |
|        7 |     134 | 1.55 |     |       27 |     143 | 1.65 |     | 47       | 161     | 1.86 |
|        8 |     165 | 1.91 |     |       28 |     139 | 1.61 |     | 48       | 170     | 1.96 |
|        9 |     174 | 2.01 |     |       29 |     166 | 1.92 |     | 49       | 159     | 1.84 |
|       10 |     148 | 1.71 |     |       30 |     140 | 1.62 |     | 50       | 159     | 1.84 |
|       11 |     162 | 1.87 |     |       31 |     164 | 1.89 |     | 51       | 182     | 2.1  |
|       12 |     165 | 1.91 |     |       32 |     164 | 1.89 |     | 52       | 163     | 1.88 |
|       13 |     150 | 1.73 |     |       33 |     158 | 1.82 |     | 53       | 166     | 1.92 |
|       14 |     157 | 1.81 |     |       34 |     178 | 2.06 |     | 54       | 149     | 1.72 |
|       15 |     148 | 1.71 |     |       35 |     155 | 1.79 |     | 55       | 155     | 1.79 |
|       16 |     146 | 1.69 |     |       36 |     147 | 1.7  |     |          |         |      |
|       17 |     145 | 1.67 |     |       37 |     143 | 1.65 |     |          |         |      |
|       18 |     161 | 1.86 |     |       38 |     145 | 1.67 |     |          |         |      |
|       19 |     155 | 1.79 |     |       39 |     149 | 1.72 |     |          |         |      |
|       20 |     165 | 1.91 |     |       40 |     170 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % |
|---------:|--------:|----:|:----|---------:|--------:|----:|
|        1 |       3 | 3.3 |     |       31 |       3 | 3.3 |
|        2 |       1 | 1.1 |     |       32 |       3 | 3.3 |
|        5 |       4 | 4.4 |     |       34 |       3 | 3.3 |
|        6 |       4 | 4.4 |     |       35 |       3 | 3.3 |
|        8 |       1 | 1.1 |     |       36 |       3 | 3.3 |
|        9 |       4 | 4.4 |     |       37 |       1 | 1.1 |
|       10 |       2 | 2.2 |     |       38 |       1 | 1.1 |
|       13 |       1 | 1.1 |     |       39 |       1 | 1.1 |
|       14 |       2 | 2.2 |     |       40 |       2 | 2.2 |
|       16 |       2 | 2.2 |     |       41 |       2 | 2.2 |
|       17 |       3 | 3.3 |     |       43 |       2 | 2.2 |
|       18 |       1 | 1.1 |     |       44 |       4 | 4.4 |
|       19 |       2 | 2.2 |     |       45 |       2 | 2.2 |
|       22 |       2 | 2.2 |     |       47 |       2 | 2.2 |
|       23 |       1 | 1.1 |     |       48 |       3 | 3.3 |
|       24 |       3 | 3.3 |     |       50 |       2 | 2.2 |
|       25 |       1 | 1.1 |     |       51 |       3 | 3.3 |
|       26 |       1 | 1.1 |     |       52 |       4 | 4.4 |
|       28 |       1 | 1.1 |     |       53 |       2 | 2.2 |
|       30 |       4 | 4.4 |     |       55 |       2 | 2.2 |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.71 |     |       24 |       6 | 3.43 |     | 45       | 5       | 2.86 |
|        2 |       2 | 1.14 |     |       25 |       1 | 0.57 |     | 46       | 1       | 0.57 |
|        3 |       1 | 0.57 |     |       26 |       3 | 1.71 |     | 47       | 3       | 1.71 |
|        4 |       1 | 0.57 |     |       28 |       4 | 2.29 |     | 48       | 7       | 4.0  |
|        5 |       7 | 4    |     |       29 |       3 | 1.71 |     | 49       | 1       | 0.57 |
|        6 |       4 | 2.29 |     |       30 |       6 | 3.43 |     | 50       | 3       | 1.71 |
|        8 |       3 | 1.71 |     |       31 |       6 | 3.43 |     | 51       | 5       | 2.86 |
|        9 |       6 | 3.43 |     |       32 |       5 | 2.86 |     | 52       | 5       | 2.86 |
|       10 |       4 | 2.29 |     |       33 |       5 | 2.86 |     | 53       | 4       | 2.29 |
|       12 |       2 | 1.14 |     |       34 |       8 | 4.57 |     | 54       | 2       | 1.14 |
|       13 |       2 | 1.14 |     |       35 |       4 | 2.29 |     | 55       | 2       | 1.14 |
|       14 |       2 | 1.14 |     |       36 |       5 | 2.86 |     |          |         |      |
|       15 |       1 | 0.57 |     |       37 |       2 | 1.14 |     |          |         |      |
|       16 |       2 | 1.14 |     |       38 |       1 | 0.57 |     |          |         |      |
|       17 |       4 | 2.29 |     |       39 |       3 | 1.71 |     |          |         |      |
|       18 |       3 | 1.71 |     |       40 |       3 | 1.71 |     |          |         |      |
|       19 |       2 | 1.14 |     |       41 |       3 | 1.71 |     |          |         |      |
|       20 |       1 | 0.57 |     |       42 |       3 | 1.71 |     |          |         |      |
|       22 |       3 | 1.71 |     |       43 |       3 | 1.71 |     |          |         |      |
|       23 |       3 | 1.71 |     |       44 |       7 | 4    |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.5  |     |       21 |       2 | 0.75 |     | 41       | 5       | 1.88 |
|        2 |       3 | 1.13 |     |       22 |       6 | 2.26 |     | 42       | 3       | 1.13 |
|        3 |       6 | 2.26 |     |       23 |       3 | 1.13 |     | 43       | 5       | 1.88 |
|        4 |       1 | 0.38 |     |       24 |       7 | 2.63 |     | 44       | 10      | 3.76 |
|        5 |       8 | 3.01 |     |       25 |       2 | 0.75 |     | 45       | 9       | 3.38 |
|        6 |       7 | 2.63 |     |       26 |       4 | 1.5  |     | 46       | 2       | 0.75 |
|        7 |       1 | 0.38 |     |       27 |       3 | 1.13 |     | 47       | 5       | 1.88 |
|        8 |       5 | 1.88 |     |       28 |       4 | 1.5  |     | 48       | 9       | 3.38 |
|        9 |       8 | 3.01 |     |       29 |       5 | 1.88 |     | 49       | 1       | 0.38 |
|       10 |       6 | 2.26 |     |       30 |       7 | 2.63 |     | 50       | 4       | 1.5  |
|       11 |       3 | 1.13 |     |       31 |       7 | 2.63 |     | 51       | 7       | 2.63 |
|       12 |       5 | 1.88 |     |       32 |       7 | 2.63 |     | 52       | 6       | 2.26 |
|       13 |       4 | 1.5  |     |       33 |       6 | 2.26 |     | 53       | 6       | 2.26 |
|       14 |       4 | 1.5  |     |       34 |      10 | 3.76 |     | 54       | 4       | 1.5  |
|       15 |       4 | 1.5  |     |       35 |       4 | 1.5  |     | 55       | 3       | 1.13 |
|       16 |       5 | 1.88 |     |       36 |       5 | 1.88 |     |          |         |      |
|       17 |       6 | 2.26 |     |       37 |       3 | 1.13 |     |          |         |      |
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

