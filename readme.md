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
|      | date       | result                    | predicted              |
|-----:|:-----------|:--------------------------|:-----------------------|
| 5957 | 2022-12-17 | [1, 2, 29, 34, 41, 42, 9] | [34, 29, 9, 2, 42, 12] | 

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
|   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       1 | 4.76 |     |          |         |     |
|       12 |       1 | 4.76 |     |          |         |     |
|       16 |       1 | 4.76 |     |          |         |     |
|       20 |       1 | 4.76 |     |          |         |     |
|       21 |       1 | 4.76 |     |          |         |     |
|       22 |       1 | 4.76 |     |          |         |     |
|       25 |       1 | 4.76 |     |          |         |     |
|       29 |       1 | 4.76 |     |          |         |     |
|       31 |       1 | 4.76 |     |          |         |     |
|       33 |       1 | 4.76 |     |          |         |     |
|       35 |       1 | 4.76 |     |          |         |     |
|       37 |       2 | 9.52 |     |          |         |     |
|       39 |       1 | 4.76 |     |          |         |     |
|       40 |       1 | 4.76 |     |          |         |     |
|       41 |       1 | 4.76 |     |          |         |     |
|       45 |       1 | 4.76 |     |          |         |     |
|       49 |       1 | 4.76 |     |          |         |     |
|       51 |       1 | 4.76 |     |          |         |     |
|       52 |       1 | 4.76 |     |          |         |     |
|       54 |       1 | 4.76 |     |          |         |     |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       1 | 4.76 |     |          |         |     |
|       12 |       1 | 4.76 |     |          |         |     |
|       16 |       1 | 4.76 |     |          |         |     |
|       20 |       1 | 4.76 |     |          |         |     |
|       21 |       1 | 4.76 |     |          |         |     |
|       22 |       1 | 4.76 |     |          |         |     |
|       25 |       1 | 4.76 |     |          |         |     |
|       29 |       1 | 4.76 |     |          |         |     |
|       31 |       1 | 4.76 |     |          |         |     |
|       33 |       1 | 4.76 |     |          |         |     |
|       35 |       1 | 4.76 |     |          |         |     |
|       37 |       2 | 9.52 |     |          |         |     |
|       39 |       1 | 4.76 |     |          |         |     |
|       40 |       1 | 4.76 |     |          |         |     |
|       41 |       1 | 4.76 |     |          |         |     |
|       45 |       1 | 4.76 |     |          |         |     |
|       49 |       1 | 4.76 |     |          |         |     |
|       51 |       1 | 4.76 |     |          |         |     |
|       52 |       1 | 4.76 |     |          |         |     |
|       54 |       1 | 4.76 |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.89 |     |       25 |       3 | 2.68 |     | 47       | 2       | 1.79 |
|        2 |       1 | 0.89 |     |       26 |       4 | 3.57 |     | 49       | 2       | 1.79 |
|        3 |       1 | 0.89 |     |       27 |       1 | 0.89 |     | 50       | 2       | 1.79 |
|        4 |       1 | 0.89 |     |       28 |       1 | 0.89 |     | 51       | 6       | 5.36 |
|        5 |       3 | 2.68 |     |       29 |       4 | 3.57 |     | 52       | 2       | 1.79 |
|        6 |       1 | 0.89 |     |       30 |       1 | 0.89 |     | 53       | 1       | 0.89 |
|        7 |       1 | 0.89 |     |       31 |       6 | 5.36 |     | 54       | 3       | 2.68 |
|        9 |       4 | 3.57 |     |       33 |       3 | 2.68 |     | 55       | 1       | 0.89 |
|       11 |       2 | 1.79 |     |       34 |       3 | 2.68 |     |          |         |      |
|       12 |       1 | 0.89 |     |       35 |       3 | 2.68 |     |          |         |      |
|       14 |       3 | 2.68 |     |       36 |       1 | 0.89 |     |          |         |      |
|       15 |       2 | 1.79 |     |       37 |       3 | 2.68 |     |          |         |      |
|       16 |       2 | 1.79 |     |       38 |       2 | 1.79 |     |          |         |      |
|       17 |       2 | 1.79 |     |       39 |       5 | 4.46 |     |          |         |      |
|       19 |       4 | 3.57 |     |       40 |       3 | 2.68 |     |          |         |      |
|       20 |       3 | 2.68 |     |       41 |       3 | 2.68 |     |          |         |      |
|       21 |       2 | 1.79 |     |       42 |       2 | 1.79 |     |          |         |      |
|       22 |       2 | 1.79 |     |       43 |       3 | 2.68 |     |          |         |      |
|       23 |       1 | 0.89 |     |       45 |       1 | 0.89 |     |          |         |      |
|       24 |       1 | 0.89 |     |       46 |       3 | 2.68 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 0.99 |     |       21 |       3 | 1.48 |     | 41       | 7       | 3.45 |
|        2 |       4 | 1.97 |     |       22 |       5 | 2.46 |     | 42       | 3       | 1.48 |
|        3 |       6 | 2.96 |     |       23 |       1 | 0.49 |     | 43       | 5       | 2.46 |
|        4 |       3 | 1.48 |     |       24 |       3 | 1.48 |     | 44       | 2       | 0.99 |
|        5 |       4 | 1.97 |     |       25 |       5 | 2.46 |     | 45       | 2       | 0.99 |
|        6 |       3 | 1.48 |     |       26 |       5 | 2.46 |     | 46       | 4       | 1.97 |
|        7 |       2 | 0.99 |     |       27 |       2 | 0.99 |     | 47       | 4       | 1.97 |
|        8 |       2 | 0.99 |     |       28 |       1 | 0.49 |     | 48       | 4       | 1.97 |
|        9 |       6 | 2.96 |     |       29 |       6 | 2.96 |     | 49       | 3       | 1.48 |
|       10 |       1 | 0.49 |     |       30 |       1 | 0.49 |     | 50       | 4       | 1.97 |
|       11 |       5 | 2.46 |     |       31 |       8 | 3.94 |     | 51       | 7       | 3.45 |
|       12 |       3 | 1.48 |     |       32 |       4 | 1.97 |     | 52       | 3       | 1.48 |
|       13 |       1 | 0.49 |     |       33 |       3 | 1.48 |     | 53       | 3       | 1.48 |
|       14 |       5 | 2.46 |     |       34 |       6 | 2.96 |     | 54       | 6       | 2.96 |
|       15 |       3 | 1.48 |     |       35 |       3 | 1.48 |     | 55       | 2       | 0.99 |
|       16 |       2 | 0.99 |     |       36 |       2 | 0.99 |     |          |         |      |
|       17 |       5 | 2.46 |     |       37 |       3 | 1.48 |     |          |         |      |
|       18 |       4 | 1.97 |     |       38 |       3 | 1.48 |     |          |         |      |
|       19 |       4 | 1.97 |     |       39 |       7 | 3.45 |     |          |         |      |
|       20 |       3 | 1.48 |     |       40 |       5 | 2.46 |     |          |         |      |

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

