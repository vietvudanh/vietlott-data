# Quick Start Guide: Testing API Changes

## TL;DR - What Changed?
The Vietlott API now requires:
1. Session cookies from vietlott.vn
2. CSRF token in X-csrftoken header
3. Ajax token in X-Ajax-Token header
4. Updated Key value for power_655: `5a0fff20`

## Quick Test (2 minutes)

### 1. Verify Configuration
```bash
python bin/diagnose_api.py | grep -A 5 "power_655"
```
✅ Should show Key: "5a0fff20"

### 2. Test One Product
```bash
export LOGURU_LEVEL="DEBUG"
python src/vietlott/cli/crawl.py power_655 --index_from 1 --index_to 1 2>&1 | tee /tmp/test.log
```
✅ Should show cookies, tokens, and successful responses

### 3. Check Logs
```bash
# Check cookies were fetched
grep "Initial cookies" /tmp/test.log

# Check tokens were added
grep "X-csrftoken\|X-Ajax-Token" /tmp/test.log

# Check response status
grep "Response status" /tmp/test.log
```
✅ Should show status 200

## If It Works
Great! Run for all products:
```bash
bash bin/test_api_calls.sh
```

## If It Doesn't Work

### Error: No cookies found
**Fix**: Check internet access to vietlott.vn

### Error: Response 401/403
**Fix**: Verify CSRF token is extracted:
```bash
python bin/diagnose_api.py | grep csrf
```

### Error: Response 400
**Fix**: Key value may be wrong. Use browser dev tools:
1. Open https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655
2. F12 → Network tab
3. Search → Look for the Key in request payload
4. Update in `src/vietlott/crawler/products/power655.py`

## Full Documentation
- `IMPLEMENTATION_SUMMARY.md` - Complete technical details
- `API_CHANGES_SUMMARY.md` - API changes explained
- `bin/README.md` - Diagnostic tools guide

## Support
1. Check debug logs: `export LOGURU_LEVEL="DEBUG"`
2. Compare with curl: `bash bin/compare_with_curl.sh`
3. Review documentation in this directory
