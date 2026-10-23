package model

import (
	"encoding/json"
	"fmt"
)

// Draw is a product-independent view of one lottery result.
type Draw interface {
	GetID() string
	GetDate() string
	ProductName() ProductName
	MarshalJSON() ([]byte, error)
}

type drawMetadata struct {
	Date string `json:"date"`
	ID   string `json:"id"`

	product ProductName
}

func (d drawMetadata) GetID() string            { return d.ID }
func (d drawMetadata) GetDate() string          { return d.Date }
func (d drawMetadata) ProductName() ProductName { return d.product }

// NumberDraw is the result shape used by Power 6/55, Power 6/45, and Power 5/35.
type NumberDraw struct {
	drawMetadata
	Result      []int  `json:"result"`
	ProcessTime string `json:"process_time"`
}

func (d NumberDraw) MarshalJSON() ([]byte, error) {
	type draw NumberDraw
	return json.Marshal(draw(d))
}

// KenoDraw is the result shape used by Keno.
type KenoDraw struct {
	drawMetadata
	Result   []int  `json:"result"`
	BigSmall string `json:"big_small"`
	OddEven  string `json:"odd_even"`
}

func (d KenoDraw) MarshalJSON() ([]byte, error) {
	type draw KenoDraw
	return json.Marshal(draw(d))
}

// Bingo18Draw is the result shape used by Bingo18.
type Bingo18Draw struct {
	drawMetadata
	Result      []int  `json:"result"`
	Total       int    `json:"total"`
	LargeSmall  string `json:"large_small"`
	ProcessTime string `json:"process_time"`
}

func (d Bingo18Draw) MarshalJSON() ([]byte, error) {
	type draw Bingo18Draw
	return json.Marshal(draw(d))
}

// ThreeDDraw is the result shape used by Max 3D and Max 3D Pro.
type ThreeDDraw struct {
	drawMetadata
	Result map[string][]string `json:"result"`
}

func (d ThreeDDraw) MarshalJSON() ([]byte, error) {
	type draw ThreeDDraw
	return json.Marshal(draw(d))
}

var (
	_ Draw = NumberDraw{}
	_ Draw = KenoDraw{}
	_ Draw = Bingo18Draw{}
	_ Draw = ThreeDDraw{}
)

// DecodeDraw decodes one stored JSON draw and attaches its product identity.
func DecodeDraw(product ProductName, data []byte) (Draw, error) {
	if _, err := Lookup(string(product)); err != nil {
		return nil, err
	}

	var draw Draw
	switch product {
	case Power655, Power645, Power535:
		draw = &NumberDraw{}
	case Keno:
		draw = &KenoDraw{}
	case Bingo18:
		draw = &Bingo18Draw{}
	case Max3D, Max3DPro:
		draw = &ThreeDDraw{}
	default:
		return nil, fmt.Errorf("unsupported product %q", product)
	}
	if err := json.Unmarshal(data, draw); err != nil {
		return nil, fmt.Errorf("decode %s draw: %w", product, err)
	}
	setDrawProduct(draw, product)
	return draw, nil
}

// UnmarshalDraw is an alias for DecodeDraw.
func UnmarshalDraw(product ProductName, data []byte) (Draw, error) {
	return DecodeDraw(product, data)
}

func setDrawProduct(draw Draw, product ProductName) {
	switch value := draw.(type) {
	case *NumberDraw:
		value.product = product
	case *KenoDraw:
		value.product = product
	case *Bingo18Draw:
		value.product = product
	case *ThreeDDraw:
		value.product = product
	}
}
