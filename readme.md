# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![PyPI](https://img.shields.io/pypi/v/vietlott-data.svg)](https://pypi.org/project/vietlott-data/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

## 🎯 Supported Lottery Products

| Product        | Link                                                                                          | Description                |
| -------------- | --------------------------------------------------------------------------------------------- | -------------------------- |
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655)                    | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645)                    | Choose 6 numbers from 1-45 |
| **Power 5/35** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535)                    | Choose 5 numbers from 1-35 |
| **Keno**       | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno)    | Fast-pace number game      |
| **Max 3D**     | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d)                 | 3-digit lottery game       |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro)              | Enhanced 3D lottery        |
| **Bingo18**    | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game    |

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

| Product   | Total Draws | Start Date | End Date   | Total Records | First ID | Latest ID |
| :-------- | ----------: | :--------- | :--------- | ------------: | :------- | :-------- |
| Power 655 |        1256 | 2017-08-01 | 2025-10-16 |          1256 | 00001    | 01256     |
| Power 645 |        1223 | 2017-10-25 | 2025-10-17 |          1223 | 00198    | 01420     |
| Power 535 |          87 | 2025-06-29 | 2025-10-17 |           174 | 00001    | 00222     |
| Keno      |         240 | 2022-12-04 | 2025-10-18 |         32500 | #0110271 | #0256276  |
| 3D        |         987 | 2019-04-22 | 2025-10-17 |           987 | 00001    | 00991     |
| 3D Pro    |         633 | 2021-09-14 | 2025-10-16 |           633 | 00001    | 00637     |
| Bingo18   |         320 | 2024-12-03 | 2025-10-18 |         50672 | 0083123  | 0133802   |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

| date       | result                    | predicted             |
| :--------- | :------------------------ | :-------------------- |
| 2023-10-12 | [5, 8, 9, 20, 36, 50, 35] | [5, 14, 8, 50, 20, 9] |

## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)

| date       |    id | result                       | page | process_time               |
| :--------- | ----: | :--------------------------- | ---: | :------------------------- |
| 2025-10-16 | 01256 | [14, 15, 24, 26, 27, 45, 36] |    0 | 2025-10-17 21:15:55.017468 |
| 2025-10-14 | 01255 | [8, 9, 16, 26, 37, 55, 12]   |    0 | 2025-10-17 21:15:55.017590 |
| 2025-10-11 | 01254 | [3, 7, 26, 43, 44, 46, 25]   |    0 | 2025-10-17 21:15:55.017694 |
| 2025-10-09 | 01253 | [7, 11, 21, 22, 39, 42, 40]  |    0 | 2025-10-17 21:15:55.017805 |
| 2025-10-07 | 01252 | [19, 22, 35, 37, 43, 45, 29] |    0 | 2025-10-17 21:15:55.017899 |
| 2025-10-04 | 01251 | [22, 33, 35, 36, 38, 40, 7]  |    0 | 2025-10-17 21:15:55.017992 |
| 2025-10-02 | 01250 | [1, 2, 20, 24, 27, 42, 43]   |    0 | 2025-10-17 21:15:55.018087 |
| 2025-09-30 | 01249 | [17, 23, 34, 39, 46, 52, 8]  |    0 | 2025-10-17 21:15:55.018180 |
| 2025-09-27 | 01248 | [8, 13, 19, 24, 39, 46, 1]   |    1 | 2025-10-17 21:15:55.028639 |
| 2025-09-25 | 01247 | [5, 17, 30, 31, 38, 53, 8]   |    1 | 2025-10-17 21:15:55.028670 |

### 🎲 Number Frequency (All Time)

|    % | result | count | -   |    % | result | count | -   | %    | result | count |
| ---: | -----: | ----: | :-- | ---: | -----: | ----: | :-- | :--- | :----- | :---- |
| 1.96 |      1 |   172 |     | 1.74 |     21 |   153 |     | 2.13 | 41     | 187   |
| 1.67 |      2 |   147 |     | 2.06 |     22 |   181 |     | 1.87 | 42     | 164   |
| 1.95 |      3 |   171 |     | 1.96 |     23 |   172 |     | 2.06 | 43     | 181   |
|  1.5 |      4 |   132 |     | 1.87 |     24 |   164 |     | 1.91 | 44     | 168   |
| 1.82 |      5 |   160 |     | 1.62 |     25 |   142 |     | 1.83 | 45     | 161   |
| 1.55 |      6 |   136 |     | 1.68 |     26 |   148 |     | 1.88 | 46     | 165   |
| 1.57 |      7 |   138 |     | 1.67 |     27 |   147 |     | 1.83 | 47     | 161   |
| 1.96 |      8 |   172 |     | 1.59 |     28 |   140 |     | 1.93 | 48     | 170   |
| 2.01 |      9 |   177 |     |  1.9 |     29 |   167 |     | 1.83 | 49     | 161   |
| 1.68 |     10 |   148 |     | 1.62 |     30 |   142 |     | 1.81 | 50     | 159   |
| 1.87 |     11 |   164 |     |  1.9 |     31 |   167 |     | 2.08 | 51     | 183   |
| 1.89 |     12 |   166 |     | 1.87 |     32 |   164 |     | 1.88 | 52     | 165   |
| 1.73 |     13 |   152 |     | 1.82 |     33 |   160 |     | 1.92 | 53     | 169   |
| 1.81 |     14 |   159 |     | 2.06 |     34 |   181 |     | 1.69 | 54     | 149   |
| 1.71 |     15 |   150 |     | 1.79 |     35 |   157 |     | 1.8  | 55     | 158   |
| 1.69 |     16 |   149 |     | 1.71 |     36 |   150 |     |      |        |       |
| 1.68 |     17 |   148 |     | 1.65 |     37 |   145 |     |      |        |       |
| 1.85 |     18 |   163 |     | 1.69 |     38 |   149 |     |      |        |       |
| 1.84 |     19 |   162 |     | 1.74 |     39 |   153 |     |      |        |       |
| 1.91 |     20 |   168 |     | 1.98 |     40 |   174 |     |      |        |       |

### 📊 Frequency Analysis by Period

#### Last 30 Days

|    % | result | count | -   |   % | result | count | -   | %   | result | count |
| ---: | -----: | ----: | :-- | --: | -----: | ----: | :-- | :-- | :----- | :---- |
|  2.2 |      1 |     2 |     | 3.3 |     24 |     3 |     | 4.4 | 46     | 4     |
|  2.2 |      2 |     2 |     | 1.1 |     25 |     1 |     | 1.1 | 52     | 1     |
|  2.2 |      3 |     2 |     | 3.3 |     26 |     3 |     | 1.1 | 53     | 1     |
|  1.1 |      5 |     1 |     | 3.3 |     27 |     3 |     | 2.2 | 55     | 2     |
|  3.3 |      7 |     3 |     | 1.1 |     29 |     1 |     |     |        |       |
| 7.69 |      8 |     7 |     | 2.2 |     30 |     2 |     |     |        |       |
|  1.1 |      9 |     1 |     | 1.1 |     31 |     1 |     |     |        |       |
|  1.1 |     11 |     1 |     | 1.1 |     33 |     1 |     |     |        |       |
|  1.1 |     12 |     1 |     | 2.2 |     34 |     2 |     |     |        |       |
|  2.2 |     13 |     2 |     | 2.2 |     35 |     2 |     |     |        |       |
|  2.2 |     14 |     2 |     | 3.3 |     36 |     3 |     |     |        |       |
|  1.1 |     15 |     1 |     | 2.2 |     37 |     2 |     |     |        |       |
|  1.1 |     16 |     1 |     | 4.4 |     38 |     4 |     |     |        |       |
|  2.2 |     17 |     2 |     | 3.3 |     39 |     3 |     |     |        |       |
|  1.1 |     18 |     1 |     | 2.2 |     40 |     2 |     |     |        |       |
|  4.4 |     19 |     4 |     | 1.1 |     41 |     1 |     |     |        |       |
|  2.2 |     20 |     2 |     | 2.2 |     42 |     2 |     |     |        |       |
|  1.1 |     21 |     1 |     | 4.4 |     43 |     4 |     |     |        |       |
|  3.3 |     22 |     3 |     | 1.1 |     44 |     1 |     |     |        |       |
|  1.1 |     23 |     1 |     | 2.2 |     45 |     2 |     |     |        |       |

#### Last 60 Days

|    % | result | count | -   |    % | result | count | -   | %    | result | count |
| ---: | -----: | ----: | :-- | ---: | -----: | ----: | :-- | :--- | :----- | :---- |
|  2.2 |      1 |     4 |     |  1.1 |     23 |     2 |     | 2.75 | 44     | 5     |
| 2.75 |      2 |     5 |     | 2.75 |     24 |     5 |     | 2.2  | 45     | 4     |
|  1.1 |      3 |     2 |     |  1.1 |     25 |     2 |     | 2.75 | 46     | 5     |
| 1.65 |      5 |     3 |     |  2.2 |     26 |     4 |     | 0.55 | 47     | 1     |
|  1.1 |      6 |     2 |     |  2.2 |     27 |     4 |     | 0.55 | 48     | 1     |
|  2.2 |      7 |     4 |     |  1.1 |     28 |     2 |     | 1.1  | 49     | 2     |
| 3.85 |      8 |     7 |     | 0.55 |     29 |     1 |     | 1.1  | 50     | 2     |
|  3.3 |      9 |     6 |     |  3.3 |     30 |     6 |     | 1.1  | 51     | 2     |
|  1.1 |     11 |     2 |     |  2.2 |     31 |     4 |     | 2.2  | 52     | 4     |
| 0.55 |     12 |     1 |     |  1.1 |     33 |     2 |     | 1.65 | 53     | 3     |
| 1.65 |     13 |     3 |     |  3.3 |     34 |     6 |     | 2.2  | 55     | 4     |
| 1.65 |     14 |     3 |     |  2.2 |     35 |     4 |     |      |        |       |
|  1.1 |     15 |     2 |     |  2.2 |     36 |     4 |     |      |        |       |
|  2.2 |     16 |     4 |     |  1.1 |     37 |     2 |     |      |        |       |
| 2.75 |     17 |     5 |     | 2.75 |     38 |     5 |     |      |        |       |
|  1.1 |     18 |     2 |     |  2.2 |     39 |     4 |     |      |        |       |
|  4.4 |     19 |     8 |     | 2.75 |     40 |     5 |     |      |        |       |
| 1.65 |     20 |     3 |     |  1.1 |     41 |     2 |     |      |        |       |
|  1.1 |     21 |     2 |     |  2.2 |     42 |     4 |     |      |        |       |
|  3.3 |     22 |     6 |     | 3.85 |     43 |     7 |     |      |        |       |

#### Last 90 Days

|    % | result | count | -   |    % | result | count | -   | %    | result | count |
| ---: | -----: | ----: | :-- | ---: | -----: | ----: | :-- | :--- | :----- | :---- |
| 1.88 |      1 |     5 |     | 0.75 |     21 |     2 |     | 1.13 | 41     | 3     |
| 1.88 |      2 |     5 |     | 2.63 |     22 |     7 |     | 1.88 | 42     | 5     |
| 0.75 |      3 |     2 |     |  1.5 |     23 |     4 |     | 3.38 | 43     | 9     |
| 0.38 |      4 |     1 |     | 3.38 |     24 |     9 |     | 2.26 | 44     | 6     |
| 3.01 |      5 |     8 |     | 0.75 |     25 |     2 |     | 2.63 | 45     | 7     |
| 1.88 |      6 |     5 |     | 1.88 |     26 |     5 |     | 2.26 | 46     | 6     |
|  1.5 |      7 |     4 |     |  1.5 |     27 |     4 |     | 1.13 | 47     | 3     |
| 3.38 |      8 |     9 |     |  1.5 |     28 |     4 |     | 1.5  | 48     | 4     |
| 3.01 |      9 |     8 |     |  1.5 |     29 |     4 |     | 1.13 | 49     | 3     |
|  1.5 |     10 |     4 |     | 2.63 |     30 |     7 |     | 0.75 | 50     | 2     |
| 0.75 |     11 |     2 |     | 2.63 |     31 |     7 |     | 1.88 | 51     | 5     |
| 0.75 |     12 |     2 |     | 1.13 |     32 |     3 |     | 2.26 | 52     | 6     |
| 1.13 |     13 |     3 |     | 1.88 |     33 |     5 |     | 1.88 | 53     | 5     |
|  1.5 |     14 |     4 |     | 3.38 |     34 |     9 |     | 0.38 | 54     | 1     |
| 1.13 |     15 |     3 |     | 2.26 |     35 |     6 |     | 1.88 | 55     | 5     |
| 1.88 |     16 |     5 |     | 2.26 |     36 |     6 |     |      |        |       |
| 2.63 |     17 |     7 |     |  1.5 |     37 |     4 |     |      |        |       |
| 1.13 |     18 |     3 |     | 1.88 |     38 |     5 |     |      |        |       |
| 3.38 |     19 |     9 |     | 1.88 |     39 |     5 |     |      |        |       |
| 1.13 |     20 |     3 |     | 2.26 |     40 |     6 |     |      |        |       |

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
# Install from PyPI (production)
pip install vietlott-data

# Or install from PyPI (development)
pip install -i https://pypi.org/simple/ vietlott-data
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
