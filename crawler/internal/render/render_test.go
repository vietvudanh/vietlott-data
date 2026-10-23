package render

import (
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"time"
)

func writeNDJSON(t *testing.T, content string) string {
	t.Helper()
	path := filepath.Join(t.TempDir(), "test.jsonl")
	if err := os.WriteFile(path, []byte(content), 0o644); err != nil {
		t.Fatal(err)
	}
	return path
}

func TestLoadDrawsSortsDateThenIDDescending(t *testing.T) {
	path := writeNDJSON(t,
		`{"date":"2024-01-02","id":"2","result":[2],"process_time":"x"}`+"\n"+
			`{"date":"2024-01-01","id":"10","result":[1],"process_time":"x"}`+"\n"+
			`{"date":"2024-01-02","id":"1","result":[3],"process_time":"x"}`+"\n")
	draws, err := LoadDraws(path)
	if err != nil {
		t.Fatal(err)
	}
	got := []string{draws[0].ID, draws[1].ID, draws[2].ID}
	if !reflect.DeepEqual(got, []string{"2", "1", "10"}) {
		t.Fatalf("order = %v", got)
	}
}

func TestFrequencyCountsAndRoundsPercentages(t *testing.T) {
	draws := []Draw{
		{Result: []int{1, 2}},
		{Result: []int{1, 3}},
		{Result: []int{1}},
	}
	got := Frequency(draws)
	want := []FreqRow{{1, 3, 60}, {2, 1, 20}, {3, 1, 20}}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("got %#v, want %#v", got, want)
	}
}

func TestFrequencyRoundsToTwoDecimals(t *testing.T) {
	draws := []Draw{{Result: []int{1}}, {Result: []int{2}}, {Result: []int{2}}}
	got := Frequency(draws)
	if len(got) != 2 || got[0].Pct != 33.33 || got[1].Pct != 66.67 {
		t.Fatalf("got %#v", got)
	}
	if s := formatFloat(got[0].Pct); s != "33.33" {
		t.Fatalf("format = %q", s)
	}
	if s := formatFloat(2.0); s != "2.0" {
		t.Fatalf("format = %q, want 2.0", s)
	}
}

func TestDaysSinceOrdersByRecency(t *testing.T) {
	day := func(s string) time.Time {
		d, _ := time.Parse("2006-01-02", s)
		return d
	}
	draws := []Draw{
		{Date: day("2024-01-10"), Result: []int{1, 2}},
		{Date: day("2024-01-01"), Result: []int{2, 3}},
	}
	got := DaysSince(draws)
	want := []DaysRow{
		{3, day("2024-01-01"), 9},
		{1, day("2024-01-10"), 0},
		{2, day("2024-01-10"), 0},
	}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("got %#v, want %#v", got, want)
	}
}

func TestBalanceColumnsChunksAndPads(t *testing.T) {
	cols := []string{"a", "b"}
	var rows [][]string
	for _, v := range []string{"1", "2", "3", "4", "5"} {
		rows = append(rows, []string{v, "x" + v})
	}
	gotCols, gotRows := BalanceColumns(cols, rows, 2)
	wantCols := []string{"a", "b", "-1", "1a", "1b", "-2", "2a", "2b"}
	if !reflect.DeepEqual(gotCols, wantCols) {
		t.Fatalf("cols = %v", gotCols)
	}
	if len(gotRows) != 2 || len(gotRows[0]) != 8 {
		t.Fatalf("rows = %v", gotRows)
	}
	if !reflect.DeepEqual(gotRows[0], []string{"1", "x1", "", "3", "x3", "", "5", "x5"}) {
		t.Fatalf("row0 = %v", gotRows[0])
	}
	if !reflect.DeepEqual(gotRows[1], []string{"2", "x2", "", "4", "x4", "", "", ""}) {
		t.Fatalf("row1 = %v", gotRows[1])
	}
}

func TestBalanceColumnsShortTableUnchanged(t *testing.T) {
	cols := []string{"a"}
	rows := [][]string{{"1"}}
	gotCols, gotRows := BalanceColumns(cols, rows, 20)
	if !reflect.DeepEqual(gotCols, cols) || !reflect.DeepEqual(gotRows, rows) {
		t.Fatalf("got %v %v", gotCols, gotRows)
	}
}

func TestMarkdownTableEmpty(t *testing.T) {
	if got := MarkdownTable([]string{"a"}, nil); got != "No data available" {
		t.Fatalf("got %q", got)
	}
}

func TestPythonTitle(t *testing.T) {
	cases := map[string]string{
		"power_655": "Power 655", "keno": "Keno", "3d": "3D",
		"3d_pro": "3D Pro", "bingo18": "Bingo18",
	}
	for in, want := range cases {
		if got := pythonTitle(in); got != want {
			t.Fatalf("title(%q) = %q, want %q", in, got, want)
		}
	}
}

func TestFormatThousands(t *testing.T) {
	if got := formatThousands(92826); got != "92,826" {
		t.Fatalf("got %q", got)
	}
	if got := formatThousands(1407); got != "1,407" {
		t.Fatalf("got %q", got)
	}
}

func TestRenderReadmeEmptyData(t *testing.T) {
	root := t.TempDir()
	if err := os.Mkdir(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	content, err := RenderReadme(filepath.Join(root, "data"), time.Now())
	if err != nil {
		t.Fatal(err)
	}
	for _, want := range []string{"# Vietlott Data", "No data available", "> No data available for analysis."} {
		if !strings.Contains(content, want) {
			t.Fatalf("readme missing %q", want)
		}
	}
}

func TestUpdateDocsHTMLReplacesStatsBody(t *testing.T) {
	root := t.TempDir()
	if err := os.MkdirAll(filepath.Join(root, "docs"), 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.MkdirAll(filepath.Join(root, "data"), 0o755); err != nil {
		t.Fatal(err)
	}
	html := `<html><body><table><tbody><tr><td>old</td></tr></tbody></table><!-- BEGIN_DAYS_SINCE_SECTION -->old section<!-- END_DAYS_SINCE_SECTION --></body></html>`
	if err := os.WriteFile(filepath.Join(root, "docs", "index.html"), []byte(html), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(root, "data", "power655.jsonl"),
		[]byte(`{"date":"2024-01-01","id":"1","result":[5]}`+"\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := UpdateDocsHTML(root); err != nil {
		t.Fatal(err)
	}
	raw, _ := os.ReadFile(filepath.Join(root, "docs", "index.html"))
	out := string(raw)
	if strings.Contains(out, "<td>old</td>") {
		t.Fatalf("old tbody not replaced: %s", out)
	}
	if !strings.Contains(out, "Power 655") || !strings.Contains(out, "BEGIN_DAYS_SINCE_SECTION") {
		t.Fatalf("missing stats or days section: %s", out)
	}
}
