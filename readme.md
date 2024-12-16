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
| 2024-12-14 | 01126 | [3, 10, 19, 20, 21, 24, 7]   |      0 | 2024-12-16 12:55:37.831668 |
| 2024-12-12 | 01125 | [1, 9, 12, 18, 37, 44, 11]   |      0 | 2024-12-16 12:55:37.831810 |
| 2024-12-10 | 01124 | [11, 15, 26, 45, 52, 55, 36] |      0 | 2024-12-16 12:55:37.831894 |
| 2024-12-07 | 01123 | [16, 17, 22, 24, 29, 37, 54] |      0 | 2024-12-16 12:55:37.831974 |
| 2024-12-05 | 01122 | [16, 21, 29, 41, 42, 47, 9]  |      0 | 2024-12-16 12:55:37.832054 |
| 2024-12-03 | 01121 | [10, 19, 33, 39, 47, 54, 16] |      0 | 2024-12-16 12:55:37.832134 |
| 2024-11-30 | 01120 | [1, 20, 24, 26, 38, 41, 36]  |      0 | 2024-12-16 12:55:37.832210 |
| 2024-11-28 | 01119 | [1, 16, 24, 28, 38, 53, 9]   |      0 | 2024-12-16 12:55:37.832288 |
| 2024-11-26 | 01118 | [8, 11, 16, 32, 40, 43, 12]  |      1 | 2024-12-16 12:55:37.849219 |
| 2024-11-23 | 01117 | [4, 12, 25, 39, 48, 51, 45]  |      1 | 2024-12-16 12:55:37.849292 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     156 | 1.98 |     |       21 |     138 | 1.75 |     | 41       | 164     | 2.08 |
|        2 |     132 | 1.67 |     |       22 |     163 | 2.07 |     | 42       | 141     | 1.79 |
|        3 |     155 | 1.97 |     |       23 |     157 | 1.99 |     | 43       | 158     | 2.0  |
|        4 |     125 | 1.59 |     |       24 |     143 | 1.81 |     | 44       | 149     | 1.89 |
|        5 |     144 | 1.83 |     |       25 |     134 | 1.7  |     | 45       | 139     | 1.76 |
|        6 |     124 | 1.57 |     |       26 |     133 | 1.69 |     | 46       | 153     | 1.94 |
|        7 |     124 | 1.57 |     |       27 |     131 | 1.66 |     | 47       | 143     | 1.81 |
|        8 |     151 | 1.92 |     |       28 |     127 | 1.61 |     | 48       | 150     | 1.9  |
|        9 |     159 | 2.02 |     |       29 |     148 | 1.88 |     | 49       | 149     | 1.89 |
|       10 |     135 | 1.71 |     |       30 |     121 | 1.54 |     | 50       | 142     | 1.8  |
|       11 |     148 | 1.88 |     |       31 |     149 | 1.89 |     | 51       | 161     | 2.04 |
|       12 |     156 | 1.98 |     |       32 |     151 | 1.92 |     | 52       | 149     | 1.89 |
|       13 |     135 | 1.71 |     |       33 |     146 | 1.85 |     | 53       | 150     | 1.9  |
|       14 |     138 | 1.75 |     |       34 |     158 | 2    |     | 54       | 139     | 1.76 |
|       15 |     133 | 1.69 |     |       35 |     148 | 1.88 |     | 55       | 143     | 1.81 |
|       16 |     130 | 1.65 |     |       36 |     135 | 1.71 |     |          |         |      |
|       17 |     131 | 1.66 |     |       37 |     127 | 1.61 |     |          |         |      |
|       18 |     145 | 1.84 |     |       38 |     136 | 1.73 |     |          |         |      |
|       19 |     141 | 1.79 |     |       39 |     133 | 1.69 |     |          |         |      |
|       20 |     156 | 1.98 |     |       40 |     155 | 1.97 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3  |     |       26 |       3 | 3.3 |     | 52       | 1       | 1.1 |
|        3 |       1 | 1.1  |     |       28 |       1 | 1.1 |     | 53       | 1       | 1.1 |
|        4 |       1 | 1.1  |     |       29 |       2 | 2.2 |     | 54       | 3       | 3.3 |
|        6 |       1 | 1.1  |     |       31 |       2 | 2.2 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1  |     |       32 |       1 | 1.1 |     |          |         |     |
|        8 |       1 | 1.1  |     |       33 |       2 | 2.2 |     |          |         |     |
|        9 |       3 | 3.3  |     |       34 |       1 | 1.1 |     |          |         |     |
|       10 |       3 | 3.3  |     |       36 |       2 | 2.2 |     |          |         |     |
|       11 |       3 | 3.3  |     |       37 |       3 | 3.3 |     |          |         |     |
|       12 |       3 | 3.3  |     |       38 |       2 | 2.2 |     |          |         |     |
|       15 |       2 | 2.2  |     |       39 |       3 | 3.3 |     |          |         |     |
|       16 |       6 | 6.59 |     |       40 |       2 | 2.2 |     |          |         |     |
|       17 |       2 | 2.2  |     |       41 |       3 | 3.3 |     |          |         |     |
|       18 |       1 | 1.1  |     |       42 |       2 | 2.2 |     |          |         |     |
|       19 |       2 | 2.2  |     |       43 |       1 | 1.1 |     |          |         |     |
|       20 |       2 | 2.2  |     |       44 |       1 | 1.1 |     |          |         |     |
|       21 |       2 | 2.2  |     |       45 |       2 | 2.2 |     |          |         |     |
|       22 |       3 | 3.3  |     |       47 |       2 | 2.2 |     |          |         |     |
|       24 |       4 | 4.4  |     |       48 |       2 | 2.2 |     |          |         |     |
|       25 |       1 | 1.1  |     |       51 |       3 | 3.3 |     |          |         |     |
## stats 6/55 -30d
|   result |   count |    % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        1 |       3 | 3.3  |     |       26 |       3 | 3.3 |     | 52       | 1       | 1.1 |
|        3 |       1 | 1.1  |     |       28 |       1 | 1.1 |     | 53       | 1       | 1.1 |
|        4 |       1 | 1.1  |     |       29 |       2 | 2.2 |     | 54       | 3       | 3.3 |
|        6 |       1 | 1.1  |     |       31 |       2 | 2.2 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1  |     |       32 |       1 | 1.1 |     |          |         |     |
|        8 |       1 | 1.1  |     |       33 |       2 | 2.2 |     |          |         |     |
|        9 |       3 | 3.3  |     |       34 |       1 | 1.1 |     |          |         |     |
|       10 |       3 | 3.3  |     |       36 |       2 | 2.2 |     |          |         |     |
|       11 |       3 | 3.3  |     |       37 |       3 | 3.3 |     |          |         |     |
|       12 |       3 | 3.3  |     |       38 |       2 | 2.2 |     |          |         |     |
|       15 |       2 | 2.2  |     |       39 |       3 | 3.3 |     |          |         |     |
|       16 |       6 | 6.59 |     |       40 |       2 | 2.2 |     |          |         |     |
|       17 |       2 | 2.2  |     |       41 |       3 | 3.3 |     |          |         |     |
|       18 |       1 | 1.1  |     |       42 |       2 | 2.2 |     |          |         |     |
|       19 |       2 | 2.2  |     |       43 |       1 | 1.1 |     |          |         |     |
|       20 |       2 | 2.2  |     |       44 |       1 | 1.1 |     |          |         |     |
|       21 |       2 | 2.2  |     |       45 |       2 | 2.2 |     |          |         |     |
|       22 |       3 | 3.3  |     |       47 |       2 | 2.2 |     |          |         |     |
|       24 |       4 | 4.4  |     |       48 |       2 | 2.2 |     |          |         |     |
|       25 |       1 | 1.1  |     |       51 |       3 | 3.3 |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.2  |     |       22 |       4 | 2.2  |     | 42       | 3       | 1.65 |
|        2 |       1 | 0.55 |     |       23 |       1 | 0.55 |     | 43       | 4       | 2.2  |
|        3 |       2 | 1.1  |     |       24 |       5 | 2.75 |     | 44       | 1       | 0.55 |
|        4 |       1 | 0.55 |     |       25 |       3 | 1.65 |     | 45       | 3       | 1.65 |
|        5 |       3 | 1.65 |     |       26 |       7 | 3.85 |     | 46       | 2       | 1.1  |
|        6 |       2 | 1.1  |     |       27 |       1 | 0.55 |     | 47       | 4       | 2.2  |
|        7 |       2 | 1.1  |     |       28 |       2 | 1.1  |     | 48       | 2       | 1.1  |
|        8 |       1 | 0.55 |     |       29 |       5 | 2.75 |     | 49       | 2       | 1.1  |
|        9 |       7 | 3.85 |     |       30 |       1 | 0.55 |     | 50       | 1       | 0.55 |
|       10 |       3 | 1.65 |     |       31 |       8 | 4.4  |     | 51       | 7       | 3.85 |
|       11 |       5 | 2.75 |     |       32 |       1 | 0.55 |     | 52       | 2       | 1.1  |
|       12 |       4 | 2.2  |     |       33 |       3 | 1.65 |     | 53       | 2       | 1.1  |
|       14 |       3 | 1.65 |     |       34 |       3 | 1.65 |     | 54       | 5       | 2.75 |
|       15 |       4 | 2.2  |     |       35 |       2 | 1.1  |     | 55       | 2       | 1.1  |
|       16 |       7 | 3.85 |     |       36 |       3 | 1.65 |     |          |         |      |
|       17 |       4 | 2.2  |     |       37 |       4 | 2.2  |     |          |         |      |
|       18 |       1 | 0.55 |     |       38 |       3 | 1.65 |     |          |         |      |
|       19 |       6 | 3.3  |     |       39 |       7 | 3.85 |     |          |         |      |
|       20 |       5 | 2.75 |     |       40 |       5 | 2.75 |     |          |         |      |
|       21 |       4 | 2.2  |     |       41 |       5 | 2.75 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       5 | 1.83 |     |       21 |       5 | 1.83 |     | 41       | 10      | 3.66 |
|        2 |       3 | 1.1  |     |       22 |       7 | 2.56 |     | 42       | 5       | 1.83 |
|        3 |       6 | 2.2  |     |       23 |       1 | 0.37 |     | 43       | 6       | 2.2  |
|        4 |       4 | 1.47 |     |       24 |       7 | 2.56 |     | 44       | 3       | 1.1  |
|        5 |       4 | 1.47 |     |       25 |       5 | 1.83 |     | 45       | 4       | 1.47 |
|        6 |       4 | 1.47 |     |       26 |       8 | 2.93 |     | 46       | 4       | 1.47 |
|        7 |       3 | 1.1  |     |       27 |       2 | 0.73 |     | 47       | 5       | 1.83 |
|        8 |       2 | 0.73 |     |       28 |       2 | 0.73 |     | 48       | 6       | 2.2  |
|        9 |       9 | 3.3  |     |       29 |       8 | 2.93 |     | 49       | 3       | 1.1  |
|       10 |       4 | 1.47 |     |       30 |       1 | 0.37 |     | 50       | 4       | 1.47 |
|       11 |       8 | 2.93 |     |       31 |       9 | 3.3  |     | 51       | 8       | 2.93 |
|       12 |       5 | 1.83 |     |       32 |       4 | 1.47 |     | 52       | 4       | 1.47 |
|       13 |       1 | 0.37 |     |       33 |       4 | 1.47 |     | 53       | 4       | 1.47 |
|       14 |       5 | 1.83 |     |       34 |       6 | 2.2  |     | 54       | 7       | 2.56 |
|       15 |       5 | 1.83 |     |       35 |       3 | 1.1  |     | 55       | 3       | 1.1  |
|       16 |       7 | 2.56 |     |       36 |       3 | 1.1  |     |          |         |      |
|       17 |       7 | 2.56 |     |       37 |       5 | 1.83 |     |          |         |      |
|       18 |       5 | 1.83 |     |       38 |       4 | 1.47 |     |          |         |      |
|       19 |       6 | 2.2  |     |       39 |       8 | 2.93 |     |          |         |      |
|       20 |       5 | 1.83 |     |       40 |       7 | 2.56 |     |          |         |      |

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

