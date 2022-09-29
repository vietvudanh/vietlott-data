from datetime import timedelta

import attr
from pathlib import Path

cwd = Path(__file__).parent

data_dir = cwd.parent / 'data'


@attr.define
class ProductConfig:
    name: str
    raw_path: Path
    min_value: int
    max_value: int
    size_output: int
    freq: timedelta  # frequency which new result are rotate
    num_thread: int = 5


power655_config = ProductConfig('power_655', data_dir / 'power655.jsonl', 1, 55, 6, timedelta(days=2))
power645_config = ProductConfig('power_645', data_dir / 'power645.jsonl', 1, 45, 6, timedelta(days=2))

product_map = {c.name: c for c in [power645_config, power655_config]}


def get_config(name: str) -> ProductConfig:
    return product_map.get(name)
