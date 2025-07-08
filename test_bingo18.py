#!/usr/bin/env python3
"""
Test script for Bingo18 configuration
"""

import sys
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from vietlott.config.map_class import map_class_name
from vietlott.config.products import get_config


def test_bingo18_config():
    """Test Bingo18 configuration"""
    print("Testing Bingo18 configuration...")

    # Test product config
    config = get_config("bingo18")
    assert config.name == "bingo18", f"Expected name 'bingo18', got '{config.name}'"
    assert config.min_value == 0, f"Expected min_value 0, got {config.min_value}"
    assert config.max_value == 9, f"Expected max_value 9, got {config.max_value}"
    assert config.size_output == 3, f"Expected size_output 3, got {config.size_output}"
    print(f"✓ Config loaded successfully: {config.name}")
    print(f"  - Min value: {config.min_value}")
    print(f"  - Max value: {config.max_value}")
    print(f"  - Size output: {config.size_output}")
    print(f"  - Interval: {config.interval}")
    print(f"  - Raw path: {config.raw_path}")

    # Test class mapping
    product_class = map_class_name.get("bingo18")
    assert product_class is not None, "Product class not found in map_class_name"
    assert product_class.__name__ == "ProductBingo18", (
        f"Expected class name 'ProductBingo18', got '{product_class.__name__}'"
    )
    print(f"✓ Product class found: {product_class.__name__}")

    # Test instantiation
    instance = product_class()
    assert instance.name == "bingo18", f"Expected instance name 'bingo18', got '{instance.name}'"
    assert "GameBingoCompareWebPart" in instance.url, (
        f"Expected URL to contain 'GameBingoCompareWebPart', got '{instance.url}'"
    )
    assert "result" in instance.stored_data_dtype, "Expected 'result' field in stored_data_dtype"
    assert len(instance.stored_data_dtype) >= 6, (
        f"Expected at least 6 data type fields, got {len(instance.stored_data_dtype)}"
    )
    print("✓ Product instance created successfully")
    print(f"  - Name: {instance.name}")
    print(f"  - URL: {instance.url}")
    print(f"  - Data types: {instance.stored_data_dtype}")

    print("\n✓ All tests passed! Bingo18 is configured correctly.")
    return True


if __name__ == "__main__":
    success = test_bingo18_config()
    sys.exit(0 if success else 1)
