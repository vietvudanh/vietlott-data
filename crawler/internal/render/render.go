package render

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

// Draw is one NDJSON record with normalized fields.
type Draw struct {
	Date        time.Time
	ID          string
	Result      []int
	ProcessTime string
}

func toString(v any) string {
	switch t := v.(type) {
	case nil:
		return ""
	case string:
		return t
	case float64:
		if t == float64(int64(t)) {
			return strconv.FormatInt(int64(t), 10)
		}
		return strconv.FormatFloat(t, 'f', -1, 64)
	case bool:
		if t {
			return "true"
		}
		return "false"
	default:
		return fmt.Sprint(t)
	}
}

func parseDate(v any) time.Time {
	switch t := v.(type) {
	case string:
		s := strings.TrimSpace(t)
		if d, err := time.Parse("2006-01-02", s); err == nil {
			return d
		}
		if len(s) >= 10 {
			if d, err := time.Parse("2006-01-02", s[:10]); err == nil {
				return d
			}
		}
		return time.Time{}
	case float64:
		return epochDate(t)
	default:
		return time.Time{}
	}
}

func epochDate(f float64) time.Time {
	if f > 1_000_000_000_000 {
		return time.UnixMicro(int64(f)).UTC()
	}
	return time.Unix(int64(f), 0).UTC()
}

// LoadDraws reads an NDJSON file and returns draws sorted by date
// descending, then ID descending (lexicographic, matching Polars string
// sort in the Python renderer).
func LoadDraws(path string) ([]Draw, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	var draws []Draw
	sc := bufio.NewScanner(f)
	sc.Buffer(make([]byte, 1<<20), 1<<20)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}
		var raw map[string]any
		if err := json.Unmarshal([]byte(line), &raw); err != nil {
			return nil, fmt.Errorf("parse %s: %w", path, err)
		}
		d := Draw{}
		if v, ok := raw["date"]; ok {
			d.Date = parseDate(v)
		}
		if v, ok := raw["id"]; ok {
			d.ID = toString(v)
		}
		if v, ok := raw["result"]; ok {
			if arr, ok := v.([]any); ok {
				for _, e := range arr {
					if f, ok := e.(float64); ok {
						d.Result = append(d.Result, int(f))
					}
				}
			}
		}
		if v, ok := raw["process_time"]; ok {
			d.ProcessTime = toString(v)
		}
		draws = append(draws, d)
	}
	if err := sc.Err(); err != nil {
		return nil, err
	}
	sort.Slice(draws, func(i, j int) bool {
		if !draws[i].Date.Equal(draws[j].Date) {
			return draws[i].Date.After(draws[j].Date)
		}
		return draws[i].ID > draws[j].ID
	})
	return draws, nil
}

// formatDate renders a date as YYYY-MM-DD, or "" for missing dates.
func formatDate(t time.Time) string {
	if t.IsZero() {
		return ""
	}
	return t.Format("2006-01-02")
}
