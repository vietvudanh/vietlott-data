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
|        1 |       1 | 1.79 |     | 33       | 2       | 3.57 |
|        2 |       1 | 1.79 |     | 34       | 2       | 3.57 |
|        5 |       1 | 1.79 |     | 35       | 1       | 1.79 |
|        6 |       1 | 1.79 |     | 36       | 1       | 1.79 |
|        7 |       1 | 1.79 |     | 37       | 2       | 3.57 |
|        9 |       3 | 5.36 |     | 39       | 3       | 5.36 |
|       11 |       1 | 1.79 |     | 40       | 2       | 3.57 |
|       12 |       1 | 1.79 |     | 41       | 1       | 1.79 |
|       14 |       1 | 1.79 |     | 43       | 1       | 1.79 |
|       16 |       2 | 3.57 |     | 45       | 1       | 1.79 |
|       19 |       1 | 1.79 |     | 46       | 1       | 1.79 |
|       20 |       3 | 5.36 |     | 49       | 2       | 3.57 |
|       21 |       1 | 1.79 |     | 50       | 1       | 1.79 |
|       22 |       1 | 1.79 |     | 51       | 3       | 5.36 |
|       24 |       1 | 1.79 |     | 52       | 1       | 1.79 |
|       25 |       1 | 1.79 |     | 54       | 3       | 5.36 |
|       26 |       2 | 3.57 |     |          |         |      |
|       29 |       2 | 3.57 |     |          |         |      |
|       30 |       1 | 1.79 |     |          |         |      |
|       31 |       3 | 5.36 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 1.79 |     | 33       | 2       | 3.57 |
|        2 |       1 | 1.79 |     | 34       | 2       | 3.57 |
|        5 |       1 | 1.79 |     | 35       | 1       | 1.79 |
|        6 |       1 | 1.79 |     | 36       | 1       | 1.79 |
|        7 |       1 | 1.79 |     | 37       | 2       | 3.57 |
|        9 |       3 | 5.36 |     | 39       | 3       | 5.36 |
|       11 |       1 | 1.79 |     | 40       | 2       | 3.57 |
|       12 |       1 | 1.79 |     | 41       | 1       | 1.79 |
|       14 |       1 | 1.79 |     | 43       | 1       | 1.79 |
|       16 |       2 | 3.57 |     | 45       | 1       | 1.79 |
|       19 |       1 | 1.79 |     | 46       | 1       | 1.79 |
|       20 |       3 | 5.36 |     | 49       | 2       | 3.57 |
|       21 |       1 | 1.79 |     | 50       | 1       | 1.79 |
|       22 |       1 | 1.79 |     | 51       | 3       | 5.36 |
|       24 |       1 | 1.79 |     | 52       | 1       | 1.79 |
|       25 |       1 | 1.79 |     | 54       | 3       | 5.36 |
|       26 |       2 | 3.57 |     |          |         |      |
|       29 |       2 | 3.57 |     |          |         |      |
|       30 |       1 | 1.79 |     |          |         |      |
|       31 |       3 | 5.36 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.68 |     |       23 |       1 | 0.68 |     | 43       | 4       | 2.72 |
|        2 |       2 | 1.36 |     |       24 |       1 | 0.68 |     | 44       | 2       | 1.36 |
|        3 |       3 | 2.04 |     |       25 |       4 | 2.72 |     | 45       | 1       | 0.68 |
|        4 |       2 | 1.36 |     |       26 |       4 | 2.72 |     | 46       | 3       | 2.04 |
|        5 |       4 | 2.72 |     |       27 |       2 | 1.36 |     | 47       | 2       | 1.36 |
|        6 |       2 | 1.36 |     |       28 |       1 | 0.68 |     | 48       | 1       | 0.68 |
|        7 |       2 | 1.36 |     |       29 |       5 | 3.4  |     | 49       | 2       | 1.36 |
|        9 |       4 | 2.72 |     |       30 |       1 | 0.68 |     | 50       | 4       | 2.72 |
|       10 |       1 | 0.68 |     |       31 |       6 | 4.08 |     | 51       | 6       | 4.08 |
|       11 |       2 | 1.36 |     |       32 |       1 | 0.68 |     | 52       | 3       | 2.04 |
|       12 |       2 | 1.36 |     |       33 |       3 | 2.04 |     | 53       | 3       | 2.04 |
|       14 |       4 | 2.72 |     |       34 |       4 | 2.72 |     | 54       | 3       | 2.04 |
|       15 |       2 | 1.36 |     |       35 |       3 | 2.04 |     | 55       | 1       | 0.68 |
|       16 |       2 | 1.36 |     |       36 |       1 | 0.68 |     |          |         |      |
|       17 |       4 | 2.72 |     |       37 |       3 | 2.04 |     |          |         |      |
|       18 |       3 | 2.04 |     |       38 |       2 | 1.36 |     |          |         |      |
|       19 |       4 | 2.72 |     |       39 |       5 | 3.4  |     |          |         |      |
|       20 |       3 | 2.04 |     |       40 |       5 | 3.4  |     |          |         |      |
|       21 |       3 | 2.04 |     |       41 |       4 | 2.72 |     |          |         |      |
|       22 |       3 | 2.04 |     |       42 |       3 | 2.04 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.26 |     |       21 |       3 | 1.26 |     | 41       | 8       | 3.36 |
|        2 |       4 | 1.68 |     |       22 |       5 | 2.1  |     | 42       | 4       | 1.68 |
|        3 |       6 | 2.52 |     |       23 |       3 | 1.26 |     | 43       | 5       | 2.1  |
|        4 |       3 | 1.26 |     |       24 |       4 | 1.68 |     | 44       | 2       | 0.84 |
|        5 |       5 | 2.1  |     |       25 |       5 | 2.1  |     | 45       | 3       | 1.26 |
|        6 |       3 | 1.26 |     |       26 |       5 | 2.1  |     | 46       | 6       | 2.52 |
|        7 |       2 | 0.84 |     |       27 |       2 | 0.84 |     | 47       | 4       | 1.68 |
|        8 |       3 | 1.26 |     |       28 |       2 | 0.84 |     | 48       | 5       | 2.1  |
|        9 |       6 | 2.52 |     |       29 |       7 | 2.94 |     | 49       | 4       | 1.68 |
|       10 |       2 | 0.84 |     |       30 |       2 | 0.84 |     | 50       | 4       | 1.68 |
|       11 |       7 | 2.94 |     |       31 |       8 | 3.36 |     | 51       | 8       | 3.36 |
|       12 |       3 | 1.26 |     |       32 |       4 | 1.68 |     | 52       | 3       | 1.26 |
|       13 |       1 | 0.42 |     |       33 |       4 | 1.68 |     | 53       | 4       | 1.68 |
|       14 |       6 | 2.52 |     |       34 |       7 | 2.94 |     | 54       | 6       | 2.52 |
|       15 |       5 | 2.1  |     |       35 |       3 | 1.26 |     | 55       | 2       | 0.84 |
|       16 |       2 | 0.84 |     |       36 |       2 | 0.84 |     |          |         |      |
|       17 |       5 | 2.1  |     |       37 |       5 | 2.1  |     |          |         |      |
|       18 |       4 | 1.68 |     |       38 |       6 | 2.52 |     |          |         |      |
|       19 |       4 | 1.68 |     |       39 |       8 | 3.36 |     |          |         |      |
|       20 |       5 | 2.1  |     |       40 |       6 | 2.52 |     |          |         |      |

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

