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
| 2025-02-27 | 01157 | [5, 9, 21, 31, 43, 53, 11]   |      0 | 2025-02-27 22:55:20.424084 |
| 2025-02-25 | 01156 | [1, 7, 11, 24, 29, 30, 48]   |      0 | 2025-02-25 20:58:27.007819 |
| 2025-02-22 | 01155 | [1, 2, 7, 22, 23, 46, 50]    |      0 | 2025-02-22 19:00:38.011886 |
| 2025-02-20 | 01154 | [13, 17, 20, 27, 36, 54, 47] |      0 | 2025-02-20 19:00:12.840993 |
| 2025-02-18 | 01153 | [12, 13, 30, 38, 40, 47, 42] |      0 | 2025-02-19 19:00:18.391949 |
| 2025-02-15 | 01152 | [22, 37, 38, 47, 51, 55, 31] |      0 | 2025-02-15 19:00:15.907100 |
| 2025-02-13 | 01151 | [2, 8, 23, 26, 42, 47, 7]    |      0 | 2025-02-13 19:00:13.398152 |
| 2025-02-11 | 01150 | [1, 9, 18, 21, 35, 40, 44]   |      0 | 2025-02-11 19:00:16.958421 |
| 2025-02-08 | 01149 | [11, 22, 28, 44, 48, 49, 23] |      0 | 2025-02-08 19:00:21.621172 |
| 2025-02-06 | 01148 | [1, 11, 31, 43, 48, 54, 19]  |      0 | 2025-02-06 19:00:16.666665 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     162 | 2    |     |       21 |     142 | 1.75 |     | 41       | 168     | 2.07 |
|        2 |     135 | 1.67 |     |       22 |     170 | 2.1  |     | 42       | 146     | 1.8  |
|        3 |     157 | 1.94 |     |       23 |     161 | 1.99 |     | 43       | 161     | 1.99 |
|        4 |     129 | 1.59 |     |       24 |     146 | 1.8  |     | 44       | 152     | 1.88 |
|        5 |     147 | 1.82 |     |       25 |     135 | 1.67 |     | 45       | 141     | 1.74 |
|        6 |     126 | 1.56 |     |       26 |     136 | 1.68 |     | 46       | 156     | 1.93 |
|        7 |     128 | 1.58 |     |       27 |     134 | 1.65 |     | 47       | 149     | 1.84 |
|        8 |     155 | 1.91 |     |       28 |     131 | 1.62 |     | 48       | 156     | 1.93 |
|        9 |     162 | 2    |     |       29 |     153 | 1.89 |     | 49       | 153     | 1.89 |
|       10 |     138 | 1.7  |     |       30 |     127 | 1.57 |     | 50       | 147     | 1.82 |
|       11 |     156 | 1.93 |     |       31 |     154 | 1.9  |     | 51       | 171     | 2.11 |
|       12 |     158 | 1.95 |     |       32 |     153 | 1.89 |     | 52       | 152     | 1.88 |
|       13 |     140 | 1.73 |     |       33 |     149 | 1.84 |     | 53       | 156     | 1.93 |
|       14 |     141 | 1.74 |     |       34 |     161 | 1.99 |     | 54       | 142     | 1.75 |
|       15 |     133 | 1.64 |     |       35 |     150 | 1.85 |     | 55       | 146     | 1.8  |
|       16 |     136 | 1.68 |     |       36 |     139 | 1.72 |     |          |         |      |
|       17 |     134 | 1.65 |     |       37 |     132 | 1.63 |     |          |         |      |
|       18 |     151 | 1.86 |     |       38 |     140 | 1.73 |     |          |         |      |
|       19 |     144 | 1.78 |     |       39 |     138 | 1.7  |     |          |         |      |
|       20 |     159 | 1.96 |     |       40 |     160 | 1.98 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       5 | 5.49 |     |       29 |       2 | 2.2  |     | 51       | 2       | 2.2 |
|        2 |       2 | 2.2  |     |       30 |       2 | 2.2  |     | 52       | 2       | 2.2 |
|        5 |       2 | 2.2  |     |       31 |       3 | 3.3  |     | 53       | 1       | 1.1 |
|        7 |       4 | 4.4  |     |       34 |       2 | 2.2  |     | 54       | 2       | 2.2 |
|        8 |       2 | 2.2  |     |       35 |       1 | 1.1  |     | 55       | 2       | 2.2 |
|        9 |       2 | 2.2  |     |       36 |       1 | 1.1  |     |          |         |     |
|       11 |       4 | 4.4  |     |       37 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1  |     |       38 |       3 | 3.3  |     |          |         |     |
|       13 |       2 | 2.2  |     |       39 |       1 | 1.1  |     |          |         |     |
|       17 |       2 | 2.2  |     |       40 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1  |     |       41 |       1 | 1.1  |     |          |         |     |
|       19 |       1 | 1.1  |     |       42 |       2 | 2.2  |     |          |         |     |
|       20 |       2 | 2.2  |     |       43 |       2 | 2.2  |     |          |         |     |
|       21 |       2 | 2.2  |     |       44 |       2 | 2.2  |     |          |         |     |
|       22 |       3 | 3.3  |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       3 | 3.3  |     |       46 |       1 | 1.1  |     |          |         |     |
|       24 |       2 | 2.2  |     |       47 |       5 | 5.49 |     |          |         |     |
|       26 |       1 | 1.1  |     |       48 |       3 | 3.3  |     |          |         |     |
|       27 |       1 | 1.1  |     |       49 |       2 | 2.2  |     |          |         |     |
|       28 |       2 | 2.2  |     |       50 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -30d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       5 | 5.49 |     |       29 |       2 | 2.2  |     | 51       | 2       | 2.2 |
|        2 |       2 | 2.2  |     |       30 |       2 | 2.2  |     | 52       | 2       | 2.2 |
|        5 |       2 | 2.2  |     |       31 |       3 | 3.3  |     | 53       | 1       | 1.1 |
|        7 |       4 | 4.4  |     |       34 |       2 | 2.2  |     | 54       | 2       | 2.2 |
|        8 |       2 | 2.2  |     |       35 |       1 | 1.1  |     | 55       | 2       | 2.2 |
|        9 |       2 | 2.2  |     |       36 |       1 | 1.1  |     |          |         |     |
|       11 |       4 | 4.4  |     |       37 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1  |     |       38 |       3 | 3.3  |     |          |         |     |
|       13 |       2 | 2.2  |     |       39 |       1 | 1.1  |     |          |         |     |
|       17 |       2 | 2.2  |     |       40 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1  |     |       41 |       1 | 1.1  |     |          |         |     |
|       19 |       1 | 1.1  |     |       42 |       2 | 2.2  |     |          |         |     |
|       20 |       2 | 2.2  |     |       43 |       2 | 2.2  |     |          |         |     |
|       21 |       2 | 2.2  |     |       44 |       2 | 2.2  |     |          |         |     |
|       22 |       3 | 3.3  |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       3 | 3.3  |     |       46 |       1 | 1.1  |     |          |         |     |
|       24 |       2 | 2.2  |     |       47 |       5 | 5.49 |     |          |         |     |
|       26 |       1 | 1.1  |     |       48 |       3 | 3.3  |     |          |         |     |
|       27 |       1 | 1.1  |     |       49 |       2 | 2.2  |     |          |         |     |
|       28 |       2 | 2.2  |     |       50 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       6 | 3.43 |     |       23 |       4 | 2.29 |     | 44       | 2       | 1.14 |
|        2 |       2 | 1.14 |     |       24 |       3 | 1.71 |     | 45       | 2       | 1.14 |
|        3 |       2 | 1.14 |     |       25 |       1 | 0.57 |     | 46       | 3       | 1.71 |
|        4 |       3 | 1.71 |     |       26 |       3 | 1.71 |     | 47       | 6       | 3.43 |
|        5 |       3 | 1.71 |     |       27 |       1 | 0.57 |     | 48       | 4       | 2.29 |
|        7 |       4 | 2.29 |     |       28 |       4 | 2.29 |     | 49       | 3       | 1.71 |
|        8 |       4 | 2.29 |     |       29 |       4 | 2.29 |     | 50       | 5       | 2.86 |
|        9 |       3 | 1.71 |     |       30 |       4 | 2.29 |     | 51       | 7       | 4.0  |
|       10 |       3 | 1.71 |     |       31 |       5 | 2.86 |     | 52       | 3       | 1.71 |
|       11 |       7 | 4    |     |       33 |       1 | 0.57 |     | 53       | 4       | 2.29 |
|       12 |       2 | 1.14 |     |       34 |       3 | 1.71 |     | 54       | 2       | 1.14 |
|       13 |       4 | 2.29 |     |       35 |       1 | 0.57 |     | 55       | 2       | 1.14 |
|       14 |       2 | 1.14 |     |       36 |       3 | 1.71 |     |          |         |      |
|       16 |       2 | 1.14 |     |       37 |       5 | 2.86 |     |          |         |      |
|       17 |       2 | 1.14 |     |       38 |       3 | 1.71 |     |          |         |      |
|       18 |       5 | 2.86 |     |       39 |       3 | 1.71 |     |          |         |      |
|       19 |       2 | 1.14 |     |       40 |       5 | 2.86 |     |          |         |      |
|       20 |       2 | 1.14 |     |       41 |       3 | 1.71 |     |          |         |      |
|       21 |       4 | 2.29 |     |       42 |       4 | 2.29 |     |          |         |      |
|       22 |       7 | 4    |     |       43 |       3 | 1.71 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       8 | 3.01 |     |       21 |       6 | 2.26 |     | 41       | 6       | 2.26 |
|        2 |       3 | 1.13 |     |       22 |       8 | 3.01 |     | 42       | 6       | 2.26 |
|        3 |       3 | 1.13 |     |       23 |       4 | 1.5  |     | 43       | 3       | 1.13 |
|        4 |       4 | 1.5  |     |       24 |       6 | 2.26 |     | 44       | 4       | 1.5  |
|        5 |       3 | 1.13 |     |       25 |       1 | 0.38 |     | 45       | 3       | 1.13 |
|        6 |       2 | 0.75 |     |       26 |       5 | 1.88 |     | 46       | 3       | 1.13 |
|        7 |       5 | 1.88 |     |       27 |       3 | 1.13 |     | 47       | 8       | 3.01 |
|        8 |       4 | 1.5  |     |       28 |       4 | 1.5  |     | 48       | 6       | 2.26 |
|        9 |       5 | 1.88 |     |       29 |       7 | 2.63 |     | 49       | 4       | 1.5  |
|       10 |       5 | 1.88 |     |       30 |       6 | 2.26 |     | 50       | 5       | 1.88 |
|       11 |      10 | 3.76 |     |       31 |       5 | 1.88 |     | 51       | 10      | 3.76 |
|       12 |       3 | 1.13 |     |       32 |       2 | 0.75 |     | 52       | 4       | 1.5  |
|       13 |       5 | 1.88 |     |       33 |       4 | 1.5  |     | 53       | 6       | 2.26 |
|       14 |       3 | 1.13 |     |       34 |       3 | 1.13 |     | 54       | 5       | 1.88 |
|       15 |       1 | 0.38 |     |       35 |       2 | 0.75 |     | 55       | 4       | 1.5  |
|       16 |       9 | 3.38 |     |       36 |       6 | 2.26 |     |          |         |      |
|       17 |       4 | 1.5  |     |       37 |       7 | 2.63 |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       5 | 1.88 |     |          |         |      |
|       19 |       5 | 1.88 |     |       39 |       6 | 2.26 |     |          |         |      |
|       20 |       5 | 1.88 |     |       40 |       5 | 1.88 |     |          |         |      |

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

