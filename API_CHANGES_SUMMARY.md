# Vietlott API Changes Summary

## Problem
The Vietlott API has changed and now requires additional authentication headers and cookies that were not previously required. This was causing crawlers to fail.

## Changes Made

### 1. Updated power_655 Key
- **File**: `src/vietlott/crawler/products/power655.py`
- **Change**: Updated Key from `23bbd667` to `5a0fff20` (as shown in the curl example)
- This matches the current API requirement for product 655

### 2. Enhanced Debug Logging
- **File**: `src/vietlott/crawler/requests_helper/fetch.py`
- **Added**:
  - Request URL logging
  - Request headers logging
  - Request cookies logging
  - Request body logging (truncated to 500 chars)
  - Request params logging
  - Response status logging
  - Response headers logging
  - Response text logging (truncated to 500 chars)
- **Purpose**: Allow developers to see exactly what's being sent and received for debugging

### 3. Improved Cookie and Token Handling
- **File**: `src/vietlott/crawler/requests_helper/fetch.py`
- **Function**: `get_vietlott_cookie()`
- **Changes**:
  - Now fetches the main vietlott.vn page instead of /ajaxpro/
  - Extracts all cookies from response headers
  - Parses JavaScript cookies if present
  - Attempts to extract CSRF tokens from page HTML/scripts
  - Attempts to extract Ajax tokens from page HTML/scripts
  - Returns empty values gracefully if fetching fails
  - Added comprehensive debug logging

### 4. Updated BaseProduct to Use New Tokens
- **File**: `src/vietlott/crawler/products/base.py`
- **Changes**:
  - Headers are now copied (not referenced) to avoid mutation
  - Adds `X-csrftoken` header from cookies if available
  - Adds `X-Ajax-Token` header from cookies if available
  - Falls back to generating Ajax token from session+csrf if not found in page
  - Gracefully handles missing cookies

### 5. Enabled Cookies for All Products
- **File**: `src/vietlott/config/products.py`
- **Changed**: Set `use_cookies=True` for all products:
  - power_655
  - power_645
  - power_535
  - keno
  - 3d
  - 3d_pro
  - bingo18
- **Reason**: The API now requires session cookies and CSRF tokens for all endpoints

### 6. Created Diagnostic Tools
- **File**: `bin/diagnose_api.py`
  - Script to analyze and compare API request format
  - Shows what headers, body, and cookies are being used
  - Compares with expected format from curl
  - Helps identify differences
  
- **File**: `bin/test_api_calls.sh`
  - Shell script to test all products with DEBUG logging
  - Saves logs to /tmp for analysis
  - Runs minimal crawls (1 page each) for quick testing

## API Changes Detected

Based on the provided curl command, the Vietlott API now requires:

1. **Session Cookie**: `session-cookie=<value>`
2. **CSRF Token Name**: `csrf-token-name=csrftoken`
3. **CSRF Token Value**: `csrf-token-value=<value>`
4. **X-csrftoken Header**: Must match the CSRF token value from cookies
5. **X-Ajax-Token Header**: A separate token (likely derived from page or session)
6. **Updated Key Values**: Different for each product (e.g., `5a0fff20` for power_655)

## How to Test

1. **Run diagnostic script**:
   ```bash
   source .venv/bin/activate
   python bin/diagnose_api.py
   ```
   This will show the current configuration for all products.

2. **Test individual products with debug logs**:
   ```bash
   source .venv/bin/activate
   export PYTHONPATH="src"
   export LOGURU_LEVEL="DEBUG"
   python src/vietlott/cli/crawl.py power_655 --index_from 1 --index_to 1
   ```

3. **Test all products**:
   ```bash
   bash bin/test_api_calls.sh
   ```
   Logs will be saved to `/tmp/*_test.log`

## Current Key Values

Power products use a "Key" field that may need periodic updates:
- **power_655**: `5a0fff20` (updated from `23bbd667`)
- **power_645**: `785cdae0` (may need update - verify when testing)
- **power_535**: `d0ea794f` (may need update - verify when testing)

Other products use GameId instead:
- **keno**: GameId="6"
- **3d**: GameId="5"
- **3d_pro**: GameId="7"
- **bingo18**: GameId="8"

## Next Steps

When testing on a system with access to vietlott.vn:

1. Run the diagnostic script to verify cookies and tokens are extracted:
   ```bash
   python bin/diagnose_api.py
   ```

2. Run the test script for each product:
   ```bash
   bash bin/test_api_calls.sh
   ```

3. Check the debug logs to ensure:
   - Cookies are being set correctly
   - X-csrftoken header is present
   - X-Ajax-Token header is present
   - Responses are successful (status 200)

4. If any product fails:
   - Check if its Key value needs updating (for Power products)
   - Compare request format with working curl command
   - Check for any missing headers or different body structure
   - Verify the response error message for clues

5. To get the correct Key for a product:
   - Open browser developer tools (F12)
   - Navigate to the product page on vietlott.vn
   - Go to Network tab
   - Trigger a search/load
   - Look for the AJAX request and check the "Key" value in the request payload

## Notes

- The Ajax token generation is currently a fallback mechanism (SHA256 of session+csrf)
- The actual Ajax token should ideally be extracted from the page HTML/JavaScript
- If the fallback doesn't work, we may need to inspect the actual vietlott.vn page source to see how the token is generated
- All products now use cookies - this is required by the new API
