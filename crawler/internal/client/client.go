package client

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
	"sync"
	"time"
)

const (
	requestTimeout = 10 * time.Second
	maxAttempts    = 3
)

var vietlottHeaders = map[string]string{
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
	"Accept":     "*/*", "Accept-Language": "en-US,en;q=0.5",
	"Content-Type": "text/plain; charset=utf-8", "X-AjaxPro-Method": "ServerSideDrawResult",
	"X-Requested-With": "XMLHttpRequest", "Origin": "https://vietlott.vn",
	"Connection": "keep-alive", "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-645",
	"Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
}

// Client is the shared HTTP client used by all product adapters.
type Client struct {
	http   *http.Client
	mu     sync.Mutex
	recent []time.Time
}

// NewClient creates a client with a persistent transport and a ten second timeout.
func NewClient() *Client {
	return NewClientWithHTTPClient(&http.Client{Timeout: requestTimeout, Transport: http.DefaultTransport})
}

// NewClientWithHTTPClient is useful for tests and callers with a custom transport.
func NewClientWithHTTPClient(h *http.Client) *Client {
	if h == nil {
		h = &http.Client{}
	}

	if h.Timeout == 0 {
		h.Timeout = requestTimeout
	}
	if h.Transport == nil {
		h.Transport = http.DefaultTransport
	}
	return &Client{http: h}
}

// New creates a client using h, or the default HTTP transport when h is nil.
func New(h *http.Client) *Client { return NewClientWithHTTPClient(h) }

// PostJSON sends a JSON request body with the shared retry, header, and rate-limit policy.
func (c *Client) PostJSON(ctx context.Context, endpoint string, body []byte) ([]byte, error) {
	return c.postBytes(ctx, endpoint, body)
}

func (c *Client) wait(ctx context.Context) error {
	for {
		c.mu.Lock()
		now := time.Now()
		i := 0
		for i < len(c.recent) && now.Sub(c.recent[i]) >= time.Second {
			i++
		}
		c.recent = c.recent[i:]
		if len(c.recent) < 5 {
			c.recent = append(c.recent, now)
			c.mu.Unlock()
			return nil
		}
		delay := time.Until(c.recent[0].Add(time.Second))
		c.mu.Unlock()
		timer := time.NewTimer(delay)
		select {
		case <-ctx.Done():
			timer.Stop()
			return ctx.Err()
		case <-timer.C:
		}
	}
}

func (c *Client) post(ctx context.Context, endpoint string, body any) (string, error) {
	data, err := json.Marshal(body)
	if err != nil {
		return "", fmt.Errorf("marshal request: %w", err)
	}
	raw, err := c.postBytes(ctx, endpoint, data)
	return string(raw), err
}

func (c *Client) postBytes(ctx context.Context, endpoint string, data []byte) ([]byte, error) {
	var last error
	for attempt := 1; attempt <= maxAttempts; attempt++ {
		if err := c.wait(ctx); err != nil {
			return nil, err
		}
		req, err := http.NewRequestWithContext(ctx, http.MethodPost, endpoint, bytes.NewReader(data))
		if err != nil {
			return nil, fmt.Errorf("create request: %w", err)
		}
		for k, v := range vietlottHeaders {
			req.Header.Set(k, v)
		}
		res, err := c.http.Do(req)
		if err == nil {
			raw, readErr := io.ReadAll(res.Body)
			res.Body.Close()
			if readErr == nil && res.StatusCode >= 200 && res.StatusCode < 300 {
				return raw, nil
			}
			if readErr != nil {
				err = readErr
			} else {
				err = fmt.Errorf("HTTP status %d: %s", res.StatusCode, strings.TrimSpace(string(raw)))
			}
			if readErr == nil && !transientStatus(res.StatusCode) {
				return nil, fmt.Errorf("request %s failed: %w", endpoint, err)
			}
		}
		last = err
		if attempt < maxAttempts {
			delay := time.Duration(1<<(attempt-1)) * 250 * time.Millisecond
			timer := time.NewTimer(delay)
			select {
			case <-ctx.Done():
				timer.Stop()
				return nil, ctx.Err()
			case <-timer.C:
			}

		}
	}
	return nil, fmt.Errorf("request %s failed after %d attempts: %w", endpoint, maxAttempts, last)
}

func transientStatus(status int) bool {
	return status == http.StatusRequestTimeout || status == http.StatusTooEarly ||
		status == http.StatusTooManyRequests || status >= 500
}
