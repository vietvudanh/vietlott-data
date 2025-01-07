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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'text/plain; charset=utf-8',
    'X-AjaxPro-Method': 'ServerSideDrawResult',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://vietlott.vn',
    'Connection': 'keep-alive',
    'Referer': 'https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-645',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

TIMEOUT = 20
