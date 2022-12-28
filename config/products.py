import attr
from datetime import timedelta
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
    interval: timedelta
    num_thread: int = 5


power655_config = ProductConfig(name='power_655',
                                raw_path=data_dir / 'power655.jsonl',
                                min_value=1, max_value=55, size_output=6,
                                interval=timedelta(days=2))
power645_config = ProductConfig(name='power_645',
                                raw_path=data_dir / 'power645.jsonl',
                                min_value=1, max_value=45, size_output=6,
                                interval=timedelta(days=2))
keno_config = ProductConfig(name='keno',
                            raw_path=data_dir / 'keno.jsonl',
                            min_value=1, max_value=45, size_output=6,
                            interval=timedelta(days=2))

product_map = {c.name: c for c in [power645_config,
                                   power655_config,
                                   keno_config]}


def get_config(name: str) -> ProductConfig:
    return product_map.get(name)
