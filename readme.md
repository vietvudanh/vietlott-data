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
<<<<<<< HEAD
|      | date       | result                    | predicted              |
|-----:|:-----------|:--------------------------|:-----------------------|
| 1986 | 2024-06-04 | [1, 2, 7, 10, 13, 19, 24] | [10, 52, 19, 13, 2, 7] | 
||||||| 09b82b2
|      | date       | result                     | predicted               |
|-----:|:-----------|:---------------------------|:------------------------|
| 4448 | 2023-08-17 | [1, 5, 25, 32, 51, 52, 54] | [5, 25, 35, 32, 52, 54] | 
=======
| date   | result   | predicted   |
|--------|----------|-------------| 
>>>>>>> 3c935affc02ccc76e95aa6b4ba1890406ab635ec

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
|        1 |       1 | 2.04 |     | 29       | 1       | 2.04 |
|        3 |       2 | 4.08 |     | 30       | 1       | 2.04 |
|        4 |       1 | 2.04 |     | 31       | 2       | 4.08 |
|        5 |       1 | 2.04 |     | 33       | 1       | 2.04 |
|        8 |       1 | 2.04 |     | 34       | 1       | 2.04 |
|        9 |       1 | 2.04 |     | 37       | 3       | 6.12 |
|       10 |       1 | 2.04 |     | 39       | 2       | 4.08 |
|       11 |       2 | 4.08 |     | 40       | 1       | 2.04 |
|       12 |       1 | 2.04 |     | 41       | 1       | 2.04 |
|       13 |       1 | 2.04 |     | 46       | 2       | 4.08 |
|       14 |       1 | 2.04 |     | 47       | 1       | 2.04 |
|       16 |       2 | 4.08 |     | 50       | 2       | 4.08 |
|       18 |       2 | 4.08 |     | 51       | 2       | 4.08 |
|       21 |       1 | 2.04 |     | 52       | 1       | 2.04 |
|       22 |       2 | 4.08 |     | 53       | 2       | 4.08 |
|       23 |       1 | 2.04 |     |          |         |      |
|       24 |       1 | 2.04 |     |          |         |      |
|       25 |       1 | 2.04 |     |          |         |      |
|       26 |       2 | 4.08 |     |          |         |      |
|       28 |       1 | 2.04 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.04 |     | 29       | 1       | 2.04 |
|        3 |       2 | 4.08 |     | 30       | 1       | 2.04 |
|        4 |       1 | 2.04 |     | 31       | 2       | 4.08 |
|        5 |       1 | 2.04 |     | 33       | 1       | 2.04 |
|        8 |       1 | 2.04 |     | 34       | 1       | 2.04 |
|        9 |       1 | 2.04 |     | 37       | 3       | 6.12 |
|       10 |       1 | 2.04 |     | 39       | 2       | 4.08 |
|       11 |       2 | 4.08 |     | 40       | 1       | 2.04 |
|       12 |       1 | 2.04 |     | 41       | 1       | 2.04 |
|       13 |       1 | 2.04 |     | 46       | 2       | 4.08 |
|       14 |       1 | 2.04 |     | 47       | 1       | 2.04 |
|       16 |       2 | 4.08 |     | 50       | 2       | 4.08 |
|       18 |       2 | 4.08 |     | 51       | 2       | 4.08 |
|       21 |       1 | 2.04 |     | 52       | 1       | 2.04 |
|       22 |       2 | 4.08 |     | 53       | 2       | 4.08 |
|       23 |       1 | 2.04 |     |          |         |      |
|       24 |       1 | 2.04 |     |          |         |      |
|       25 |       1 | 2.04 |     |          |         |      |
|       26 |       2 | 4.08 |     |          |         |      |
|       28 |       1 | 2.04 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.43 |     |       21 |       2 | 1.43 |     | 41       | 3       | 2.14 |
|        2 |       1 | 0.71 |     |       22 |       4 | 2.86 |     | 42       | 2       | 1.43 |
|        3 |       3 | 2.14 |     |       23 |       1 | 0.71 |     | 43       | 1       | 0.71 |
|        4 |       4 | 2.86 |     |       24 |       3 | 2.14 |     | 44       | 2       | 1.43 |
|        5 |       1 | 0.71 |     |       25 |       1 | 0.71 |     | 45       | 2       | 1.43 |
|        6 |       2 | 1.43 |     |       26 |       3 | 2.14 |     | 46       | 2       | 1.43 |
|        7 |       1 | 0.71 |     |       27 |       2 | 1.43 |     | 47       | 1       | 0.71 |
|        8 |       2 | 1.43 |     |       28 |       2 | 1.43 |     | 48       | 2       | 1.43 |
|        9 |       2 | 1.43 |     |       29 |       4 | 2.86 |     | 49       | 1       | 0.71 |
|       10 |       4 | 2.86 |     |       30 |       4 | 2.86 |     | 50       | 3       | 2.14 |
|       11 |       5 | 3.57 |     |       31 |       2 | 1.43 |     | 51       | 6       | 4.29 |
|       12 |       2 | 1.43 |     |       32 |       2 | 1.43 |     | 52       | 2       | 1.43 |
|       13 |       3 | 2.14 |     |       33 |       3 | 2.14 |     | 53       | 5       | 3.57 |
|       14 |       2 | 1.43 |     |       34 |       1 | 0.71 |     | 54       | 2       | 1.43 |
|       15 |       1 | 0.71 |     |       35 |       1 | 0.71 |     | 55       | 2       | 1.43 |
|       16 |       7 | 5    |     |       36 |       4 | 2.86 |     |          |         |      |
|       17 |       2 | 1.43 |     |       37 |       5 | 3.57 |     |          |         |      |
|       18 |       5 | 3.57 |     |       38 |       1 | 0.71 |     |          |         |      |
|       19 |       2 | 1.43 |     |       39 |       4 | 2.86 |     |          |         |      |
|       20 |       2 | 1.43 |     |       40 |       2 | 1.43 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 2.16 |     |       21 |       4 | 1.73 |     | 41       | 7       | 3.03 |
|        2 |       1 | 0.43 |     |       22 |       6 | 2.6  |     | 42       | 4       | 1.73 |
|        3 |       3 | 1.3  |     |       23 |       1 | 0.43 |     | 43       | 3       | 1.3  |
|        4 |       5 | 2.16 |     |       24 |       6 | 2.6  |     | 44       | 2       | 0.87 |
|        5 |       1 | 0.43 |     |       25 |       3 | 1.3  |     | 45       | 4       | 1.73 |
|        6 |       4 | 1.73 |     |       26 |       6 | 2.6  |     | 46       | 2       | 0.87 |
|        7 |       1 | 0.43 |     |       27 |       2 | 0.87 |     | 47       | 3       | 1.3  |
|        8 |       3 | 1.3  |     |       28 |       3 | 1.3  |     | 48       | 4       | 1.73 |
|        9 |       5 | 2.16 |     |       29 |       6 | 2.6  |     | 49       | 2       | 0.87 |
|       10 |       6 | 2.6  |     |       30 |       4 | 1.73 |     | 50       | 4       | 1.73 |
|       11 |       7 | 3.03 |     |       31 |       5 | 2.16 |     | 51       | 11      | 4.76 |
|       12 |       5 | 2.16 |     |       32 |       3 | 1.3  |     | 52       | 3       | 1.3  |
|       13 |       3 | 1.3  |     |       33 |       6 | 2.6  |     | 53       | 6       | 2.6  |
|       14 |       3 | 1.3  |     |       34 |       3 | 1.3  |     | 54       | 4       | 1.73 |
|       15 |       2 | 0.87 |     |       35 |       2 | 0.87 |     | 55       | 2       | 0.87 |
|       16 |      12 | 5.19 |     |       36 |       5 | 2.16 |     |          |         |      |
|       17 |       3 | 1.3  |     |       37 |       7 | 3.03 |     |          |         |      |
|       18 |       5 | 2.16 |     |       38 |       3 | 1.3  |     |          |         |      |
|       19 |       3 | 1.3  |     |       39 |       8 | 3.46 |     |          |         |      |
|       20 |       4 | 1.73 |     |       40 |       6 | 2.6  |     |          |         |      |

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

