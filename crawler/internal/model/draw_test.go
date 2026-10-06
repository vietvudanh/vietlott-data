package model

import (
	"bytes"
	"encoding/json"
	"os"
	"path/filepath"
	"testing"
)

func TestDecodeDrawPreservesSamples(t *testing.T) {
	tests := []struct {
		product ProductName
		file    string
		id      string
		date    string
	}{
		{Power655, "power655.jsonl", "00001", "2017-08-01"},
		{Power645, "power645.jsonl", "00198", "2017-10-25"},
		{Power535, "power535.jsonl", "00001", "2025-06-29"},
		{Keno, "keno.jsonl", "#0110271", "2022-12-04"},
		{Bingo18, "bingo18.jsonl", "0083123", "2024-12-03"},
		{Max3D, "3d.jsonl", "00001", "2019-04-22"},
		{Max3DPro, "3d_pro.jsonl", "00001", "2021-09-14"},
	}
	for _, tt := range tests {
		t.Run(string(tt.product), func(t *testing.T) {
			raw, err := os.ReadFile(filepath.Join("..", "..", "..", "data", tt.file))
			if err != nil {
				t.Fatal(err)
			}
			raw = bytes.TrimSpace(bytes.Split(raw, []byte("\n"))[0])
			draw, err := DecodeDraw(tt.product, raw)
			if err != nil {
				t.Fatalf("DecodeDraw() error = %v", err)
			}
			if draw.ProductName() != tt.product {
				t.Fatalf("ProductName() = %q, want %q", draw.ProductName(), tt.product)
			}
			if draw.GetID() != tt.id || draw.GetDate() != tt.date {
				t.Fatalf("metadata = (%q, %q), want (%q, %q)", draw.GetID(), draw.GetDate(), tt.id, tt.date)
			}
			if tt.product == Keno && draw.GetID() != "#0110271" {
				t.Fatalf("Keno ID = %q, want #0110271", draw.GetID())
			}
			encoded, err := json.Marshal(draw)
			if err != nil {
				t.Fatal(err)
			}
			var want, got any
			if err := json.Unmarshal(raw, &want); err != nil {
				t.Fatal(err)
			}
			if err := json.Unmarshal(encoded, &got); err != nil {
				t.Fatal(err)
			}
			if !jsonEqual(want, got) {
				t.Fatalf("JSON changed:\nwant %s\ngot  %s", raw, encoded)
			}
		})
	}
}

func TestDecodeDrawPreservesSpecialIDsAndOptionalProcessTime(t *testing.T) {
	keno, err := DecodeDraw(Keno, []byte(`{"date":"2022-12-04","id":"#0110271","result":[3],"big_small":"Lẻ (11)","odd_even":"Nhỏ (11)"}`))
	if err != nil {
		t.Fatal(err)
	}
	if keno.GetID() != "#0110271" {
		t.Fatalf("GetID() = %q", keno.GetID())
	}
	encoded, err := json.Marshal(keno)
	if err != nil {
		t.Fatal(err)
	}
	if bytes.Contains(encoded, []byte("process_time")) {
		t.Fatalf("Keno unexpectedly encoded process_time: %s", encoded)
	}
}

func jsonEqual(a, b any) bool {
	left, _ := json.Marshal(a)
	right, _ := json.Marshal(b)
	return bytes.Equal(left, right)
}
