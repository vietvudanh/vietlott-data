from vietlott.crawler.products.power535 import ProductPower535


def make_sample_html():
    # Minimal HTML similar to site structure: table with header row then data rows
    return (
        '<table>'
        '<tr><th>Ngày</th><th>Mã</th><th>Kết quả</th></tr>'
        '<tr>'
        '<td>10/10/2025</td>'
        '<td>00001</td>'
        '<td><span>01</span><span>|</span><span>12</span><span>|</span><span>23</span><span>|</span><span>34</span><span>|</span><span>35</span></td>'
        '</tr>'
        '</table>'
    )


def test_power535_process_result_parses_sample():
    prod = ProductPower535()
    sample_html = make_sample_html()
    res_json = {"value": {"HtmlContent": sample_html}}
    body = {"PageIndex": 0}
    results = prod.process_result({}, body, res_json, {})

    assert isinstance(results, list)
    assert len(results) == 1
    row = results[0]
    assert row["date"] == "2025-10-10"
    assert row["id"] == "00001"
    # numbers should be parsed (filtering out '|' tokens)
    assert row["result"] == [1, 12, 23, 34, 35]
    assert row["page"] == 0
