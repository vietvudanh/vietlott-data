package client

import (
	"context"
	"encoding/json"
	"fmt"
	"html"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/PuerkitoBio/goquery"
	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
)

// ProductAdapter retrieves pages of draws for one product. The Vietlott
// AJAX endpoints only serve newest-first result pages; they do not support
// fetching an individual draw by identifier.
type ProductAdapter interface {
	Latest(context.Context) (int, error)
	FetchPage(context.Context, int) ([]model.Draw, error)
}

type productAdapter struct {
	c       *Client
	product model.Product
}

var layouts = map[model.ProductName]struct{ gameID, key string }{
	model.Power655: {"655", "23bbd667"}, model.Power645: {"645", "8290fce2"}, model.Power535: {"535", "d0ea794f"},
	model.Keno: {"6", ""}, model.Bingo18: {"8", ""}, model.Max3D: {"5", ""}, model.Max3DPro: {"7", ""},
}

// Products returns adapters for all supported products.
func (c *Client) Products() map[model.ProductName]ProductAdapter {
	out := map[model.ProductName]ProductAdapter{}
	for _, name := range []model.ProductName{model.Power655, model.Power645, model.Power535, model.Keno, model.Bingo18, model.Max3D, model.Max3DPro} {
		product, _ := model.Lookup(string(name))
		out[name] = &productAdapter{c: c, product: product}
	}

	return out
}

// NewProductAdapter creates an adapter for a named product.
func NewProductAdapter(c *Client, name model.ProductName) (ProductAdapter, error) {
	if c == nil {
		c = NewClient()
	}
	product, err := model.Lookup(string(name))
	if err != nil {
		return nil, err
	}
	if _, ok := layouts[name]; !ok {
		return nil, fmt.Errorf("unsupported product %q", name)
	}
	return &productAdapter{c: c, product: product}, nil
}

func (a *productAdapter) Latest(ctx context.Context) (int, error) {
	draws, err := a.FetchPage(ctx, 0)
	if err != nil {
		return 0, err
	}
	if len(draws) == 0 {
		return 0, fmt.Errorf("%s latest: no result rows", a.product.Name)
	}
	max := 0
	for _, draw := range draws {
		id, e := model.NormalizeID(draw.GetID())
		if e != nil {
			return 0, fmt.Errorf("%s latest: %w", a.product.Name, e)
		}
		if id.Number > max {
			max = id.Number
		}
	}
	return max, nil
}

// FetchPage returns the parsed draws from one newest-first result page.
// Page 0 holds the most recent draws, matching the Python crawler which
// crawls PageIndex values from 0 upward with an empty draw identifier.
func (a *productAdapter) FetchPage(ctx context.Context, page int) ([]model.Draw, error) {
	l := layouts[a.product.Name]
	body := requestBody(a.product.Name, l, page)
	raw, err := a.c.post(ctx, a.product.Endpoint, body)
	if err != nil {
		return nil, fmt.Errorf("%s page %d: %w", a.product.Name, page, err)
	}
	var envelope struct {
		Value json.RawMessage `json:"value"`
		Error bool            `json:"Error"`
	}
	if err := json.Unmarshal([]byte(raw), &envelope); err != nil {
		return nil, fmt.Errorf("%s response JSON: %w", a.product.Name, err)
	}
	if envelope.Error {
		return nil, fmt.Errorf("%s page %d: AJAX response reported Error=true", a.product.Name, page)
	}
	var value struct {
		HtmlContent string `json:"HtmlContent"`
		Error       bool   `json:"Error"`
		InfoMessage string `json:"InfoMessage"`
	}
	if err := json.Unmarshal(envelope.Value, &value); err != nil {
		if err2 := json.Unmarshal(envelope.Value, &value.HtmlContent); err2 != nil {
			return nil, fmt.Errorf("%s response value: %w", a.product.Name, err)
		}
	}
	if value.Error {
		message := strings.TrimSpace(value.InfoMessage)
		if message == "" {
			message = "AJAX response reported Error=true"
		}
		return nil, fmt.Errorf("%s page %d: %s", a.product.Name, page, message)
	}
	if value.HtmlContent == "" {
		return nil, fmt.Errorf("%s response has no HTML content", a.product.Name)
	}
	draws, err := parseHTML(a.product.Name, value.HtmlContent)
	if err != nil {
		return nil, fmt.Errorf("%s parse: %w", a.product.Name, err)
	}
	return draws, nil
}

// requestBody builds a page-listing request with an empty draw identifier,
// mirroring the Python product org_body payloads. Page 0 is the newest page.
func requestBody(name model.ProductName, l struct{ gameID, key string }, page int) map[string]any {
	ri := map[string]any{"SiteId": "main.frontend.vi", "SiteAlias": "main.vi", "UserSessionId": "", "SiteLang": "vi", "IsPageDesign": false, "ExtraParam1": "", "ExtraParam2": "", "ExtraParam3": "", "SiteURL": "", "WebPage": nil, "SiteName": "Vietlott", "OrgPageAlias": nil, "PageAlias": nil, "RefKey": nil, "FullPageAlias": nil}
	switch name {
	case model.Power655, model.Power645, model.Power535:
		rows := 5
		cols := 18
		if name == model.Power645 {
			rows = 6
		}
		if name == model.Power535 {
			// The live 5/35 endpoint indexes the search grid as 35 columns,
			// matching the Python RequestPower535 ArrayNumbers dimensions.
			cols = 35
		}
		arr := make([][]string, rows)
		for i := range arr {
			arr[i] = make([]string, cols)
		}
		return map[string]any{"ORenderInfo": ri, "Key": l.key, "GameDrawId": "", "ArrayNumbers": arr, "CheckMulti": false, "PageIndex": page}
	case model.Keno:
		return map[string]any{"DrawDate": "", "GameDrawNo": "", "GameId": l.gameID, "ORenderInfo": ri, "OddEven": 2, "PageIndex": page, "ProcessType": 0, "TotalRow": 112453, "UpperLower": 2, "number": ""}
	case model.Bingo18:
		return map[string]any{"ORenderInfo": ri, "GameId": l.gameID, "GameDrawNo": "", "number": "", "DrawDate": "", "PageIndex": page, "TotalRow": 43569}
	case model.Max3D, model.Max3DPro:
		return map[string]any{"CheckMulti": 0, "GameDrawId": "", "GameId": l.gameID, "ORenderInfo": ri, "PageIndex": page, "number01": "123", "number02": "321"}
	}
	return nil
}

func text(s *goquery.Selection) string { return strings.TrimSpace(html.UnescapeString(s.Text())) }

var dateRE = regexp.MustCompile(`(\d{1,2})/(\d{1,2})/(\d{4})`)

func parseDate(s string) (string, error) {
	m := dateRE.FindStringSubmatch(s)
	if m == nil {
		return "", fmt.Errorf("invalid date %q", s)
	}
	t, err := time.Parse("2/1/2006", fmt.Sprintf("%s/%s/%s", m[1], m[2], m[3]))
	if err != nil {
		return "", err
	}
	return t.Format("2006-01-02"), nil
}
func ints(s *goquery.Selection) []int {
	out := []int{}
	s.Find("span").Each(func(_ int, x *goquery.Selection) {
		n, e := strconv.Atoi(strings.TrimSpace(x.Text()))
		if e == nil {
			out = append(out, n)
		}
	})
	return out
}
func parseHTML(name model.ProductName, content string) ([]model.Draw, error) {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(content))
	if err != nil {
		return nil, err
	}
	var out []model.Draw
	doc.Find("table tr").EachWithBreak(func(i int, tr *goquery.Selection) bool {
		if i == 0 {
			return true
		}
		cells := tr.Find("td")
		if cells.Length() < 1 {
			return true
		}
		id, date := "", ""
		tr.Find("*").Each(func(_ int, x *goquery.Selection) {
			if date == "" {
				if d, e := parseDate(text(x)); e == nil {
					date = d
				}
			}
		})
		cells.First().Find("a").Each(func(_ int, x *goquery.Selection) {
			v := text(x)
			if date == "" {
				if d, e := parseDate(v); e == nil {
					date = d
				}
			}
			if id == "" && v != "" {
				if _, e := parseDate(v); e != nil {
					id = strings.TrimSpace(strings.TrimPrefix(v, "#"))
				}
			}
		})
		if date == "" {
			date, _ = parseDate(text(cells.Eq(0)))
		}
		if id == "" {
			id = text(cells.Eq(1))
		}
		if date == "" || id == "" {
			return true
		}
		switch name {
		case model.Max3D, model.Max3DPro:
			m := map[string][]string{}
			var vals []string
			result := tr.Find("div.tong_day_so_ket_qua")
			if result.Length() == 0 {
				result = cells.Last()
			}
			result.Find("span").Each(func(_ int, x *goquery.Selection) {
				v := strings.TrimSpace(x.Text())
				if v != "" {
					vals = append(vals, v)
				}
			})
			if len(vals) == 0 {
				return true
			}
			prizes := []struct {
				name  string
				count int
			}{
				{"Giải Đặc biệt", 6}, {"Giải Nhất", 12}, {"Giải Nhì", 18}, {"Giải ba", 24},
			}
			pos := 0
			for _, prize := range prizes {
				for j := 0; j+2 < prize.count && pos+2 < len(vals); j += 3 {
					m[prize.name] = append(m[prize.name], vals[pos]+vals[pos+1]+vals[pos+2])
					pos += 3
				}
			}
			if len(m) == 0 {
				return true
			}
			total := 0
			for _, values := range m {
				total += len(values)
			}
			if total != 20 {
				return true
			}
			out = appendDraw(out, name, date, id, map[string]any{"result": m})
			return true
		case model.Keno:
			if cells.Length() < 4 {
				return true
			}
			r := ints(cells.Eq(1))
			if len(r) != 20 {
				return true
			}
			out = appendDraw(out, name, date, "#"+id, map[string]any{"result": r, "big_small": text(cells.Eq(2)), "odd_even": text(cells.Eq(3))})
		case model.Bingo18:
			if cells.Length() < 4 {
				return true
			}
			r := ints(cells.Eq(1))
			if len(r) != 3 {
				return true
			}
			total, e := strconv.Atoi(text(cells.Eq(2)))
			if e != nil {
				return true
			}
			out = appendDraw(out, name, date, id, map[string]any{"result": r, "total": total, "large_small": text(cells.Eq(3)), "process_time": time.Now().Format(time.RFC3339)})
		default:
			if cells.Length() < 3 {
				return true
			}
			r := ints(cells.Eq(2))
			expected := 6
			if name == model.Power655 {
				expected = 7
			}
			if len(r) != expected {
				return true
			}
			out = appendDraw(out, name, date, id, map[string]any{"result": r, "process_time": time.Now().Format(time.RFC3339)})
		}
		return true
	})
	return out, nil
}

func appendDraw(out []model.Draw, name model.ProductName, date, id string, fields map[string]any) []model.Draw {
	fields["date"], fields["id"] = date, id
	raw, err := json.Marshal(fields)
	if err != nil {
		return out
	}
	draw, err := model.DecodeDraw(name, raw)
	if err == nil {
		out = append(out, draw)
	}
	return out
}
