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
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.59 |     |       26 |       1 | 1.59 |     | 54       | 3       | 4.76 |
|        2 |       1 | 1.59 |     |       27 |       1 | 1.59 |     | 55       | 1       | 1.59 |
|        3 |       1 | 1.59 |     |       29 |       3 | 4.76 |     |          |         |      |
|        4 |       1 | 1.59 |     |       30 |       2 | 3.17 |     |          |         |      |
|        7 |       1 | 1.59 |     |       32 |       1 | 1.59 |     |          |         |      |
|        9 |       2 | 3.17 |     |       33 |       1 | 1.59 |     |          |         |      |
|       10 |       2 | 3.17 |     |       35 |       1 | 1.59 |     |          |         |      |
|       11 |       3 | 4.76 |     |       36 |       1 | 1.59 |     |          |         |      |
|       12 |       1 | 1.59 |     |       37 |       2 | 3.17 |     |          |         |      |
|       13 |       1 | 1.59 |     |       39 |       2 | 3.17 |     |          |         |      |
|       14 |       1 | 1.59 |     |       41 |       1 | 1.59 |     |          |         |      |
|       15 |       1 | 1.59 |     |       42 |       1 | 1.59 |     |          |         |      |
|       16 |       6 | 9.52 |     |       44 |       1 | 1.59 |     |          |         |      |
|       17 |       1 | 1.59 |     |       45 |       1 | 1.59 |     |          |         |      |
|       18 |       1 | 1.59 |     |       47 |       2 | 3.17 |     |          |         |      |
|       19 |       2 | 3.17 |     |       48 |       1 | 1.59 |     |          |         |      |
|       20 |       1 | 1.59 |     |       49 |       1 | 1.59 |     |          |         |      |
|       21 |       2 | 3.17 |     |       51 |       2 | 3.17 |     |          |         |      |
|       22 |       1 | 1.59 |     |       52 |       1 | 1.59 |     |          |         |      |
|       24 |       2 | 3.17 |     |       53 |       1 | 1.59 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.59 |     |       26 |       1 | 1.59 |     | 54       | 3       | 4.76 |
|        2 |       1 | 1.59 |     |       27 |       1 | 1.59 |     | 55       | 1       | 1.59 |
|        3 |       1 | 1.59 |     |       29 |       3 | 4.76 |     |          |         |      |
|        4 |       1 | 1.59 |     |       30 |       2 | 3.17 |     |          |         |      |
|        7 |       1 | 1.59 |     |       32 |       1 | 1.59 |     |          |         |      |
|        9 |       2 | 3.17 |     |       33 |       1 | 1.59 |     |          |         |      |
|       10 |       2 | 3.17 |     |       35 |       1 | 1.59 |     |          |         |      |
|       11 |       3 | 4.76 |     |       36 |       1 | 1.59 |     |          |         |      |
|       12 |       1 | 1.59 |     |       37 |       2 | 3.17 |     |          |         |      |
|       13 |       1 | 1.59 |     |       39 |       2 | 3.17 |     |          |         |      |
|       14 |       1 | 1.59 |     |       41 |       1 | 1.59 |     |          |         |      |
|       15 |       1 | 1.59 |     |       42 |       1 | 1.59 |     |          |         |      |
|       16 |       6 | 9.52 |     |       44 |       1 | 1.59 |     |          |         |      |
|       17 |       1 | 1.59 |     |       45 |       1 | 1.59 |     |          |         |      |
|       18 |       1 | 1.59 |     |       47 |       2 | 3.17 |     |          |         |      |
|       19 |       2 | 3.17 |     |       48 |       1 | 1.59 |     |          |         |      |
|       20 |       1 | 1.59 |     |       49 |       1 | 1.59 |     |          |         |      |
|       21 |       2 | 3.17 |     |       51 |       2 | 3.17 |     |          |         |      |
|       22 |       1 | 1.59 |     |       52 |       1 | 1.59 |     |          |         |      |
|       24 |       2 | 3.17 |     |       53 |       1 | 1.59 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.6  |     |       22 |       3 | 1.95 |     | 43       | 2       | 1.3  |
|        2 |       2 | 1.3  |     |       24 |       5 | 3.25 |     | 44       | 1       | 0.65 |
|        3 |       1 | 0.65 |     |       25 |       2 | 1.3  |     | 45       | 3       | 1.95 |
|        4 |       2 | 1.3  |     |       26 |       5 | 3.25 |     | 46       | 1       | 0.65 |
|        6 |       2 | 1.3  |     |       27 |       1 | 0.65 |     | 47       | 2       | 1.3  |
|        7 |       2 | 1.3  |     |       28 |       1 | 0.65 |     | 48       | 3       | 1.95 |
|        8 |       1 | 0.65 |     |       29 |       4 | 2.6  |     | 49       | 3       | 1.95 |
|        9 |       6 | 3.9  |     |       30 |       2 | 1.3  |     | 50       | 1       | 0.65 |
|       10 |       3 | 1.95 |     |       31 |       4 | 2.6  |     | 51       | 7       | 4.55 |
|       11 |       5 | 3.25 |     |       32 |       2 | 1.3  |     | 52       | 2       | 1.3  |
|       12 |       4 | 2.6  |     |       33 |       3 | 1.95 |     | 53       | 2       | 1.3  |
|       13 |       1 | 0.65 |     |       34 |       3 | 1.95 |     | 54       | 6       | 3.9  |
|       14 |       2 | 1.3  |     |       35 |       2 | 1.3  |     | 55       | 1       | 0.65 |
|       15 |       2 | 1.3  |     |       36 |       3 | 1.95 |     |          |         |      |
|       16 |       9 | 5.84 |     |       37 |       4 | 2.6  |     |          |         |      |
|       17 |       2 | 1.3  |     |       38 |       2 | 1.3  |     |          |         |      |
|       18 |       1 | 0.65 |     |       39 |       5 | 3.25 |     |          |         |      |
|       19 |       3 | 1.95 |     |       40 |       4 | 2.6  |     |          |         |      |
|       20 |       4 | 2.6  |     |       41 |       4 | 2.6  |     |          |         |      |
|       21 |       3 | 1.95 |     |       42 |       2 | 1.3  |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 1.63 |     |       21 |       5 | 2.04 |     | 41       | 6       | 2.45 |
|        2 |       3 | 1.22 |     |       22 |       4 | 1.63 |     | 42       | 5       | 2.04 |
|        3 |       3 | 1.22 |     |       23 |       1 | 0.41 |     | 43       | 4       | 1.63 |
|        4 |       4 | 1.63 |     |       24 |       5 | 2.04 |     | 44       | 2       | 0.82 |
|        5 |       4 | 1.63 |     |       25 |       5 | 2.04 |     | 45       | 3       | 1.22 |
|        6 |       3 | 1.22 |     |       26 |       7 | 2.86 |     | 46       | 3       | 1.22 |
|        7 |       3 | 1.22 |     |       27 |       3 | 1.22 |     | 47       | 4       | 1.63 |
|        8 |       1 | 0.41 |     |       28 |       2 | 0.82 |     | 48       | 4       | 1.63 |
|        9 |       7 | 2.86 |     |       29 |       8 | 3.27 |     | 49       | 3       | 1.22 |
|       10 |       4 | 1.63 |     |       30 |       3 | 1.22 |     | 50       | 4       | 1.63 |
|       11 |       6 | 2.45 |     |       31 |       8 | 3.27 |     | 51       | 10      | 4.08 |
|       12 |       4 | 1.63 |     |       32 |       3 | 1.22 |     | 52       | 4       | 1.63 |
|       13 |       1 | 0.41 |     |       33 |       4 | 1.63 |     | 53       | 5       | 2.04 |
|       14 |       5 | 2.04 |     |       34 |       5 | 2.04 |     | 54       | 6       | 2.45 |
|       15 |       4 | 1.63 |     |       35 |       4 | 1.63 |     | 55       | 2       | 0.82 |
|       16 |      10 | 4.08 |     |       36 |       3 | 1.22 |     |          |         |      |
|       17 |       6 | 2.45 |     |       37 |       5 | 2.04 |     |          |         |      |
|       18 |       3 | 1.22 |     |       38 |       4 | 1.63 |     |          |         |      |
|       19 |       6 | 2.45 |     |       39 |       8 | 3.27 |     |          |         |      |
|       20 |       5 | 2.04 |     |       40 |       7 | 2.86 |     |          |         |      |

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

