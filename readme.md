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
| 2025-02-22 | 01155 | [1, 2, 7, 22, 23, 46, 50]    |      0 | 2025-02-22 19:00:38.011886 |
| 2025-02-20 | 01154 | [13, 17, 20, 27, 36, 54, 47] |      0 | 2025-02-20 19:00:12.840993 |
| 2025-02-18 | 01153 | [12, 13, 30, 38, 40, 47, 42] |      0 | 2025-02-19 19:00:18.391949 |
| 2025-02-15 | 01152 | [22, 37, 38, 47, 51, 55, 31] |      0 | 2025-02-15 19:00:15.907100 |
| 2025-02-13 | 01151 | [2, 8, 23, 26, 42, 47, 7]    |      0 | 2025-02-13 19:00:13.398152 |
| 2025-02-11 | 01150 | [1, 9, 18, 21, 35, 40, 44]   |      0 | 2025-02-11 19:00:16.958421 |
| 2025-02-08 | 01149 | [11, 22, 28, 44, 48, 49, 23] |      0 | 2025-02-08 19:00:21.621172 |
| 2025-02-06 | 01148 | [1, 11, 31, 43, 48, 54, 19]  |      0 | 2025-02-06 19:00:16.666665 |
| 2025-02-04 | 01147 | [7, 17, 29, 51, 52, 55, 41]  |      0 | 2025-02-05 14:08:09.861421 |
| 2025-02-01 | 01146 | [1, 20, 34, 38, 45, 47, 49]  |      0 | 2025-02-04 09:10:01.052603 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     161 | 1.99 |     |       21 |     141 | 1.74 |     | 41       | 168     | 2.08 |
|        2 |     135 | 1.67 |     |       22 |     170 | 2.1  |     | 42       | 146     | 1.81 |
|        3 |     157 | 1.94 |     |       23 |     161 | 1.99 |     | 43       | 160     | 1.98 |
|        4 |     129 | 1.6  |     |       24 |     145 | 1.79 |     | 44       | 152     | 1.88 |
|        5 |     146 | 1.81 |     |       25 |     135 | 1.67 |     | 45       | 141     | 1.74 |
|        6 |     126 | 1.56 |     |       26 |     136 | 1.68 |     | 46       | 156     | 1.93 |
|        7 |     127 | 1.57 |     |       27 |     134 | 1.66 |     | 47       | 149     | 1.84 |
|        8 |     155 | 1.92 |     |       28 |     131 | 1.62 |     | 48       | 155     | 1.92 |
|        9 |     161 | 1.99 |     |       29 |     152 | 1.88 |     | 49       | 153     | 1.89 |
|       10 |     138 | 1.71 |     |       30 |     126 | 1.56 |     | 50       | 147     | 1.82 |
|       11 |     154 | 1.9  |     |       31 |     153 | 1.89 |     | 51       | 171     | 2.12 |
|       12 |     158 | 1.95 |     |       32 |     153 | 1.89 |     | 52       | 152     | 1.88 |
|       13 |     140 | 1.73 |     |       33 |     149 | 1.84 |     | 53       | 155     | 1.92 |
|       14 |     141 | 1.74 |     |       34 |     161 | 1.99 |     | 54       | 142     | 1.76 |
|       15 |     133 | 1.65 |     |       35 |     150 | 1.86 |     | 55       | 146     | 1.81 |
|       16 |     136 | 1.68 |     |       36 |     139 | 1.72 |     |          |         |      |
|       17 |     134 | 1.66 |     |       37 |     132 | 1.63 |     |          |         |      |
|       18 |     151 | 1.87 |     |       38 |     140 | 1.73 |     |          |         |      |
|       19 |     144 | 1.78 |     |       39 |     138 | 1.71 |     |          |         |      |
|       20 |     159 | 1.97 |     |       40 |     160 | 1.98 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       4 | 4.4 |     |       28 |       2 | 2.2  |     | 50       | 2       | 2.2 |
|        2 |       2 | 2.2 |     |       29 |       1 | 1.1  |     | 51       | 4       | 4.4 |
|        5 |       1 | 1.1 |     |       30 |       1 | 1.1  |     | 52       | 2       | 2.2 |
|        7 |       3 | 3.3 |     |       31 |       2 | 2.2  |     | 54       | 2       | 2.2 |
|        8 |       2 | 2.2 |     |       34 |       2 | 2.2  |     | 55       | 2       | 2.2 |
|        9 |       1 | 1.1 |     |       35 |       1 | 1.1  |     |          |         |     |
|       11 |       3 | 3.3 |     |       36 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       2 | 2.2 |     |       38 |       3 | 3.3  |     |          |         |     |
|       14 |       1 | 1.1 |     |       39 |       1 | 1.1  |     |          |         |     |
|       17 |       2 | 2.2 |     |       40 |       3 | 3.3  |     |          |         |     |
|       18 |       2 | 2.2 |     |       41 |       1 | 1.1  |     |          |         |     |
|       19 |       2 | 2.2 |     |       42 |       3 | 3.3  |     |          |         |     |
|       20 |       2 | 2.2 |     |       43 |       1 | 1.1  |     |          |         |     |
|       21 |       2 | 2.2 |     |       44 |       2 | 2.2  |     |          |         |     |
|       22 |       4 | 4.4 |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       3 | 3.3 |     |       46 |       1 | 1.1  |     |          |         |     |
|       24 |       1 | 1.1 |     |       47 |       5 | 5.49 |     |          |         |     |
|       26 |       1 | 1.1 |     |       48 |       3 | 3.3  |     |          |         |     |
|       27 |       1 | 1.1 |     |       49 |       3 | 3.3  |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       4 | 4.4 |     |       28 |       2 | 2.2  |     | 50       | 2       | 2.2 |
|        2 |       2 | 2.2 |     |       29 |       1 | 1.1  |     | 51       | 4       | 4.4 |
|        5 |       1 | 1.1 |     |       30 |       1 | 1.1  |     | 52       | 2       | 2.2 |
|        7 |       3 | 3.3 |     |       31 |       2 | 2.2  |     | 54       | 2       | 2.2 |
|        8 |       2 | 2.2 |     |       34 |       2 | 2.2  |     | 55       | 2       | 2.2 |
|        9 |       1 | 1.1 |     |       35 |       1 | 1.1  |     |          |         |     |
|       11 |       3 | 3.3 |     |       36 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       2 | 2.2 |     |       38 |       3 | 3.3  |     |          |         |     |
|       14 |       1 | 1.1 |     |       39 |       1 | 1.1  |     |          |         |     |
|       17 |       2 | 2.2 |     |       40 |       3 | 3.3  |     |          |         |     |
|       18 |       2 | 2.2 |     |       41 |       1 | 1.1  |     |          |         |     |
|       19 |       2 | 2.2 |     |       42 |       3 | 3.3  |     |          |         |     |
|       20 |       2 | 2.2 |     |       43 |       1 | 1.1  |     |          |         |     |
|       21 |       2 | 2.2 |     |       44 |       2 | 2.2  |     |          |         |     |
|       22 |       4 | 4.4 |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       3 | 3.3 |     |       46 |       1 | 1.1  |     |          |         |     |
|       24 |       1 | 1.1 |     |       47 |       5 | 5.49 |     |          |         |     |
|       26 |       1 | 1.1 |     |       48 |       3 | 3.3  |     |          |         |     |
|       27 |       1 | 1.1 |     |       49 |       3 | 3.3  |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 2.75 |     |       22 |       7 | 3.85 |     | 42       | 5       | 2.75 |
|        2 |       2 | 1.1  |     |       23 |       4 | 2.2  |     | 43       | 2       | 1.1  |
|        3 |       2 | 1.1  |     |       24 |       2 | 1.1  |     | 44       | 3       | 1.65 |
|        4 |       3 | 1.65 |     |       25 |       1 | 0.55 |     | 45       | 2       | 1.1  |
|        5 |       2 | 1.1  |     |       26 |       3 | 1.65 |     | 46       | 3       | 1.65 |
|        6 |       2 | 1.1  |     |       27 |       2 | 1.1  |     | 47       | 6       | 3.3  |
|        7 |       3 | 1.65 |     |       28 |       4 | 2.2  |     | 48       | 4       | 2.2  |
|        8 |       4 | 2.2  |     |       29 |       3 | 1.65 |     | 49       | 3       | 1.65 |
|        9 |       2 | 1.1  |     |       30 |       3 | 1.65 |     | 50       | 5       | 2.75 |
|       10 |       3 | 1.65 |     |       31 |       4 | 2.2  |     | 51       | 8       | 4.4  |
|       11 |       5 | 2.75 |     |       32 |       1 | 0.55 |     | 52       | 3       | 1.65 |
|       12 |       2 | 1.1  |     |       33 |       3 | 1.65 |     | 53       | 4       | 2.2  |
|       13 |       4 | 2.2  |     |       34 |       3 | 1.65 |     | 54       | 2       | 1.1  |
|       14 |       2 | 1.1  |     |       35 |       1 | 0.55 |     | 55       | 3       | 1.65 |
|       16 |       3 | 1.65 |     |       36 |       4 | 2.2  |     |          |         |      |
|       17 |       3 | 1.65 |     |       37 |       5 | 2.75 |     |          |         |      |
|       18 |       6 | 3.3  |     |       38 |       4 | 2.2  |     |          |         |      |
|       19 |       3 | 1.65 |     |       39 |       4 | 2.2  |     |          |         |      |
|       20 |       3 | 1.65 |     |       40 |       5 | 2.75 |     |          |         |      |
|       21 |       3 | 1.65 |     |       41 |       4 | 2.2  |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       8 | 3.01 |     |       21 |       5 | 1.88 |     | 41       | 6       | 2.26 |
|        2 |       3 | 1.13 |     |       22 |       8 | 3.01 |     | 42       | 6       | 2.26 |
|        3 |       3 | 1.13 |     |       23 |       4 | 1.5  |     | 43       | 3       | 1.13 |
|        4 |       4 | 1.5  |     |       24 |       6 | 2.26 |     | 44       | 4       | 1.5  |
|        5 |       2 | 0.75 |     |       25 |       1 | 0.38 |     | 45       | 3       | 1.13 |
|        6 |       2 | 0.75 |     |       26 |       5 | 1.88 |     | 46       | 3       | 1.13 |
|        7 |       4 | 1.5  |     |       27 |       3 | 1.13 |     | 47       | 8       | 3.01 |
|        8 |       5 | 1.88 |     |       28 |       5 | 1.88 |     | 48       | 5       | 1.88 |
|        9 |       5 | 1.88 |     |       29 |       6 | 2.26 |     | 49       | 4       | 1.5  |
|       10 |       5 | 1.88 |     |       30 |       5 | 1.88 |     | 50       | 5       | 1.88 |
|       11 |       9 | 3.38 |     |       31 |       4 | 1.5  |     | 51       | 10      | 3.76 |
|       12 |       4 | 1.5  |     |       32 |       3 | 1.13 |     | 52       | 4       | 1.5  |
|       13 |       5 | 1.88 |     |       33 |       4 | 1.5  |     | 53       | 6       | 2.26 |
|       14 |       3 | 1.13 |     |       34 |       3 | 1.13 |     | 54       | 5       | 1.88 |
|       15 |       1 | 0.38 |     |       35 |       2 | 0.75 |     | 55       | 4       | 1.5  |
|       16 |      11 | 4.14 |     |       36 |       6 | 2.26 |     |          |         |      |
|       17 |       4 | 1.5  |     |       37 |       7 | 2.63 |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       6 | 2.26 |     |          |         |      |
|       19 |       5 | 1.88 |     |       39 |       6 | 2.26 |     |          |         |      |
|       20 |       5 | 1.88 |     |       40 |       6 | 2.26 |     |          |         |      |

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

