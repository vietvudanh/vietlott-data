import cattrs

from vietlott.crawler.schema.requests import ORenderInfoCls, RequestPower535


def test_power535_schema_structure():
    """
    Test that the Power 535 schema structure is valid.
    """
    
    # Test basic schema construction
    schema_object = RequestPower535(
        ORenderInfo=ORenderInfoCls(
            SiteId="main.frontend.vi",
            SiteAlias="main.vi",
            UserSessionId="",
            SiteLang="vi",
            IsPageDesign=False,
            ExtraParam1="",
            ExtraParam2="",
            ExtraParam3="",
            SiteURL="",
            WebPage=None,
            SiteName="Vietlott",
            OrgPageAlias=None,
            PageAlias=None,
            RefKey=None,
            FullPageAlias=None,
        ),
        Key="",
        GameDrawId="",
        ArrayNumbers=[["" for _ in range(15)] for _ in range(5)],  # 5 rows for Power 5/35
        CheckMulti=False,
        PageIndex=0,
    )

    # Test that it can be serialized
    rendered_object = cattrs.unstructure(schema_object)
    
    # Basic validation
    assert "ORenderInfo" in rendered_object
    assert "Key" in rendered_object
    assert "ArrayNumbers" in rendered_object
    assert len(rendered_object["ArrayNumbers"]) == 5  # 5 rows
    assert len(rendered_object["ArrayNumbers"][0]) == 15  # 15 columns per row
    
    print("✓ Power 535 schema validates correctly")


if __name__ == "__main__":
    test_power535_schema_structure()