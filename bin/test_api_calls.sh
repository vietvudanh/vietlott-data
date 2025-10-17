#!/usr/bin/env bash
# Test script to check API calls for all products with debug logging

# Activate virtual environment if it exists
VENV=".venv"
if [ -n "$VENV" ]; then
  source "$VENV/bin/activate"
fi

export PYTHONPATH="src"
export LOGURU_LEVEL="DEBUG"

echo "================================"
echo "Testing API calls with DEBUG logs"
echo "================================"
echo ""

echo "Testing keno..."
python src/vietlott/cli/crawl.py keno --index_from 1 --index_to 1 2>&1 | tee /tmp/keno_test.log
echo ""

echo "Testing power_655..."
python src/vietlott/cli/crawl.py power_655 --index_from 1 --index_to 1 2>&1 | tee /tmp/power_655_test.log
echo ""

echo "Testing power_645..."
python src/vietlott/cli/crawl.py power_645 --index_from 1 --index_to 1 2>&1 | tee /tmp/power_645_test.log
echo ""

echo "Testing power_535..."
python src/vietlott/cli/crawl.py power_535 --index_from 1 --index_to 1 2>&1 | tee /tmp/power_535_test.log
echo ""

echo "Testing 3d..."
python src/vietlott/cli/crawl.py 3d --index_from 1 --index_to 1 2>&1 | tee /tmp/3d_test.log
echo ""

echo "Testing 3d_pro..."
python src/vietlott/cli/crawl.py 3d_pro --index_from 1 --index_to 1 2>&1 | tee /tmp/3d_pro_test.log
echo ""

echo "Testing bingo18..."
python src/vietlott/cli/crawl.py bingo18 --index_from 1 --index_to 1 2>&1 | tee /tmp/bingo18_test.log
echo ""

echo "================================"
echo "Test logs saved to /tmp/*_test.log"
echo "================================"
