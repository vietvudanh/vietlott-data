#!/usr/bin/env python
"""
Diagnostic script to compare expected API request format with what we're sending
"""
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import cattrs
from loguru import logger

from vietlott.crawler.products import (
    ProductPower655,
    ProductPower645,
    ProductPower535,
    ProductKeno,
    P3D,
    P3DPro,
    ProductBingo18,
)

# Expected format from the curl command for power_655
EXPECTED_POWER655_CURL = {
    "url": "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "text/plain; charset=utf-8",
        "X-AjaxPro-Method": "ServerSideDrawResult",
        "X-Requested-With": "XMLHttpRequest",
        "X-csrftoken": "186f48db37618fb935425acd17f3d05227c9f40ec088bbf656265b1b416fb4d62a064074c01c9353",
        "X-Ajax-Token": "3c7ed79d78e978209b27088f99c21f9d2b057d624ae399fb3a95f19ae81dfb89",
        "Origin": "https://vietlott.vn",
        "Connection": "keep-alive",
        "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655",
        "Cookie": "session-cookie=186f48da4e9101a9deb39ea24c95548fc280ec9f18fd414bb6407b30925cf31e724164ce03a70244bae10df28b4a8411; csrf-token-name=csrftoken; csrf-token-value=186f48dc5cebd228392493e6ec408e896b1ea7e1501f04d60ef791667645bebc4ed100a57ca24e66",
    },
    "body": {
        "ORenderInfo": {
            "SiteId": "main.frontend.vi",
            "SiteAlias": "main.vi",
            "UserSessionId": "",
            "SiteLang": "vi",
            "IsPageDesign": False,
            "ExtraParam1": "",
            "ExtraParam2": "",
            "ExtraParam3": "",
            "SiteURL": "",
            "WebPage": None,
            "SiteName": "Vietlott",
            "OrgPageAlias": None,
            "PageAlias": None,
            "FullPageAlias": None,
            "RefKey": None,
            "System": 1,
        },
        "Key": "5a0fff20",
        "GameDrawId": "",
        "ArrayNumbers": [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ],
        "CheckMulti": False,
        "PageIndex": 1,
    },
}


def diagnose_product(product_class, product_name):
    """Diagnose a single product"""
    logger.info(f"\n{'='*60}")
    logger.info(f"Diagnosing {product_name}")
    logger.info(f"{'='*60}")

    product = product_class()

    logger.info(f"\nURL: {product.url}")
    logger.info(f"\nHeaders configured:")
    for key, value in product.headers.items():
        logger.info(f"  {key}: {value}")

    logger.info(f"\nBody structure:")
    body = cattrs.unstructure(product.org_body)
    body["PageIndex"] = 1  # Set to 1 for comparison
    logger.info(json.dumps(body, indent=2))

    logger.info(f"\nCookies: {product.cookies}")

    if product_name == "power_655":
        logger.info(f"\n{'='*60}")
        logger.info("COMPARISON WITH EXPECTED (from curl)")
        logger.info(f"{'='*60}")

        # Compare URL
        if product.url == EXPECTED_POWER655_CURL["url"]:
            logger.info("✓ URL matches")
        else:
            logger.error(f"✗ URL mismatch: {product.url}")

        # Compare Key
        expected_key = EXPECTED_POWER655_CURL["body"]["Key"]
        actual_key = body.get("Key", "")
        if actual_key == expected_key:
            logger.info(f"✓ Key matches: {actual_key}")
        else:
            logger.error(f"✗ Key mismatch: expected={expected_key}, actual={actual_key}")

        # Compare ORenderInfo
        expected_orender = EXPECTED_POWER655_CURL["body"]["ORenderInfo"]
        actual_orender = body.get("ORenderInfo", {})
        
        orender_matches = True
        for key in expected_orender:
            if expected_orender[key] != actual_orender.get(key):
                logger.error(
                    f"✗ ORenderInfo.{key} mismatch: expected={expected_orender[key]}, actual={actual_orender.get(key)}"
                )
                orender_matches = False
        
        if orender_matches:
            logger.info("✓ ORenderInfo matches")

        # Check required headers
        required_headers = ["X-AjaxPro-Method", "X-Requested-With", "X-csrftoken", "X-Ajax-Token"]
        for header in required_headers:
            if header in product.headers:
                logger.info(f"✓ Header '{header}' present")
            else:
                logger.warning(f"⚠ Header '{header}' missing (might be dynamic)")


def main():
    logger.remove()  # Remove default handler
    logger.add(sys.stdout, level="INFO")

    products = [
        (ProductPower655, "power_655"),
        (ProductPower645, "power_645"),
        (ProductPower535, "power_535"),
        (ProductKeno, "keno"),
        (P3D, "3d"),
        (P3DPro, "3d_pro"),
        (ProductBingo18, "bingo18"),
    ]

    for product_class, product_name in products:
        try:
            diagnose_product(product_class, product_name)
        except Exception as e:
            logger.error(f"Error diagnosing {product_name}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
