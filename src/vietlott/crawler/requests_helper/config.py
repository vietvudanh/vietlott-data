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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/octet-stream",
    "X-Requested-With": "XMLHttpRequest",
    "X-csrftoken": "1813c50925a5f035fe1d472bf49fd2760de7f4694b082b2d5ba8a2aad77c7886dc16b6ac9946c6fb",
    "X-Ajax-Token": "f5cfca365b94035ece913dd1d70f7d9e91597ca23872847b74bc2f5d84cb1356",
    "Origin": "https://vietlott.vn",
    "Connection": "keep-alive",
    "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
}

TIMEOUT = 20
