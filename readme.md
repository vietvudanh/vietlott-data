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
| 2025-03-15 | 01164 | [1, 34, 39, 40, 42, 50, 25]  |      0 | 2025-03-15 19:00:14.000659 |
| 2025-03-13 | 01163 | [7, 13, 21, 43, 52, 53, 17]  |      0 | 2025-03-13 19:00:15.799984 |
| 2025-03-11 | 01162 | [1, 16, 18, 30, 31, 44, 34]  |      0 | 2025-03-11 19:00:14.832710 |
| 2025-03-08 | 01161 | [10, 38, 41, 43, 45, 48, 8]  |      0 | 2025-03-10 11:41:38.454144 |
| 2025-03-06 | 01160 | [5, 10, 21, 26, 43, 51, 15]  |      0 | 2025-03-10 11:41:38.454275 |
| 2025-03-04 | 01159 | [5, 14, 27, 43, 45, 53, 47]  |      0 | 2025-03-04 19:00:14.873524 |
| 2025-03-01 | 01158 | [15, 17, 34, 37, 39, 45, 41] |      0 | 2025-03-01 19:00:19.333042 |
| 2025-02-27 | 01157 | [5, 9, 21, 31, 43, 53, 11]   |      0 | 2025-02-27 22:55:20.424084 |
| 2025-02-25 | 01156 | [1, 7, 11, 24, 29, 30, 48]   |      0 | 2025-02-25 20:58:27.007819 |
| 2025-02-22 | 01155 | [1, 2, 7, 22, 23, 46, 50]    |      0 | 2025-02-22 19:00:38.011886 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     164 | 2.01 |     |       21 |     144 | 1.77 |     | 41       | 170     | 2.09 |
|        2 |     135 | 1.66 |     |       22 |     170 | 2.09 |     | 42       | 147     | 1.8  |
|        3 |     157 | 1.93 |     |       23 |     161 | 1.98 |     | 43       | 165     | 2.03 |
|        4 |     129 | 1.58 |     |       24 |     146 | 1.79 |     | 44       | 153     | 1.88 |
|        5 |     149 | 1.83 |     |       25 |     136 | 1.67 |     | 45       | 144     | 1.77 |
|        6 |     126 | 1.55 |     |       26 |     137 | 1.68 |     | 46       | 156     | 1.91 |
|        7 |     129 | 1.58 |     |       27 |     135 | 1.66 |     | 47       | 150     | 1.84 |
|        8 |     156 | 1.91 |     |       28 |     131 | 1.61 |     | 48       | 157     | 1.93 |
|        9 |     162 | 1.99 |     |       29 |     153 | 1.88 |     | 49       | 153     | 1.88 |
|       10 |     140 | 1.72 |     |       30 |     128 | 1.57 |     | 50       | 148     | 1.82 |
|       11 |     156 | 1.91 |     |       31 |     155 | 1.9  |     | 51       | 172     | 2.11 |
|       12 |     158 | 1.94 |     |       32 |     153 | 1.88 |     | 52       | 153     | 1.88 |
|       13 |     141 | 1.73 |     |       33 |     149 | 1.83 |     | 53       | 158     | 1.94 |
|       14 |     142 | 1.74 |     |       34 |     164 | 2.01 |     | 54       | 142     | 1.74 |
|       15 |     135 | 1.66 |     |       35 |     150 | 1.84 |     | 55       | 146     | 1.79 |
|       16 |     137 | 1.68 |     |       36 |     139 | 1.71 |     |          |         |      |
|       17 |     136 | 1.67 |     |       37 |     133 | 1.63 |     |          |         |      |
|       18 |     152 | 1.87 |     |       38 |     141 | 1.73 |     |          |         |      |
|       19 |     144 | 1.77 |     |       39 |     140 | 1.72 |     |          |         |      |
|       20 |     159 | 1.95 |     |       40 |     161 | 1.98 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       4 | 4.4 |     |       25 |       1 | 1.1  |     | 50       | 2       | 2.2 |
|        2 |       1 | 1.1 |     |       26 |       1 | 1.1  |     | 51       | 2       | 2.2 |
|        5 |       3 | 3.3 |     |       27 |       2 | 2.2  |     | 52       | 1       | 1.1 |
|        7 |       3 | 3.3 |     |       29 |       1 | 1.1  |     | 53       | 3       | 3.3 |
|        8 |       1 | 1.1 |     |       30 |       3 | 3.3  |     | 54       | 1       | 1.1 |
|        9 |       1 | 1.1 |     |       31 |       3 | 3.3  |     | 55       | 1       | 1.1 |
|       10 |       2 | 2.2 |     |       34 |       3 | 3.3  |     |          |         |     |
|       11 |       2 | 2.2 |     |       36 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       3 | 3.3 |     |       38 |       3 | 3.3  |     |          |         |     |
|       14 |       1 | 1.1 |     |       39 |       2 | 2.2  |     |          |         |     |
|       15 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       16 |       1 | 1.1 |     |       41 |       2 | 2.2  |     |          |         |     |
|       17 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1 |     |       43 |       5 | 5.49 |     |          |         |     |
|       20 |       1 | 1.1 |     |       44 |       1 | 1.1  |     |          |         |     |
|       21 |       3 | 3.3 |     |       45 |       3 | 3.3  |     |          |         |     |
|       22 |       2 | 2.2 |     |       46 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1 |     |       47 |       4 | 4.4  |     |          |         |     |
|       24 |       1 | 1.1 |     |       48 |       2 | 2.2  |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       4 | 4.4 |     |       25 |       1 | 1.1  |     | 50       | 2       | 2.2 |
|        2 |       1 | 1.1 |     |       26 |       1 | 1.1  |     | 51       | 2       | 2.2 |
|        5 |       3 | 3.3 |     |       27 |       2 | 2.2  |     | 52       | 1       | 1.1 |
|        7 |       3 | 3.3 |     |       29 |       1 | 1.1  |     | 53       | 3       | 3.3 |
|        8 |       1 | 1.1 |     |       30 |       3 | 3.3  |     | 54       | 1       | 1.1 |
|        9 |       1 | 1.1 |     |       31 |       3 | 3.3  |     | 55       | 1       | 1.1 |
|       10 |       2 | 2.2 |     |       34 |       3 | 3.3  |     |          |         |     |
|       11 |       2 | 2.2 |     |       36 |       1 | 1.1  |     |          |         |     |
|       12 |       1 | 1.1 |     |       37 |       2 | 2.2  |     |          |         |     |
|       13 |       3 | 3.3 |     |       38 |       3 | 3.3  |     |          |         |     |
|       14 |       1 | 1.1 |     |       39 |       2 | 2.2  |     |          |         |     |
|       15 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       16 |       1 | 1.1 |     |       41 |       2 | 2.2  |     |          |         |     |
|       17 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       18 |       1 | 1.1 |     |       43 |       5 | 5.49 |     |          |         |     |
|       20 |       1 | 1.1 |     |       44 |       1 | 1.1  |     |          |         |     |
|       21 |       3 | 3.3 |     |       45 |       3 | 3.3  |     |          |         |     |
|       22 |       2 | 2.2 |     |       46 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1 |     |       47 |       4 | 4.4  |     |          |         |     |
|       24 |       1 | 1.1 |     |       48 |       2 | 2.2  |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       8 | 4.57 |     |       23 |       4 | 2.29 |     | 45       | 4       | 2.29 |
|        2 |       2 | 1.14 |     |       24 |       2 | 1.14 |     | 46       | 1       | 0.57 |
|        3 |       1 | 0.57 |     |       25 |       1 | 0.57 |     | 47       | 7       | 4.0  |
|        5 |       4 | 2.29 |     |       26 |       3 | 1.71 |     | 48       | 5       | 2.86 |
|        7 |       5 | 2.86 |     |       27 |       2 | 1.14 |     | 49       | 3       | 1.71 |
|        8 |       4 | 2.29 |     |       28 |       3 | 1.71 |     | 50       | 4       | 2.29 |
|        9 |       2 | 1.14 |     |       29 |       2 | 1.14 |     | 51       | 7       | 4.0  |
|       10 |       2 | 1.14 |     |       30 |       3 | 1.71 |     | 52       | 4       | 2.29 |
|       11 |       6 | 3.43 |     |       31 |       5 | 2.86 |     | 53       | 4       | 2.29 |
|       12 |       1 | 0.57 |     |       34 |       6 | 3.43 |     | 54       | 2       | 1.14 |
|       13 |       3 | 1.71 |     |       35 |       1 | 0.57 |     | 55       | 2       | 1.14 |
|       14 |       2 | 1.14 |     |       36 |       1 | 0.57 |     |          |         |      |
|       15 |       2 | 1.14 |     |       37 |       5 | 2.86 |     |          |         |      |
|       16 |       2 | 1.14 |     |       38 |       4 | 2.29 |     |          |         |      |
|       17 |       4 | 2.29 |     |       39 |       3 | 1.71 |     |          |         |      |
|       18 |       4 | 2.29 |     |       40 |       4 | 2.29 |     |          |         |      |
|       19 |       2 | 1.14 |     |       41 |       4 | 2.29 |     |          |         |      |
|       20 |       2 | 1.14 |     |       42 |       4 | 2.29 |     |          |         |      |
|       21 |       5 | 2.86 |     |       43 |       6 | 3.43 |     |          |         |      |
|       22 |       5 | 2.86 |     |       44 |       3 | 1.71 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       8 | 3.01 |     |       21 |       6 | 2.26 |     | 41       | 6       | 2.26 |
|        2 |       3 | 1.13 |     |       22 |       7 | 2.63 |     | 42       | 6       | 2.26 |
|        3 |       2 | 0.75 |     |       23 |       4 | 1.5  |     | 43       | 7       | 2.63 |
|        4 |       4 | 1.5  |     |       24 |       3 | 1.13 |     | 44       | 4       | 1.5  |
|        5 |       5 | 1.88 |     |       25 |       2 | 0.75 |     | 45       | 5       | 1.88 |
|        6 |       2 | 0.75 |     |       26 |       4 | 1.5  |     | 46       | 3       | 1.13 |
|        7 |       5 | 1.88 |     |       27 |       4 | 1.5  |     | 47       | 7       | 2.63 |
|        8 |       5 | 1.88 |     |       28 |       4 | 1.5  |     | 48       | 7       | 2.63 |
|        9 |       3 | 1.13 |     |       29 |       5 | 1.88 |     | 49       | 4       | 1.5  |
|       10 |       5 | 1.88 |     |       30 |       7 | 2.63 |     | 50       | 6       | 2.26 |
|       11 |       8 | 3.01 |     |       31 |       6 | 2.26 |     | 51       | 11      | 4.14 |
|       12 |       2 | 0.75 |     |       32 |       2 | 0.75 |     | 52       | 4       | 1.5  |
|       13 |       6 | 2.26 |     |       33 |       3 | 1.13 |     | 53       | 8       | 3.01 |
|       14 |       4 | 1.5  |     |       34 |       6 | 2.26 |     | 54       | 3       | 1.13 |
|       15 |       2 | 0.75 |     |       35 |       2 | 0.75 |     | 55       | 3       | 1.13 |
|       16 |       7 | 2.63 |     |       36 |       4 | 1.5  |     |          |         |      |
|       17 |       5 | 1.88 |     |       37 |       6 | 2.26 |     |          |         |      |
|       18 |       7 | 2.63 |     |       38 |       5 | 1.88 |     |          |         |      |
|       19 |       3 | 1.13 |     |       39 |       7 | 2.63 |     |          |         |      |
|       20 |       3 | 1.13 |     |       40 |       6 | 2.26 |     |          |         |      |

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

