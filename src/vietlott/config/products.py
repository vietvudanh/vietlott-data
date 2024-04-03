import attr
from datetime import timedelta
from pathlib import Path

cwd = Path(__file__).parent
project_root = Path(__file__).parent.parent.parent

data_dir = project_root.parent / "data"


@attr.define
class ProductConfig:
    name: str
    raw_path: Path
    min_value: int
    max_value: int
    size_output: int
    interval: timedelta
    num_thread: int = 10
    use_cookies: bool = True
    default_index_to: int = 1
    page_size: int = 6


power655_config = ProductConfig(
    name="power_655",
    raw_path=data_dir / "power655.jsonl",
    min_value=1,
    max_value=55,
    size_output=6,
    interval=timedelta(days=2),
    use_cookies=False,
)
power645_config = ProductConfig(
    name="power_645",
    raw_path=data_dir / "power645.jsonl",
    min_value=1,
    max_value=45,
    size_output=6,
    interval=timedelta(days=2),
    use_cookies=False,
)
keno_config = ProductConfig(
    name="keno",
    raw_path=data_dir / "keno.jsonl",
    min_value=1,
    max_value=45,
    size_output=6,
    interval=timedelta(days=2),
    default_index_to=24,
    num_thread=20,
    page_size=6,
    use_cookies=False,
)

product_config_map = {c.name: c for c in [power645_config, power655_config, keno_config]}


def get_config(name: str) -> ProductConfig:
    if name in product_config_map:
        return product_config_map[name]
    else:
        raise ValueError(f"Unknown product: {name}")
