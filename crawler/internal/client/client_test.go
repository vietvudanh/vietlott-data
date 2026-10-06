package client

import (
	"context"
	"io"
	"net/http"
	"strings"
	"sync/atomic"
	"testing"
)

func TestClientRetriesAndSetsVietlottHeaders(t *testing.T) {
	var calls atomic.Int32
	h := &http.Client{Transport: roundTripFunc(func(r *http.Request) (*http.Response, error) {
		if r.Header.Get("X-AjaxPro-Method") != "ServerSideDrawResult" || r.Header.Get("User-Agent") == "" {
			t.Errorf("missing Vietlott headers: %v", r.Header)
		}
		n := calls.Add(1)
		status, body := http.StatusServiceUnavailable, `down`
		if n == 3 {
			status, body = http.StatusOK, `ok`
		}
		return &http.Response{StatusCode: status, Body: io.NopCloser(strings.NewReader(body)), Header: make(http.Header)}, nil
	})}
	got, err := NewClientWithHTTPClient(h).post(context.Background(), "http://example.test", map[string]string{"x": "y"})
	if err != nil || got != "ok" || calls.Load() != 3 {
		t.Fatalf("got %q, %v after %d calls", got, err, calls.Load())
	}
}

func TestExportedPostJSONWrapper(t *testing.T) {
	h := &http.Client{Transport: roundTripFunc(func(r *http.Request) (*http.Response, error) {
		body, _ := io.ReadAll(r.Body)
		if string(body) != `{"ok":true}` {
			t.Errorf("request body = %q", body)
		}

		return &http.Response{StatusCode: http.StatusOK, Body: io.NopCloser(strings.NewReader(`{"value":"ok"}`)), Header: make(http.Header)}, nil
	})}
	got, err := New(h).PostJSON(context.Background(), "http://example.test", []byte(`{"ok":true}`))
	if err != nil || string(got) != `{"value":"ok"}` {
		t.Fatalf("PostJSON = %q, %v", got, err)
	}

}

func TestPermanentHTTPErrorIsNotRetried(t *testing.T) {
	var calls atomic.Int32
	h := &http.Client{Transport: roundTripFunc(func(*http.Request) (*http.Response, error) {
		calls.Add(1)
		return &http.Response{StatusCode: http.StatusBadRequest, Body: io.NopCloser(strings.NewReader("bad request")), Header: make(http.Header)}, nil
	})}
	_, err := New(h).PostJSON(context.Background(), "http://example.test", []byte(`{}`))
	if err == nil || calls.Load() != 1 {
		t.Fatalf("expected one permanent-error request, calls=%d err=%v", calls.Load(), err)
	}
}

type roundTripFunc func(*http.Request) (*http.Response, error)

func (f roundTripFunc) RoundTrip(r *http.Request) (*http.Response, error) { return f(r) }
