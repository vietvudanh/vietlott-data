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
| 2025-02-01 | 01146 | [1, 20, 34, 38, 45, 47, 49]  |      0 | 2025-02-04 09:10:01.052603 |
| 2025-01-30 | 01145 | [5, 8, 24, 28, 34, 52, 39]   |      0 | 2025-02-04 09:10:01.052699 |
| 2025-01-25 | 01144 | [14, 21, 40, 42, 48, 51, 19] |      0 | 2025-02-04 09:10:01.052775 |
| 2025-01-23 | 01143 | [11, 18, 22, 49, 50, 51, 37] |      0 | 2025-02-04 09:10:01.052847 |
| 2025-01-21 | 01142 | [11, 18, 22, 28, 51, 52, 53] |      0 | 2025-01-22 16:21:35.655272 |
| 2025-01-18 | 01141 | [1, 3, 26, 31, 37, 41, 51]   |      0 | 2025-01-21 16:53:35.592973 |
| 2025-01-16 | 01140 | [8, 16, 34, 37, 47, 50, 23]  |      0 | 2025-01-21 16:53:35.593229 |
| 2025-01-14 | 01139 | [3, 11, 12, 24, 33, 40, 46]  |      0 | 2025-01-21 16:53:35.593336 |
| 2025-01-11 | 01138 | [10, 25, 26, 29, 37, 46, 14] |      0 | 2025-01-21 16:53:35.593432 |
| 2025-01-09 | 01137 | [18, 21, 31, 39, 50, 53, 13] |      0 | 2025-01-21 16:53:35.593527 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     158 | 1.97 |     |       21 |     140 | 1.75 |     | 41       | 167     | 2.08 |
|        2 |     133 | 1.66 |     |       22 |     167 | 2.08 |     | 42       | 144     | 1.8  |
|        3 |     157 | 1.96 |     |       23 |     158 | 1.97 |     | 43       | 159     | 1.98 |
|        4 |     129 | 1.61 |     |       24 |     145 | 1.81 |     | 44       | 150     | 1.87 |
|        5 |     146 | 1.82 |     |       25 |     135 | 1.68 |     | 45       | 141     | 1.76 |
|        6 |     126 | 1.57 |     |       26 |     135 | 1.68 |     | 46       | 155     | 1.93 |
|        7 |     124 | 1.55 |     |       27 |     133 | 1.66 |     | 47       | 145     | 1.81 |
|        8 |     154 | 1.92 |     |       28 |     130 | 1.62 |     | 48       | 153     | 1.91 |
|        9 |     160 | 1.99 |     |       29 |     151 | 1.88 |     | 49       | 152     | 1.9  |
|       10 |     138 | 1.72 |     |       30 |     125 | 1.56 |     | 50       | 146     | 1.82 |
|       11 |     152 | 1.9  |     |       31 |     151 | 1.88 |     | 51       | 169     | 2.11 |
|       12 |     157 | 1.96 |     |       32 |     153 | 1.91 |     | 52       | 151     | 1.88 |
|       13 |     138 | 1.72 |     |       33 |     149 | 1.86 |     | 53       | 155     | 1.93 |
|       14 |     141 | 1.76 |     |       34 |     161 | 2.01 |     | 54       | 140     | 1.75 |
|       15 |     133 | 1.66 |     |       35 |     149 | 1.86 |     | 55       | 144     | 1.8  |
|       16 |     136 | 1.7  |     |       36 |     138 | 1.72 |     |          |         |      |
|       17 |     132 | 1.65 |     |       37 |     131 | 1.63 |     |          |         |      |
|       18 |     150 | 1.87 |     |       38 |     138 | 1.72 |     |          |         |      |
|       19 |     143 | 1.78 |     |       39 |     138 | 1.72 |     |          |         |      |
|       20 |     158 | 1.97 |     |       40 |     158 | 1.97 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.6 |     |       26 |       2 | 2.6  |     | 52       | 2       | 2.6 |
|        3 |       2 | 2.6 |     |       28 |       2 | 2.6  |     | 53       | 2       | 2.6 |
|        4 |       1 | 1.3 |     |       29 |       1 | 1.3  |     |          |         |     |
|        5 |       2 | 2.6 |     |       30 |       1 | 1.3  |     |          |         |     |
|        8 |       2 | 2.6 |     |       31 |       2 | 2.6  |     |          |         |     |
|        9 |       1 | 1.3 |     |       33 |       1 | 1.3  |     |          |         |     |
|       10 |       1 | 1.3 |     |       34 |       3 | 3.9  |     |          |         |     |
|       11 |       3 | 3.9 |     |       37 |       4 | 5.19 |     |          |         |     |
|       12 |       1 | 1.3 |     |       38 |       1 | 1.3  |     |          |         |     |
|       13 |       1 | 1.3 |     |       39 |       3 | 3.9  |     |          |         |     |
|       14 |       2 | 2.6 |     |       40 |       2 | 2.6  |     |          |         |     |
|       16 |       2 | 2.6 |     |       41 |       1 | 1.3  |     |          |         |     |
|       18 |       3 | 3.9 |     |       42 |       1 | 1.3  |     |          |         |     |
|       19 |       1 | 1.3 |     |       45 |       1 | 1.3  |     |          |         |     |
|       20 |       1 | 1.3 |     |       46 |       2 | 2.6  |     |          |         |     |
|       21 |       2 | 2.6 |     |       47 |       2 | 2.6  |     |          |         |     |
|       22 |       3 | 3.9 |     |       48 |       1 | 1.3  |     |          |         |     |
|       23 |       1 | 1.3 |     |       49 |       2 | 2.6  |     |          |         |     |
|       24 |       2 | 2.6 |     |       50 |       3 | 3.9  |     |          |         |     |
|       25 |       1 | 1.3 |     |       51 |       4 | 5.19 |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       2 | 2.6 |     |       26 |       2 | 2.6  |     | 52       | 2       | 2.6 |
|        3 |       2 | 2.6 |     |       28 |       2 | 2.6  |     | 53       | 2       | 2.6 |
|        4 |       1 | 1.3 |     |       29 |       1 | 1.3  |     |          |         |     |
|        5 |       2 | 2.6 |     |       30 |       1 | 1.3  |     |          |         |     |
|        8 |       2 | 2.6 |     |       31 |       2 | 2.6  |     |          |         |     |
|        9 |       1 | 1.3 |     |       33 |       1 | 1.3  |     |          |         |     |
|       10 |       1 | 1.3 |     |       34 |       3 | 3.9  |     |          |         |     |
|       11 |       3 | 3.9 |     |       37 |       4 | 5.19 |     |          |         |     |
|       12 |       1 | 1.3 |     |       38 |       1 | 1.3  |     |          |         |     |
|       13 |       1 | 1.3 |     |       39 |       3 | 3.9  |     |          |         |     |
|       14 |       2 | 2.6 |     |       40 |       2 | 2.6  |     |          |         |     |
|       16 |       2 | 2.6 |     |       41 |       1 | 1.3  |     |          |         |     |
|       18 |       3 | 3.9 |     |       42 |       1 | 1.3  |     |          |         |     |
|       19 |       1 | 1.3 |     |       45 |       1 | 1.3  |     |          |         |     |
|       20 |       1 | 1.3 |     |       46 |       2 | 2.6  |     |          |         |     |
|       21 |       2 | 2.6 |     |       47 |       2 | 2.6  |     |          |         |     |
|       22 |       3 | 3.9 |     |       48 |       1 | 1.3  |     |          |         |     |
|       23 |       1 | 1.3 |     |       49 |       2 | 2.6  |     |          |         |     |
|       24 |       2 | 2.6 |     |       50 |       3 | 3.9  |     |          |         |     |
|       25 |       1 | 1.3 |     |       51 |       4 | 5.19 |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.79 |     |       21 |       3 | 1.79 |     | 41       | 3       | 1.79 |
|        2 |       1 | 0.6  |     |       22 |       5 | 2.98 |     | 42       | 3       | 1.79 |
|        3 |       3 | 1.79 |     |       23 |       1 | 0.6  |     | 43       | 1       | 0.6  |
|        4 |       4 | 2.38 |     |       24 |       4 | 2.38 |     | 44       | 2       | 1.19 |
|        5 |       2 | 1.19 |     |       25 |       1 | 0.6  |     | 45       | 3       | 1.79 |
|        6 |       2 | 1.19 |     |       26 |       3 | 1.79 |     | 46       | 2       | 1.19 |
|        7 |       1 | 0.6  |     |       27 |       2 | 1.19 |     | 47       | 2       | 1.19 |
|        8 |       3 | 1.79 |     |       28 |       3 | 1.79 |     | 48       | 3       | 1.79 |
|        9 |       2 | 1.19 |     |       29 |       4 | 2.38 |     | 49       | 3       | 1.79 |
|       10 |       4 | 2.38 |     |       30 |       4 | 2.38 |     | 50       | 4       | 2.38 |
|       11 |       6 | 3.57 |     |       31 |       2 | 1.19 |     | 51       | 8       | 4.76 |
|       12 |       2 | 1.19 |     |       32 |       2 | 1.19 |     | 52       | 3       | 1.79 |
|       13 |       3 | 1.79 |     |       33 |       3 | 1.79 |     | 53       | 5       | 2.98 |
|       14 |       3 | 1.79 |     |       34 |       3 | 1.79 |     | 54       | 2       | 1.19 |
|       15 |       1 | 0.6  |     |       35 |       1 | 0.6  |     | 55       | 2       | 1.19 |
|       16 |       7 | 4.17 |     |       36 |       4 | 2.38 |     |          |         |      |
|       17 |       2 | 1.19 |     |       37 |       6 | 3.57 |     |          |         |      |
|       18 |       6 | 3.57 |     |       38 |       2 | 1.19 |     |          |         |      |
|       19 |       3 | 1.79 |     |       39 |       5 | 2.98 |     |          |         |      |
|       20 |       3 | 1.79 |     |       40 |       3 | 1.79 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       6 | 2.32 |     |       21 |       5 | 1.93 |     | 41       | 7       | 2.7  |
|        2 |       1 | 0.39 |     |       22 |       7 | 2.7  |     | 42       | 5       | 1.93 |
|        3 |       3 | 1.16 |     |       23 |       1 | 0.39 |     | 43       | 3       | 1.16 |
|        4 |       5 | 1.93 |     |       24 |       7 | 2.7  |     | 44       | 2       | 0.77 |
|        5 |       2 | 0.77 |     |       25 |       3 | 1.16 |     | 45       | 5       | 1.93 |
|        6 |       4 | 1.54 |     |       26 |       6 | 2.32 |     | 46       | 2       | 0.77 |
|        7 |       1 | 0.39 |     |       27 |       2 | 0.77 |     | 47       | 4       | 1.54 |
|        8 |       4 | 1.54 |     |       28 |       4 | 1.54 |     | 48       | 5       | 1.93 |
|        9 |       5 | 1.93 |     |       29 |       6 | 2.32 |     | 49       | 4       | 1.54 |
|       10 |       6 | 2.32 |     |       30 |       4 | 1.54 |     | 50       | 5       | 1.93 |
|       11 |       8 | 3.09 |     |       31 |       5 | 1.93 |     | 51       | 13      | 5.02 |
|       12 |       5 | 1.93 |     |       32 |       3 | 1.16 |     | 52       | 4       | 1.54 |
|       13 |       3 | 1.16 |     |       33 |       6 | 2.32 |     | 53       | 6       | 2.32 |
|       14 |       4 | 1.54 |     |       34 |       5 | 1.93 |     | 54       | 4       | 1.54 |
|       15 |       2 | 0.77 |     |       35 |       2 | 0.77 |     | 55       | 2       | 0.77 |
|       16 |      12 | 4.63 |     |       36 |       5 | 1.93 |     |          |         |      |
|       17 |       3 | 1.16 |     |       37 |       8 | 3.09 |     |          |         |      |
|       18 |       6 | 2.32 |     |       38 |       4 | 1.54 |     |          |         |      |
|       19 |       4 | 1.54 |     |       39 |       9 | 3.47 |     |          |         |      |
|       20 |       5 | 1.93 |     |       40 |       7 | 2.7  |     |          |         |      |

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

