package model

import (
	"strings"
	"testing"
)

func TestLookupProductRegistry(t *testing.T) {
	tests := []struct {
		name       string
		file       string
		width      int
		prefix     string
		minID      int
		resultKind string
	}{
		{"power655", "power655.jsonl", 5, "", 1, "number"},
		{"power645", "power645.jsonl", 5, "", 198, "number"},
		{"power535", "power535.jsonl", 5, "", 1, "number"},
		{"keno", "keno.jsonl", 7, "#", 110271, "keno"},
		{"bingo18", "bingo18.jsonl", 7, "", 83123, "bingo18"},
		{"3d", "3d.jsonl", 5, "", 1, "3d"},
		{"3d_pro", "3d_pro.jsonl", 5, "", 1, "3d"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p, err := Lookup(tt.name)
			if err != nil {
				t.Fatalf("Lookup() error = %v", err)
			}
			if p.Name != ProductName(tt.name) || p.FileName != tt.file || p.IDWidth != tt.width || p.IDPrefix != tt.prefix || p.MinID != tt.minID || p.ResultKind != tt.resultKind {
				t.Fatalf("unexpected product: %#v", p)
			}
			if p.Endpoint == "" {
				t.Fatal("endpoint must be configured")
			}
		})
	}
}

func TestLookupRejectsUnknownProduct(t *testing.T) {
	if _, err := Lookup("unknown"); err == nil {
		t.Fatal("Lookup() accepted unknown product")
	}
}

func TestNormalizeIDPreservesRawAndParsesNumericValue(t *testing.T) {
	for _, tt := range []struct {
		raw    string
		number int
	}{{"0000123", 123}, {"#0000123", 123}, {"  #0000001 ", 1}} {
		got, err := NormalizeID(tt.raw)
		if err != nil || got.Raw != strings.TrimSpace(tt.raw) || got.Number != tt.number {
			t.Fatalf("NormalizeID(%q) = %#v, %v", tt.raw, got, err)
		}
	}
}

func TestNormalizeIDRejectsInvalidValues(t *testing.T) {
	for _, raw := range []string{"", "   ", "#", "-1", "abc", "##1"} {
		if _, err := NormalizeID(raw); err == nil {
			t.Errorf("NormalizeID(%q) accepted invalid ID", raw)
		}
	}
}
