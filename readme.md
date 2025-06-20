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
| Power 655 |          1205 | 2017-08-01   | 2025-06-19 |            1205 | 00001      | 01205       |
| Power 645 |          1172 | 2017-10-25   | 2025-06-20 |            1172 | 00198      | 01369       |
| Keno      |           908 | 2022-12-04   | 2025-06-02 |          129077 | #0110271   | #0239906    |
| 3D        |           937 | 2019-04-22   | 2025-06-13 |             937 | 00001      | 00937       |
| 3D Pro    |           586 | 2021-09-14   | 2025-06-19 |             586 | 00001      | 00586       |
| Bingo18   |             8 | 2024-12-03   | 2025-06-20 |             112 | 0083144    | 0114792     |

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
| 2025-06-19 | 01205 | [3, 5, 9, 10, 16, 47, 34]    |      0 | 2025-06-19 19:00:12.105342 |
| 2025-06-17 | 01204 | [7, 13, 18, 22, 32, 44, 43]  |      0 | 2025-06-17 19:00:14.248629 |
| 2025-06-14 | 01203 | [11, 12, 22, 26, 41, 47, 24] |      0 | 2025-06-15 19:00:27.381690 |
| 2025-06-12 | 01202 | [6, 8, 16, 18, 34, 44, 17]   |      0 | 2025-06-12 19:00:09.940893 |
| 2025-06-10 | 01201 | [3, 6, 21, 29, 40, 41, 37]   |      0 | 2025-06-11 19:00:17.010268 |
| 2025-06-07 | 01200 | [12, 17, 21, 46, 48, 52, 45] |      0 | 2025-06-08 19:00:23.946470 |
| 2025-06-05 | 01199 | [14, 21, 33, 37, 46, 49, 34] |      0 | 2025-06-05 19:00:16.186371 |
| 2025-06-03 | 01198 | [2, 11, 14, 16, 27, 38, 51]  |      0 | 2025-06-03 19:01:13.225100 |
| 2025-05-31 | 01197 | [6, 24, 41, 45, 49, 55, 8]   |      0 | 2025-05-31 19:00:15.708033 |
| 2025-05-29 | 01196 | [9, 37, 42, 45, 46, 50, 14]  |      0 | 2025-05-29 19:00:15.005246 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     166 | 1.97 |     |       21 |     151 | 1.79 |     | 41       | 183     | 2.17 |
|        2 |     140 | 1.66 |     |       22 |     173 | 2.05 |     | 42       | 157     | 1.86 |
|        3 |     165 | 1.96 |     |       23 |     167 | 1.98 |     | 43       | 171     | 2.03 |
|        4 |     131 | 1.55 |     |       24 |     154 | 1.83 |     | 44       | 159     | 1.89 |
|        5 |     152 | 1.8  |     |       25 |     139 | 1.65 |     | 45       | 150     | 1.78 |
|        6 |     130 | 1.54 |     |       26 |     142 | 1.68 |     | 46       | 159     | 1.89 |
|        7 |     134 | 1.59 |     |       27 |     140 | 1.66 |     | 47       | 158     | 1.87 |
|        8 |     161 | 1.91 |     |       28 |     135 | 1.6  |     | 48       | 162     | 1.92 |
|        9 |     167 | 1.98 |     |       29 |     162 | 1.92 |     | 49       | 158     | 1.87 |
|       10 |     143 | 1.7  |     |       30 |     133 | 1.58 |     | 50       | 155     | 1.84 |
|       11 |     160 | 1.9  |     |       31 |     157 | 1.86 |     | 51       | 175     | 2.07 |
|       12 |     162 | 1.92 |     |       32 |     158 | 1.87 |     | 52       | 158     | 1.87 |
|       13 |     147 | 1.74 |     |       33 |     152 | 1.8  |     | 53       | 160     | 1.9  |
|       14 |     153 | 1.81 |     |       34 |     170 | 2.02 |     | 54       | 145     | 1.72 |
|       15 |     144 | 1.71 |     |       35 |     151 | 1.79 |     | 55       | 152     | 1.8  |
|       16 |     143 | 1.7  |     |       36 |     142 | 1.68 |     |          |         |      |
|       17 |     141 | 1.67 |     |       37 |     141 | 1.67 |     |          |         |      |
|       18 |     156 | 1.85 |     |       38 |     144 | 1.71 |     |          |         |      |
|       19 |     152 | 1.8  |     |       39 |     146 | 1.73 |     |          |         |      |
|       20 |     162 | 1.92 |     |       40 |     166 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.1 |     |       22 |       3 | 3.3 |     | 49       | 2       | 2.2 |
|        3 |       3 | 3.3 |     |       24 |       2 | 2.2 |     | 50       | 1       | 1.1 |
|        4 |       1 | 1.1 |     |       26 |       1 | 1.1 |     | 51       | 1       | 1.1 |
|        5 |       1 | 1.1 |     |       27 |       2 | 2.2 |     | 52       | 1       | 1.1 |
|        6 |       3 | 3.3 |     |       29 |       1 | 1.1 |     | 55       | 3       | 3.3 |
|        7 |       1 | 1.1 |     |       30 |       1 | 1.1 |     |          |         |     |
|        8 |       2 | 2.2 |     |       32 |       1 | 1.1 |     |          |         |     |
|        9 |       3 | 3.3 |     |       33 |       1 | 1.1 |     |          |         |     |
|       10 |       1 | 1.1 |     |       34 |       3 | 3.3 |     |          |         |     |
|       11 |       2 | 2.2 |     |       37 |       3 | 3.3 |     |          |         |     |
|       12 |       3 | 3.3 |     |       38 |       1 | 1.1 |     |          |         |     |
|       13 |       1 | 1.1 |     |       40 |       1 | 1.1 |     |          |         |     |
|       14 |       4 | 4.4 |     |       41 |       4 | 4.4 |     |          |         |     |
|       15 |       1 | 1.1 |     |       42 |       2 | 2.2 |     |          |         |     |
|       16 |       3 | 3.3 |     |       43 |       1 | 1.1 |     |          |         |     |
|       17 |       2 | 2.2 |     |       44 |       3 | 3.3 |     |          |         |     |
|       18 |       3 | 3.3 |     |       45 |       4 | 4.4 |     |          |         |     |
|       19 |       2 | 2.2 |     |       46 |       3 | 3.3 |     |          |         |     |
|       20 |       1 | 1.1 |     |       47 |       3 | 3.3 |     |          |         |     |
|       21 |       3 | 3.3 |     |       48 |       2 | 2.2 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.55 |     |       21 |       6 | 3.3  |     | 43       | 3       | 1.65 |
|        2 |       3 | 1.65 |     |       22 |       3 | 1.65 |     | 44       | 5       | 2.75 |
|        3 |       6 | 3.3  |     |       23 |       1 | 0.55 |     | 45       | 6       | 3.3  |
|        4 |       1 | 0.55 |     |       24 |       4 | 2.2  |     | 46       | 3       | 1.65 |
|        5 |       2 | 1.1  |     |       25 |       2 | 1.1  |     | 47       | 7       | 3.85 |
|        6 |       4 | 2.2  |     |       26 |       3 | 1.65 |     | 48       | 4       | 2.2  |
|        7 |       4 | 2.2  |     |       27 |       3 | 1.65 |     | 49       | 3       | 1.65 |
|        8 |       3 | 1.65 |     |       28 |       3 | 1.65 |     | 50       | 4       | 2.2  |
|        9 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 51       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       30 |       2 | 1.1  |     | 52       | 3       | 1.65 |
|       11 |       2 | 1.1  |     |       31 |       1 | 0.55 |     | 54       | 2       | 1.1  |
|       12 |       4 | 2.2  |     |       32 |       2 | 1.1  |     | 55       | 4       | 2.2  |
|       13 |       2 | 1.1  |     |       33 |       2 | 1.1  |     |          |         |      |
|       14 |       6 | 3.3  |     |       34 |       4 | 2.2  |     |          |         |      |
|       15 |       7 | 3.85 |     |       37 |       5 | 2.75 |     |          |         |      |
|       16 |       6 | 3.3  |     |       38 |       2 | 1.1  |     |          |         |      |
|       17 |       3 | 1.65 |     |       39 |       4 | 2.2  |     |          |         |      |
|       18 |       4 | 2.2  |     |       40 |       3 | 1.65 |     |          |         |      |
|       19 |       6 | 3.3  |     |       41 |       7 | 3.85 |     |          |         |      |
|       20 |       1 | 0.55 |     |       42 |       4 | 2.2  |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 0.73 |     |       21 |       7 | 2.56 |     | 41       | 12      | 4.4  |
|        2 |       4 | 1.47 |     |       22 |       3 | 1.1  |     | 42       | 10      | 3.66 |
|        3 |       8 | 2.93 |     |       23 |       6 | 2.2  |     | 43       | 6       | 2.2  |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 6       | 2.2  |
|        5 |       3 | 1.1  |     |       25 |       3 | 1.1  |     | 45       | 6       | 2.2  |
|        6 |       4 | 1.47 |     |       26 |       5 | 1.83 |     | 46       | 3       | 1.1  |
|        7 |       5 | 1.83 |     |       27 |       4 | 1.47 |     | 47       | 8       | 2.93 |
|        8 |       4 | 1.47 |     |       28 |       3 | 1.1  |     | 48       | 5       | 1.83 |
|        9 |       5 | 1.83 |     |       29 |       8 | 2.93 |     | 49       | 5       | 1.83 |
|       10 |       3 | 1.1  |     |       30 |       4 | 1.47 |     | 50       | 6       | 2.2  |
|       11 |       3 | 1.1  |     |       31 |       2 | 0.73 |     | 51       | 3       | 1.1  |
|       12 |       4 | 1.47 |     |       32 |       5 | 1.83 |     | 52       | 5       | 1.83 |
|       13 |       5 | 1.83 |     |       33 |       3 | 1.1  |     | 53       | 2       | 0.73 |
|       14 |      11 | 4.03 |     |       34 |       6 | 2.2  |     | 54       | 3       | 1.1  |
|       15 |       9 | 3.3  |     |       35 |       1 | 0.37 |     | 55       | 5       | 1.83 |
|       16 |       6 | 2.2  |     |       36 |       2 | 0.73 |     |          |         |      |
|       17 |       5 | 1.83 |     |       37 |       7 | 2.56 |     |          |         |      |
|       18 |       4 | 1.47 |     |       38 |       3 | 1.1  |     |          |         |      |
|       19 |       8 | 2.93 |     |       39 |       6 | 2.2  |     |          |         |      |
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

