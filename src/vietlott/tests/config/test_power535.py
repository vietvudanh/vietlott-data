#!/usr/bin/env python3
"""
Test script for Power 535 configuration
"""

import sys
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from vietlott.config.map_class import map_class_name
from vietlott.config.products import get_config


def test_power535_config():
    """Test Power 535 configuration"""
    print("Testing Power 535 configuration...")

    # Test product config
    config = get_config("power_535")
    assert config.name == "power_535", f"Expected name 'power_535', got '{config.name}'"
    assert config.min_value == 1, f"Expected min_value 1, got {config.min_value}"
    assert config.max_value == 35, f"Expected max_value 35, got {config.max_value}"
    assert config.size_output == 5, f"Expected size_output 5, got {config.size_output}"
    print(f"✓ Config loaded successfully: {config.name}")
    print(f"  - Min value: {config.min_value}")
    print(f"  - Max value: {config.max_value}")
    print(f"  - Size output: {config.size_output}")
    print(f"  - Interval: {config.interval}")
    print(f"  - Raw path: {config.raw_path}")

    # Test class mapping
    product_class = map_class_name.get("power_535")
    assert product_class is not None, "Product class not found in map_class_name"
    assert (
        product_class.__name__ == "ProductPower535"
    ), f"Expected class name 'ProductPower535', got '{product_class.__name__}'"
    print(f"✓ Product class found: {product_class.__name__}")

    # Test instantiation
    instance = product_class()
    assert instance.name == "power_535", f"Expected instance name 'power_535', got '{instance.name}'"
    assert (
        "Game535CompareWebPart" in instance.url
    ), f"Expected URL to contain 'Game535CompareWebPart', got '{instance.url}'"
    assert "result" in instance.stored_data_dtype, "Expected 'result' field in stored_data_dtype"
    assert (
        len(instance.stored_data_dtype) >= 4
    ), f"Expected at least 4 data type fields, got {len(instance.stored_data_dtype)}"
    print("✓ Product instance created successfully")
    print(f"  - Name: {instance.name}")
    print(f"  - URL: {instance.url}")
    print(f"  - Data types: {instance.stored_data_dtype}")

    print("\n✓ All tests passed! Power 535 is configured correctly.")
