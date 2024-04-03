import cattrs

from vietlott.crawler.schema.requests import RequestPower655, ORenderInfoCls


def find_diff(d1, d2, path=""):
    diffs = []
    for k in d1:
        if k in d2:
            if isinstance(d1[k], dict):
                find_diff(d1[k], d2[k], "%s -> %s" % (path, k) if path else k)
            if d1[k] != d2[k]:
                result = [
                    "%s: " % path,
                    " - %s : %s" % (k, d1[k]),
                    " + %s : %s" % (k, d2[k]),
                ]
                print("DIFF", "\n".join(result))
                diffs.append(result)
        else:
            msg = "%s%s as key not in d2\n" % ("%s: " % path if path else "", k)
            print(msg)
            diffs.append(msg)
    return diffs


def test_schema_structure():
    """
    Test that the schema structure is as expected.
    """

    # using raw data from browser
    org_body = {
        "ORenderInfo": {
            "SiteId": "main.frontend.vi",
            "SiteAlias": "main.vi",
            "UserSessionId": "",
            "SiteLang": "en",
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
        "Key": "23bbd667",
        "GameDrawId": "",
        "ArrayNumbers": [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ],
        "CheckMulti": False,
        "PageIndex": 0,
    }

    schema_object = RequestPower655(
        ORenderInfo=ORenderInfoCls(
            SiteId="main.frontend.vi",
            SiteAlias="main.vi",
            UserSessionId="",
            SiteLang="en",
            IsPageDesign=False,
            ExtraParam1="",
            ExtraParam2="",
            ExtraParam3="",
            SiteURL="",
            WebPage=None,
            SiteName="Vietlott",
            OrgPageAlias=None,
            PageAlias=None,
            FullPageAlias=None,
            RefKey=None,
        ),
        Key="23bbd667",
        GameDrawId="",
        ArrayNumbers=[["" for _ in range(18)] for _ in range(5)],
        CheckMulti=False,
        PageIndex=0,
    )

    rendered_object = cattrs.unstructure(schema_object)

    diffs = find_diff(rendered_object, org_body)
    assert len(diffs) == 0, diffs
