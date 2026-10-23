#!/usr/bin/env python3
"""
Test script for Keno configuration
"""

from vietlott.config.map_class import map_class_name
from vietlott.config.products import get_config


def test_keno_config():
    """Test Keno configuration"""
    config = get_config("keno")
    assert config.name == "keno", f"Expected name 'keno', got '{config.name}'"
    assert config.min_value == 1, f"Expected min_value 1, got {config.min_value}"
    assert config.max_value == 80, f"Expected max_value 80, got {config.max_value}"
    assert config.size_output == 20, f"Expected size_output 20, got {config.size_output}"

    product_class = map_class_name.get("keno")
    assert product_class is not None, "Product class not found in map_class_name"
    assert product_class.__name__ == "ProductKeno"

    instance = product_class()
    assert instance.name == "keno"
    assert "GameKenoCompareWebPart" in instance.url
