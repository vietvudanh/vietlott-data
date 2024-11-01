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
| 2024-10-31 | 01107 | [5, 16, 20, 29, 30, 31, 39]  |      0 | 2024-10-31 14:08:16.746749 |
| 2024-10-29 | 01106 | [14, 17, 19, 28, 47, 51, 55] |      0 | 2024-10-29 14:08:48.629579 |
| 2024-10-26 | 01105 | [5, 19, 27, 29, 42, 47, 40]  |      0 | 2024-10-26 14:06:46.276827 |
| 2024-10-24 | 01104 | [5, 17, 31, 39, 46, 53, 3]   |      0 | 2024-10-24 14:08:28.302617 |
| 2024-10-22 | 01103 | [15, 21, 23, 26, 31, 43, 35] |      0 | 2024-10-22 14:08:22.006721 |
| 2024-10-19 | 01102 | [9, 22, 31, 39, 43, 51, 19]  |      0 | 2024-10-19 14:07:01.732285 |
| 2024-10-17 | 01101 | [11, 14, 15, 26, 38, 41, 25] |      0 | 2024-10-17 14:08:38.965236 |
| 2024-10-15 | 01100 | [4, 25, 41, 42, 46, 52, 33]  |      0 | 2024-10-15 14:08:16.788716 |
| 2024-10-12 | 01099 | [29, 34, 35, 38, 50, 51, 37] |      0 | 2024-10-12 14:06:38.873281 |
| 2024-10-10 | 01098 | [4, 5, 6, 29, 32, 44, 53]    |      0 | 2024-10-10 14:08:31.717284 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     152 | 1.96 |     |       21 |     135 | 1.74 |     | 41       | 160     | 2.07 |
|        2 |     131 | 1.69 |     |       22 |     160 | 2.07 |     | 42       | 139     | 1.79 |
|        3 |     154 | 1.99 |     |       23 |     157 | 2.03 |     | 43       | 156     | 2.01 |
|        4 |     124 | 1.6  |     |       24 |     138 | 1.78 |     | 44       | 148     | 1.91 |
|        5 |     144 | 1.86 |     |       25 |     132 | 1.7  |     | 45       | 136     | 1.76 |
|        6 |     122 | 1.57 |     |       26 |     128 | 1.65 |     | 46       | 152     | 1.96 |
|        7 |     122 | 1.57 |     |       27 |     131 | 1.69 |     | 47       | 141     | 1.82 |
|        8 |     150 | 1.94 |     |       28 |     126 | 1.63 |     | 48       | 148     | 1.91 |
|        9 |     153 | 1.97 |     |       29 |     145 | 1.87 |     | 49       | 147     | 1.9  |
|       10 |     132 | 1.7  |     |       30 |     121 | 1.56 |     | 50       | 141     | 1.82 |
|       11 |     144 | 1.86 |     |       31 |     145 | 1.87 |     | 51       | 156     | 2.01 |
|       12 |     152 | 1.96 |     |       32 |     150 | 1.94 |     | 52       | 147     | 1.9  |
|       13 |     135 | 1.74 |     |       33 |     143 | 1.85 |     | 53       | 149     | 1.92 |
|       14 |     137 | 1.77 |     |       34 |     155 | 2    |     | 54       | 134     | 1.73 |
|       15 |     131 | 1.69 |     |       35 |     147 | 1.9  |     | 55       | 142     | 1.83 |
|       16 |     124 | 1.6  |     |       36 |     132 | 1.7  |     |          |         |      |
|       17 |     129 | 1.66 |     |       37 |     123 | 1.59 |     |          |         |      |
|       18 |     144 | 1.86 |     |       38 |     134 | 1.73 |     |          |         |      |
|       19 |     138 | 1.78 |     |       39 |     129 | 1.66 |     |          |         |      |
|       20 |     152 | 1.96 |     |       40 |     151 | 1.95 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.1 |     |       26 |       2 | 2.2 |     | 48       | 1       | 1.1 |
|        3 |       2 | 2.2 |     |       27 |       2 | 2.2 |     | 50       | 3       | 3.3 |
|        4 |       2 | 2.2 |     |       28 |       1 | 1.1 |     | 51       | 3       | 3.3 |
|        5 |       4 | 4.4 |     |       29 |       4 | 4.4 |     | 52       | 2       | 2.2 |
|        6 |       1 | 1.1 |     |       30 |       1 | 1.1 |     | 53       | 3       | 3.3 |
|        7 |       1 | 1.1 |     |       31 |       4 | 4.4 |     | 55       | 1       | 1.1 |
|        9 |       1 | 1.1 |     |       32 |       1 | 1.1 |     |          |         |     |
|       10 |       1 | 1.1 |     |       33 |       1 | 1.1 |     |          |         |     |
|       11 |       1 | 1.1 |     |       34 |       2 | 2.2 |     |          |         |     |
|       14 |       3 | 3.3 |     |       35 |       2 | 2.2 |     |          |         |     |
|       15 |       2 | 2.2 |     |       37 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1 |     |       38 |       2 | 2.2 |     |          |         |     |
|       17 |       4 | 4.4 |     |       39 |       3 | 3.3 |     |          |         |     |
|       18 |       2 | 2.2 |     |       40 |       3 | 3.3 |     |          |         |     |
|       19 |       3 | 3.3 |     |       41 |       2 | 2.2 |     |          |         |     |
|       20 |       1 | 1.1 |     |       42 |       3 | 3.3 |     |          |         |     |
|       21 |       2 | 2.2 |     |       43 |       2 | 2.2 |     |          |         |     |
|       22 |       1 | 1.1 |     |       44 |       1 | 1.1 |     |          |         |     |
|       23 |       1 | 1.1 |     |       46 |       2 | 2.2 |     |          |         |     |
|       25 |       3 | 3.3 |     |       47 |       2 | 2.2 |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |   % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|----:|:----|:---------|:--------|:----|
|        2 |       1 | 1.1 |     |       26 |       2 | 2.2 |     | 48       | 1       | 1.1 |
|        3 |       2 | 2.2 |     |       27 |       2 | 2.2 |     | 50       | 3       | 3.3 |
|        4 |       2 | 2.2 |     |       28 |       1 | 1.1 |     | 51       | 3       | 3.3 |
|        5 |       4 | 4.4 |     |       29 |       4 | 4.4 |     | 52       | 2       | 2.2 |
|        6 |       1 | 1.1 |     |       30 |       1 | 1.1 |     | 53       | 3       | 3.3 |
|        7 |       1 | 1.1 |     |       31 |       4 | 4.4 |     | 55       | 1       | 1.1 |
|        9 |       1 | 1.1 |     |       32 |       1 | 1.1 |     |          |         |     |
|       10 |       1 | 1.1 |     |       33 |       1 | 1.1 |     |          |         |     |
|       11 |       1 | 1.1 |     |       34 |       2 | 2.2 |     |          |         |     |
|       14 |       3 | 3.3 |     |       35 |       2 | 2.2 |     |          |         |     |
|       15 |       2 | 2.2 |     |       37 |       1 | 1.1 |     |          |         |     |
|       16 |       1 | 1.1 |     |       38 |       2 | 2.2 |     |          |         |     |
|       17 |       4 | 4.4 |     |       39 |       3 | 3.3 |     |          |         |     |
|       18 |       2 | 2.2 |     |       40 |       3 | 3.3 |     |          |         |     |
|       19 |       3 | 3.3 |     |       41 |       2 | 2.2 |     |          |         |     |
|       20 |       1 | 1.1 |     |       42 |       3 | 3.3 |     |          |         |     |
|       21 |       2 | 2.2 |     |       43 |       2 | 2.2 |     |          |         |     |
|       22 |       1 | 1.1 |     |       44 |       1 | 1.1 |     |          |         |     |
|       23 |       1 | 1.1 |     |       46 |       2 | 2.2 |     |          |         |     |
|       25 |       3 | 3.3 |     |       47 |       2 | 2.2 |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.1  |     |       21 |       2 | 1.1  |     | 41       | 7       | 3.85 |
|        2 |       3 | 1.65 |     |       22 |       4 | 2.2  |     | 42       | 3       | 1.65 |
|        3 |       6 | 3.3  |     |       23 |       3 | 1.65 |     | 43       | 4       | 2.2  |
|        4 |       3 | 1.65 |     |       24 |       2 | 1.1  |     | 44       | 2       | 1.1  |
|        5 |       5 | 2.75 |     |       25 |       4 | 2.2  |     | 45       | 2       | 1.1  |
|        6 |       2 | 1.1  |     |       26 |       3 | 1.65 |     | 46       | 5       | 2.75 |
|        7 |       1 | 0.55 |     |       27 |       2 | 1.1  |     | 47       | 4       | 2.2  |
|        8 |       3 | 1.65 |     |       28 |       1 | 0.55 |     | 48       | 5       | 2.75 |
|        9 |       3 | 1.65 |     |       29 |       6 | 3.3  |     | 49       | 2       | 1.1  |
|       10 |       2 | 1.1  |     |       30 |       2 | 1.1  |     | 50       | 3       | 1.65 |
|       11 |       6 | 3.3  |     |       31 |       6 | 3.3  |     | 51       | 4       | 2.2  |
|       12 |       2 | 1.1  |     |       32 |       4 | 2.2  |     | 52       | 2       | 1.1  |
|       13 |       1 | 0.55 |     |       33 |       1 | 0.55 |     | 53       | 4       | 2.2  |
|       14 |       5 | 2.75 |     |       34 |       5 | 2.75 |     | 54       | 3       | 1.65 |
|       15 |       5 | 2.75 |     |       35 |       2 | 1.1  |     | 55       | 2       | 1.1  |
|       16 |       1 | 0.55 |     |       36 |       1 | 0.55 |     |          |         |      |
|       17 |       5 | 2.75 |     |       37 |       3 | 1.65 |     |          |         |      |
|       18 |       4 | 2.2  |     |       38 |       5 | 2.75 |     |          |         |      |
|       19 |       3 | 1.65 |     |       39 |       6 | 3.3  |     |          |         |      |
|       20 |       3 | 1.65 |     |       40 |       3 | 1.65 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       4 | 1.47 |     | 41       | 9       | 3.3  |
|        2 |       5 | 1.83 |     |       22 |       6 | 2.2  |     | 42       | 5       | 1.83 |
|        3 |       6 | 2.2  |     |       23 |       5 | 1.83 |     | 43       | 6       | 2.2  |
|        4 |       4 | 1.47 |     |       24 |       4 | 1.47 |     | 44       | 4       | 1.47 |
|        5 |       8 | 2.93 |     |       25 |       4 | 1.47 |     | 45       | 4       | 1.47 |
|        6 |       4 | 1.47 |     |       26 |       5 | 1.83 |     | 46       | 9       | 3.3  |
|        7 |       3 | 1.1  |     |       27 |       4 | 1.47 |     | 47       | 4       | 1.47 |
|        8 |       5 | 1.83 |     |       28 |       3 | 1.1  |     | 48       | 8       | 2.93 |
|        9 |       4 | 1.47 |     |       29 |      10 | 3.66 |     | 49       | 2       | 0.73 |
|       10 |       3 | 1.1  |     |       30 |       3 | 1.1  |     | 50       | 4       | 1.47 |
|       11 |       8 | 2.93 |     |       31 |       7 | 2.56 |     | 51       | 6       | 2.2  |
|       12 |       3 | 1.1  |     |       32 |       6 | 2.2  |     | 52       | 2       | 0.73 |
|       13 |       1 | 0.37 |     |       33 |       3 | 1.1  |     | 53       | 4       | 1.47 |
|       14 |       7 | 2.56 |     |       34 |       8 | 2.93 |     | 54       | 5       | 1.83 |
|       15 |       5 | 1.83 |     |       35 |       3 | 1.1  |     | 55       | 5       | 1.83 |
|       16 |       3 | 1.1  |     |       36 |       2 | 0.73 |     |          |         |      |
|       17 |       6 | 2.2  |     |       37 |       5 | 1.83 |     |          |         |      |
|       18 |       5 | 1.83 |     |       38 |       9 | 3.3  |     |          |         |      |
|       19 |       3 | 1.1  |     |       39 |       7 | 2.56 |     |          |         |      |
|       20 |       7 | 2.56 |     |       40 |       5 | 1.83 |     |          |         |      |

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

