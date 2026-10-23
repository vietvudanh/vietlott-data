package render

import (
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
	"unicode"
)

// FreqRow is one number-frequency record.
type FreqRow struct {
	Result int
	Count  int
	Pct    float64
}

// Frequency counts result-number appearances across draws, returning rows
// sorted by number ascending with percentages rounded to two decimals.
func Frequency(draws []Draw) []FreqRow {
	counts := map[int]int{}
	total := 0
	for _, d := range draws {
		for _, n := range d.Result {
			counts[n]++
			total++
		}
	}
	if total == 0 {
		return nil
	}
	rows := make([]FreqRow, 0, len(counts))
	for n, c := range counts {
		rows = append(rows, FreqRow{Result: n, Count: c, Pct: math.Round(float64(c)/float64(total)*100*100) / 100})
	}
	sort.Slice(rows, func(i, j int) bool { return rows[i].Result < rows[j].Result })
	return rows
}

// DaysRow is one days-since-last-appearance record.
type DaysRow struct {
	Result   int
	LastDate time.Time
	Days     int
}

// DaysSince computes days since each number last appeared relative to the
// newest draw date, sorted by days descending (ties by number ascending).
func DaysSince(draws []Draw) []DaysRow {
	if len(draws) == 0 {
		return nil
	}
	latest := draws[0].Date
	for _, d := range draws[1:] {
		if d.Date.After(latest) {
			latest = d.Date
		}
	}
	last := map[int]time.Time{}
	for _, d := range draws {
		for _, n := range d.Result {
			if prev, ok := last[n]; !ok || d.Date.After(prev) {
				last[n] = d.Date
			}
		}
	}
	rows := make([]DaysRow, 0, len(last))
	for n, t := range last {
		rows = append(rows, DaysRow{Result: n, LastDate: t, Days: int(latest.Sub(t).Hours() / 24)})
	}
	sort.Slice(rows, func(i, j int) bool {
		if rows[i].Days != rows[j].Days {
			return rows[i].Days > rows[j].Days
		}
		return rows[i].Result < rows[j].Result
	})
	return rows
}

// sortByResult sorts days rows by number ascending in place.
func sortByResult(rows []DaysRow) {
	sort.Slice(rows, func(i, j int) bool { return rows[i].Result < rows[j].Result })
}

// formatFloat renders floats the way Polars stringifies them: integer-valued
// floats keep one decimal ("2.0"), others use the shortest representation.
func formatFloat(v float64) string {
	if v == math.Trunc(v) && !math.IsInf(v, 0) && !math.IsNaN(v) {
		return strconv.FormatFloat(v, 'f', 1, 64)
	}
	return strconv.FormatFloat(v, 'f', -1, 64)
}

// formatIntList renders an int slice like Python str(list): "[1, 2, 3]".
func formatIntList(nums []int) string {
	if nums == nil {
		return "[]"
	}
	parts := make([]string, len(nums))
	for i, n := range nums {
		parts[i] = strconv.Itoa(n)
	}
	return "[" + strings.Join(parts, ", ") + "]"
}

// MarkdownTable converts string columns and rows to a Markdown table,
// mirroring df_to_markdown ("No data available" for empty input).
func MarkdownTable(cols []string, rows [][]string) string {
	if len(rows) == 0 {
		return "No data available"
	}
	lines := make([]string, 0, len(rows)+2)
	lines = append(lines, "| "+strings.Join(cols, " | ")+" |")
	sep := make([]string, len(cols))
	for i := range sep {
		sep[i] = "---"
	}
	lines = append(lines, "| "+strings.Join(sep, " | ")+" |")
	for _, r := range rows {
		lines = append(lines, "| "+strings.Join(r, " | ")+" |")
	}
	return strings.Join(lines, "\n")
}

// BalanceColumns folds a long string table into side-by-side chunks of
// nSplits rows, mirroring _balance_long_df: later chunks get a "-i"
// separator column and "i"-prefixed headers, short chunks are padded.
func BalanceColumns(cols []string, rows [][]string, nSplits int) ([]string, [][]string) {
	if len(rows) == 0 {
		return cols, rows
	}
	total := len(rows)
	chunks := (total + nSplits - 1) / nSplits
	if chunks <= 1 {
		return cols, rows
	}
	outCols := append([]string{}, cols...)
	for i := 1; i < chunks; i++ {
		outCols = append(outCols, strconv.Itoa(-i))
		for _, c := range cols {
			outCols = append(outCols, strconv.Itoa(i)+c)
		}
	}
	chunkRow := func(chunk, r int) []string {
		idx := chunk*nSplits + r
		if idx < total {
			return rows[idx]
		}
		blank := make([]string, len(cols))
		for i := range blank {
			blank[i] = ""
		}
		return blank
	}
	outRows := make([]([]string), 0, nSplits)
	for r := 0; r < nSplits; r++ {
		row := append([]string{}, chunkRow(0, r)...)
		for i := 1; i < chunks; i++ {
			row = append(row, "")
			row = append(row, chunkRow(i, r)...)
		}
		outRows = append(outRows, row)
	}
	return outCols, outRows
}

// pythonTitle replicates "s.replace('_', ' ').title()": a letter is
// uppercased when the previous character is not a letter.
func pythonTitle(s string) string {
	var b strings.Builder
	prevLetter := false
	for _, r := range strings.ReplaceAll(s, "_", " ") {
		isLetter := (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z')
		switch {
		case isLetter && !prevLetter:
			b.WriteRune(unicode.ToUpper(r))
		case isLetter:
			b.WriteRune(unicode.ToLower(r))
		default:
			b.WriteRune(r)
		}
		prevLetter = isLetter
	}
	return b.String()
}

// formatThousands replicates f"{num:,}".
func formatThousands(n int) string {
	neg := n < 0
	if neg {
		n = -n
	}
	s := strconv.Itoa(n)
	var b strings.Builder
	if neg {
		b.WriteByte('-')
	}
	for i, c := range s {
		if i > 0 && (len(s)-i)%3 == 0 {
			b.WriteByte(',')
		}
		b.WriteRune(c)
	}
	return b.String()
}
