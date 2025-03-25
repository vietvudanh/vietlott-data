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
| 2025-03-25 | 01168 | [14, 23, 29, 30, 35, 40, 17] |      0 | 2025-03-25 19:00:13.251916 |
| 2025-03-22 | 01167 | [2, 23, 42, 50, 52, 54, 44]  |      0 | 2025-03-22 19:00:24.768659 |
| 2025-03-20 | 01166 | [11, 13, 24, 28, 36, 41, 37] |      0 | 2025-03-20 19:00:22.564476 |
| 2025-03-18 | 01165 | [2, 8, 29, 30, 50, 55, 27]   |      0 | 2025-03-19 16:05:09.000808 |
| 2025-03-15 | 01164 | [1, 34, 39, 40, 42, 50, 25]  |      0 | 2025-03-15 19:00:14.000659 |
| 2025-03-13 | 01163 | [7, 13, 21, 43, 52, 53, 17]  |      0 | 2025-03-13 19:00:15.799984 |
| 2025-03-11 | 01162 | [1, 16, 18, 30, 31, 44, 34]  |      0 | 2025-03-11 19:00:14.832710 |
| 2025-03-08 | 01161 | [10, 38, 41, 43, 45, 48, 8]  |      0 | 2025-03-10 11:41:38.454144 |
| 2025-03-06 | 01160 | [5, 10, 21, 26, 43, 51, 15]  |      0 | 2025-03-10 11:41:38.454275 |
| 2025-03-04 | 01159 | [5, 14, 27, 43, 45, 53, 47]  |      0 | 2025-03-04 19:00:14.873524 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     164 | 2.01 |     |       21 |     144 | 1.76 |     | 41       | 171     | 2.09 |
|        2 |     137 | 1.68 |     |       22 |     170 | 2.08 |     | 42       | 148     | 1.81 |
|        3 |     157 | 1.92 |     |       23 |     163 | 1.99 |     | 43       | 165     | 2.02 |
|        4 |     129 | 1.58 |     |       24 |     147 | 1.8  |     | 44       | 154     | 1.88 |
|        5 |     149 | 1.82 |     |       25 |     136 | 1.66 |     | 45       | 144     | 1.76 |
|        6 |     126 | 1.54 |     |       26 |     137 | 1.68 |     | 46       | 156     | 1.91 |
|        7 |     129 | 1.58 |     |       27 |     136 | 1.66 |     | 47       | 150     | 1.83 |
|        8 |     157 | 1.92 |     |       28 |     132 | 1.61 |     | 48       | 157     | 1.92 |
|        9 |     162 | 1.98 |     |       29 |     155 | 1.9  |     | 49       | 153     | 1.87 |
|       10 |     140 | 1.71 |     |       30 |     130 | 1.59 |     | 50       | 150     | 1.83 |
|       11 |     157 | 1.92 |     |       31 |     155 | 1.9  |     | 51       | 172     | 2.1  |
|       12 |     158 | 1.93 |     |       32 |     153 | 1.87 |     | 52       | 154     | 1.88 |
|       13 |     142 | 1.74 |     |       33 |     149 | 1.82 |     | 53       | 158     | 1.93 |
|       14 |     143 | 1.75 |     |       34 |     164 | 2.01 |     | 54       | 143     | 1.75 |
|       15 |     135 | 1.65 |     |       35 |     151 | 1.85 |     | 55       | 147     | 1.8  |
|       16 |     137 | 1.68 |     |       36 |     140 | 1.71 |     |          |         |      |
|       17 |     137 | 1.68 |     |       37 |     134 | 1.64 |     |          |         |      |
|       18 |     152 | 1.86 |     |       38 |     141 | 1.72 |     |          |         |      |
|       19 |     144 | 1.76 |     |       39 |     140 | 1.71 |     |          |         |      |
|       20 |     159 | 1.94 |     |       40 |     162 | 1.98 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3 |     |       28 |       1 | 1.1  |     | 52       | 2       | 2.2 |
|        2 |       2 | 2.2 |     |       29 |       3 | 3.3  |     | 53       | 3       | 3.3 |
|        5 |       3 | 3.3 |     |       30 |       4 | 4.4  |     | 54       | 1       | 1.1 |
|        7 |       2 | 2.2 |     |       31 |       2 | 2.2  |     | 55       | 1       | 1.1 |
|        8 |       2 | 2.2 |     |       34 |       3 | 3.3  |     |          |         |     |
|        9 |       1 | 1.1 |     |       35 |       1 | 1.1  |     |          |         |     |
|       10 |       2 | 2.2 |     |       36 |       1 | 1.1  |     |          |         |     |
|       11 |       3 | 3.3 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       2 | 2.2 |     |       38 |       1 | 1.1  |     |          |         |     |
|       14 |       2 | 2.2 |     |       39 |       2 | 2.2  |     |          |         |     |
|       15 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       16 |       1 | 1.1 |     |       41 |       3 | 3.3  |     |          |         |     |
|       17 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1 |     |       43 |       5 | 5.49 |     |          |         |     |
|       21 |       3 | 3.3 |     |       44 |       2 | 2.2  |     |          |         |     |
|       23 |       2 | 2.2 |     |       45 |       3 | 3.3  |     |          |         |     |
|       24 |       2 | 2.2 |     |       47 |       1 | 1.1  |     |          |         |     |
|       25 |       1 | 1.1 |     |       48 |       2 | 2.2  |     |          |         |     |
|       26 |       1 | 1.1 |     |       50 |       3 | 3.3  |     |          |         |     |
|       27 |       2 | 2.2 |     |       51 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3 |     |       28 |       1 | 1.1  |     | 52       | 2       | 2.2 |
|        2 |       2 | 2.2 |     |       29 |       3 | 3.3  |     | 53       | 3       | 3.3 |
|        5 |       3 | 3.3 |     |       30 |       4 | 4.4  |     | 54       | 1       | 1.1 |
|        7 |       2 | 2.2 |     |       31 |       2 | 2.2  |     | 55       | 1       | 1.1 |
|        8 |       2 | 2.2 |     |       34 |       3 | 3.3  |     |          |         |     |
|        9 |       1 | 1.1 |     |       35 |       1 | 1.1  |     |          |         |     |
|       10 |       2 | 2.2 |     |       36 |       1 | 1.1  |     |          |         |     |
|       11 |       3 | 3.3 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       2 | 2.2 |     |       38 |       1 | 1.1  |     |          |         |     |
|       14 |       2 | 2.2 |     |       39 |       2 | 2.2  |     |          |         |     |
|       15 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       16 |       1 | 1.1 |     |       41 |       3 | 3.3  |     |          |         |     |
|       17 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1 |     |       43 |       5 | 5.49 |     |          |         |     |
|       21 |       3 | 3.3 |     |       44 |       2 | 2.2  |     |          |         |     |
|       23 |       2 | 2.2 |     |       45 |       3 | 3.3  |     |          |         |     |
|       24 |       2 | 2.2 |     |       47 |       1 | 1.1  |     |          |         |     |
|       25 |       1 | 1.1 |     |       48 |       2 | 2.2  |     |          |         |     |
|       26 |       1 | 1.1 |     |       50 |       3 | 3.3  |     |          |         |     |
|       27 |       2 | 2.2 |     |       51 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       7 | 4    |     |       24 |       3 | 1.71 |     | 46       | 1       | 0.57 |
|        2 |       4 | 2.29 |     |       25 |       1 | 0.57 |     | 47       | 6       | 3.43 |
|        5 |       4 | 2.29 |     |       26 |       2 | 1.14 |     | 48       | 5       | 2.86 |
|        7 |       5 | 2.86 |     |       27 |       3 | 1.71 |     | 49       | 2       | 1.14 |
|        8 |       4 | 2.29 |     |       28 |       3 | 1.71 |     | 50       | 4       | 2.29 |
|        9 |       2 | 1.14 |     |       29 |       4 | 2.29 |     | 51       | 4       | 2.29 |
|       10 |       2 | 1.14 |     |       30 |       5 | 2.86 |     | 52       | 4       | 2.29 |
|       11 |       5 | 2.86 |     |       31 |       4 | 2.29 |     | 53       | 3       | 1.71 |
|       12 |       1 | 0.57 |     |       34 |       5 | 2.86 |     | 54       | 3       | 1.71 |
|       13 |       4 | 2.29 |     |       35 |       2 | 1.14 |     | 55       | 3       | 1.71 |
|       14 |       3 | 1.71 |     |       36 |       2 | 1.14 |     |          |         |      |
|       15 |       2 | 1.14 |     |       37 |       3 | 1.71 |     |          |         |      |
|       16 |       1 | 0.57 |     |       38 |       4 | 2.29 |     |          |         |      |
|       17 |       5 | 2.86 |     |       39 |       3 | 1.71 |     |          |         |      |
|       18 |       2 | 1.14 |     |       40 |       5 | 2.86 |     |          |         |      |
|       19 |       2 | 1.14 |     |       41 |       4 | 2.29 |     |          |         |      |
|       20 |       2 | 1.14 |     |       42 |       5 | 2.86 |     |          |         |      |
|       21 |       5 | 2.86 |     |       43 |       6 | 3.43 |     |          |         |      |
|       22 |       3 | 1.71 |     |       44 |       4 | 2.29 |     |          |         |      |
|       23 |       5 | 2.86 |     |       45 |       4 | 2.29 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       8 | 3.01 |     |       21 |       6 | 2.26 |     | 42       | 7       | 2.63 |
|        2 |       4 | 1.5  |     |       22 |       7 | 2.63 |     | 43       | 7       | 2.63 |
|        3 |       2 | 0.75 |     |       23 |       6 | 2.26 |     | 44       | 4       | 1.5  |
|        4 |       3 | 1.13 |     |       24 |       4 | 1.5  |     | 45       | 5       | 1.88 |
|        5 |       5 | 1.88 |     |       25 |       2 | 0.75 |     | 46       | 3       | 1.13 |
|        6 |       2 | 0.75 |     |       26 |       4 | 1.5  |     | 47       | 7       | 2.63 |
|        7 |       5 | 1.88 |     |       27 |       3 | 1.13 |     | 48       | 6       | 2.26 |
|        8 |       6 | 2.26 |     |       28 |       5 | 1.88 |     | 49       | 3       | 1.13 |
|        9 |       3 | 1.13 |     |       29 |       6 | 2.26 |     | 50       | 8       | 3.01 |
|       10 |       5 | 1.88 |     |       30 |       7 | 2.63 |     | 51       | 8       | 3.01 |
|       11 |       8 | 3.01 |     |       31 |       6 | 2.26 |     | 52       | 5       | 1.88 |
|       12 |       2 | 0.75 |     |       33 |       2 | 0.75 |     | 53       | 7       | 2.63 |
|       13 |       6 | 2.26 |     |       34 |       6 | 2.26 |     | 54       | 3       | 1.13 |
|       14 |       4 | 1.5  |     |       35 |       2 | 0.75 |     | 55       | 4       | 1.5  |
|       15 |       2 | 0.75 |     |       36 |       5 | 1.88 |     |          |         |      |
|       16 |       4 | 1.5  |     |       37 |       7 | 2.63 |     |          |         |      |
|       17 |       5 | 1.88 |     |       38 |       5 | 1.88 |     |          |         |      |
|       18 |       7 | 2.63 |     |       39 |       6 | 2.26 |     |          |         |      |
|       19 |       3 | 1.13 |     |       40 |       7 | 2.63 |     |          |         |      |
|       20 |       2 | 0.75 |     |       41 |       7 | 2.63 |     |          |         |      |

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

