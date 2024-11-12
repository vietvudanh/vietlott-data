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
| 2024-11-12 | 01112 | [1, 21, 29, 35, 41, 45, 20]  |      0 | 2024-11-12 14:08:35.280505 |
| 2024-11-09 | 01111 | [11, 14, 24, 26, 34, 51, 40] |      0 | 2024-11-10 02:14:10.380124 |
| 2024-11-07 | 01110 | [6, 9, 33, 39, 50, 51, 43]   |      0 | 2024-11-07 14:08:25.399717 |
| 2024-11-05 | 01109 | [9, 31, 36, 46, 49, 54, 7]   |      0 | 2024-11-05 14:08:24.678745 |
| 2024-11-02 | 01108 | [2, 9, 19, 20, 34, 54, 26]   |      0 | 2024-11-02 14:07:17.372355 |
| 2024-10-31 | 01107 | [5, 16, 20, 29, 30, 31, 39]  |      0 | 2024-10-31 14:08:16.746749 |
| 2024-10-29 | 01106 | [14, 17, 19, 28, 47, 51, 55] |      0 | 2024-10-29 14:08:48.629579 |
| 2024-10-26 | 01105 | [5, 19, 27, 29, 42, 47, 40]  |      0 | 2024-10-26 14:06:46.276827 |
| 2024-10-24 | 01104 | [5, 17, 31, 39, 46, 53, 3]   |      0 | 2024-10-24 14:08:28.302617 |
| 2024-10-22 | 01103 | [15, 21, 23, 26, 31, 43, 35] |      0 | 2024-10-22 14:08:22.006721 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     153 | 1.97 |     |       21 |     136 | 1.75 |     | 41       | 161     | 2.07 |
|        2 |     132 | 1.7  |     |       22 |     160 | 2.06 |     | 42       | 139     | 1.79 |
|        3 |     154 | 1.98 |     |       23 |     157 | 2.02 |     | 43       | 157     | 2.02 |
|        4 |     124 | 1.59 |     |       24 |     139 | 1.79 |     | 44       | 148     | 1.9  |
|        5 |     144 | 1.85 |     |       25 |     132 | 1.7  |     | 45       | 137     | 1.76 |
|        6 |     123 | 1.58 |     |       26 |     130 | 1.67 |     | 46       | 153     | 1.97 |
|        7 |     123 | 1.58 |     |       27 |     131 | 1.68 |     | 47       | 141     | 1.81 |
|        8 |     150 | 1.93 |     |       28 |     126 | 1.62 |     | 48       | 148     | 1.9  |
|        9 |     156 | 2    |     |       29 |     146 | 1.88 |     | 49       | 148     | 1.9  |
|       10 |     132 | 1.7  |     |       30 |     121 | 1.55 |     | 50       | 142     | 1.82 |
|       11 |     145 | 1.86 |     |       31 |     146 | 1.88 |     | 51       | 158     | 2.03 |
|       12 |     152 | 1.95 |     |       32 |     150 | 1.93 |     | 52       | 147     | 1.89 |
|       13 |     135 | 1.73 |     |       33 |     144 | 1.85 |     | 53       | 149     | 1.91 |
|       14 |     138 | 1.77 |     |       34 |     157 | 2.02 |     | 54       | 136     | 1.75 |
|       15 |     131 | 1.68 |     |       35 |     148 | 1.9  |     | 55       | 142     | 1.82 |
|       16 |     124 | 1.59 |     |       36 |     133 | 1.71 |     |          |         |      |
|       17 |     129 | 1.66 |     |       37 |     123 | 1.58 |     |          |         |      |
|       18 |     144 | 1.85 |     |       38 |     134 | 1.72 |     |          |         |      |
|       19 |     139 | 1.79 |     |       39 |     130 | 1.67 |     |          |         |      |
|       20 |     154 | 1.98 |     |       40 |     152 | 1.95 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1 |     |       26 |       4 | 4.4  |     | 50       | 1       | 1.1 |
|        2 |       1 | 1.1 |     |       27 |       1 | 1.1  |     | 51       | 4       | 4.4 |
|        3 |       1 | 1.1 |     |       28 |       1 | 1.1  |     | 52       | 1       | 1.1 |
|        4 |       1 | 1.1 |     |       29 |       3 | 3.3  |     | 53       | 1       | 1.1 |
|        5 |       3 | 3.3 |     |       30 |       1 | 1.1  |     | 54       | 2       | 2.2 |
|        6 |       1 | 1.1 |     |       31 |       5 | 5.49 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1 |     |       33 |       2 | 2.2  |     |          |         |     |
|        9 |       4 | 4.4 |     |       34 |       2 | 2.2  |     |          |         |     |
|       11 |       2 | 2.2 |     |       35 |       2 | 2.2  |     |          |         |     |
|       14 |       3 | 3.3 |     |       36 |       1 | 1.1  |     |          |         |     |
|       15 |       2 | 2.2 |     |       38 |       1 | 1.1  |     |          |         |     |
|       16 |       1 | 1.1 |     |       39 |       4 | 4.4  |     |          |         |     |
|       17 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       19 |       4 | 4.4 |     |       41 |       3 | 3.3  |     |          |         |     |
|       20 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       21 |       2 | 2.2 |     |       43 |       3 | 3.3  |     |          |         |     |
|       22 |       1 | 1.1 |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1 |     |       46 |       3 | 3.3  |     |          |         |     |
|       24 |       1 | 1.1 |     |       47 |       2 | 2.2  |     |          |         |     |
|       25 |       2 | 2.2 |     |       49 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -30d
|   result |   count |   % | -   |   result |   count |    % | -   | result   | count   | %   |
|---------:|--------:|----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:----|
|        1 |       1 | 1.1 |     |       26 |       4 | 4.4  |     | 50       | 1       | 1.1 |
|        2 |       1 | 1.1 |     |       27 |       1 | 1.1  |     | 51       | 4       | 4.4 |
|        3 |       1 | 1.1 |     |       28 |       1 | 1.1  |     | 52       | 1       | 1.1 |
|        4 |       1 | 1.1 |     |       29 |       3 | 3.3  |     | 53       | 1       | 1.1 |
|        5 |       3 | 3.3 |     |       30 |       1 | 1.1  |     | 54       | 2       | 2.2 |
|        6 |       1 | 1.1 |     |       31 |       5 | 5.49 |     | 55       | 1       | 1.1 |
|        7 |       1 | 1.1 |     |       33 |       2 | 2.2  |     |          |         |     |
|        9 |       4 | 4.4 |     |       34 |       2 | 2.2  |     |          |         |     |
|       11 |       2 | 2.2 |     |       35 |       2 | 2.2  |     |          |         |     |
|       14 |       3 | 3.3 |     |       36 |       1 | 1.1  |     |          |         |     |
|       15 |       2 | 2.2 |     |       38 |       1 | 1.1  |     |          |         |     |
|       16 |       1 | 1.1 |     |       39 |       4 | 4.4  |     |          |         |     |
|       17 |       2 | 2.2 |     |       40 |       2 | 2.2  |     |          |         |     |
|       19 |       4 | 4.4 |     |       41 |       3 | 3.3  |     |          |         |     |
|       20 |       3 | 3.3 |     |       42 |       2 | 2.2  |     |          |         |     |
|       21 |       2 | 2.2 |     |       43 |       3 | 3.3  |     |          |         |     |
|       22 |       1 | 1.1 |     |       45 |       1 | 1.1  |     |          |         |     |
|       23 |       1 | 1.1 |     |       46 |       3 | 3.3  |     |          |         |     |
|       24 |       1 | 1.1 |     |       47 |       2 | 2.2  |     |          |         |     |
|       25 |       2 | 2.2 |     |       49 |       1 | 1.1  |     |          |         |     |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 1.1  |     |       21 |       3 | 1.65 |     | 41       | 7       | 3.85 |
|        2 |       4 | 2.2  |     |       22 |       4 | 2.2  |     | 42       | 3       | 1.65 |
|        3 |       5 | 2.75 |     |       23 |       1 | 0.55 |     | 43       | 5       | 2.75 |
|        4 |       3 | 1.65 |     |       24 |       3 | 1.65 |     | 44       | 2       | 1.1  |
|        5 |       4 | 2.2  |     |       25 |       4 | 2.2  |     | 45       | 2       | 1.1  |
|        6 |       3 | 1.65 |     |       26 |       5 | 2.75 |     | 46       | 4       | 2.2  |
|        7 |       2 | 1.1  |     |       27 |       2 | 1.1  |     | 47       | 3       | 1.65 |
|        8 |       1 | 0.55 |     |       28 |       1 | 0.55 |     | 48       | 4       | 2.2  |
|        9 |       6 | 3.3  |     |       29 |       6 | 3.3  |     | 49       | 2       | 1.1  |
|       10 |       1 | 0.55 |     |       30 |       1 | 0.55 |     | 50       | 4       | 2.2  |
|       11 |       5 | 2.75 |     |       31 |       6 | 3.3  |     | 51       | 6       | 3.3  |
|       12 |       2 | 1.1  |     |       32 |       4 | 2.2  |     | 52       | 2       | 1.1  |
|       13 |       1 | 0.55 |     |       33 |       2 | 1.1  |     | 53       | 3       | 1.65 |
|       14 |       5 | 2.75 |     |       34 |       6 | 3.3  |     | 54       | 5       | 2.75 |
|       15 |       3 | 1.65 |     |       35 |       3 | 1.65 |     | 55       | 2       | 1.1  |
|       16 |       1 | 0.55 |     |       36 |       1 | 0.55 |     |          |         |      |
|       17 |       5 | 2.75 |     |       37 |       1 | 0.55 |     |          |         |      |
|       18 |       4 | 2.2  |     |       38 |       2 | 1.1  |     |          |         |      |
|       19 |       4 | 2.2  |     |       39 |       5 | 2.75 |     |          |         |      |
|       20 |       3 | 1.65 |     |       40 |       4 | 2.2  |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       3 | 1.1  |     |       21 |       5 | 1.83 |     | 41       | 9       | 3.3  |
|        2 |       6 | 2.2  |     |       22 |       5 | 1.83 |     | 42       | 4       | 1.47 |
|        3 |       6 | 2.2  |     |       23 |       4 | 1.47 |     | 43       | 6       | 2.2  |
|        4 |       4 | 1.47 |     |       24 |       5 | 1.83 |     | 44       | 2       | 0.73 |
|        5 |       8 | 2.93 |     |       25 |       4 | 1.47 |     | 45       | 4       | 1.47 |
|        6 |       5 | 1.83 |     |       26 |       6 | 2.2  |     | 46       | 8       | 2.93 |
|        7 |       2 | 0.73 |     |       27 |       3 | 1.1  |     | 47       | 4       | 1.47 |
|        8 |       5 | 1.83 |     |       28 |       3 | 1.1  |     | 48       | 6       | 2.2  |
|        9 |       6 | 2.2  |     |       29 |      10 | 3.66 |     | 49       | 3       | 1.1  |
|       10 |       2 | 0.73 |     |       30 |       3 | 1.1  |     | 50       | 4       | 1.47 |
|       11 |       9 | 3.3  |     |       31 |       8 | 2.93 |     | 51       | 7       | 2.56 |
|       12 |       3 | 1.1  |     |       32 |       5 | 1.83 |     | 52       | 2       | 0.73 |
|       13 |       1 | 0.37 |     |       33 |       4 | 1.47 |     | 53       | 4       | 1.47 |
|       14 |       6 | 2.2  |     |       34 |       8 | 2.93 |     | 54       | 6       | 2.2  |
|       15 |       5 | 1.83 |     |       35 |       4 | 1.47 |     | 55       | 3       | 1.1  |
|       16 |       2 | 0.73 |     |       36 |       2 | 0.73 |     |          |         |      |
|       17 |       6 | 2.2  |     |       37 |       4 | 1.47 |     |          |         |      |
|       18 |       5 | 1.83 |     |       38 |       9 | 3.3  |     |          |         |      |
|       19 |       4 | 1.47 |     |       39 |       8 | 2.93 |     |          |         |      |
|       20 |       8 | 2.93 |     |       40 |       5 | 1.83 |     |          |         |      |

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

