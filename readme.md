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
| Power 655 |          1198 | 2017-08-01   | 2025-06-03 |            1198 | 00001      | 01198       |
| Power 645 |          1165 | 2017-10-25   | 2025-06-04 |            1165 | 00198      | 01362       |
| Keno      |           908 | 2022-12-04   | 2025-06-02 |          129077 | #0110271   | #0239906    |
| 3D        |           931 | 2019-04-22   | 2025-06-04 |             931 | 00001      | 00933       |
| 3D Pro    |           577 | 2021-09-14   | 2025-06-03 |             577 | 00001      | 00579       |

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
| 2025-06-03 | 01198 | [2, 11, 14, 16, 27, 38, 51]  |      0 | 2025-06-03 19:01:13.225100 |
| 2025-05-31 | 01197 | [6, 24, 41, 45, 49, 55, 8]   |      0 | 2025-05-31 19:00:15.708033 |
| 2025-05-29 | 01196 | [9, 37, 42, 45, 46, 50, 14]  |      0 | 2025-05-29 19:00:15.005246 |
| 2025-05-27 | 01195 | [4, 12, 18, 19, 44, 48, 42]  |      0 | 2025-05-27 19:00:27.363743 |
| 2025-05-24 | 01194 | [19, 20, 27, 30, 45, 55, 15] |      0 | 2025-05-26 19:00:21.730573 |
| 2025-05-22 | 01193 | [3, 9, 14, 41, 47, 55, 22]   |      0 | 2025-05-22 19:01:11.003151 |
| 2025-05-20 | 01192 | [19, 27, 44, 45, 47, 52, 15] |      0 | 2025-05-20 19:00:19.102116 |
| 2025-05-17 | 01191 | [2, 7, 26, 29, 41, 50, 43]   |      0 | 2025-05-19 09:08:44.622335 |
| 2025-05-15 | 01190 | [6, 9, 13, 44, 49, 54, 47]   |      0 | 2025-05-19 09:08:44.622459 |
| 2025-05-13 | 01189 | [3, 7, 24, 39, 54, 55, 42]   |      0 | 2025-05-19 09:08:44.622555 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     166 | 1.98 |     |       21 |     148 | 1.77 |     | 41       | 181     | 2.16 |
|        2 |     140 | 1.67 |     |       22 |     171 | 2.04 |     | 42       | 157     | 1.87 |
|        3 |     163 | 1.94 |     |       23 |     167 | 1.99 |     | 43       | 170     | 2.03 |
|        4 |     131 | 1.56 |     |       24 |     153 | 1.82 |     | 44       | 157     | 1.87 |
|        5 |     151 | 1.8  |     |       25 |     139 | 1.66 |     | 45       | 149     | 1.78 |
|        6 |     128 | 1.53 |     |       26 |     141 | 1.68 |     | 46       | 157     | 1.87 |
|        7 |     133 | 1.59 |     |       27 |     140 | 1.67 |     | 47       | 156     | 1.86 |
|        8 |     160 | 1.91 |     |       28 |     135 | 1.61 |     | 48       | 161     | 1.92 |
|        9 |     166 | 1.98 |     |       29 |     161 | 1.92 |     | 49       | 157     | 1.87 |
|       10 |     142 | 1.69 |     |       30 |     133 | 1.59 |     | 50       | 155     | 1.85 |
|       11 |     159 | 1.9  |     |       31 |     157 | 1.87 |     | 51       | 175     | 2.09 |
|       12 |     160 | 1.91 |     |       32 |     157 | 1.87 |     | 52       | 157     | 1.87 |
|       13 |     146 | 1.74 |     |       33 |     151 | 1.8  |     | 53       | 160     | 1.91 |
|       14 |     152 | 1.81 |     |       34 |     167 | 1.99 |     | 54       | 145     | 1.73 |
|       15 |     144 | 1.72 |     |       35 |     151 | 1.8  |     | 55       | 152     | 1.81 |
|       16 |     141 | 1.68 |     |       36 |     142 | 1.69 |     |          |         |      |
|       17 |     139 | 1.66 |     |       37 |     139 | 1.66 |     |          |         |      |
|       18 |     154 | 1.84 |     |       38 |     144 | 1.72 |     |          |         |      |
|       19 |     152 | 1.81 |     |       39 |     146 | 1.74 |     |          |         |      |
|       20 |     162 | 1.93 |     |       40 |     165 | 1.97 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        2 |       2 | 2.2 |     |       25 |       1 | 1.1 |     | 51       | 2       | 2.2 |
|        3 |       2 | 2.2 |     |       26 |       1 | 1.1 |     | 52       | 1       | 1.1 |
|        4 |       1 | 1.1 |     |       27 |       3 | 3.3 |     | 54       | 2       | 2.2 |
|        5 |       1 | 1.1 |     |       28 |       2 | 2.2 |     | 55       | 4       | 4.4 |
|        6 |       2 | 2.2 |     |       29 |       2 | 2.2 |     |          |         |     |
|        7 |       3 | 3.3 |     |       30 |       2 | 2.2 |     |          |         |     |
|        8 |       2 | 2.2 |     |       34 |       1 | 1.1 |     |          |         |     |
|        9 |       3 | 3.3 |     |       37 |       2 | 2.2 |     |          |         |     |
|       11 |       1 | 1.1 |     |       38 |       1 | 1.1 |     |          |         |     |
|       12 |       2 | 2.2 |     |       39 |       3 | 3.3 |     |          |         |     |
|       13 |       1 | 1.1 |     |       41 |       3 | 3.3 |     |          |         |     |
|       14 |       4 | 4.4 |     |       42 |       3 | 3.3 |     |          |         |     |
|       15 |       3 | 3.3 |     |       43 |       1 | 1.1 |     |          |         |     |
|       16 |       3 | 3.3 |     |       44 |       3 | 3.3 |     |          |         |     |
|       18 |       1 | 1.1 |     |       45 |       4 | 4.4 |     |          |         |     |
|       19 |       4 | 4.4 |     |       46 |       1 | 1.1 |     |          |         |     |
|       20 |       1 | 1.1 |     |       47 |       3 | 3.3 |     |          |         |     |
|       21 |       1 | 1.1 |     |       48 |       1 | 1.1 |     |          |         |     |
|       22 |       1 | 1.1 |     |       49 |       2 | 2.2 |     |          |         |     |
|       24 |       2 | 2.2 |     |       50 |       3 | 3.3 |     |          |         |     |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.1  |     |       21 |       3 | 1.65 |     | 42       | 8       | 4.4  |
|        2 |       3 | 1.65 |     |       22 |       1 | 0.55 |     | 43       | 5       | 2.75 |
|        3 |       6 | 3.3  |     |       23 |       4 | 2.2  |     | 44       | 3       | 1.65 |
|        4 |       1 | 0.55 |     |       24 |       4 | 2.2  |     | 45       | 5       | 2.75 |
|        5 |       2 | 1.1  |     |       25 |       2 | 1.1  |     | 46       | 1       | 0.55 |
|        6 |       2 | 1.1  |     |       26 |       2 | 1.1  |     | 47       | 5       | 2.75 |
|        7 |       4 | 2.2  |     |       27 |       4 | 2.2  |     | 48       | 3       | 1.65 |
|        8 |       3 | 1.65 |     |       28 |       3 | 1.65 |     | 49       | 4       | 2.2  |
|        9 |       4 | 2.2  |     |       29 |       4 | 2.2  |     | 50       | 4       | 2.2  |
|       10 |       2 | 1.1  |     |       30 |       2 | 1.1  |     | 51       | 2       | 1.1  |
|       11 |       2 | 1.1  |     |       31 |       2 | 1.1  |     | 52       | 3       | 1.65 |
|       12 |       2 | 1.1  |     |       32 |       3 | 1.65 |     | 53       | 1       | 0.55 |
|       13 |       3 | 1.65 |     |       33 |       1 | 0.55 |     | 54       | 2       | 1.1  |
|       14 |       7 | 3.85 |     |       34 |       2 | 1.1  |     | 55       | 5       | 2.75 |
|       15 |       8 | 4.4  |     |       36 |       1 | 0.55 |     |          |         |      |
|       16 |       4 | 2.2  |     |       37 |       5 | 2.75 |     |          |         |      |
|       17 |       2 | 1.1  |     |       38 |       3 | 1.65 |     |          |         |      |
|       18 |       2 | 1.1  |     |       39 |       4 | 2.2  |     |          |         |      |
|       19 |       7 | 3.85 |     |       40 |       3 | 1.65 |     |          |         |      |
|       20 |       3 | 1.65 |     |       41 |       9 | 4.95 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.47 |     |       21 |       6 | 2.2  |     | 41       | 12      | 4.4  |
|        2 |       5 | 1.83 |     |       22 |       1 | 0.37 |     | 42       | 11      | 4.03 |
|        3 |       6 | 2.2  |     |       23 |       6 | 2.2  |     | 43       | 8       | 2.93 |
|        4 |       2 | 0.73 |     |       24 |       7 | 2.56 |     | 44       | 5       | 1.83 |
|        5 |       3 | 1.1  |     |       25 |       4 | 1.47 |     | 45       | 6       | 2.2  |
|        6 |       2 | 0.73 |     |       26 |       5 | 1.83 |     | 46       | 1       | 0.37 |
|        7 |       5 | 1.83 |     |       27 |       5 | 1.83 |     | 47       | 6       | 2.2  |
|        8 |       5 | 1.83 |     |       28 |       4 | 1.47 |     | 48       | 5       | 1.83 |
|        9 |       4 | 1.47 |     |       29 |       8 | 2.93 |     | 49       | 4       | 1.47 |
|       10 |       4 | 1.47 |     |       30 |       6 | 2.2  |     | 50       | 8       | 2.93 |
|       11 |       3 | 1.1  |     |       31 |       3 | 1.1  |     | 51       | 4       | 1.47 |
|       12 |       2 | 0.73 |     |       32 |       4 | 1.47 |     | 52       | 5       | 1.83 |
|       13 |       6 | 2.2  |     |       33 |       2 | 0.73 |     | 53       | 3       | 1.1  |
|       14 |      10 | 3.66 |     |       34 |       5 | 1.83 |     | 54       | 3       | 1.1  |
|       15 |      10 | 3.66 |     |       35 |       1 | 0.37 |     | 55       | 6       | 2.2  |
|       16 |       5 | 1.83 |     |       36 |       3 | 1.1  |     |          |         |      |
|       17 |       4 | 1.47 |     |       37 |       6 | 2.2  |     |          |         |      |
|       18 |       3 | 1.1  |     |       38 |       4 | 1.47 |     |          |         |      |
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

