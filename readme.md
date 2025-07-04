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
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## 📊 Data Statistics

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1212 | 2017-08-01   | 2025-07-05 |            1212 | 00001      | 01212       |
| Power 645 |          1178 | 2017-10-25   | 2025-07-04 |            1178 | 00198      | 01375       |
| Keno      |           941 | 2022-12-04   | 2025-07-05 |          132958 | #0110271   | #0243855    |
| 3D        |           946 | 2019-04-22   | 2025-07-04 |             946 | 00001      | 00946       |
| 3D Pro    |           593 | 2021-09-14   | 2025-07-05 |             593 | 00001      | 00593       |
| Bingo18   |           215 | 2024-12-03   | 2025-07-05 |           34057 | 0083123    | 0117206     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                       | predicted               |
|:-----------|:-----------------------------|:------------------------|
| 2022-06-09 | [30, 31, 35, 43, 48, 50, 22] | [35, 22, 30, 50, 31, 9] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-07-05 | 01212 | [3, 15, 22, 45, 51, 55, 54]  |      0 | 2025-07-06 00:01:25.986584 |
| 2025-07-03 | 01211 | [18, 19, 29, 31, 45, 54, 27] |      0 | 2025-07-04 00:01:20.834544 |
| 2025-07-01 | 01210 | [3, 11, 12, 14, 27, 33, 15]  |      0 | 2025-07-02 00:01:16.154567 |
| 2025-06-28 | 01209 | [8, 11, 13, 20, 45, 50, 25]  |      0 | 2025-06-30 15:30:00.150910 |
| 2025-06-26 | 01208 | [1, 14, 16, 27, 40, 51, 2]   |      0 | 2025-06-30 15:30:00.151037 |
| 2025-06-24 | 01207 | [3, 9, 18, 20, 30, 53, 48]   |      0 | 2025-06-30 15:30:00.151131 |
| 2025-06-21 | 01206 | [6, 10, 15, 43, 44, 53, 32]  |      0 | 2025-06-22 19:00:16.907461 |
| 2025-06-19 | 01205 | [3, 5, 9, 10, 16, 47, 34]    |      0 | 2025-06-19 19:00:12.105342 |
| 2025-06-17 | 01204 | [7, 13, 18, 22, 32, 44, 43]  |      0 | 2025-06-17 19:00:14.248629 |
| 2025-06-14 | 01203 | [11, 12, 22, 26, 41, 47, 24] |      0 | 2025-06-15 19:00:27.381690 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.97 |     |       21 |     151 | 1.78 |     | 41       | 183     | 2.16 |
|        2 |     141 | 1.66 |     |       22 |     174 | 2.05 |     | 42       | 157     | 1.85 |
|        3 |     168 | 1.98 |     |       23 |     167 | 1.97 |     | 43       | 172     | 2.03 |
|        4 |     131 | 1.54 |     |       24 |     154 | 1.82 |     | 44       | 160     | 1.89 |
|        5 |     152 | 1.79 |     |       25 |     140 | 1.65 |     | 45       | 153     | 1.8  |
|        6 |     131 | 1.54 |     |       26 |     142 | 1.67 |     | 46       | 159     | 1.87 |
|        7 |     134 | 1.58 |     |       27 |     143 | 1.69 |     | 47       | 158     | 1.86 |
|        8 |     162 | 1.91 |     |       28 |     135 | 1.59 |     | 48       | 163     | 1.92 |
|        9 |     168 | 1.98 |     |       29 |     163 | 1.92 |     | 49       | 158     | 1.86 |
|       10 |     144 | 1.7  |     |       30 |     134 | 1.58 |     | 50       | 156     | 1.84 |
|       11 |     162 | 1.91 |     |       31 |     158 | 1.86 |     | 51       | 177     | 2.09 |
|       12 |     163 | 1.92 |     |       32 |     159 | 1.87 |     | 52       | 158     | 1.86 |
|       13 |     148 | 1.74 |     |       33 |     153 | 1.8  |     | 53       | 162     | 1.91 |
|       14 |     155 | 1.83 |     |       34 |     170 | 2    |     | 54       | 147     | 1.73 |
|       15 |     147 | 1.73 |     |       35 |     151 | 1.78 |     | 55       | 153     | 1.8  |
|       16 |     144 | 1.7  |     |       36 |     142 | 1.67 |     |          |         |      |
|       17 |     141 | 1.66 |     |       37 |     141 | 1.66 |     |          |         |      |
|       18 |     158 | 1.86 |     |       38 |     144 | 1.7  |     |          |         |      |
|       19 |     153 | 1.8  |     |       39 |     146 | 1.72 |     |          |         |      |
|       20 |     164 | 1.93 |     |       40 |     167 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1  |     |       22 |       3 | 3.3 |     | 50       | 1       | 1.1 |
|        2 |       1 | 1.1  |     |       24 |       1 | 1.1 |     | 51       | 2       | 2.2 |
|        3 |       5 | 5.49 |     |       25 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        5 |       1 | 1.1  |     |       26 |       1 | 1.1 |     | 53       | 2       | 2.2 |
|        6 |       3 | 3.3  |     |       27 |       3 | 3.3 |     | 54       | 2       | 2.2 |
|        7 |       1 | 1.1  |     |       29 |       2 | 2.2 |     | 55       | 1       | 1.1 |
|        8 |       2 | 2.2  |     |       30 |       1 | 1.1 |     |          |         |     |
|        9 |       2 | 2.2  |     |       31 |       1 | 1.1 |     |          |         |     |
|       10 |       2 | 2.2  |     |       32 |       2 | 2.2 |     |          |         |     |
|       11 |       3 | 3.3  |     |       33 |       1 | 1.1 |     |          |         |     |
|       12 |       3 | 3.3  |     |       34 |       2 | 2.2 |     |          |         |     |
|       13 |       2 | 2.2  |     |       37 |       1 | 1.1 |     |          |         |     |
|       14 |       2 | 2.2  |     |       40 |       2 | 2.2 |     |          |         |     |
|       15 |       3 | 3.3  |     |       41 |       2 | 2.2 |     |          |         |     |
|       16 |       3 | 3.3  |     |       43 |       2 | 2.2 |     |          |         |     |
|       17 |       2 | 2.2  |     |       44 |       3 | 3.3 |     |          |         |     |
|       18 |       4 | 4.4  |     |       45 |       4 | 4.4 |     |          |         |     |
|       19 |       1 | 1.1  |     |       46 |       1 | 1.1 |     |          |         |     |
|       20 |       2 | 2.2  |     |       47 |       2 | 2.2 |     |          |         |     |
|       21 |       2 | 2.2  |     |       48 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.55 |     |       21 |       4 | 2.2  |     | 44       | 6       | 3.3  |
|        2 |       3 | 1.65 |     |       22 |       4 | 2.2  |     | 45       | 8       | 4.4  |
|        3 |       7 | 3.85 |     |       24 |       3 | 1.65 |     | 46       | 3       | 1.65 |
|        4 |       1 | 0.55 |     |       25 |       1 | 0.55 |     | 47       | 5       | 2.75 |
|        5 |       1 | 0.55 |     |       26 |       2 | 1.1  |     | 48       | 3       | 1.65 |
|        6 |       5 | 2.75 |     |       27 |       6 | 3.3  |     | 49       | 3       | 1.65 |
|        7 |       4 | 2.2  |     |       28 |       1 | 0.55 |     | 50       | 4       | 2.2  |
|        8 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 51       | 4       | 2.2  |
|        9 |       5 | 2.75 |     |       30 |       2 | 1.1  |     | 52       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       31 |       1 | 0.55 |     | 53       | 2       | 1.1  |
|       11 |       4 | 2.2  |     |       32 |       2 | 1.1  |     | 54       | 4       | 2.2  |
|       12 |       4 | 2.2  |     |       33 |       2 | 1.1  |     | 55       | 5       | 2.75 |
|       13 |       3 | 1.65 |     |       34 |       4 | 2.2  |     |          |         |      |
|       14 |       7 | 3.85 |     |       37 |       4 | 2.2  |     |          |         |      |
|       15 |       6 | 3.3  |     |       38 |       1 | 0.55 |     |          |         |      |
|       16 |       5 | 2.75 |     |       39 |       2 | 1.1  |     |          |         |      |
|       17 |       2 | 1.1  |     |       40 |       2 | 1.1  |     |          |         |      |
|       18 |       5 | 2.75 |     |       41 |       5 | 2.75 |     |          |         |      |
|       19 |       5 | 2.75 |     |       42 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       43 |       3 | 1.65 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       6 | 2.2  |     | 42       | 7       | 2.56 |
|        2 |       4 | 1.47 |     |       22 |       4 | 1.47 |     | 43       | 7       | 2.56 |
|        3 |      11 | 4.03 |     |       23 |       3 | 1.1  |     | 44       | 6       | 2.2  |
|        4 |       1 | 0.37 |     |       24 |       5 | 1.83 |     | 45       | 9       | 3.3  |
|        5 |       3 | 1.1  |     |       25 |       3 | 1.1  |     | 46       | 3       | 1.1  |
|        6 |       5 | 1.83 |     |       26 |       3 | 1.1  |     | 47       | 7       | 2.56 |
|        7 |       5 | 1.83 |     |       27 |       7 | 2.56 |     | 48       | 5       | 1.83 |
|        8 |       5 | 1.83 |     |       28 |       3 | 1.1  |     | 49       | 5       | 1.83 |
|        9 |       5 | 1.83 |     |       29 |       5 | 1.83 |     | 50       | 5       | 1.83 |
|       10 |       4 | 1.47 |     |       30 |       3 | 1.1  |     | 51       | 4       | 1.47 |
|       11 |       5 | 1.83 |     |       31 |       3 | 1.1  |     | 52       | 4       | 1.47 |
|       12 |       5 | 1.83 |     |       32 |       4 | 1.47 |     | 53       | 3       | 1.1  |
|       13 |       4 | 1.47 |     |       33 |       3 | 1.1  |     | 54       | 4       | 1.47 |
|       14 |      10 | 3.66 |     |       34 |       5 | 1.83 |     | 55       | 6       | 2.2  |
|       15 |      11 | 4.03 |     |       36 |       1 | 0.37 |     |          |         |      |
|       16 |       7 | 2.56 |     |       37 |       7 | 2.56 |     |          |         |      |
|       17 |       4 | 1.47 |     |       38 |       3 | 1.1  |     |          |         |      |
|       18 |       6 | 2.2  |     |       39 |       4 | 1.47 |     |          |         |      |
|       19 |       8 | 2.93 |     |       40 |       5 | 1.83 |     |          |         |      |
|       20 |       5 | 1.83 |     |       41 |      10 | 3.66 |     |          |         |      |



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

