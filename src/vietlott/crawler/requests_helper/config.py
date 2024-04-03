from pathlib import Path

cwd = Path(__file__).parent

# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
#     "Accept": "*/*",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Content-Type": "text/plain; charset=utf-8",
#     "X-AjaxPro-Method": "ServerSideDrawResult",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin"
# }

headers = {
    "Host": "vietlott.vn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "text/plain; charset=utf-8",
    "X-AjaxPro-Method": "ServerSideDrawResult",
    "Content-Length": "670",
    "Origin": "https://vietlott.vn",
    "Connection": "keep-alive",
    "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655",
    # "Cookie": "D1N=4ba207a670090cbab6b026f2d64e4d5b",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
}

TIMEOUT = 20
