package client

import (
	"context"
	"encoding/json"
	"io"
	"net/http"
	"strconv"
	"strings"
	"testing"

	"github.com/vietvudanh/vietlott-data/crawler/internal/model"
)

func TestPower535RequestBodyUsesSchemaDimensions(t *testing.T) {
	body := requestBody(model.Power535, layouts[model.Power535], 0)
	arr := body["ArrayNumbers"].([][]string)
	if len(arr) != 5 || len(arr[0]) != 35 {
		t.Fatalf("dimensions = %dx%d, want 5x35", len(arr), len(arr[0]))
	}
	if body["GameDrawId"] != "" {
		t.Fatalf("GameDrawId = %#v, want empty page-listing identifier", body["GameDrawId"])
	}
}

func TestAllProductAdaptersSendPageListingRequests(t *testing.T) {
	fixtures := map[model.ProductName]string{
		model.Power655: `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>42</td><td>` + strings.Repeat("<span>1</span>", 7) + `</td></tr></table>`,
		model.Power645: `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>42</td><td>` + strings.Repeat("<span>1</span>", 6) + `</td></tr></table>`,
		model.Power535: `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>42</td><td>` + strings.Repeat("<span>1</span>", 6) + `</td></tr></table>`,
		model.Keno:     `<table><tr><th>x</th></tr><tr><td><a>01/02/2024</a><a>#42</a></td><td>` + strings.Repeat("<span>1</span>", 20) + `</td><td>Big</td><td>Odd</td></tr></table>`,
		model.Bingo18:  `<table><tr><th>x</th></tr><tr><td><a>01/02/2024</a><a>42</a></td><td><span>1</span><span>2</span><span>3</span></td><td>6</td><td>Small</td></tr></table>`,
		model.Max3D:    `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>42</td><td><div class="tong_day_so_ket_qua">` + strings.Repeat(`<span>1</span>`, 60) + `</div></td></tr></table>`,
		model.Max3DPro: `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>42</td><td><div class="tong_day_so_ket_qua">` + strings.Repeat(`<span>1</span>`, 60) + `</div></td></tr></table>`,
	}
	for _, name := range []model.ProductName{model.Power655, model.Power645, model.Power535, model.Keno, model.Bingo18, model.Max3D, model.Max3DPro} {
		var got map[string]any
		h := &http.Client{Transport: roundTripFunc(func(r *http.Request) (*http.Response, error) {
			data, _ := io.ReadAll(r.Body)
			_ = json.Unmarshal(data, &got)
			return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"value":{"HtmlContent":` + strconv.Quote(fixtures[name]) + `}}`)), Header: make(http.Header)}, nil
		})}
		adapter, _ := NewProductAdapter(NewClientWithHTTPClient(h), name)
		draws, err := adapter.FetchPage(context.Background(), 2)
		if err != nil {
			t.Fatalf("%s FetchPage: %v", name, err)
		}
		if len(draws) == 0 {
			t.Fatalf("%s FetchPage returned no draws", name)
		}
		if got["PageIndex"] != float64(2) {
			t.Fatalf("%s PageIndex = %#v, want 2", name, got["PageIndex"])
		}
		for _, field := range []string{"GameDrawId", "GameDrawNo"} {
			if value, ok := got[field]; ok && value != "" {
				t.Fatalf("%s %s = %#v, want empty page-listing identifier", name, field, value)
			}
		}
	}
}

func TestParseNumberProduct(t *testing.T) {
	html := `<table><tr><th>Date</th></tr><tr><td>01/02/2024</td><td>123</td><td><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span></td></tr></table>`
	draws, err := parseHTML(model.Power655, html)
	if err != nil || len(draws) != 1 || draws[0].GetDate() != "2024-02-01" {
		t.Fatalf("unexpected parse: %v %#v", err, draws)
	}
}

func TestParseAllProductLayouts(t *testing.T) {
	number := `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>123</td><td><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span></td></tr></table>`
	if draws, err := parseHTML(model.Power655, number); err != nil || len(draws) != 1 {
		t.Fatalf("655: %v", err)
	}
	six := strings.Replace(number, "<span>7</span>", "", 1)
	if draws, err := parseHTML(model.Power645, six); err != nil || len(draws) != 1 {
		t.Fatalf("645: %v", err)
	}
	if draws, err := parseHTML(model.Power535, six); err != nil || len(draws) != 1 {
		t.Fatalf("535: %v", err)
	}
	keno := `<table><tr><th>x</th></tr><tr><td><a>01/02/2024</a><a>#7</a></td><td>` + strings.Repeat("<span>1</span>", 20) + `</td><td>Big</td><td>Odd</td></tr></table>`
	if draws, err := parseHTML(model.Keno, keno); err != nil || len(draws) != 1 || draws[0].GetID() != "#7" {
		t.Fatalf("keno: %v", err)
	}
	bingo := `<table><tr><th>x</th></tr><tr><td><a>01/02/2024</a><a>8</a></td><td><span>1</span><span>2</span><span>3</span></td><td>6</td><td>Small</td></tr></table>`
	if draws, err := parseHTML(model.Bingo18, bingo); err != nil || len(draws) != 1 {
		t.Fatalf("bingo: %v", err)
	}
	for _, name := range []model.ProductName{model.Max3D, model.Max3DPro} {
		if _, err := NewProductAdapter(nil, name); err != nil {
			t.Fatalf("%s: %v", name, err)
		}
	}
}

func TestMax3DSkipsMalformedRowAndParsesFollowingRow(t *testing.T) {
	valid := strings.Repeat(`<span class="bong_tron">1</span>`, 60)
	html := `<table><tr><th>x</th></tr>` +
		`<tr><td>01/02/2024</td><td>8</td><td><span class="bong_tron">1</span></td></tr>` +
		`<tr><td>02/02/2024</td><td>9</td><td>` + valid + `</td></tr></table>`
	draws, err := parseHTML(model.Max3D, html)
	if err != nil || len(draws) != 1 || draws[0].GetID() != "9" {
		t.Fatalf("draws = %#v, err = %v", draws, err)
	}
}

func TestBingo18SkipsMalformedTotalAndParsesFollowingRow(t *testing.T) {
	row := func(date, id, total string) string {
		return `<tr><td><a>` + date + `</a><a>` + id + `</a></td><td><span>1</span><span>2</span><span>3</span></td><td>` + total + `</td><td>Small</td></tr>`
	}
	html := `<table><tr><th>x</th></tr>` + row("01/02/2024", "8", "invalid") + row("02/02/2024", "9", "6") + `</table>`
	draws, err := parseHTML(model.Bingo18, html)
	if err != nil || len(draws) != 1 || draws[0].GetID() != "9" {
		t.Fatalf("draws = %#v, err = %v", draws, err)
	}
}

func TestLatestReturnsMaximumID(t *testing.T) {
	html := `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>3</td><td>` + strings.Repeat("<span>1</span>", 7) + `</td></tr><tr><td>02/02/2024</td><td>9</td><td>` + strings.Repeat("<span>1</span>", 7) + `</td></tr></table>`
	h := &http.Client{Transport: roundTripFunc(func(*http.Request) (*http.Response, error) {
		return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"value":{"HtmlContent":` + strconv.Quote(html) + `}}`)), Header: make(http.Header)}, nil
	})}
	a, _ := NewProductAdapter(NewClientWithHTTPClient(h), model.Power655)
	if got, err := a.Latest(context.Background()); err != nil || got != 9 {
		t.Fatalf("latest = %d, %v", got, err)
	}
}

func TestLatestUsesFirstPageDiscoveryRequest(t *testing.T) {
	var request map[string]any
	html := `<table><tr><th>x</th></tr><tr><td>01/02/2024</td><td>9</td><td>` + strings.Repeat("<span>1</span>", 7) + `</td></tr></table>`
	h := &http.Client{Transport: roundTripFunc(func(r *http.Request) (*http.Response, error) {
		body, _ := io.ReadAll(r.Body)
		_ = json.Unmarshal(body, &request)
		return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"Error":false,"value":{"HtmlContent":` + strconv.Quote(html) + `}}`)), Header: make(http.Header)}, nil
	})}
	a, _ := NewProductAdapter(NewClientWithHTTPClient(h), model.Power655)
	if _, err := a.Latest(context.Background()); err != nil {
		t.Fatal(err)
	}
	if request["PageIndex"] != float64(0) || request["GameDrawId"] != "" {
		t.Fatalf("latest request = %#v", request)
	}
}

func TestPageRequestsUseGivenPageWithEmptyIdentifier(t *testing.T) {
	for _, name := range []model.ProductName{model.Power655, model.Power645, model.Power535, model.Keno, model.Bingo18, model.Max3D, model.Max3DPro} {
		body := requestBody(name, layouts[name], 2)
		if body["PageIndex"] != 2 {
			t.Fatalf("%s page = %#v, want 2", name, body["PageIndex"])
		}
		for _, field := range []string{"GameDrawId", "GameDrawNo"} {
			if value, ok := body[field]; ok && value != "" {
				t.Fatalf("%s %s = %#v, want empty page-listing identifier", name, field, value)
			}
		}
	}
}

func TestLatestPropagatesAJAXError(t *testing.T) {
	h := &http.Client{Transport: roundTripFunc(func(*http.Request) (*http.Response, error) {
		return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"Error":true,"value":{}}`)), Header: make(http.Header)}, nil
	})}
	a, _ := NewProductAdapter(NewClientWithHTTPClient(h), model.Power655)
	if _, err := a.Latest(context.Background()); err == nil || !strings.Contains(err.Error(), "Error=true") {
		t.Fatalf("expected contextual AJAX error, got %v", err)
	}
}

func TestFetchPagePropagatesInnerAJAXError(t *testing.T) {
	h := &http.Client{Transport: roundTripFunc(func(*http.Request) (*http.Response, error) {
		return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"value":{"HtmlContent":"Index was outside the bounds of the array.","InfoMessage":"Index was outside the bounds of the array.","Error":true}}`)), Header: make(http.Header)}, nil
	})}
	a, _ := NewProductAdapter(NewClientWithHTTPClient(h), model.Power535)
	_, err := a.FetchPage(context.Background(), 0)
	if err == nil || !strings.Contains(err.Error(), "Index was outside the bounds") {
		t.Fatalf("expected inner AJAX error message, got %v", err)
	}
}

func TestFetchPageReturnsEmptySliceWhenNoRows(t *testing.T) {
	h := &http.Client{Transport: roundTripFunc(func(*http.Request) (*http.Response, error) {
		return &http.Response{StatusCode: 200, Body: io.NopCloser(strings.NewReader(`{"value":{"HtmlContent":"<table><tr><th>x</th></tr></table>"}}`)), Header: make(http.Header)}, nil
	})}
	a, _ := NewProductAdapter(NewClientWithHTTPClient(h), model.Power655)
	draws, err := a.FetchPage(context.Background(), 9)
	if err != nil || len(draws) != 0 {
		t.Fatalf("draws = %#v, err = %v, want empty page without error", draws, err)
	}
}
