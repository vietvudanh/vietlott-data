from typing import List, Optional
from attrs import define, field


@define
class ORenderInfoCls:
    ExtraParam1: str = field(default="")
    ExtraParam2: str = field(default="")
    ExtraParam3: str = field(default="")
    FullPageAlias: Optional[str] = field(default="")
    IsPageDesign: bool = field(default=False)
    OrgPageAlias: Optional[str] = field(default="")
    PageAlias: Optional[str] = field(default="")
    RefKey: Optional[str] = field(default="")
    SiteAlias: str = field(default="")
    SiteId: str = field(default="")
    SiteLang: str = field(default="")
    SiteName: str = field(default="")
    SiteURL: str = field(default="")
    System: int = field(default=1)
    UserSessionId: str = field(default="")
    WebPage: Optional[str] = field(default="")


@define
class RequestPower655:
    """
    Request Power 655
    """

    # Request Power 655
    ORenderInfo: ORenderInfoCls = field(default=ORenderInfoCls())
    Key: str = field(default="")
    GameDrawId: str = field(default="")
    ArrayNumbers: List[List[str]] = field(default=[[]])
    CheckMulti: bool = field(default=False)
    PageIndex: int = field(default=1)


@define
class Keno:
    DrawDate: str = field(default="")
    GameDrawNo: str = field(default="")
    GameId: str = field(default="")
    ORenderInfo: ORenderInfoCls = field(default=ORenderInfoCls())
    OddEven: int = field(default=2)
    PageIndex: int = field(default=1)
    ProcessType: int = field(default=0)
    TotalRow: int = field(default=10)
    UpperLower: int = field(default=2)
    number: str = field(default="")
