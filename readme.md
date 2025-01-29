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
|      | date       | result                       | predicted                |
|-----:|:-----------|:-----------------------------|:-------------------------|
| 9884 | 2021-11-18 | [18, 30, 32, 37, 39, 40, 10] | [39, 10, 32, 37, 18, 40] | 

## raw details 6/55 last 10 days
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-01-21 | 01142 | [11, 18, 22, 28, 51, 52, 53] |      0 | 2025-01-22 16:21:35.655272 |
| 2025-01-18 | 01141 | [1, 3, 26, 31, 37, 41, 51]   |      0 | 2025-01-21 16:53:35.592973 |
| 2025-01-16 | 01140 | [8, 16, 34, 37, 47, 50, 23]  |      0 | 2025-01-21 16:53:35.593229 |
| 2025-01-14 | 01139 | [3, 11, 12, 24, 33, 40, 46]  |      0 | 2025-01-21 16:53:35.593336 |
| 2025-01-11 | 01138 | [10, 25, 26, 29, 37, 46, 14] |      0 | 2025-01-21 16:53:35.593432 |
| 2025-01-09 | 01137 | [18, 21, 31, 39, 50, 53, 13] |      0 | 2025-01-21 16:53:35.593527 |
| 2025-01-07 | 01136 | [4, 5, 9, 16, 22, 39, 30]    |      0 | 2025-01-08 10:41:06.663806 |
| 2025-01-04 | 01135 | [4, 10, 30, 36, 40, 53, 51]  |      0 | 2025-01-07 13:09:17.203436 |
| 2025-01-02 | 01134 | [4, 10, 18, 22, 41, 45, 50]  |      0 | 2025-01-07 13:09:17.203531 |
| 2024-12-31 | 01133 | [8, 13, 29, 36, 42, 43, 28]  |      0 | 2025-01-07 13:09:17.203777 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     157 | 1.96 |     |       21 |     139 | 1.74 |     | 41       | 167     | 2.09 |
|        2 |     133 | 1.66 |     |       22 |     166 | 2.08 |     | 42       | 143     | 1.79 |
|        3 |     157 | 1.96 |     |       23 |     158 | 1.98 |     | 43       | 159     | 1.99 |
|        4 |     129 | 1.61 |     |       24 |     144 | 1.8  |     | 44       | 150     | 1.88 |
|        5 |     145 | 1.81 |     |       25 |     135 | 1.69 |     | 45       | 140     | 1.75 |
|        6 |     126 | 1.58 |     |       26 |     135 | 1.69 |     | 46       | 155     | 1.94 |
|        7 |     124 | 1.55 |     |       27 |     133 | 1.66 |     | 47       | 144     | 1.8  |
|        8 |     153 | 1.91 |     |       28 |     129 | 1.61 |     | 48       | 152     | 1.9  |
|        9 |     160 | 2    |     |       29 |     151 | 1.89 |     | 49       | 150     | 1.88 |
|       10 |     138 | 1.73 |     |       30 |     125 | 1.56 |     | 50       | 145     | 1.81 |
|       11 |     151 | 1.89 |     |       31 |     151 | 1.89 |     | 51       | 167     | 2.09 |
|       12 |     157 | 1.96 |     |       32 |     153 | 1.91 |     | 52       | 150     | 1.88 |
|       13 |     138 | 1.73 |     |       33 |     149 | 1.86 |     | 53       | 155     | 1.94 |
|       14 |     140 | 1.75 |     |       34 |     159 | 1.99 |     | 54       | 140     | 1.75 |
|       15 |     133 | 1.66 |     |       35 |     149 | 1.86 |     | 55       | 144     | 1.8  |
|       16 |     136 | 1.7  |     |       36 |     138 | 1.73 |     |          |         |      |
|       17 |     132 | 1.65 |     |       37 |     130 | 1.63 |     |          |         |      |
|       18 |     149 | 1.86 |     |       38 |     137 | 1.71 |     |          |         |      |
|       19 |     142 | 1.78 |     |       39 |     137 | 1.71 |     |          |         |      |
|       20 |     157 | 1.96 |     |       40 |     157 | 1.96 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.43 |     | 29       | 2       | 2.86 |
|        3 |       2 | 2.86 |     | 30       | 2       | 2.86 |
|        4 |       3 | 4.29 |     | 31       | 2       | 2.86 |
|        5 |       1 | 1.43 |     | 33       | 1       | 1.43 |
|        8 |       2 | 2.86 |     | 34       | 1       | 1.43 |
|        9 |       1 | 1.43 |     | 36       | 2       | 2.86 |
|       10 |       3 | 4.29 |     | 37       | 3       | 4.29 |
|       11 |       2 | 2.86 |     | 39       | 2       | 2.86 |
|       12 |       1 | 1.43 |     | 40       | 2       | 2.86 |
|       13 |       2 | 2.86 |     | 41       | 2       | 2.86 |
|       14 |       1 | 1.43 |     | 42       | 1       | 1.43 |
|       16 |       2 | 2.86 |     | 43       | 1       | 1.43 |
|       18 |       3 | 4.29 |     | 45       | 1       | 1.43 |
|       21 |       1 | 1.43 |     | 46       | 2       | 2.86 |
|       22 |       3 | 4.29 |     | 47       | 1       | 1.43 |
|       23 |       1 | 1.43 |     | 50       | 3       | 4.29 |
|       24 |       1 | 1.43 |     | 51       | 3       | 4.29 |
|       25 |       1 | 1.43 |     | 52       | 1       | 1.43 |
|       26 |       2 | 2.86 |     | 53       | 3       | 4.29 |
|       28 |       2 | 2.86 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.43 |     | 29       | 2       | 2.86 |
|        3 |       2 | 2.86 |     | 30       | 2       | 2.86 |
|        4 |       3 | 4.29 |     | 31       | 2       | 2.86 |
|        5 |       1 | 1.43 |     | 33       | 1       | 1.43 |
|        8 |       2 | 2.86 |     | 34       | 1       | 1.43 |
|        9 |       1 | 1.43 |     | 36       | 2       | 2.86 |
|       10 |       3 | 4.29 |     | 37       | 3       | 4.29 |
|       11 |       2 | 2.86 |     | 39       | 2       | 2.86 |
|       12 |       1 | 1.43 |     | 40       | 2       | 2.86 |
|       13 |       2 | 2.86 |     | 41       | 2       | 2.86 |
|       14 |       1 | 1.43 |     | 42       | 1       | 1.43 |
|       16 |       2 | 2.86 |     | 43       | 1       | 1.43 |
|       18 |       3 | 4.29 |     | 45       | 1       | 1.43 |
|       21 |       1 | 1.43 |     | 46       | 2       | 2.86 |
|       22 |       3 | 4.29 |     | 47       | 1       | 1.43 |
|       23 |       1 | 1.43 |     | 50       | 3       | 4.29 |
|       24 |       1 | 1.43 |     | 51       | 3       | 4.29 |
|       25 |       1 | 1.43 |     | 52       | 1       | 1.43 |
|       26 |       2 | 2.86 |     | 53       | 3       | 4.29 |
|       28 |       2 | 2.86 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.86 |     |       21 |       3 | 1.86 |     | 41       | 5       | 3.11 |
|        2 |       1 | 0.62 |     |       22 |       4 | 2.48 |     | 42       | 3       | 1.86 |
|        3 |       3 | 1.86 |     |       23 |       1 | 0.62 |     | 43       | 1       | 0.62 |
|        4 |       4 | 2.48 |     |       24 |       4 | 2.48 |     | 44       | 2       | 1.24 |
|        5 |       1 | 0.62 |     |       25 |       1 | 0.62 |     | 45       | 2       | 1.24 |
|        6 |       2 | 1.24 |     |       26 |       4 | 2.48 |     | 46       | 2       | 1.24 |
|        7 |       1 | 0.62 |     |       27 |       2 | 1.24 |     | 47       | 3       | 1.86 |
|        8 |       2 | 1.24 |     |       28 |       2 | 1.24 |     | 48       | 2       | 1.24 |
|        9 |       3 | 1.86 |     |       29 |       5 | 3.11 |     | 49       | 1       | 0.62 |
|       10 |       5 | 3.11 |     |       30 |       4 | 2.48 |     | 50       | 3       | 1.86 |
|       11 |       5 | 3.11 |     |       31 |       2 | 1.24 |     | 51       | 6       | 3.73 |
|       12 |       2 | 1.24 |     |       32 |       2 | 1.24 |     | 52       | 2       | 1.24 |
|       13 |       3 | 1.86 |     |       33 |       4 | 2.48 |     | 53       | 5       | 3.11 |
|       14 |       2 | 1.24 |     |       34 |       1 | 0.62 |     | 54       | 3       | 1.86 |
|       15 |       1 | 0.62 |     |       35 |       1 | 0.62 |     | 55       | 2       | 1.24 |
|       16 |       9 | 5.59 |     |       36 |       5 | 3.11 |     |          |         |      |
|       17 |       2 | 1.24 |     |       37 |       5 | 3.11 |     |          |         |      |
|       18 |       5 | 3.11 |     |       38 |       2 | 1.24 |     |          |         |      |
|       19 |       3 | 1.86 |     |       39 |       5 | 3.11 |     |          |         |      |
|       20 |       3 | 1.86 |     |       40 |       2 | 1.24 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.98 |     |       21 |       4 | 1.59 |     | 41       | 7       | 2.78 |
|        2 |       2 | 0.79 |     |       22 |       6 | 2.38 |     | 42       | 4       | 1.59 |
|        3 |       3 | 1.19 |     |       23 |       1 | 0.4  |     | 43       | 3       | 1.19 |
|        4 |       5 | 1.98 |     |       24 |       6 | 2.38 |     | 44       | 2       | 0.79 |
|        5 |       2 | 0.79 |     |       25 |       3 | 1.19 |     | 45       | 4       | 1.59 |
|        6 |       4 | 1.59 |     |       26 |       7 | 2.78 |     | 46       | 3       | 1.19 |
|        7 |       2 | 0.79 |     |       27 |       2 | 0.79 |     | 47       | 3       | 1.19 |
|        8 |       3 | 1.19 |     |       28 |       3 | 1.19 |     | 48       | 4       | 1.59 |
|        9 |       7 | 2.78 |     |       29 |       7 | 2.78 |     | 49       | 3       | 1.19 |
|       10 |       6 | 2.38 |     |       30 |       5 | 1.98 |     | 50       | 4       | 1.59 |
|       11 |       7 | 2.78 |     |       31 |       7 | 2.78 |     | 51       | 11      | 4.37 |
|       12 |       5 | 1.98 |     |       32 |       3 | 1.19 |     | 52       | 3       | 1.19 |
|       13 |       3 | 1.19 |     |       33 |       6 | 2.38 |     | 53       | 6       | 2.38 |
|       14 |       3 | 1.19 |     |       34 |       4 | 1.59 |     | 54       | 6       | 2.38 |
|       15 |       2 | 0.79 |     |       35 |       2 | 0.79 |     | 55       | 2       | 0.79 |
|       16 |      13 | 5.16 |     |       36 |       6 | 2.38 |     |          |         |      |
|       17 |       3 | 1.19 |     |       37 |       7 | 2.78 |     |          |         |      |
|       18 |       5 | 1.98 |     |       38 |       3 | 1.19 |     |          |         |      |
|       19 |       4 | 1.59 |     |       39 |       9 | 3.57 |     |          |         |      |
|       20 |       6 | 2.38 |     |       40 |       6 | 2.38 |     |          |         |      |

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

