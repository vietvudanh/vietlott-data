# Vietlot data

Data crawling from https://vietlott.vn/, results for products:
- [6/55](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655)
- [6/45](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645)
- [Keno](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno)
- [Max 3D](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d)
- [Max 3D Pro](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro)

## Table of content
- [Vietlot data](#vietlot-data)
  * [Predictions (just for testing, not a financial advice)](#predictions--just-for-testing--not-a-financial-advice-)
    + [random](#random)
  * [raw details 6/55](#raw-details-6-55)
  * [stats 6/55 all time](#stats-6-55-all-time)
  * [stats 6/55 -15d](#stats-6-55--15d)
  * [stats 6/55 -30d](#stats-6-55--30d)
  * [stats 6/55 -60d](#stats-6-55--60d)
  * [stats 6/55 -90d](#stats-6-55--90d)
- [Install](#install)
  * [via pip](#via-pip)
  * [cli](#cli)
    + [crawl](#crawl)
    + [Backfill missing data](#backfill-missing-data)


## Predictions (just for testing, not a financial advice)
These are backtest results for the strategies I have tested (just the abstract method at the moment, you can't predict lotery lol)

### random strategy
predicted: 20 / day (20 tickets perday or 200,000 vnd)
predicted corrected:
| date   | result   | predicted   |
|--------|----------|-------------| 

## raw details 6/55 last 10 days
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-01-07 | 01136 | [4, 5, 9, 16, 22, 39, 30]    |      0 | 2025-01-08 10:41:06.663806 |
| 2025-01-04 | 01135 | [4, 10, 30, 36, 40, 53, 51]  |      0 | 2025-01-07 13:09:17.203436 |
| 2025-01-02 | 01134 | [4, 10, 18, 22, 41, 45, 50]  |      0 | 2025-01-07 13:09:17.203531 |
| 2024-12-31 | 01133 | [8, 13, 29, 36, 42, 43, 28]  |      0 | 2025-01-07 13:09:17.203777 |
| 2024-12-28 | 01132 | [6, 19, 36, 42, 53, 55, 39]  |      0 | 2025-01-07 13:09:17.203893 |
| 2024-12-26 | 01131 | [6, 18, 33, 38, 41, 48, 16]  |      0 | 2025-01-07 13:09:17.203980 |
| 2024-12-24 | 01130 | [17, 20, 27, 32, 44, 51, 33] |      0 | 2025-01-07 13:09:17.204055 |
| 2024-12-21 | 01129 | [4, 16, 29, 30, 35, 51, 48]  |      0 | 2024-12-23 16:21:56.452504 |
| 2024-12-19 | 01128 | [13, 16, 32, 39, 49, 51, 11] |      0 | 2024-12-23 16:21:56.452645 |
| 2024-12-17 | 01127 | [2, 14, 27, 30, 53, 54, 16]  |      0 | 2024-12-23 16:21:56.452777 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     156 | 1.96 |     |       21 |     138 | 1.74 |     | 41       | 166     | 2.09 |
|        2 |     133 | 1.67 |     |       22 |     165 | 2.08 |     | 42       | 143     | 1.8  |
|        3 |     155 | 1.95 |     |       23 |     157 | 1.97 |     | 43       | 159     | 2.0  |
|        4 |     129 | 1.62 |     |       24 |     143 | 1.8  |     | 44       | 150     | 1.89 |
|        5 |     145 | 1.82 |     |       25 |     134 | 1.69 |     | 45       | 140     | 1.76 |
|        6 |     126 | 1.58 |     |       26 |     133 | 1.67 |     | 46       | 153     | 1.92 |
|        7 |     124 | 1.56 |     |       27 |     133 | 1.67 |     | 47       | 143     | 1.8  |
|        8 |     152 | 1.91 |     |       28 |     128 | 1.61 |     | 48       | 152     | 1.91 |
|        9 |     160 | 2.01 |     |       29 |     150 | 1.89 |     | 49       | 150     | 1.89 |
|       10 |     137 | 1.72 |     |       30 |     125 | 1.57 |     | 50       | 143     | 1.8  |
|       11 |     149 | 1.87 |     |       31 |     149 | 1.87 |     | 51       | 165     | 2.08 |
|       12 |     156 | 1.96 |     |       32 |     153 | 1.92 |     | 52       | 149     | 1.87 |
|       13 |     137 | 1.72 |     |       33 |     148 | 1.86 |     | 53       | 153     | 1.92 |
|       14 |     139 | 1.75 |     |       34 |     158 | 1.99 |     | 54       | 140     | 1.76 |
|       15 |     133 | 1.67 |     |       35 |     149 | 1.87 |     | 55       | 144     | 1.81 |
|       16 |     135 | 1.7  |     |       36 |     138 | 1.74 |     |          |         |      |
|       17 |     132 | 1.66 |     |       37 |     127 | 1.6  |     |          |         |      |
|       18 |     147 | 1.85 |     |       38 |     137 | 1.72 |     |          |         |      |
|       19 |     142 | 1.79 |     |       39 |     136 | 1.71 |     |          |         |      |
|       20 |     157 | 1.97 |     |       40 |     156 | 1.96 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.3  |     |       27 |       2 | 2.6  |     | 53       | 3       | 3.9 |
|        3 |       1 | 1.3  |     |       28 |       1 | 1.3  |     | 54       | 1       | 1.3 |
|        4 |       4 | 5.19 |     |       29 |       2 | 2.6  |     | 55       | 1       | 1.3 |
|        5 |       1 | 1.3  |     |       30 |       4 | 5.19 |     |          |         |     |
|        6 |       2 | 2.6  |     |       32 |       2 | 2.6  |     |          |         |     |
|        7 |       1 | 1.3  |     |       33 |       2 | 2.6  |     |          |         |     |
|        8 |       1 | 1.3  |     |       35 |       1 | 1.3  |     |          |         |     |
|        9 |       1 | 1.3  |     |       36 |       3 | 3.9  |     |          |         |     |
|       10 |       3 | 3.9  |     |       38 |       1 | 1.3  |     |          |         |     |
|       11 |       1 | 1.3  |     |       39 |       3 | 3.9  |     |          |         |     |
|       13 |       2 | 2.6  |     |       40 |       1 | 1.3  |     |          |         |     |
|       14 |       1 | 1.3  |     |       41 |       2 | 2.6  |     |          |         |     |
|       16 |       5 | 6.49 |     |       42 |       2 | 2.6  |     |          |         |     |
|       17 |       1 | 1.3  |     |       43 |       1 | 1.3  |     |          |         |     |
|       18 |       2 | 2.6  |     |       44 |       1 | 1.3  |     |          |         |     |
|       19 |       2 | 2.6  |     |       45 |       1 | 1.3  |     |          |         |     |
|       20 |       2 | 2.6  |     |       48 |       2 | 2.6  |     |          |         |     |
|       21 |       1 | 1.3  |     |       49 |       1 | 1.3  |     |          |         |     |
|       22 |       2 | 2.6  |     |       50 |       1 | 1.3  |     |          |         |     |
|       24 |       1 | 1.3  |     |       51 |       4 | 5.19 |     |          |         |     |
## stats 6/55 -30d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.3  |     |       27 |       2 | 2.6  |     | 53       | 3       | 3.9 |
|        3 |       1 | 1.3  |     |       28 |       1 | 1.3  |     | 54       | 1       | 1.3 |
|        4 |       4 | 5.19 |     |       29 |       2 | 2.6  |     | 55       | 1       | 1.3 |
|        5 |       1 | 1.3  |     |       30 |       4 | 5.19 |     |          |         |     |
|        6 |       2 | 2.6  |     |       32 |       2 | 2.6  |     |          |         |     |
|        7 |       1 | 1.3  |     |       33 |       2 | 2.6  |     |          |         |     |
|        8 |       1 | 1.3  |     |       35 |       1 | 1.3  |     |          |         |     |
|        9 |       1 | 1.3  |     |       36 |       3 | 3.9  |     |          |         |     |
|       10 |       3 | 3.9  |     |       38 |       1 | 1.3  |     |          |         |     |
|       11 |       1 | 1.3  |     |       39 |       3 | 3.9  |     |          |         |     |
|       13 |       2 | 2.6  |     |       40 |       1 | 1.3  |     |          |         |     |
|       14 |       1 | 1.3  |     |       41 |       2 | 2.6  |     |          |         |     |
|       16 |       5 | 6.49 |     |       42 |       2 | 2.6  |     |          |         |     |
|       17 |       1 | 1.3  |     |       43 |       1 | 1.3  |     |          |         |     |
|       18 |       2 | 2.6  |     |       44 |       1 | 1.3  |     |          |         |     |
|       19 |       2 | 2.6  |     |       45 |       1 | 1.3  |     |          |         |     |
|       20 |       2 | 2.6  |     |       48 |       2 | 2.6  |     |          |         |     |
|       21 |       1 | 1.3  |     |       49 |       1 | 1.3  |     |          |         |     |
|       22 |       2 | 2.6  |     |       50 |       1 | 1.3  |     |          |         |     |
|       24 |       1 | 1.3  |     |       51 |       4 | 5.19 |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.79 |     |       21 |       2 | 1.19 |     | 42       | 4       | 2.38 |
|        2 |       1 | 0.6  |     |       22 |       5 | 2.98 |     | 43       | 2       | 1.19 |
|        3 |       1 | 0.6  |     |       24 |       4 | 2.38 |     | 44       | 2       | 1.19 |
|        4 |       5 | 2.98 |     |       25 |       2 | 1.19 |     | 45       | 3       | 1.79 |
|        5 |       1 | 0.6  |     |       26 |       3 | 1.79 |     | 47       | 2       | 1.19 |
|        6 |       3 | 1.79 |     |       27 |       2 | 1.19 |     | 48       | 4       | 2.38 |
|        7 |       1 | 0.6  |     |       28 |       2 | 1.19 |     | 49       | 2       | 1.19 |
|        8 |       2 | 1.19 |     |       29 |       4 | 2.38 |     | 50       | 1       | 0.6  |
|        9 |       4 | 2.38 |     |       30 |       4 | 2.38 |     | 51       | 7       | 4.17 |
|       10 |       5 | 2.98 |     |       31 |       3 | 1.79 |     | 52       | 2       | 1.19 |
|       11 |       4 | 2.38 |     |       32 |       3 | 1.79 |     | 53       | 4       | 2.38 |
|       12 |       4 | 2.38 |     |       33 |       4 | 2.38 |     | 54       | 4       | 2.38 |
|       13 |       2 | 1.19 |     |       34 |       1 | 0.6  |     | 55       | 2       | 1.19 |
|       14 |       1 | 0.6  |     |       35 |       1 | 0.6  |     |          |         |      |
|       15 |       2 | 1.19 |     |       36 |       5 | 2.98 |     |          |         |      |
|       16 |      11 | 6.55 |     |       37 |       4 | 2.38 |     |          |         |      |
|       17 |       3 | 1.79 |     |       38 |       3 | 1.79 |     |          |         |      |
|       18 |       3 | 1.79 |     |       39 |       6 | 3.57 |     |          |         |      |
|       19 |       3 | 1.79 |     |       40 |       4 | 2.38 |     |          |         |      |
|       20 |       3 | 1.79 |     |       41 |       5 | 2.98 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.54 |     |       21 |       4 | 1.54 |     | 41       | 8       | 3.09 |
|        2 |       2 | 0.77 |     |       22 |       6 | 2.32 |     | 42       | 6       | 2.32 |
|        3 |       2 | 0.77 |     |       23 |       1 | 0.39 |     | 43       | 5       | 1.93 |
|        4 |       6 | 2.32 |     |       24 |       5 | 1.93 |     | 44       | 2       | 0.77 |
|        5 |       4 | 1.54 |     |       25 |       4 | 1.54 |     | 45       | 4       | 1.54 |
|        6 |       4 | 1.54 |     |       26 |       7 | 2.7  |     | 46       | 3       | 1.16 |
|        7 |       2 | 0.77 |     |       27 |       3 | 1.16 |     | 47       | 4       | 1.54 |
|        8 |       2 | 0.77 |     |       28 |       3 | 1.16 |     | 48       | 4       | 1.54 |
|        9 |       8 | 3.09 |     |       29 |       7 | 2.7  |     | 49       | 3       | 1.16 |
|       10 |       5 | 1.93 |     |       30 |       5 | 1.93 |     | 50       | 2       | 0.77 |
|       11 |       6 | 2.32 |     |       31 |       8 | 3.09 |     | 51       | 11      | 4.25 |
|       12 |       4 | 1.54 |     |       32 |       3 | 1.16 |     | 52       | 3       | 1.16 |
|       13 |       2 | 0.77 |     |       33 |       6 | 2.32 |     | 53       | 5       | 1.93 |
|       14 |       4 | 1.54 |     |       34 |       3 | 1.16 |     | 54       | 6       | 2.32 |
|       15 |       4 | 1.54 |     |       35 |       3 | 1.16 |     | 55       | 3       | 1.16 |
|       16 |      12 | 4.63 |     |       36 |       6 | 2.32 |     |          |         |      |
|       17 |       5 | 1.93 |     |       37 |       4 | 1.54 |     |          |         |      |
|       18 |       3 | 1.16 |     |       38 |       4 | 1.54 |     |          |         |      |
|       19 |       7 | 2.7  |     |       39 |      10 | 3.86 |     |          |         |      |
|       20 |       6 | 2.32 |     |       40 |       6 | 2.32 |     |          |         |      |

# How project works
Since there are many people asked, I write this section.

## Schedule
The project is schedule automatically via Github Actions, run a script, fetch data and auto commit to Github. No server is required, I don't need to do anything.
Details in [workflow file](https://github.com/vietvudanh/vietlott-data/blob/dffb2bcdfa860a0dfc3f2e22e269e6978d478965/.github/workflows/crawl.yaml#L8)

## How crawling works
I just inspected network packages sent between browser and server to find out how data is fetched and replicated that in Python code. 

# Install
 
## via pip

```shell
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
```

## cli
project provides two cli

### crawl
```shell
Usage: vietlott-crawl [OPTIONS] PRODUCT

  crawl a product with a given run date or from/to index page 

Options:
  --run-date TEXT
  --index_from INTEGER  page index from run since we crawl by pagination the
                        pages
  --index_to INTEGER    page index from run since we crawl by pagination the
                        pages
  --help                Show this message and exit.
```

### Backfill missing data

```shell
Usage: vietlott-missing [OPTIONS] PRODUCT

  detect_missing_data and run if needed :param ctx: context :param product:
  product to run :param limit: number of pages to run :return:

Options:
  --limit INTEGER
  --help           Show this message and exit.
```

