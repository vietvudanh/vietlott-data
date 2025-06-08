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
| Power 655 |          1200 | 2017-08-01   | 2025-06-07 |            1200 | 00001      | 01200       |
| Power 645 |          1167 | 2017-10-25   | 2025-06-08 |            1167 | 00198      | 01364       |
| Keno      |           908 | 2022-12-04   | 2025-06-02 |          129077 | #0110271   | #0239906    |
| 3D        |           932 | 2019-04-22   | 2025-06-06 |             932 | 00001      | 00934       |
| 3D Pro    |           578 | 2021-09-14   | 2025-06-05 |             578 | 00001      | 00580       |

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
| 2025-06-07 | 01200 | [12, 17, 21, 46, 48, 52, 45] |      0 | 2025-06-08T19:00:23.946470 |
| 2025-06-05 | 01199 | [14, 21, 33, 37, 46, 49, 34] |      0 | 2025-06-05 19:00:16.186371 |
| 2025-06-03 | 01198 | [2, 11, 14, 16, 27, 38, 51]  |      0 | 2025-06-03 19:01:13.225100 |
| 2025-05-31 | 01197 | [6, 24, 41, 45, 49, 55, 8]   |      0 | 2025-05-31 19:00:15.708033 |
| 2025-05-29 | 01196 | [9, 37, 42, 45, 46, 50, 14]  |      0 | 2025-05-29 19:00:15.005246 |
| 2025-05-27 | 01195 | [4, 12, 18, 19, 44, 48, 42]  |      0 | 2025-05-27 19:00:27.363743 |
| 2025-05-24 | 01194 | [19, 20, 27, 30, 45, 55, 15] |      0 | 2025-05-26 19:00:21.730573 |
| 2025-05-22 | 01193 | [3, 9, 14, 41, 47, 55, 22]   |      0 | 2025-05-22 19:01:11.003151 |
| 2025-05-20 | 01192 | [19, 27, 44, 45, 47, 52, 15] |      0 | 2025-05-20 19:00:19.102116 |
| 2025-05-17 | 01191 | [2, 7, 26, 29, 41, 50, 43]   |      0 | 2025-05-19 09:08:44.622335 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     166 | 1.98 |     |       21 |     150 | 1.79 |     | 41       | 181     | 2.16 |
|        2 |     140 | 1.67 |     |       22 |     171 | 2.04 |     | 42       | 157     | 1.87 |
|        3 |     163 | 1.94 |     |       23 |     167 | 1.99 |     | 43       | 170     | 2.02 |
|        4 |     131 | 1.56 |     |       24 |     153 | 1.82 |     | 44       | 157     | 1.87 |
|        5 |     151 | 1.8  |     |       25 |     139 | 1.65 |     | 45       | 150     | 1.79 |
|        6 |     128 | 1.52 |     |       26 |     141 | 1.68 |     | 46       | 159     | 1.89 |
|        7 |     133 | 1.58 |     |       27 |     140 | 1.67 |     | 47       | 156     | 1.86 |
|        8 |     160 | 1.9  |     |       28 |     135 | 1.61 |     | 48       | 162     | 1.93 |
|        9 |     166 | 1.98 |     |       29 |     161 | 1.92 |     | 49       | 158     | 1.88 |
|       10 |     142 | 1.69 |     |       30 |     133 | 1.58 |     | 50       | 155     | 1.85 |
|       11 |     159 | 1.89 |     |       31 |     157 | 1.87 |     | 51       | 175     | 2.08 |
|       12 |     161 | 1.92 |     |       32 |     157 | 1.87 |     | 52       | 158     | 1.88 |
|       13 |     146 | 1.74 |     |       33 |     152 | 1.81 |     | 53       | 160     | 1.9  |
|       14 |     153 | 1.82 |     |       34 |     168 | 2    |     | 54       | 145     | 1.73 |
|       15 |     144 | 1.71 |     |       35 |     151 | 1.8  |     | 55       | 152     | 1.81 |
|       16 |     141 | 1.68 |     |       36 |     142 | 1.69 |     |          |         |      |
|       17 |     140 | 1.67 |     |       37 |     140 | 1.67 |     |          |         |      |
|       18 |     154 | 1.83 |     |       38 |     144 | 1.71 |     |          |         |      |
|       19 |     152 | 1.81 |     |       39 |     146 | 1.74 |     |          |         |      |
|       20 |     162 | 1.93 |     |       40 |     165 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        2 |       2 | 2.2 |     |       26 |       1 | 1.1  |     | 51       | 2       | 2.2 |
|        3 |       2 | 2.2 |     |       27 |       3 | 3.3  |     | 52       | 2       | 2.2 |
|        4 |       1 | 1.1 |     |       28 |       1 | 1.1  |     | 54       | 2       | 2.2 |
|        6 |       2 | 2.2 |     |       29 |       1 | 1.1  |     | 55       | 4       | 4.4 |
|        7 |       3 | 3.3 |     |       30 |       1 | 1.1  |     |          |         |     |
|        8 |       1 | 1.1 |     |       33 |       1 | 1.1  |     |          |         |     |
|        9 |       3 | 3.3 |     |       34 |       2 | 2.2  |     |          |         |     |
|       11 |       1 | 1.1 |     |       37 |       2 | 2.2  |     |          |         |     |
|       12 |       2 | 2.2 |     |       38 |       1 | 1.1  |     |          |         |     |
|       13 |       1 | 1.1 |     |       39 |       1 | 1.1  |     |          |         |     |
|       14 |       4 | 4.4 |     |       41 |       3 | 3.3  |     |          |         |     |
|       15 |       3 | 3.3 |     |       42 |       3 | 3.3  |     |          |         |     |
|       16 |       2 | 2.2 |     |       43 |       1 | 1.1  |     |          |         |     |
|       17 |       1 | 1.1 |     |       44 |       3 | 3.3  |     |          |         |     |
|       18 |       1 | 1.1 |     |       45 |       5 | 5.49 |     |          |         |     |
|       19 |       4 | 4.4 |     |       46 |       3 | 3.3  |     |          |         |     |
|       20 |       1 | 1.1 |     |       47 |       3 | 3.3  |     |          |         |     |
|       21 |       2 | 2.2 |     |       48 |       2 | 2.2  |     |          |         |     |
|       22 |       1 | 1.1 |     |       49 |       3 | 3.3  |     |          |         |     |
|       24 |       2 | 2.2 |     |       50 |       2 | 2.2  |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.1  |     |       21 |       5 | 2.75 |     | 42       | 7       | 3.85 |
|        2 |       3 | 1.65 |     |       22 |       1 | 0.55 |     | 43       | 4       | 2.2  |
|        3 |       5 | 2.75 |     |       23 |       3 | 1.65 |     | 44       | 3       | 1.65 |
|        4 |       1 | 0.55 |     |       24 |       4 | 2.2  |     | 45       | 6       | 3.3  |
|        5 |       2 | 1.1  |     |       25 |       2 | 1.1  |     | 46       | 3       | 1.65 |
|        6 |       2 | 1.1  |     |       26 |       2 | 1.1  |     | 47       | 5       | 2.75 |
|        7 |       3 | 1.65 |     |       27 |       4 | 2.2  |     | 48       | 4       | 2.2  |
|        8 |       3 | 1.65 |     |       28 |       3 | 1.65 |     | 49       | 5       | 2.75 |
|        9 |       3 | 1.65 |     |       29 |       3 | 1.65 |     | 50       | 4       | 2.2  |
|       10 |       2 | 1.1  |     |       30 |       2 | 1.1  |     | 51       | 2       | 1.1  |
|       11 |       2 | 1.1  |     |       31 |       1 | 0.55 |     | 52       | 4       | 2.2  |
|       12 |       3 | 1.65 |     |       32 |       2 | 1.1  |     | 54       | 2       | 1.1  |
|       13 |       2 | 1.1  |     |       33 |       2 | 1.1  |     | 55       | 5       | 2.75 |
|       14 |       8 | 4.4  |     |       34 |       2 | 1.1  |     |          |         |      |
|       15 |       8 | 4.4  |     |       36 |       1 | 0.55 |     |          |         |      |
|       16 |       4 | 2.2  |     |       37 |       6 | 3.3  |     |          |         |      |
|       17 |       3 | 1.65 |     |       38 |       3 | 1.65 |     |          |         |      |
|       18 |       2 | 1.1  |     |       39 |       4 | 2.2  |     |          |         |      |
|       19 |       7 | 3.85 |     |       40 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       41 |       7 | 3.85 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       7 | 2.56 |     | 41       | 11      | 4.03 |
|        2 |       5 | 1.83 |     |       22 |       1 | 0.37 |     | 42       | 11      | 4.03 |
|        3 |       6 | 2.2  |     |       23 |       6 | 2.2  |     | 43       | 6       | 2.2  |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 5       | 1.83 |
|        5 |       2 | 0.73 |     |       25 |       4 | 1.47 |     | 45       | 6       | 2.2  |
|        6 |       2 | 0.73 |     |       26 |       4 | 1.47 |     | 46       | 3       | 1.1  |
|        7 |       5 | 1.83 |     |       27 |       5 | 1.83 |     | 47       | 6       | 2.2  |
|        8 |       4 | 1.47 |     |       28 |       4 | 1.47 |     | 48       | 5       | 1.83 |
|        9 |       4 | 1.47 |     |       29 |       8 | 2.93 |     | 49       | 5       | 1.83 |
|       10 |       2 | 0.73 |     |       30 |       6 | 2.2  |     | 50       | 8       | 2.93 |
|       11 |       3 | 1.1  |     |       31 |       3 | 1.1  |     | 51       | 3       | 1.1  |
|       12 |       3 | 1.1  |     |       32 |       4 | 1.47 |     | 52       | 6       | 2.2  |
|       13 |       6 | 2.2  |     |       33 |       3 | 1.1  |     | 53       | 3       | 1.1  |
|       14 |      11 | 4.03 |     |       34 |       6 | 2.2  |     | 54       | 3       | 1.1  |
|       15 |       9 | 3.3  |     |       35 |       1 | 0.37 |     | 55       | 6       | 2.2  |
|       16 |       5 | 1.83 |     |       36 |       3 | 1.1  |     |          |         |      |
|       17 |       5 | 1.83 |     |       37 |       7 | 2.56 |     |          |         |      |
|       18 |       3 | 1.1  |     |       38 |       3 | 1.1  |     |          |         |      |
|       19 |       8 | 2.93 |     |       39 |       7 | 2.56 |     |          |         |      |
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

