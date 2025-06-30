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
| Power 655 |          1209 | 2017-08-01   | 2025-06-28 |            1209 | 00001      | 01209       |
| Power 645 |          1176 | 2017-10-25   | 2025-06-29 |            1176 | 00198      | 01373       |
| Keno      |           936 | 2022-12-04   | 2025-06-30 |          132324 | #0110271   | #0243221    |
| 3D        |           943 | 2019-04-22   | 2025-06-27 |             943 | 00001      | 00943       |
| 3D Pro    |           590 | 2021-09-14   | 2025-06-28 |             590 | 00001      | 00590       |
| Bingo18   |           205 | 2024-12-03   | 2025-06-30 |           32265 | 0083123    | 0116359     |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                     | predicted               |
|:-----------|:---------------------------|:------------------------|
| 2023-08-01 | [4, 18, 22, 25, 33, 48, 2] | [16, 2, 25, 22, 18, 33] |



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-06-28 | 01209 | [8, 11, 13, 20, 45, 50, 25]  |      0 | 2025-06-30 15:30:00.150910 |
| 2025-06-26 | 01208 | [1, 14, 16, 27, 40, 51, 2]   |      0 | 2025-06-30 15:30:00.151037 |
| 2025-06-24 | 01207 | [3, 9, 18, 20, 30, 53, 48]   |      0 | 2025-06-30 15:30:00.151131 |
| 2025-06-21 | 01206 | [6, 10, 15, 43, 44, 53, 32]  |      0 | 2025-06-22 19:00:16.907461 |
| 2025-06-19 | 01205 | [3, 5, 9, 10, 16, 47, 34]    |      0 | 2025-06-19 19:00:12.105342 |
| 2025-06-17 | 01204 | [7, 13, 18, 22, 32, 44, 43]  |      0 | 2025-06-17 19:00:14.248629 |
| 2025-06-14 | 01203 | [11, 12, 22, 26, 41, 47, 24] |      0 | 2025-06-15 19:00:27.381690 |
| 2025-06-12 | 01202 | [6, 8, 16, 18, 34, 44, 17]   |      0 | 2025-06-12 19:00:09.940893 |
| 2025-06-10 | 01201 | [3, 6, 21, 29, 40, 41, 37]   |      0 | 2025-06-11 19:00:17.010268 |
| 2025-06-07 | 01200 | [12, 17, 21, 46, 48, 52, 45] |      0 | 2025-06-08 19:00:23.946470 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     167 | 1.97 |     |       21 |     151 | 1.78 |     | 41       | 183     | 2.16 |
|        2 |     141 | 1.67 |     |       22 |     173 | 2.04 |     | 42       | 157     | 1.86 |
|        3 |     166 | 1.96 |     |       23 |     167 | 1.97 |     | 43       | 172     | 2.03 |
|        4 |     131 | 1.55 |     |       24 |     154 | 1.82 |     | 44       | 160     | 1.89 |
|        5 |     152 | 1.8  |     |       25 |     140 | 1.65 |     | 45       | 151     | 1.78 |
|        6 |     131 | 1.55 |     |       26 |     142 | 1.68 |     | 46       | 159     | 1.88 |
|        7 |     134 | 1.58 |     |       27 |     141 | 1.67 |     | 47       | 158     | 1.87 |
|        8 |     162 | 1.91 |     |       28 |     135 | 1.6  |     | 48       | 163     | 1.93 |
|        9 |     168 | 1.99 |     |       29 |     162 | 1.91 |     | 49       | 158     | 1.87 |
|       10 |     144 | 1.7  |     |       30 |     134 | 1.58 |     | 50       | 156     | 1.84 |
|       11 |     161 | 1.9  |     |       31 |     157 | 1.86 |     | 51       | 176     | 2.08 |
|       12 |     162 | 1.91 |     |       32 |     159 | 1.88 |     | 52       | 158     | 1.87 |
|       13 |     148 | 1.75 |     |       33 |     152 | 1.8  |     | 53       | 162     | 1.91 |
|       14 |     154 | 1.82 |     |       34 |     170 | 2.01 |     | 54       | 145     | 1.71 |
|       15 |     145 | 1.71 |     |       35 |     151 | 1.78 |     | 55       | 152     | 1.8  |
|       16 |     144 | 1.7  |     |       36 |     142 | 1.68 |     |          |         |      |
|       17 |     141 | 1.67 |     |       37 |     141 | 1.67 |     |          |         |      |
|       18 |     157 | 1.86 |     |       38 |     144 | 1.7  |     |          |         |      |
|       19 |     152 | 1.8  |     |       39 |     146 | 1.73 |     |          |         |      |
|       20 |     164 | 1.94 |     |       40 |     167 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1 |     |       24 |       2 | 2.2 |     | 50       | 1       | 1.1 |
|        2 |       2 | 2.2 |     |       25 |       1 | 1.1 |     | 51       | 2       | 2.2 |
|        3 |       3 | 3.3 |     |       26 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        5 |       1 | 1.1 |     |       27 |       2 | 2.2 |     | 53       | 2       | 2.2 |
|        6 |       4 | 4.4 |     |       29 |       1 | 1.1 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1 |     |       30 |       1 | 1.1 |     |          |         |     |
|        8 |       3 | 3.3 |     |       32 |       2 | 2.2 |     |          |         |     |
|        9 |       2 | 2.2 |     |       33 |       1 | 1.1 |     |          |         |     |
|       10 |       2 | 2.2 |     |       34 |       3 | 3.3 |     |          |         |     |
|       11 |       3 | 3.3 |     |       37 |       2 | 2.2 |     |          |         |     |
|       12 |       2 | 2.2 |     |       38 |       1 | 1.1 |     |          |         |     |
|       13 |       2 | 2.2 |     |       40 |       2 | 2.2 |     |          |         |     |
|       14 |       3 | 3.3 |     |       41 |       3 | 3.3 |     |          |         |     |
|       15 |       1 | 1.1 |     |       43 |       2 | 2.2 |     |          |         |     |
|       16 |       4 | 4.4 |     |       44 |       3 | 3.3 |     |          |         |     |
|       17 |       2 | 2.2 |     |       45 |       3 | 3.3 |     |          |         |     |
|       18 |       3 | 3.3 |     |       46 |       2 | 2.2 |     |          |         |     |
|       20 |       2 | 2.2 |     |       47 |       2 | 2.2 |     |          |         |     |
|       21 |       3 | 3.3 |     |       48 |       2 | 2.2 |     |          |         |     |
|       22 |       2 | 2.2 |     |       49 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.55 |     |       21 |       5 | 2.75 |     | 45       | 7       | 3.85 |
|        2 |       3 | 1.65 |     |       22 |       3 | 1.65 |     | 46       | 3       | 1.65 |
|        3 |       6 | 3.3  |     |       24 |       3 | 1.65 |     | 47       | 6       | 3.3  |
|        4 |       1 | 0.55 |     |       25 |       2 | 1.1  |     | 48       | 3       | 1.65 |
|        5 |       2 | 1.1  |     |       26 |       3 | 1.65 |     | 49       | 3       | 1.65 |
|        6 |       5 | 2.75 |     |       27 |       4 | 2.2  |     | 50       | 5       | 2.75 |
|        7 |       4 | 2.2  |     |       28 |       2 | 1.1  |     | 51       | 3       | 1.65 |
|        8 |       4 | 2.2  |     |       29 |       3 | 1.65 |     | 52       | 2       | 1.1  |
|        9 |       5 | 2.75 |     |       30 |       3 | 1.65 |     | 53       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       32 |       2 | 1.1  |     | 54       | 2       | 1.1  |
|       11 |       3 | 1.65 |     |       33 |       1 | 0.55 |     | 55       | 4       | 2.2  |
|       12 |       4 | 2.2  |     |       34 |       4 | 2.2  |     |          |         |      |
|       13 |       3 | 1.65 |     |       37 |       4 | 2.2  |     |          |         |      |
|       14 |       6 | 3.3  |     |       38 |       2 | 1.1  |     |          |         |      |
|       15 |       5 | 2.75 |     |       39 |       3 | 1.65 |     |          |         |      |
|       16 |       6 | 3.3  |     |       40 |       2 | 1.1  |     |          |         |      |
|       17 |       3 | 1.65 |     |       41 |       6 | 3.3  |     |          |         |      |
|       18 |       4 | 2.2  |     |       42 |       4 | 2.2  |     |          |         |      |
|       19 |       6 | 3.3  |     |       43 |       4 | 2.2  |     |          |         |      |
|       20 |       3 | 1.65 |     |       44 |       6 | 3.3  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       6 | 2.2  |     | 42       | 9       | 3.3  |
|        2 |       4 | 1.47 |     |       22 |       3 | 1.1  |     | 43       | 7       | 2.56 |
|        3 |       9 | 3.3  |     |       23 |       4 | 1.47 |     | 44       | 6       | 2.2  |
|        4 |       2 | 0.73 |     |       24 |       6 | 2.2  |     | 45       | 7       | 2.56 |
|        5 |       3 | 1.1  |     |       25 |       3 | 1.1  |     | 46       | 3       | 1.1  |
|        6 |       5 | 1.83 |     |       26 |       4 | 1.47 |     | 47       | 8       | 2.93 |
|        7 |       5 | 1.83 |     |       27 |       5 | 1.83 |     | 48       | 5       | 1.83 |
|        8 |       5 | 1.83 |     |       28 |       3 | 1.1  |     | 49       | 5       | 1.83 |
|        9 |       6 | 2.2  |     |       29 |       6 | 2.2  |     | 50       | 6       | 2.2  |
|       10 |       4 | 1.47 |     |       30 |       4 | 1.47 |     | 51       | 4       | 1.47 |
|       11 |       4 | 1.47 |     |       31 |       2 | 0.73 |     | 52       | 4       | 1.47 |
|       12 |       4 | 1.47 |     |       32 |       5 | 1.83 |     | 53       | 3       | 1.1  |
|       13 |       5 | 1.83 |     |       33 |       3 | 1.1  |     | 54       | 2       | 0.73 |
|       14 |      10 | 3.66 |     |       34 |       6 | 2.2  |     | 55       | 5       | 1.83 |
|       15 |      10 | 3.66 |     |       36 |       1 | 0.37 |     |          |         |      |
|       16 |       7 | 2.56 |     |       37 |       7 | 2.56 |     |          |         |      |
|       17 |       4 | 1.47 |     |       38 |       3 | 1.1  |     |          |         |      |
|       18 |       5 | 1.83 |     |       39 |       5 | 1.83 |     |          |         |      |
|       19 |       7 | 2.56 |     |       40 |       5 | 1.83 |     |          |         |      |
|       20 |       5 | 1.83 |     |       41 |      11 | 4.03 |     |          |         |      |



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

