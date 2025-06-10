#!/usr/bin/env python3
"""
Test script for Bingo18 configuration
"""

import sys
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from vietlott.config.products import get_config
from vietlott.config.map_class import map_class_name


def test_bingo18_config():
    """Test Bingo18 configuration"""
    print("Testing Bingo18 configuration...")

    try:
        # Test product config
        config = get_config("bingo18")
        print(f"✓ Config loaded successfully: {config.name}")
        print(f"  - Min value: {config.min_value}")
        print(f"  - Max value: {config.max_value}")
        print(f"  - Size output: {config.size_output}")
        print(f"  - Interval: {config.interval}")
        print(f"  - Raw path: {config.raw_path}")

        # Test class mapping
        product_class = map_class_name.get("bingo18")
        if product_class:
            print(f"✓ Product class found: {product_class.__name__}")

            # Test instantiation
            instance = product_class()
            print("✓ Product instance created successfully")
            print(f"  - Name: {instance.name}")
            print(f"  - URL: {instance.url}")
            print(f"  - Data types: {instance.stored_data_dtype}")

        else:
            print("✗ Product class not found in map_class_name")
            return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

    print("\n✓ All tests passed! Bingo18 is configured correctly.")
    return True


if __name__ == "__main__":
    success = test_bingo18_config()
    sys.exit(0 if success else 1)
