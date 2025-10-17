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

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1256 | 2017-08-01   | 2025-10-16 |            1256 | 00001      | 01256       |
| Power 645 |          1209 | 2017-10-25   | 2025-09-14 |            1209 | 00198      | 01406       |
| Power 535 |            79 | 2025-06-29   | 2025-09-15 |             158 | 00001      | 00158       |
| Keno      |           118 | 2022-12-04   | 2025-09-16 |           18149 | #0110271   | #0252450    |
| 3D        |           977 | 2019-04-22   | 2025-09-15 |             977 | 00001      | 00977       |
| 3D Pro    |           623 | 2021-09-14   | 2025-09-13 |             623 | 00001      | 00623       |
| Bingo18   |           289 | 2024-12-03   | 2025-10-17 |           45584 | 0083123    | 0133739     |

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
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-10-16 | 01256 | [14, 15, 24, 26, 27, 45, 36] |      0 | 2025-10-17 21:15:55.017468 |
| 2025-10-14 | 01255 | [8, 9, 16, 26, 37, 55, 12]   |      0 | 2025-10-17 21:15:55.017590 |
| 2025-10-11 | 01254 | [3, 7, 26, 43, 44, 46, 25]   |      0 | 2025-10-17 21:15:55.017694 |
| 2025-10-09 | 01253 | [7, 11, 21, 22, 39, 42, 40]  |      0 | 2025-10-17 21:15:55.017805 |
| 2025-10-07 | 01252 | [19, 22, 35, 37, 43, 45, 29] |      0 | 2025-10-17 21:15:55.017899 |
| 2025-10-04 | 01251 | [22, 33, 35, 36, 38, 40, 7]  |      0 | 2025-10-17 21:15:55.017992 |
| 2025-10-02 | 01250 | [1, 2, 20, 24, 27, 42, 43]   |      0 | 2025-10-17 21:15:55.018087 |
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |      0 | 2025-10-17 21:15:55.018180 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |      1 | 2025-10-17 21:15:55.028639 |
| 2025-09-25 | 01247 | [5, 17, 30, 31, 38, 53, 8]   |      1 | 2025-10-17 21:15:55.028670 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     172 | 1.96 |     |       21 |     153 | 1.74 |     | 41       | 187     | 2.13 |
|        2 |     147 | 1.67 |     |       22 |     181 | 2.06 |     | 42       | 164     | 1.87 |
|        3 |     171 | 1.95 |     |       23 |     172 | 1.96 |     | 43       | 181     | 2.06 |
|        4 |     132 | 1.5  |     |       24 |     164 | 1.87 |     | 44       | 168     | 1.91 |
|        5 |     160 | 1.82 |     |       25 |     142 | 1.62 |     | 45       | 161     | 1.83 |
|        6 |     136 | 1.55 |     |       26 |     148 | 1.68 |     | 46       | 165     | 1.88 |
|        7 |     138 | 1.57 |     |       27 |     147 | 1.67 |     | 47       | 161     | 1.83 |
|        8 |     172 | 1.96 |     |       28 |     140 | 1.59 |     | 48       | 170     | 1.93 |
|        9 |     177 | 2.01 |     |       29 |     167 | 1.9  |     | 49       | 161     | 1.83 |
|       10 |     148 | 1.68 |     |       30 |     142 | 1.62 |     | 50       | 159     | 1.81 |
|       11 |     164 | 1.87 |     |       31 |     167 | 1.9  |     | 51       | 183     | 2.08 |
|       12 |     166 | 1.89 |     |       32 |     164 | 1.87 |     | 52       | 165     | 1.88 |
|       13 |     152 | 1.73 |     |       33 |     160 | 1.82 |     | 53       | 169     | 1.92 |
|       14 |     159 | 1.81 |     |       34 |     181 | 2.06 |     | 54       | 149     | 1.69 |
|       15 |     150 | 1.71 |     |       35 |     157 | 1.79 |     | 55       | 158     | 1.8  |
|       16 |     149 | 1.69 |     |       36 |     150 | 1.71 |     |          |         |      |
|       17 |     148 | 1.68 |     |       37 |     145 | 1.65 |     |          |         |      |
|       18 |     163 | 1.85 |     |       38 |     149 | 1.69 |     |          |         |      |
|       19 |     162 | 1.84 |     |       39 |     153 | 1.74 |     |          |         |      |
|       20 |     168 | 1.91 |     |       40 |     174 | 1.98 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.2  |     |       24 |       3 | 3.3 |     | 46       | 4       | 4.4 |
|        2 |       2 | 2.2  |     |       25 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        3 |       2 | 2.2  |     |       26 |       3 | 3.3 |     | 53       | 1       | 1.1 |
|        5 |       1 | 1.1  |     |       27 |       3 | 3.3 |     | 55       | 2       | 2.2 |
|        7 |       3 | 3.3  |     |       29 |       1 | 1.1 |     |          |         |     |
|        8 |       7 | 7.69 |     |       30 |       2 | 2.2 |     |          |         |     |
|        9 |       1 | 1.1  |     |       31 |       1 | 1.1 |     |          |         |     |
|       11 |       1 | 1.1  |     |       33 |       1 | 1.1 |     |          |         |     |
|       12 |       1 | 1.1  |     |       34 |       2 | 2.2 |     |          |         |     |
|       13 |       2 | 2.2  |     |       35 |       2 | 2.2 |     |          |         |     |
|       14 |       2 | 2.2  |     |       36 |       3 | 3.3 |     |          |         |     |
|       15 |       1 | 1.1  |     |       37 |       2 | 2.2 |     |          |         |     |
|       16 |       1 | 1.1  |     |       38 |       4 | 4.4 |     |          |         |     |
|       17 |       2 | 2.2  |     |       39 |       3 | 3.3 |     |          |         |     |
|       18 |       1 | 1.1  |     |       40 |       2 | 2.2 |     |          |         |     |
|       19 |       4 | 4.4  |     |       41 |       1 | 1.1 |     |          |         |     |
|       20 |       2 | 2.2  |     |       42 |       2 | 2.2 |     |          |         |     |
|       21 |       1 | 1.1  |     |       43 |       4 | 4.4 |     |          |         |     |
|       22 |       3 | 3.3  |     |       44 |       1 | 1.1 |     |          |         |     |
|       23 |       1 | 1.1  |     |       45 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.2  |     |       23 |       2 | 1.1  |     | 44       | 5       | 2.75 |
|        2 |       5 | 2.75 |     |       24 |       5 | 2.75 |     | 45       | 4       | 2.2  |
|        3 |       2 | 1.1  |     |       25 |       2 | 1.1  |     | 46       | 5       | 2.75 |
|        5 |       3 | 1.65 |     |       26 |       4 | 2.2  |     | 47       | 1       | 0.55 |
|        6 |       2 | 1.1  |     |       27 |       4 | 2.2  |     | 48       | 1       | 0.55 |
|        7 |       4 | 2.2  |     |       28 |       2 | 1.1  |     | 49       | 2       | 1.1  |
|        8 |       7 | 3.85 |     |       29 |       1 | 0.55 |     | 50       | 2       | 1.1  |
|        9 |       6 | 3.3  |     |       30 |       6 | 3.3  |     | 51       | 2       | 1.1  |
|       11 |       2 | 1.1  |     |       31 |       4 | 2.2  |     | 52       | 4       | 2.2  |
|       12 |       1 | 0.55 |     |       33 |       2 | 1.1  |     | 53       | 3       | 1.65 |
|       13 |       3 | 1.65 |     |       34 |       6 | 3.3  |     | 55       | 4       | 2.2  |
|       14 |       3 | 1.65 |     |       35 |       4 | 2.2  |     |          |         |      |
|       15 |       2 | 1.1  |     |       36 |       4 | 2.2  |     |          |         |      |
|       16 |       4 | 2.2  |     |       37 |       2 | 1.1  |     |          |         |      |
|       17 |       5 | 2.75 |     |       38 |       5 | 2.75 |     |          |         |      |
|       18 |       2 | 1.1  |     |       39 |       4 | 2.2  |     |          |         |      |
|       19 |       8 | 4.4  |     |       40 |       5 | 2.75 |     |          |         |      |
|       20 |       3 | 1.65 |     |       41 |       2 | 1.1  |     |          |         |      |
|       21 |       2 | 1.1  |     |       42 |       4 | 2.2  |     |          |         |      |
|       22 |       6 | 3.3  |     |       43 |       7 | 3.85 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.83 |     |       21 |       2 | 0.73 |     | 41       | 3       | 1.1  |
|        2 |       5 | 1.83 |     |       22 |       7 | 2.56 |     | 42       | 5       | 1.83 |
|        3 |       2 | 0.73 |     |       23 |       4 | 1.47 |     | 43       | 9       | 3.3  |
|        4 |       1 | 0.37 |     |       24 |       9 | 3.3  |     | 44       | 7       | 2.56 |
|        5 |       8 | 2.93 |     |       25 |       2 | 0.73 |     | 45       | 7       | 2.56 |
|        6 |       5 | 1.83 |     |       26 |       5 | 1.83 |     | 46       | 6       | 2.2  |
|        7 |       4 | 1.47 |     |       27 |       4 | 1.47 |     | 47       | 3       | 1.1  |
|        8 |      10 | 3.66 |     |       28 |       5 | 1.83 |     | 48       | 4       | 1.47 |
|        9 |       9 | 3.3  |     |       29 |       4 | 1.47 |     | 49       | 3       | 1.1  |
|       10 |       4 | 1.47 |     |       30 |       7 | 2.56 |     | 50       | 2       | 0.73 |
|       11 |       2 | 0.73 |     |       31 |       7 | 2.56 |     | 51       | 5       | 1.83 |
|       12 |       2 | 0.73 |     |       32 |       3 | 1.1  |     | 52       | 6       | 2.2  |
|       13 |       3 | 1.1  |     |       33 |       5 | 1.83 |     | 53       | 5       | 1.83 |
|       14 |       4 | 1.47 |     |       34 |       9 | 3.3  |     | 54       | 1       | 0.37 |
|       15 |       3 | 1.1  |     |       35 |       6 | 2.2  |     | 55       | 5       | 1.83 |
|       16 |       5 | 1.83 |     |       36 |       7 | 2.56 |     |          |         |      |
|       17 |       7 | 2.56 |     |       37 |       4 | 1.47 |     |          |         |      |
|       18 |       3 | 1.1  |     |       38 |       5 | 1.83 |     |          |         |      |
|       19 |       9 | 3.3  |     |       39 |       6 | 2.2  |     |          |         |      |
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

