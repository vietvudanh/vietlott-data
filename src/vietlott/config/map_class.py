from vietlott.crawler.products import (
    P3D,
    P3DPro,
    ProductBingo18,
    ProductKeno,
    ProductPower535,
    ProductPower645,
    ProductPower655,
)

map_class_name = {
    "keno": ProductKeno,
    "power_655": ProductPower655,
    "power_645": ProductPower645,
    "power_535": ProductPower535,
    "3d": P3D,
    "3d_pro": P3DPro,
    "bingo18": ProductBingo18,
}
