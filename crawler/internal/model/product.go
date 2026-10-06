package model

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

type ProductName string

const (
	Power655 ProductName = "power655"
	Power645 ProductName = "power645"
	Power535 ProductName = "power535"
	Keno     ProductName = "keno"
	Bingo18  ProductName = "bingo18"
	Max3D    ProductName = "3d"
	Max3DPro ProductName = "3d_pro"
)

type Product struct {
	Name       ProductName
	FileName   string
	Endpoint   string
	IDWidth    int
	IDPrefix   string
	MinID      int
	ResultKind string
}

type NormalizedID struct {
	Raw    string
	Number int
}

var products = map[ProductName]Product{
	Power655: {Power655, "power655.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx", 5, "", 1, "number"},
	Power645: {Power645, "power645.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game645CompareWebPart,Vietlott.PlugIn.WebParts.ashx", 5, "", 198, "number"},
	Power535: {Power535, "power535.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game535CompareWebPart,Vietlott.PlugIn.WebParts.ashx", 5, "", 1, "number"},
	Keno:     {Keno, "keno.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameKenoCompareWebPart,Vietlott.PlugIn.WebParts.ashx", 7, "#", 110271, "keno"},
	Bingo18:  {Bingo18, "bingo18.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameBingoCompareWebPart,Vietlott.PlugIn.WebParts.ashx", 7, "", 83123, "bingo18"},
	Max3D:    {Max3D, "3d.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameMax3DCompareWebPart,Vietlott.PlugIn.WebParts.ashx", 5, "", 1, "3d"},
	Max3DPro: {Max3DPro, "3d_pro.jsonl", "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameMax3DProCompareWebPart,Vietlott.PlugIn.WebParts.ashx", 5, "", 1, "3d"},
}

func Lookup(name string) (Product, error) {
	product, ok := products[ProductName(name)]
	if !ok {
		return Product{}, fmt.Errorf("unknown product %q", name)
	}
	return product, nil
}

func NormalizeID(raw string) (NormalizedID, error) {
	trimmed := strings.TrimSpace(raw)
	if trimmed == "" {
		return NormalizedID{}, errors.New("draw ID is empty")
	}
	numeric := strings.TrimPrefix(trimmed, "#")
	number, err := strconv.Atoi(numeric)
	if err != nil || number < 0 {
		return NormalizedID{}, fmt.Errorf("invalid draw ID %q", raw)
	}
	return NormalizedID{Raw: trimmed, Number: number}, nil
}
