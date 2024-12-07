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
|      | date       | result                      | predicted                |
|-----:|:-----------|:----------------------------|:-------------------------|
| 9389 | 2021-11-11 | [3, 35, 37, 41, 45, 49, 31] | [41, 31, 45, 39, 35, 37] | 

## raw details 6/55 last 10 days
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2024-11-16 | 01114 | [16, 22, 33, 37, 39, 51, 54] |      0 | 2024-11-16 14:07:21.034678 |
| 2024-11-14 | 01113 | [12, 25, 37, 40, 49, 52, 31] |      0 | 2024-11-14 14:09:18.242315 |
| 2024-11-12 | 01112 | [1, 21, 29, 35, 41, 45, 20]  |      0 | 2024-11-12 14:08:35.280505 |
| 2024-11-09 | 01111 | [11, 14, 24, 26, 34, 51, 40] |      0 | 2024-11-10 02:14:10.380124 |
| 2024-11-07 | 01110 | [6, 9, 33, 39, 50, 51, 43]   |      0 | 2024-11-07 14:08:25.399717 |
| 2024-11-05 | 01109 | [9, 31, 36, 46, 49, 54, 7]   |      0 | 2024-11-05 14:08:24.678745 |
| 2024-11-02 | 01108 | [2, 9, 19, 20, 34, 54, 26]   |      0 | 2024-11-02 14:07:17.372355 |
| 2024-10-31 | 01107 | [5, 16, 20, 29, 30, 31, 39]  |      0 | 2024-10-31 14:08:16.746749 |
| 2024-10-29 | 01106 | [14, 17, 19, 28, 47, 51, 55] |      0 | 2024-10-29 14:08:48.629579 |
| 2024-10-26 | 01105 | [5, 19, 27, 29, 42, 47, 40]  |      0 | 2024-10-26 14:06:46.276827 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     153 | 1.96 |     |       21 |     136 | 1.74 |     | 41       | 161     | 2.06 |
|        2 |     132 | 1.69 |     |       22 |     161 | 2.06 |     | 42       | 139     | 1.78 |
|        3 |     154 | 1.98 |     |       23 |     157 | 2.01 |     | 43       | 157     | 2.01 |
|        4 |     124 | 1.59 |     |       24 |     139 | 1.78 |     | 44       | 148     | 1.9  |
|        5 |     144 | 1.85 |     |       25 |     133 | 1.71 |     | 45       | 137     | 1.76 |
|        6 |     123 | 1.58 |     |       26 |     130 | 1.67 |     | 46       | 153     | 1.96 |
|        7 |     123 | 1.58 |     |       27 |     131 | 1.68 |     | 47       | 141     | 1.81 |
|        8 |     150 | 1.92 |     |       28 |     126 | 1.62 |     | 48       | 148     | 1.9  |
|        9 |     156 | 2    |     |       29 |     146 | 1.87 |     | 49       | 149     | 1.91 |
|       10 |     132 | 1.69 |     |       30 |     121 | 1.55 |     | 50       | 142     | 1.82 |
|       11 |     145 | 1.86 |     |       31 |     147 | 1.89 |     | 51       | 159     | 2.04 |
|       12 |     153 | 1.96 |     |       32 |     150 | 1.92 |     | 52       | 148     | 1.9  |
|       13 |     135 | 1.73 |     |       33 |     145 | 1.86 |     | 53       | 149     | 1.91 |
|       14 |     138 | 1.77 |     |       34 |     157 | 2.01 |     | 54       | 137     | 1.76 |
|       15 |     131 | 1.68 |     |       35 |     148 | 1.9  |     | 55       | 142     | 1.82 |
|       16 |     125 | 1.6  |     |       36 |     133 | 1.71 |     |          |         |      |
|       17 |     129 | 1.65 |     |       37 |     125 | 1.6  |     |          |         |      |
|       18 |     144 | 1.85 |     |       38 |     134 | 1.72 |     |          |         |      |
|       19 |     139 | 1.78 |     |       39 |     131 | 1.68 |     |          |         |      |
|       20 |     154 | 1.98 |     |       40 |     153 | 1.96 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.86 |     | 40       | 2       | 5.71 |
|        6 |       1 | 2.86 |     | 41       | 1       | 2.86 |
|        9 |       1 | 2.86 |     | 43       | 1       | 2.86 |
|       11 |       1 | 2.86 |     | 45       | 1       | 2.86 |
|       12 |       1 | 2.86 |     | 49       | 1       | 2.86 |
|       14 |       1 | 2.86 |     | 50       | 1       | 2.86 |
|       16 |       1 | 2.86 |     | 51       | 3       | 8.57 |
|       20 |       1 | 2.86 |     | 52       | 1       | 2.86 |
|       21 |       1 | 2.86 |     | 54       | 1       | 2.86 |
|       22 |       1 | 2.86 |     |          |         |      |
|       24 |       1 | 2.86 |     |          |         |      |
|       25 |       1 | 2.86 |     |          |         |      |
|       26 |       1 | 2.86 |     |          |         |      |
|       29 |       1 | 2.86 |     |          |         |      |
|       31 |       1 | 2.86 |     |          |         |      |
|       33 |       2 | 5.71 |     |          |         |      |
|       34 |       1 | 2.86 |     |          |         |      |
|       35 |       1 | 2.86 |     |          |         |      |
|       37 |       2 | 5.71 |     |          |         |      |
|       39 |       2 | 5.71 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.86 |     | 40       | 2       | 5.71 |
|        6 |       1 | 2.86 |     | 41       | 1       | 2.86 |
|        9 |       1 | 2.86 |     | 43       | 1       | 2.86 |
|       11 |       1 | 2.86 |     | 45       | 1       | 2.86 |
|       12 |       1 | 2.86 |     | 49       | 1       | 2.86 |
|       14 |       1 | 2.86 |     | 50       | 1       | 2.86 |
|       16 |       1 | 2.86 |     | 51       | 3       | 8.57 |
|       20 |       1 | 2.86 |     | 52       | 1       | 2.86 |
|       21 |       1 | 2.86 |     | 54       | 1       | 2.86 |
|       22 |       1 | 2.86 |     |          |         |      |
|       24 |       1 | 2.86 |     |          |         |      |
|       25 |       1 | 2.86 |     |          |         |      |
|       26 |       1 | 2.86 |     |          |         |      |
|       29 |       1 | 2.86 |     |          |         |      |
|       31 |       1 | 2.86 |     |          |         |      |
|       33 |       2 | 5.71 |     |          |         |      |
|       34 |       1 | 2.86 |     |          |         |      |
|       35 |       1 | 2.86 |     |          |         |      |
|       37 |       2 | 5.71 |     |          |         |      |
|       39 |       2 | 5.71 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.79 |     |       25 |       3 | 2.38 |     | 45       | 1       | 0.79 |
|        2 |       1 | 0.79 |     |       26 |       4 | 3.17 |     | 46       | 3       | 2.38 |
|        3 |       2 | 1.59 |     |       27 |       1 | 0.79 |     | 47       | 2       | 1.59 |
|        4 |       2 | 1.59 |     |       28 |       1 | 0.79 |     | 48       | 1       | 0.79 |
|        5 |       4 | 3.17 |     |       29 |       5 | 3.97 |     | 49       | 2       | 1.59 |
|        6 |       2 | 1.59 |     |       30 |       1 | 0.79 |     | 50       | 3       | 2.38 |
|        7 |       2 | 1.59 |     |       31 |       6 | 4.76 |     | 51       | 6       | 4.76 |
|        9 |       4 | 3.17 |     |       32 |       1 | 0.79 |     | 52       | 2       | 1.59 |
|       11 |       2 | 1.59 |     |       33 |       3 | 2.38 |     | 53       | 2       | 1.59 |
|       12 |       1 | 0.79 |     |       34 |       3 | 2.38 |     | 54       | 3       | 2.38 |
|       14 |       4 | 3.17 |     |       35 |       3 | 2.38 |     | 55       | 1       | 0.79 |
|       15 |       2 | 1.59 |     |       36 |       1 | 0.79 |     |          |         |      |
|       16 |       2 | 1.59 |     |       37 |       3 | 2.38 |     |          |         |      |
|       17 |       3 | 2.38 |     |       38 |       2 | 1.59 |     |          |         |      |
|       19 |       4 | 3.17 |     |       39 |       5 | 3.97 |     |          |         |      |
|       20 |       3 | 2.38 |     |       40 |       4 | 3.17 |     |          |         |      |
|       21 |       2 | 1.59 |     |       41 |       3 | 2.38 |     |          |         |      |
|       22 |       2 | 1.59 |     |       42 |       2 | 1.59 |     |          |         |      |
|       23 |       1 | 0.79 |     |       43 |       3 | 2.38 |     |          |         |      |
|       24 |       1 | 0.79 |     |       44 |       1 | 0.79 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 0.95 |     |       21 |       3 | 1.43 |     | 41       | 7       | 3.33 |
|        2 |       4 | 1.9  |     |       22 |       5 | 2.38 |     | 42       | 3       | 1.43 |
|        3 |       6 | 2.86 |     |       23 |       2 | 0.95 |     | 43       | 5       | 2.38 |
|        4 |       3 | 1.43 |     |       24 |       3 | 1.43 |     | 44       | 2       | 0.95 |
|        5 |       4 | 1.9  |     |       25 |       5 | 2.38 |     | 45       | 3       | 1.43 |
|        6 |       3 | 1.43 |     |       26 |       5 | 2.38 |     | 46       | 4       | 1.9  |
|        7 |       2 | 0.95 |     |       27 |       2 | 0.95 |     | 47       | 4       | 1.9  |
|        8 |       2 | 0.95 |     |       28 |       1 | 0.48 |     | 48       | 4       | 1.9  |
|        9 |       6 | 2.86 |     |       29 |       6 | 2.86 |     | 49       | 4       | 1.9  |
|       10 |       1 | 0.48 |     |       30 |       2 | 0.95 |     | 50       | 4       | 1.9  |
|       11 |       5 | 2.38 |     |       31 |       8 | 3.81 |     | 51       | 7       | 3.33 |
|       12 |       3 | 1.43 |     |       32 |       4 | 1.9  |     | 52       | 3       | 1.43 |
|       13 |       1 | 0.48 |     |       33 |       3 | 1.43 |     | 53       | 3       | 1.43 |
|       14 |       5 | 2.38 |     |       34 |       6 | 2.86 |     | 54       | 6       | 2.86 |
|       15 |       4 | 1.9  |     |       35 |       3 | 1.43 |     | 55       | 2       | 0.95 |
|       16 |       2 | 0.95 |     |       36 |       2 | 0.95 |     |          |         |      |
|       17 |       5 | 2.38 |     |       37 |       4 | 1.9  |     |          |         |      |
|       18 |       4 | 1.9  |     |       38 |       4 | 1.9  |     |          |         |      |
|       19 |       4 | 1.9  |     |       39 |       7 | 3.33 |     |          |         |      |
|       20 |       3 | 1.43 |     |       40 |       5 | 2.38 |     |          |         |      |

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

