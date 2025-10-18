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

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 4 | 1970-01-18 | 1970-01-21 | 1256 | 00001 | 01256 |
| Power 645 | 4 | 1970-01-18 | 1970-01-21 | 1223 | 00198 | 01420 |
| Power 535 | 1 | 1970-01-21 | 1970-01-21 | 174 | 00001 | 00222 |
| Keno | 2 | 1970-01-20 | 1970-01-21 | 32500 | #0110271 | #0256276 |
| 3D | 3 | 1970-01-19 | 1970-01-21 | 987 | 00001 | 00991 |
| 3D Pro | 3 | 1970-01-19 | 1970-01-21 | 633 | 00001 | 00637 |
| Bingo18 | 1 | 1970-01-21 | 1970-01-21 | 50672 | 0083123 | 0133802 |

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
| date | id | result | page | process_time |
| --- | --- | --- | --- | --- |
| 1970-01-21 | 01256 | [14, 15, 24, 26, 27, 45, 36] | 0 | 2025-10-17 21:15:55.017468 |
| 1970-01-21 | 01255 | [8, 9, 16, 26, 37, 55, 12] | 0 | 2025-10-17 21:15:55.017590 |
| 1970-01-21 | 01254 | [3, 7, 26, 43, 44, 46, 25] | 0 | 2025-10-17 21:15:55.017694 |
| 1970-01-21 | 01253 | [7, 11, 21, 22, 39, 42, 40] | 0 | 2025-10-17 21:15:55.017805 |
| 1970-01-21 | 01252 | [19, 22, 35, 37, 43, 45, 29] | 0 | 2025-10-17 21:15:55.017899 |
| 1970-01-21 | 01251 | [22, 33, 35, 36, 38, 40, 7] | 0 | 2025-10-17 21:15:55.017992 |
| 1970-01-21 | 01250 | [1, 2, 20, 24, 27, 42, 43] | 0 | 2025-10-17 21:15:55.018087 |
| 1970-01-21 | 01249 | [17, 23, 34, 39, 46, 52, 8] | 0 | 2025-10-17 21:15:55.018180 |
| 1970-01-21 | 01248 | [8, 13, 19, 24, 39, 46, 1] | 1 | 2025-10-17 21:15:55.028639 |
| 1970-01-21 | 01247 | [5, 17, 30, 31, 38, 53, 8] | 1 | 2025-10-17 21:15:55.028670 |

### 🎲 Number Frequency (All Time)
| result | count | % |
| --- | --- | --- |
| 48 | 170 | 1.93 |
| 9 | 177 | 2.01 |
| 45 | 161 | 1.83 |
| 15 | 150 | 1.71 |
| 30 | 142 | 1.62 |
| 6 | 136 | 1.55 |
| 27 | 147 | 1.67 |
| 21 | 153 | 1.74 |
| 33 | 160 | 1.82 |
| 24 | 164 | 1.87 |
| 18 | 163 | 1.85 |
| 12 | 166 | 1.89 |
| 39 | 153 | 1.74 |
| 3 | 171 | 1.95 |
| 42 | 164 | 1.87 |
| 36 | 150 | 1.71 |
| 54 | 149 | 1.69 |
| 51 | 183 | 2.08 |
| 1 | 172 | 1.96 |
| 16 | 149 | 1.69 |
| 13 | 152 | 1.73 |
| 7 | 138 | 1.57 |
| 4 | 132 | 1.5 |
| 10 | 148 | 1.68 |
| 31 | 167 | 1.9 |
| 40 | 174 | 1.98 |
| 49 | 161 | 1.83 |
| 37 | 145 | 1.65 |
| 34 | 181 | 2.06 |
| 28 | 140 | 1.59 |
| 55 | 158 | 1.8 |
| 46 | 165 | 1.88 |
| 22 | 181 | 2.06 |
| 25 | 142 | 1.62 |
| 43 | 181 | 2.06 |
| 52 | 165 | 1.88 |
| 19 | 162 | 1.84 |
| 23 | 172 | 1.96 |
| 26 | 148 | 1.68 |
| 17 | 148 | 1.68 |
| 8 | 172 | 1.96 |
| 29 | 167 | 1.9 |
| 14 | 159 | 1.81 |
| 2 | 147 | 1.67 |
| 32 | 164 | 1.87 |
| 20 | 168 | 1.91 |
| 5 | 160 | 1.82 |
| 11 | 164 | 1.87 |
| 38 | 149 | 1.69 |
| 41 | 187 | 2.13 |
| 50 | 159 | 1.81 |
| 44 | 168 | 1.91 |
| 35 | 157 | 1.79 |
| 53 | 169 | 1.92 |
| 47 | 161 | 1.83 |

### 📊 Frequency Analysis by Period

#### Last 30 Days
No data available

#### Last 60 Days
No data available

#### Last 90 Days
No data available



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

