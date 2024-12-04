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
|       | date       | result                       | predicted                |
|------:|:-----------|:-----------------------------|:-------------------------|
| 10728 | 2021-05-13 | [13, 24, 25, 35, 39, 41, 29] | [41, 13, 35, 11, 24, 29] |
| 13475 | 2020-06-23 | [2, 18, 28, 46, 52, 54, 19]  | [54, 19, 18, 14, 52, 28] |
| 16879 | 2019-04-27 | [1, 11, 22, 26, 33, 51, 4]   | [22, 33, 51, 4, 29, 1]   | 

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
|        1 |       1 | 2.38 |     | 37       | 2       | 4.76 |
|        6 |       1 | 2.38 |     | 39       | 2       | 4.76 |
|        7 |       1 | 2.38 |     | 40       | 2       | 4.76 |
|        9 |       2 | 4.76 |     | 41       | 1       | 2.38 |
|       11 |       1 | 2.38 |     | 43       | 1       | 2.38 |
|       12 |       1 | 2.38 |     | 45       | 1       | 2.38 |
|       14 |       1 | 2.38 |     | 46       | 1       | 2.38 |
|       16 |       1 | 2.38 |     | 49       | 2       | 4.76 |
|       20 |       1 | 2.38 |     | 50       | 1       | 2.38 |
|       21 |       1 | 2.38 |     | 51       | 3       | 7.14 |
|       22 |       1 | 2.38 |     | 52       | 1       | 2.38 |
|       24 |       1 | 2.38 |     | 54       | 2       | 4.76 |
|       25 |       1 | 2.38 |     |          |         |      |
|       26 |       1 | 2.38 |     |          |         |      |
|       29 |       1 | 2.38 |     |          |         |      |
|       31 |       2 | 4.76 |     |          |         |      |
|       33 |       2 | 4.76 |     |          |         |      |
|       34 |       1 | 2.38 |     |          |         |      |
|       35 |       1 | 2.38 |     |          |         |      |
|       36 |       1 | 2.38 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 2.38 |     | 37       | 2       | 4.76 |
|        6 |       1 | 2.38 |     | 39       | 2       | 4.76 |
|        7 |       1 | 2.38 |     | 40       | 2       | 4.76 |
|        9 |       2 | 4.76 |     | 41       | 1       | 2.38 |
|       11 |       1 | 2.38 |     | 43       | 1       | 2.38 |
|       12 |       1 | 2.38 |     | 45       | 1       | 2.38 |
|       14 |       1 | 2.38 |     | 46       | 1       | 2.38 |
|       16 |       1 | 2.38 |     | 49       | 2       | 4.76 |
|       20 |       1 | 2.38 |     | 50       | 1       | 2.38 |
|       21 |       1 | 2.38 |     | 51       | 3       | 7.14 |
|       22 |       1 | 2.38 |     | 52       | 1       | 2.38 |
|       24 |       1 | 2.38 |     | 54       | 2       | 4.76 |
|       25 |       1 | 2.38 |     |          |         |      |
|       26 |       1 | 2.38 |     |          |         |      |
|       29 |       1 | 2.38 |     |          |         |      |
|       31 |       2 | 4.76 |     |          |         |      |
|       33 |       2 | 4.76 |     |          |         |      |
|       34 |       1 | 2.38 |     |          |         |      |
|       35 |       1 | 2.38 |     |          |         |      |
|       36 |       1 | 2.38 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.75 |     |       23 |       1 | 0.75 |     | 43       | 3       | 2.26 |
|        2 |       2 | 1.5  |     |       24 |       1 | 0.75 |     | 44       | 1       | 0.75 |
|        3 |       2 | 1.5  |     |       25 |       3 | 2.26 |     | 45       | 1       | 0.75 |
|        4 |       2 | 1.5  |     |       26 |       4 | 3.01 |     | 46       | 3       | 2.26 |
|        5 |       4 | 3.01 |     |       27 |       2 | 1.5  |     | 47       | 2       | 1.5  |
|        6 |       2 | 1.5  |     |       28 |       1 | 0.75 |     | 48       | 1       | 0.75 |
|        7 |       2 | 1.5  |     |       29 |       5 | 3.76 |     | 49       | 2       | 1.5  |
|        9 |       4 | 3.01 |     |       30 |       1 | 0.75 |     | 50       | 4       | 3.01 |
|       10 |       1 | 0.75 |     |       31 |       6 | 4.51 |     | 51       | 6       | 4.51 |
|       11 |       2 | 1.5  |     |       32 |       1 | 0.75 |     | 52       | 3       | 2.26 |
|       12 |       1 | 0.75 |     |       33 |       3 | 2.26 |     | 53       | 2       | 1.5  |
|       14 |       4 | 3.01 |     |       34 |       3 | 2.26 |     | 54       | 3       | 2.26 |
|       15 |       2 | 1.5  |     |       35 |       3 | 2.26 |     | 55       | 1       | 0.75 |
|       16 |       2 | 1.5  |     |       36 |       1 | 0.75 |     |          |         |      |
|       17 |       4 | 3.01 |     |       37 |       3 | 2.26 |     |          |         |      |
|       18 |       1 | 0.75 |     |       38 |       2 | 1.5  |     |          |         |      |
|       19 |       4 | 3.01 |     |       39 |       5 | 3.76 |     |          |         |      |
|       20 |       3 | 2.26 |     |       40 |       4 | 3.01 |     |          |         |      |
|       21 |       2 | 1.5  |     |       41 |       3 | 2.26 |     |          |         |      |
|       22 |       2 | 1.5  |     |       42 |       2 | 1.5  |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.34 |     |       21 |       3 | 1.34 |     | 41       | 7       | 3.12 |
|        2 |       4 | 1.79 |     |       22 |       5 | 2.23 |     | 42       | 3       | 1.34 |
|        3 |       6 | 2.68 |     |       23 |       3 | 1.34 |     | 43       | 5       | 2.23 |
|        4 |       3 | 1.34 |     |       24 |       3 | 1.34 |     | 44       | 2       | 0.89 |
|        5 |       5 | 2.23 |     |       25 |       5 | 2.23 |     | 45       | 3       | 1.34 |
|        6 |       3 | 1.34 |     |       26 |       5 | 2.23 |     | 46       | 6       | 2.68 |
|        7 |       2 | 0.89 |     |       27 |       2 | 0.89 |     | 47       | 4       | 1.79 |
|        8 |       2 | 0.89 |     |       28 |       1 | 0.45 |     | 48       | 4       | 1.79 |
|        9 |       6 | 2.68 |     |       29 |       7 | 3.12 |     | 49       | 4       | 1.79 |
|       10 |       1 | 0.45 |     |       30 |       2 | 0.89 |     | 50       | 4       | 1.79 |
|       11 |       6 | 2.68 |     |       31 |       8 | 3.57 |     | 51       | 7       | 3.12 |
|       12 |       3 | 1.34 |     |       32 |       4 | 1.79 |     | 52       | 3       | 1.34 |
|       13 |       1 | 0.45 |     |       33 |       3 | 1.34 |     | 53       | 4       | 1.79 |
|       14 |       5 | 2.23 |     |       34 |       7 | 3.12 |     | 54       | 6       | 2.68 |
|       15 |       5 | 2.23 |     |       35 |       3 | 1.34 |     | 55       | 2       | 0.89 |
|       16 |       2 | 0.89 |     |       36 |       2 | 0.89 |     |          |         |      |
|       17 |       5 | 2.23 |     |       37 |       5 | 2.23 |     |          |         |      |
|       18 |       4 | 1.79 |     |       38 |       4 | 1.79 |     |          |         |      |
|       19 |       4 | 1.79 |     |       39 |       8 | 3.57 |     |          |         |      |
|       20 |       5 | 2.23 |     |       40 |       5 | 2.23 |     |          |         |      |

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

