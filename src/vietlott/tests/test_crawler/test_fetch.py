import cattrs

from vietlott.crawler.products.power645 import ProductPower645
from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.requests_helper import config as requests_config
from vietlott.crawler.requests_helper.fetch import fetch_wrapper


def test_power_655():
    def _fn(params, body, parsed_json, task_data):
        return parsed_json

    # vietlott_cookie, cookies = get_vietlott_cookie()
    vietlott_cookie, cookies = None, None
    fn_fetch = fetch_wrapper(
        ProductPower655.url,
        dict(Cookie=vietlott_cookie, **requests_config.headers),
        ProductPower655.org_params,
        cattrs.unstructure(ProductPower655.org_body),
        _fn,
        cookies,
    )
    resp = fn_fetch([{"task_id": "1", "task_data": {"params": {}, "body": {"PageIndex": 1}}}])

    assert len(resp) == 1, "some task fail"


def test_power_645():
    def _fn(params, body, parsed_json, task_data):
        return parsed_json

    # vietlott_cookie, cookies = get_vietlott_cookie()
    vietlott_cookie, cookies = None, None
    fn_fetch = fetch_wrapper(
        ProductPower645.url,
        dict(Cookie=vietlott_cookie, **requests_config.headers),
        ProductPower645.org_params,
        cattrs.unstructure(ProductPower645.org_body),
        _fn,
        cookies,
    )
    resp = fn_fetch([{"task_id": "1", "task_data": {"params": {}, "body": {"PageIndex": 1}}}])

    assert len(resp) == 1, "some task fail"
