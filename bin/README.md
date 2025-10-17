# Diagnostic and Testing Tools

This directory contains scripts to help diagnose and test the Vietlott API crawler.

## Scripts

### 1. `diagnose_api.py`
**Purpose**: Analyze and display the current API configuration for all products.

**Usage**:
```bash
python bin/diagnose_api.py
```

**What it does**:
- Shows the URL, headers, body structure, and cookies for each product
- Compares power_655 configuration with the expected format from the working curl command
- Identifies missing headers or mismatched values
- Helps verify that the implementation matches API requirements

**When to use**:
- Before running crawlers to verify configuration
- When debugging API issues
- After making configuration changes

### 2. `test_api_calls.sh`
**Purpose**: Test all products with DEBUG logging enabled.

**Usage**:
```bash
bash bin/test_api_calls.sh
```

**What it does**:
- Runs each product crawler (keno, power_655, power_645, power_535, 3d, 3d_pro, bingo18)
- Uses DEBUG log level to show detailed request/response information
- Saves logs to `/tmp/*_test.log` for analysis
- Tests with minimal page ranges (1 page each) for quick validation

**When to use**:
- When testing API changes
- To verify all products work correctly
- To collect debug logs for troubleshooting

### 3. `compare_with_curl.sh`
**Purpose**: Compare our implementation with the working curl command.

**Usage**:
```bash
bash bin/compare_with_curl.sh
```

**What it does**:
- Executes the known-working curl command for power_655
- Saves the response to `/tmp/curl_response.json`
- Provides instructions for running our implementation
- Lists key comparison points to verify

**When to use**:
- When curl works but our implementation doesn't
- To compare responses and identify differences
- To verify that both produce the same results

### 4. `github_data.sh`
**Purpose**: Main data collection script used by GitHub Actions.

**Usage**:
```bash
bash bin/github_data.sh
```

**What it does**:
- Crawls all products
- Fills in missing data
- Renders the README with updated statistics
- Commits and pushes changes to GitHub

**When to use**:
- Automated daily runs (via GitHub Actions)
- Manual data updates
- Testing the complete data pipeline

## Debug Logging

All crawlers support DEBUG logging to show detailed information about API requests and responses.

**Enable DEBUG logging**:
```bash
export LOGURU_LEVEL="DEBUG"
```

**What DEBUG logs show**:
- Request URL
- Request headers (including cookies and tokens)
- Request body (truncated to 500 chars)
- Request params
- Response status code
- Response headers
- Response text (truncated to 500 chars)

## Troubleshooting Workflow

1. **Configuration Check**:
   ```bash
   python bin/diagnose_api.py
   ```
   Verify that headers, body, and cookies are correct.

2. **Test Single Product**:
   ```bash
   export LOGURU_LEVEL="DEBUG"
   python src/vietlott/cli/crawl.py power_655 --index_from 1 --index_to 1
   ```
   Check logs for errors or unexpected responses.

3. **Compare with Working Curl**:
   ```bash
   bash bin/compare_with_curl.sh
   ```
   Verify our request matches the working curl command.

4. **Test All Products**:
   ```bash
   bash bin/test_api_calls.sh
   ```
   Check which products work and which fail.

5. **Review Logs**:
   ```bash
   cat /tmp/power_655_test.log | grep -A 10 "error\|Error\|ERROR"
   ```
   Look for error messages and API responses.

## Common Issues and Solutions

### Issue: "Failed to resolve 'vietlott.vn'"
**Cause**: No network access to vietlott.vn
**Solution**: Run from a system with internet access

### Issue: Response status 400/401/403
**Cause**: Missing or incorrect authentication
**Solution**: 
- Check cookies are being fetched correctly
- Verify X-csrftoken and X-Ajax-Token headers are present
- Update Key value if needed

### Issue: Response status 200 but no data
**Cause**: Incorrect Key value or body structure
**Solution**:
- Use browser dev tools to capture a working request
- Compare the Key value with what we're sending
- Verify body structure matches

### Issue: Empty response or timeout
**Cause**: API rate limiting or service down
**Solution**:
- Add delays between requests
- Check vietlott.vn is accessible
- Try again later

## Finding Correct Key Values

To find the correct Key value for a Power product:

1. Open browser (Chrome/Firefox)
2. Open Developer Tools (F12)
3. Go to Network tab
4. Navigate to the product page (e.g., https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655)
5. Trigger a search or page load
6. Look for the AJAX request in the Network tab
7. Click on the request and view the "Request Payload"
8. Copy the "Key" value
9. Update the corresponding product file in `src/vietlott/crawler/products/`

## See Also

- `API_CHANGES_SUMMARY.md` - Details about recent API changes
- `src/vietlott/crawler/` - Crawler implementation
- `src/vietlott/config/products.py` - Product configurations
