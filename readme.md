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
|       | date       | result                      | predicted                |
|------:|:-----------|:----------------------------|:-------------------------|
| 21060 | 2018-01-23 | [3, 10, 15, 23, 41, 53, 35] | [23, 54, 10, 41, 35, 53] | 

## raw details 6/55 last 10 days
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2024-12-21 | 01129 | [4, 16, 29, 30, 35, 51, 48]  |      0 | 2024-12-23 16:21:56.452504 |
| 2024-12-19 | 01128 | [13, 16, 32, 39, 49, 51, 11] |      0 | 2024-12-23 16:21:56.452645 |
| 2024-12-17 | 01127 | [2, 14, 27, 30, 53, 54, 16]  |      0 | 2024-12-23 16:21:56.452777 |
| 2024-12-14 | 01126 | [3, 10, 19, 20, 21, 24, 7]   |      0 | 2024-12-16 12:55:37.831668 |
| 2024-12-12 | 01125 | [1, 9, 12, 18, 37, 44, 11]   |      0 | 2024-12-16 12:55:37.831810 |
| 2024-12-10 | 01124 | [11, 15, 26, 45, 52, 55, 36] |      0 | 2024-12-16 12:55:37.831894 |
| 2024-12-07 | 01123 | [16, 17, 22, 24, 29, 37, 54] |      0 | 2024-12-16 12:55:37.831974 |
| 2024-12-05 | 01122 | [16, 21, 29, 41, 42, 47, 9]  |      0 | 2024-12-16 12:55:37.832054 |
| 2024-12-03 | 01121 | [10, 19, 33, 39, 47, 54, 16] |      0 | 2024-12-16 12:55:37.832134 |
| 2024-11-30 | 01120 | [1, 20, 24, 26, 38, 41, 36]  |      0 | 2024-12-16 12:55:37.832210 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     156 | 1.97 |     |       21 |     138 | 1.75 |     | 41       | 164     | 2.08 |
|        2 |     133 | 1.68 |     |       22 |     163 | 2.06 |     | 42       | 141     | 1.78 |
|        3 |     155 | 1.96 |     |       23 |     157 | 1.99 |     | 43       | 158     | 2.0  |
|        4 |     126 | 1.59 |     |       24 |     143 | 1.81 |     | 44       | 149     | 1.89 |
|        5 |     144 | 1.82 |     |       25 |     134 | 1.7  |     | 45       | 139     | 1.76 |
|        6 |     124 | 1.57 |     |       26 |     133 | 1.68 |     | 46       | 153     | 1.94 |
|        7 |     124 | 1.57 |     |       27 |     132 | 1.67 |     | 47       | 143     | 1.81 |
|        8 |     151 | 1.91 |     |       28 |     127 | 1.61 |     | 48       | 151     | 1.91 |
|        9 |     159 | 2.01 |     |       29 |     149 | 1.89 |     | 49       | 150     | 1.9  |
|       10 |     135 | 1.71 |     |       30 |     123 | 1.56 |     | 50       | 142     | 1.8  |
|       11 |     149 | 1.89 |     |       31 |     149 | 1.89 |     | 51       | 163     | 2.06 |
|       12 |     156 | 1.97 |     |       32 |     152 | 1.92 |     | 52       | 149     | 1.89 |
|       13 |     136 | 1.72 |     |       33 |     146 | 1.85 |     | 53       | 151     | 1.91 |
|       14 |     139 | 1.76 |     |       34 |     158 | 2    |     | 54       | 140     | 1.77 |
|       15 |     133 | 1.68 |     |       35 |     149 | 1.89 |     | 55       | 143     | 1.81 |
|       16 |     133 | 1.68 |     |       36 |     135 | 1.71 |     |          |         |      |
|       17 |     131 | 1.66 |     |       37 |     127 | 1.61 |     |          |         |      |
|       18 |     145 | 1.83 |     |       38 |     136 | 1.72 |     |          |         |      |
|       19 |     141 | 1.78 |     |       39 |     134 | 1.7  |     |          |         |      |
|       20 |     156 | 1.97 |     |       40 |     155 | 1.96 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.04 |     | 26       | 1       | 2.04 |
|        2 |       1 | 2.04 |     | 27       | 1       | 2.04 |
|        3 |       1 | 2.04 |     | 29       | 2       | 4.08 |
|        4 |       1 | 2.04 |     | 30       | 2       | 4.08 |
|        7 |       1 | 2.04 |     | 32       | 1       | 2.04 |
|        9 |       1 | 2.04 |     | 35       | 1       | 2.04 |
|       10 |       1 | 2.04 |     | 36       | 1       | 2.04 |
|       11 |       3 | 6.12 |     | 37       | 2       | 4.08 |
|       12 |       1 | 2.04 |     | 39       | 1       | 2.04 |
|       13 |       1 | 2.04 |     | 44       | 1       | 2.04 |
|       14 |       1 | 2.04 |     | 45       | 1       | 2.04 |
|       15 |       1 | 2.04 |     | 48       | 1       | 2.04 |
|       16 |       4 | 8.16 |     | 49       | 1       | 2.04 |
|       17 |       1 | 2.04 |     | 51       | 2       | 4.08 |
|       18 |       1 | 2.04 |     | 52       | 1       | 2.04 |
|       19 |       1 | 2.04 |     | 53       | 1       | 2.04 |
|       20 |       1 | 2.04 |     | 54       | 2       | 4.08 |
|       21 |       1 | 2.04 |     | 55       | 1       | 2.04 |
|       22 |       1 | 2.04 |     |          |         |      |
|       24 |       2 | 4.08 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.04 |     | 26       | 1       | 2.04 |
|        2 |       1 | 2.04 |     | 27       | 1       | 2.04 |
|        3 |       1 | 2.04 |     | 29       | 2       | 4.08 |
|        4 |       1 | 2.04 |     | 30       | 2       | 4.08 |
|        7 |       1 | 2.04 |     | 32       | 1       | 2.04 |
|        9 |       1 | 2.04 |     | 35       | 1       | 2.04 |
|       10 |       1 | 2.04 |     | 36       | 1       | 2.04 |
|       11 |       3 | 6.12 |     | 37       | 2       | 4.08 |
|       12 |       1 | 2.04 |     | 39       | 1       | 2.04 |
|       13 |       1 | 2.04 |     | 44       | 1       | 2.04 |
|       14 |       1 | 2.04 |     | 45       | 1       | 2.04 |
|       15 |       1 | 2.04 |     | 48       | 1       | 2.04 |
|       16 |       4 | 8.16 |     | 49       | 1       | 2.04 |
|       17 |       1 | 2.04 |     | 51       | 2       | 4.08 |
|       18 |       1 | 2.04 |     | 52       | 1       | 2.04 |
|       19 |       1 | 2.04 |     | 53       | 1       | 2.04 |
|       20 |       1 | 2.04 |     | 54       | 2       | 4.08 |
|       21 |       1 | 2.04 |     | 55       | 1       | 2.04 |
|       22 |       1 | 2.04 |     |          |         |      |
|       24 |       2 | 4.08 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.86 |     |       22 |       3 | 2.14 |     | 43       | 2       | 1.43 |
|        2 |       1 | 0.71 |     |       24 |       5 | 3.57 |     | 44       | 1       | 0.71 |
|        3 |       1 | 0.71 |     |       25 |       2 | 1.43 |     | 45       | 3       | 2.14 |
|        4 |       2 | 1.43 |     |       26 |       4 | 2.86 |     | 47       | 2       | 1.43 |
|        6 |       2 | 1.43 |     |       27 |       1 | 0.71 |     | 48       | 3       | 2.14 |
|        7 |       1 | 0.71 |     |       28 |       1 | 0.71 |     | 49       | 2       | 1.43 |
|        8 |       1 | 0.71 |     |       29 |       4 | 2.86 |     | 50       | 1       | 0.71 |
|        9 |       4 | 2.86 |     |       30 |       2 | 1.43 |     | 51       | 7       | 5.0  |
|       10 |       3 | 2.14 |     |       31 |       3 | 2.14 |     | 52       | 2       | 1.43 |
|       11 |       5 | 3.57 |     |       32 |       2 | 1.43 |     | 53       | 2       | 1.43 |
|       12 |       4 | 2.86 |     |       33 |       3 | 2.14 |     | 54       | 4       | 2.86 |
|       13 |       1 | 0.71 |     |       34 |       2 | 1.43 |     | 55       | 1       | 0.71 |
|       14 |       2 | 1.43 |     |       35 |       2 | 1.43 |     |          |         |      |
|       15 |       2 | 1.43 |     |       36 |       2 | 1.43 |     |          |         |      |
|       16 |       9 | 6.43 |     |       37 |       4 | 2.86 |     |          |         |      |
|       17 |       2 | 1.43 |     |       38 |       2 | 1.43 |     |          |         |      |
|       18 |       1 | 0.71 |     |       39 |       5 | 3.57 |     |          |         |      |
|       19 |       2 | 1.43 |     |       40 |       4 | 2.86 |     |          |         |      |
|       20 |       3 | 2.14 |     |       41 |       4 | 2.86 |     |          |         |      |
|       21 |       3 | 2.14 |     |       42 |       2 | 1.43 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.73 |     |       21 |       4 | 1.73 |     | 41       | 6       | 2.6  |
|        2 |       2 | 0.87 |     |       22 |       4 | 1.73 |     | 42       | 4       | 1.73 |
|        3 |       3 | 1.3  |     |       23 |       1 | 0.43 |     | 43       | 4       | 1.73 |
|        4 |       4 | 1.73 |     |       24 |       5 | 2.16 |     | 44       | 2       | 0.87 |
|        5 |       4 | 1.73 |     |       25 |       4 | 1.73 |     | 45       | 3       | 1.3  |
|        6 |       3 | 1.3  |     |       26 |       7 | 3.03 |     | 46       | 3       | 1.3  |
|        7 |       3 | 1.3  |     |       27 |       2 | 0.87 |     | 47       | 4       | 1.73 |
|        8 |       1 | 0.43 |     |       28 |       2 | 0.87 |     | 48       | 4       | 1.73 |
|        9 |       7 | 3.03 |     |       29 |       8 | 3.46 |     | 49       | 3       | 1.3  |
|       10 |       3 | 1.3  |     |       30 |       3 | 1.3  |     | 50       | 3       | 1.3  |
|       11 |       6 | 2.6  |     |       31 |       8 | 3.46 |     | 51       | 10      | 4.33 |
|       12 |       4 | 1.73 |     |       32 |       3 | 1.3  |     | 52       | 3       | 1.3  |
|       13 |       1 | 0.43 |     |       33 |       4 | 1.73 |     | 53       | 4       | 1.73 |
|       14 |       5 | 2.16 |     |       34 |       4 | 1.73 |     | 54       | 6       | 2.6  |
|       15 |       4 | 1.73 |     |       35 |       4 | 1.73 |     | 55       | 2       | 0.87 |
|       16 |      10 | 4.33 |     |       36 |       3 | 1.3  |     |          |         |      |
|       17 |       5 | 2.16 |     |       37 |       5 | 2.16 |     |          |         |      |
|       18 |       1 | 0.43 |     |       38 |       4 | 1.73 |     |          |         |      |
|       19 |       6 | 2.6  |     |       39 |       8 | 3.46 |     |          |         |      |
|       20 |       5 | 2.16 |     |       40 |       6 | 2.6  |     |          |         |      |

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

