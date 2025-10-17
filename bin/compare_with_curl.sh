#!/usr/bin/env bash
# Script to compare our API calls with the working curl command
# This helps verify that our implementation matches the expected format

echo "================================"
echo "Comparing API Implementation"
echo "================================"
echo ""

# First, test the actual curl command provided
echo "1. Testing the provided curl command for power_655..."
echo "   (This should work if run from a system with access to vietlott.vn)"
echo ""

curl 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx' \
  --compressed \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Content-Type: text/plain; charset=utf-8' \
  -H 'X-AjaxPro-Method: ServerSideDrawResult' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Origin: https://vietlott.vn' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-655' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'TE: trailers' \
  --data-raw '{"ORenderInfo":{"SiteId":"main.frontend.vi","SiteAlias":"main.vi","UserSessionId":"","SiteLang":"vi","IsPageDesign":false,"ExtraParam1":"","ExtraParam2":"","ExtraParam3":"","SiteURL":"","WebPage":null,"SiteName":"Vietlott","OrgPageAlias":null,"PageAlias":null,"FullPageAlias":null,"RefKey":null,"System":1},"Key":"5a0fff20","GameDrawId":"","ArrayNumbers":[["","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","",""]],"CheckMulti":false,"PageIndex":1}' \
  -o /tmp/curl_response.json

echo ""
echo "Curl response saved to /tmp/curl_response.json"
echo ""

# Now run our implementation
echo "2. Testing our Python implementation..."
echo "   Run this to see what our code sends:"
echo ""
echo "   LOGURU_LEVEL=DEBUG python src/vietlott/cli/crawl.py power_655 --index_from 1 --index_to 1"
echo ""

# Show comparison points
echo "================================"
echo "Key Comparison Points"
echo "================================"
echo ""
echo "Expected (from curl):"
echo "  - URL: https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx"
echo "  - Key: 5a0fff20"
echo "  - Headers: X-AjaxPro-Method, X-Requested-With, X-csrftoken, X-Ajax-Token"
echo "  - Cookies: session-cookie, csrf-token-name, csrf-token-value"
echo "  - System: 1 (in ORenderInfo)"
echo ""
echo "To verify our implementation:"
echo "  1. Check the debug logs show the correct URL"
echo "  2. Verify Key is '5a0fff20' in the body"
echo "  3. Check X-csrftoken header is present"
echo "  4. Check X-Ajax-Token header is present"  
echo "  5. Check cookies are being sent"
echo "  6. Compare the response with /tmp/curl_response.json"
echo ""
echo "If responses differ:"
echo "  - Compare headers carefully"
echo "  - Check if Key value needs updating"
echo "  - Verify ORenderInfo structure matches"
echo "  - Check ArrayNumbers structure"
echo ""
