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
|       | date       | result                      | predicted                |
|------:|:-----------|:----------------------------|:-------------------------|
| 17459 | 2019-08-10 | [7, 17, 36, 42, 43, 50, 44] | [44, 45, 36, 43, 42, 17] | 

## Data stats
| product   |   n_dates | start_date   | end_date   |   n_ids | start_id   | end_id   |
|:----------|----------:|:-------------|:-----------|--------:|:-----------|:---------|
| power_655 |      1188 | 2017-08-01   | 2025-05-10 |    1188 | 00001      | 01188    |
| power_645 |      1154 | 2017-10-25   | 2025-05-09 |    1154 | 00198      | 01351    |
| keno      |       887 | 2022-12-04   | 2025-05-10 |  126596 | #0110271   | #0237169 |
| 3d        |       920 | 2019-04-22   | 2025-05-09 |     920 | 00001      | 00922    |
| 3d_pro    |       567 | 2021-09-14   | 2025-05-10 |     567 | 00001      | 00569    |

## raw details 6/55 last 10 days
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-05-10 | 01188 | [7, 16, 19, 28, 34, 51, 15]  |      0 | 2025-05-10 19:00:18.573880 |
| 2025-05-08 | 01187 | [8, 14, 29, 37, 39, 50, 21]  |      0 | 2025-05-08 19:00:23.631699 |
| 2025-05-06 | 01186 | [12, 16, 25, 28, 30, 39, 5]  |      0 | 2025-05-06 19:00:19.321090 |
| 2025-05-03 | 01185 | [15, 19, 21, 26, 42, 47, 38] |      0 | 2025-05-03 19:00:20.829914 |
| 2025-05-01 | 01184 | [3, 17, 19, 41, 45, 50, 43]  |      0 | 2025-05-01 19:00:24.795215 |
| 2025-04-29 | 01183 | [14, 15, 18, 23, 28, 33, 29] |      0 | 2025-04-29 19:00:22.162238 |
| 2025-04-26 | 01182 | [3, 15, 16, 31, 48, 52, 21]  |      0 | 2025-04-26 19:00:37.192125 |
| 2025-04-24 | 01181 | [1, 2, 15, 39, 40, 47, 24]   |      0 | 2025-04-24 19:00:16.311335 |
| 2025-04-22 | 01180 | [10, 25, 37, 40, 41, 48, 32] |      0 | 2025-04-22 19:00:14.976080 |
| 2025-04-19 | 01179 | [5, 11, 15, 32, 42, 49, 43]  |      0 | 2025-04-21 11:33:24.124207 |
## stats 6/55 all time
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     166 | 2    |     |       21 |     148 | 1.78 |     | 41       | 178     | 2.14 |
|        2 |     138 | 1.66 |     |       22 |     170 | 2.04 |     | 42       | 154     | 1.85 |
|        3 |     161 | 1.94 |     |       23 |     167 | 2.01 |     | 43       | 169     | 2.03 |
|        4 |     130 | 1.56 |     |       24 |     151 | 1.82 |     | 44       | 154     | 1.85 |
|        5 |     151 | 1.82 |     |       25 |     139 | 1.67 |     | 45       | 145     | 1.74 |
|        6 |     126 | 1.52 |     |       26 |     140 | 1.68 |     | 46       | 156     | 1.88 |
|        7 |     131 | 1.58 |     |       27 |     137 | 1.65 |     | 47       | 153     | 1.84 |
|        8 |     159 | 1.91 |     |       28 |     135 | 1.62 |     | 48       | 160     | 1.92 |
|        9 |     163 | 1.96 |     |       29 |     160 | 1.92 |     | 49       | 155     | 1.86 |
|       10 |     142 | 1.71 |     |       30 |     132 | 1.59 |     | 50       | 153     | 1.84 |
|       11 |     158 | 1.9  |     |       31 |     157 | 1.89 |     | 51       | 174     | 2.09 |
|       12 |     159 | 1.91 |     |       32 |     157 | 1.89 |     | 52       | 156     | 1.88 |
|       13 |     145 | 1.74 |     |       33 |     151 | 1.82 |     | 53       | 160     | 1.92 |
|       14 |     149 | 1.79 |     |       34 |     167 | 2.01 |     | 54       | 143     | 1.72 |
|       15 |     142 | 1.71 |     |       35 |     151 | 1.82 |     | 55       | 148     | 1.78 |
|       16 |     140 | 1.68 |     |       36 |     142 | 1.71 |     |          |         |      |
|       17 |     139 | 1.67 |     |       37 |     138 | 1.66 |     |          |         |      |
|       18 |     153 | 1.84 |     |       38 |     143 | 1.72 |     |          |         |      |
|       19 |     149 | 1.79 |     |       39 |     145 | 1.74 |     |          |         |      |
|       20 |     161 | 1.94 |     |       40 |     165 | 1.98 |     |          |         |      |
## stats 6/55 -15d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 2.04 |     |       25 |       2 | 2.04 |     | 48       | 2       | 2.04 |
|        2 |       1 | 1.02 |     |       26 |       1 | 1.02 |     | 49       | 2       | 2.04 |
|        3 |       3 | 3.06 |     |       27 |       1 | 1.02 |     | 50       | 2       | 2.04 |
|        5 |       2 | 2.04 |     |       28 |       3 | 3.06 |     | 51       | 1       | 1.02 |
|        7 |       1 | 1.02 |     |       29 |       2 | 2.04 |     | 52       | 2       | 2.04 |
|        8 |       2 | 2.04 |     |       30 |       1 | 1.02 |     | 55       | 1       | 1.02 |
|       10 |       2 | 2.04 |     |       31 |       1 | 1.02 |     |          |         |      |
|       11 |       1 | 1.02 |     |       32 |       2 | 2.04 |     |          |         |      |
|       12 |       1 | 1.02 |     |       33 |       1 | 1.02 |     |          |         |      |
|       13 |       1 | 1.02 |     |       34 |       1 | 1.02 |     |          |         |      |
|       14 |       4 | 4.08 |     |       36 |       1 | 1.02 |     |          |         |      |
|       15 |       6 | 6.12 |     |       37 |       4 | 4.08 |     |          |         |      |
|       16 |       3 | 3.06 |     |       38 |       2 | 2.04 |     |          |         |      |
|       17 |       2 | 2.04 |     |       39 |       3 | 3.06 |     |          |         |      |
|       18 |       1 | 1.02 |     |       40 |       3 | 3.06 |     |          |         |      |
|       19 |       4 | 4.08 |     |       41 |       4 | 4.08 |     |          |         |      |
|       20 |       2 | 2.04 |     |       42 |       4 | 4.08 |     |          |         |      |
|       21 |       3 | 3.06 |     |       43 |       3 | 3.06 |     |          |         |      |
|       23 |       3 | 3.06 |     |       45 |       1 | 1.02 |     |          |         |      |
|       24 |       2 | 2.04 |     |       47 |       2 | 2.04 |     |          |         |      |
## stats 6/55 -30d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 2.04 |     |       25 |       2 | 2.04 |     | 48       | 2       | 2.04 |
|        2 |       1 | 1.02 |     |       26 |       1 | 1.02 |     | 49       | 2       | 2.04 |
|        3 |       3 | 3.06 |     |       27 |       1 | 1.02 |     | 50       | 2       | 2.04 |
|        5 |       2 | 2.04 |     |       28 |       3 | 3.06 |     | 51       | 1       | 1.02 |
|        7 |       1 | 1.02 |     |       29 |       2 | 2.04 |     | 52       | 2       | 2.04 |
|        8 |       2 | 2.04 |     |       30 |       1 | 1.02 |     | 55       | 1       | 1.02 |
|       10 |       2 | 2.04 |     |       31 |       1 | 1.02 |     |          |         |      |
|       11 |       1 | 1.02 |     |       32 |       2 | 2.04 |     |          |         |      |
|       12 |       1 | 1.02 |     |       33 |       1 | 1.02 |     |          |         |      |
|       13 |       1 | 1.02 |     |       34 |       1 | 1.02 |     |          |         |      |
|       14 |       4 | 4.08 |     |       36 |       1 | 1.02 |     |          |         |      |
|       15 |       6 | 6.12 |     |       37 |       4 | 4.08 |     |          |         |      |
|       16 |       3 | 3.06 |     |       38 |       2 | 2.04 |     |          |         |      |
|       17 |       2 | 2.04 |     |       39 |       3 | 3.06 |     |          |         |      |
|       18 |       1 | 1.02 |     |       40 |       3 | 3.06 |     |          |         |      |
|       19 |       4 | 4.08 |     |       41 |       4 | 4.08 |     |          |         |      |
|       20 |       2 | 2.04 |     |       42 |       4 | 4.08 |     |          |         |      |
|       21 |       3 | 3.06 |     |       43 |       3 | 3.06 |     |          |         |      |
|       23 |       3 | 3.06 |     |       45 |       1 | 1.02 |     |          |         |      |
|       24 |       2 | 2.04 |     |       47 |       2 | 2.04 |     |          |         |      |
## stats 6/55 -60d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       4 | 2.12 |     |       23 |       6 | 3.17 |     | 43       | 5       | 2.65 |
|        2 |       3 | 1.59 |     |       24 |       5 | 2.65 |     | 44       | 2       | 1.06 |
|        3 |       4 | 2.12 |     |       25 |       4 | 2.12 |     | 45       | 1       | 0.53 |
|        4 |       1 | 0.53 |     |       26 |       3 | 1.59 |     | 47       | 3       | 1.59 |
|        5 |       2 | 1.06 |     |       27 |       2 | 1.06 |     | 48       | 3       | 1.59 |
|        7 |       3 | 1.59 |     |       28 |       4 | 2.12 |     | 49       | 2       | 1.06 |
|        8 |       3 | 1.59 |     |       29 |       7 | 3.7  |     | 50       | 6       | 3.17 |
|        9 |       1 | 0.53 |     |       30 |       5 | 2.65 |     | 51       | 2       | 1.06 |
|       10 |       2 | 1.06 |     |       31 |       3 | 1.59 |     | 52       | 4       | 2.12 |
|       11 |       2 | 1.06 |     |       32 |       4 | 2.12 |     | 53       | 3       | 1.59 |
|       12 |       1 | 0.53 |     |       33 |       2 | 1.06 |     | 54       | 1       | 0.53 |
|       13 |       5 | 2.65 |     |       34 |       5 | 2.65 |     | 55       | 2       | 1.06 |
|       14 |       7 | 3.7  |     |       35 |       1 | 0.53 |     |          |         |      |
|       15 |       7 | 3.7  |     |       36 |       3 | 1.59 |     |          |         |      |
|       16 |       4 | 2.12 |     |       37 |       5 | 2.65 |     |          |         |      |
|       17 |       4 | 2.12 |     |       38 |       2 | 1.06 |     |          |         |      |
|       18 |       2 | 1.06 |     |       39 |       6 | 3.17 |     |          |         |      |
|       19 |       5 | 2.65 |     |       40 |       5 | 2.65 |     |          |         |      |
|       20 |       2 | 1.06 |     |       41 |       8 | 4.23 |     |          |         |      |
|       21 |       5 | 2.65 |     |       42 |       8 | 4.23 |     |          |         |      |
## stats 6/55 -90d
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       7 | 2.56 |     |       22 |       2 | 0.73 |     | 42       | 10      | 3.66 |
|        2 |       5 | 1.83 |     |       23 |       8 | 2.93 |     | 43       | 9       | 3.3  |
|        3 |       4 | 1.47 |     |       24 |       6 | 2.2  |     | 44       | 3       | 1.1  |
|        4 |       1 | 0.37 |     |       25 |       4 | 1.47 |     | 45       | 4       | 1.47 |
|        5 |       5 | 1.83 |     |       26 |       5 | 1.83 |     | 46       | 1       | 0.37 |
|        7 |       6 | 2.2  |     |       27 |       4 | 1.47 |     | 47       | 8       | 2.93 |
|        8 |       5 | 1.83 |     |       28 |       4 | 1.47 |     | 48       | 5       | 1.83 |
|        9 |       3 | 1.1  |     |       29 |       8 | 2.93 |     | 49       | 2       | 0.73 |
|       10 |       4 | 1.47 |     |       30 |       7 | 2.56 |     | 50       | 7       | 2.56 |
|       11 |       4 | 1.47 |     |       31 |       5 | 1.83 |     | 51       | 4       | 1.47 |
|       12 |       2 | 0.73 |     |       32 |       4 | 1.47 |     | 52       | 4       | 1.47 |
|       13 |       7 | 2.56 |     |       33 |       2 | 0.73 |     | 53       | 5       | 1.83 |
|       14 |       8 | 2.93 |     |       34 |       6 | 2.2  |     | 54       | 2       | 0.73 |
|       15 |       9 | 3.3  |     |       35 |       2 | 0.73 |     | 55       | 3       | 1.1  |
|       16 |       4 | 1.47 |     |       36 |       4 | 1.47 |     |          |         |      |
|       17 |       6 | 2.2  |     |       37 |       7 | 2.56 |     |          |         |      |
|       18 |       3 | 1.1  |     |       38 |       5 | 1.83 |     |          |         |      |
|       19 |       5 | 1.83 |     |       39 |       7 | 2.56 |     |          |         |      |
|       20 |       3 | 1.1  |     |       40 |       7 | 2.56 |     |          |         |      |
|       21 |       8 | 2.93 |     |       41 |      10 | 3.66 |     |          |         |      |

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

