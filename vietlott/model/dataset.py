from typing import List

import numpy as np
import pandas as pd

from vietlott.config.products import get_config


def load_dataset(product_name: str):
    """load dataset from given product_name"""
    p_config = get_config(product_name)
    return pd.read_json(p_config.raw_path, lines=True)


def gen_random_list(min_val: int, max_val: int, size: int) -> List[int]:
    """load dataset from given product_name"""
    return np.random.randint(min_val, max_val, size).tolist()
