# Vietlott-data architecture

The project is quite simple with all sources are in `/src`

You can start with `/src/cli` to check what are available and start there

## product config

I tried to make the process of adding new product as easy as possible via config first approach.

The base config is at `vietlott.config.products.ProductConfig`, with settings mostly works for all products of Vietlott.

Key points:
- cookies used to needed to crawl but not anymore (disabled for all products)
- data on website are in [pages](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655) so the fetching are designed around that mechanism (also the detect missing and back-filled mechanism at [missing.py](https://github.com/vietvudanh/vietlott-data/blob/89c6aaa632011c6ef248e43178f38e05daeee1b9/src/vietlott/cli/missing.py#L22))  

## runner

The project uses Github Actions with [config](https://github.com/vietvudanh/vietlott-data/blob/master/.github/workflows/crawl.yaml) 
to schedule the run daily to crawl & push to itself. So no server required.

To make it easier (for me) to dev, the [binary file](https://github.com/vietvudanh/vietlott-data/blob/master/.github/workflows/crawl.yaml)
set `PYTHONPATH` to `/src`, but it can and should be using installed cli:

```toml
[project.scripts]
vietlott-crawl = "vietlott.cli.crawl:crawl"
vietlott-missing = "vietlott.cli.crawl:detect_missing_data"
```