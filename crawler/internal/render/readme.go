package render

import (
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

// products lists every dataset in Python-config order with the Go file name.
var products = []struct {
	key  string
	file string
}{
	{"power_655", "power655.jsonl"},
	{"power_645", "power645.jsonl"},
	{"power_535", "power535.jsonl"},
	{"keno", "keno.jsonl"},
	{"3d", "3d.jsonl"},
	{"3d_pro", "3d_pro.jsonl"},
	{"bingo18", "bingo18.jsonl"},
}

const readmeHeader = `# Vietlott Data

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing statistics and insights for all major lottery products.

## Links

- [Website](https://vietvudanh.github.io/vietlott-data/) - Interactive data visualization
- [Blog Post](https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the) - About this project

## Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Power 5/35** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535) | Choose 5 numbers from 1-35 |
| **Keno** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |
| **Bingo18** | [Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game |
`

const readmeTOC = `## Table of Contents

- [Links](#links)
- [Supported Lottery Products](#supported-lottery-products)
- [Predictions](#predictions)
- [Data Statistics](#data-statistics)
- [Power 6/55 Analysis](#power-655-analysis)
  - [Recent Results](#recent-results-last-10-draws)
  - [Number Frequency (All Time)](#number-frequency-all-time)
  - [Frequency Analysis by Period](#frequency-analysis-by-period)
  - [Top 10 Numbers by Days Since Last Appearance](#top-10-numbers-by-days-since-last-appearance)
  - [Days Since Last Appearance - All Numbers](#days-since-last-appearance---all-numbers)
- [How It Works](#how-it-works)
- [Installation & Usage](#installation--usage)
- [License](#license)
`

const readmeHowItWorks = `## How It Works

Vietlott blocks non-Vietnam IPs ([issue #13](https://github.com/vietvudanh/vietlott-data/issues/13)), so crawling runs on a scheduled local runner (` + "`bin/github_data.sh`" + `) and commits updated data back to GitHub.

For architecture and runner setup, see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
`

const readmeInstall = `## Installation & Usage

### CLI Usage (using uv)

` + "```bash" + `
# Crawl latest data
uv run vietlott-crawl keno

# Backfill missing data
uv run vietlott-missing power_655

# Available products: power_655, power_645, power_535, keno, 3d, 3d_pro, bingo18
` + "```" + `

### Development Setup

` + "```bash" + `
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data
uv sync --dev
uv run pytest
` + "```" + `

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE).

---

<div align="center">
  <strong>If you find this project useful, please consider giving it a star!</strong>
</div>
`

func freqTable(freq []FreqRow) string {
	cols := []string{"result", "count", "%"}
	rows := make([][]string, 0, len(freq))
	for _, r := range freq {
		rows = append(rows, []string{strconv.Itoa(r.Result), strconv.Itoa(r.Count), formatFloat(r.Pct)})
	}
	cols, rows = BalanceColumns(cols, rows, 20)
	return MarkdownTable(cols, rows)
}

func daysTable(rows []DaysRow) string {
	out := make([][]string, 0, len(rows))
	for _, r := range rows {
		out = append(out, []string{strconv.Itoa(r.Result), formatDate(r.LastDate), strconv.Itoa(r.Days)})
	}
	return MarkdownTable([]string{"result", "last_date", "days_since"}, out)
}

func filterSince(draws []Draw, cutoff time.Time) []Draw {
	out := draws[:0:0]
	for _, d := range draws {
		if !d.Date.Before(cutoff) {
			out = append(out, d)
		}
	}
	return out
}

func dataOverview(dataDir string) string {
	header := "| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |"
	sep := "| --- | --- | --- | --- | --- | --- | --- |"
	body := []string{}
	for _, p := range products {
		draws, err := LoadDraws(filepath.Join(dataDir, p.file))
		if err != nil || len(draws) == 0 {
			continue
		}
		dates := map[string]struct{}{}
		ids := map[string]struct{}{}
		var loDate, hiDate, loID, hiID string
		first := true
		for _, d := range draws {
			if ds := formatDate(d.Date); ds != "" {
				dates[ds] = struct{}{}
				if first || ds < loDate {
					loDate = ds
				}
				if first || ds > hiDate {
					hiDate = ds
				}
			}
			ids[d.ID] = struct{}{}
			if first || d.ID < loID {
				loID = d.ID
			}
			if first || d.ID > hiID {
				hiID = d.ID
			}
			first = false
		}
		body = append(body, "| "+strings.Join([]string{
			pythonTitle(p.key),
			strconv.Itoa(len(dates)),
			loDate, hiDate,
			strconv.Itoa(len(ids)),
			loID, hiID,
		}, " | ")+" |")
	}
	if len(body) == 0 {
		return "No data available"
	}
	return strings.Join(append([]string{header, sep}, body...), "\n")
}

func power655Analysis(draws []Draw, now time.Time) string {
	if len(draws) == 0 {
		return "## Power 6/55 Analysis\n\n> No data available for analysis.\n"
	}
	today := time.Date(now.Year(), now.Month(), now.Day(), 0, 0, 0, 0, time.UTC)
	statsAll := freqTable(Frequency(draws))
	stats30 := freqTable(Frequency(filterSince(draws, today.AddDate(0, 0, -30))))
	stats60 := freqTable(Frequency(filterSince(draws, today.AddDate(0, 0, -60))))
	stats90 := freqTable(Frequency(filterSince(draws, today.AddDate(0, 0, -90))))

	recent := draws
	if len(recent) > 10 {
		recent = recent[:10]
	}
	recentRows := make([][]string, 0, len(recent))
	for _, d := range recent {
		recentRows = append(recentRows, []string{formatDate(d.Date), d.ID, formatIntList(d.Result), d.ProcessTime})
	}
	recentMD := MarkdownTable([]string{"date", "id", "result", "process_time"}, recentRows)

	days := DaysSince(draws)
	top10 := days
	if len(top10) > 10 {
		top10 = top10[:10]
	}
	byResult := append([]DaysRow{}, days...)
	sortByResult(byResult)

	var b strings.Builder
	b.WriteString("## Power 6/55 Analysis\n\n### Recent Results (Last 10 draws)\n")
	b.WriteString(recentMD)
	b.WriteString("\n\n### Number Frequency (All Time)\n")
	b.WriteString(statsAll)
	b.WriteString("\n\n### Frequency Analysis by Period\n\n#### Last 30 Days\n")
	b.WriteString(stats30)
	b.WriteString("\n\n#### Last 60 Days\n")
	b.WriteString(stats60)
	b.WriteString("\n\n#### Last 90 Days\n")
	b.WriteString(stats90)
	b.WriteString("\n\n### Top 10 Numbers by Days Since Last Appearance\n")
	b.WriteString(daysTable(top10))
	b.WriteString("\n\n### Days Since Last Appearance - All Numbers\n")
	b.WriteString(daysTable(byResult))
	b.WriteString("\n\n")
	return b.String()
}

// RenderReadme generates the full readme content from dataDir.
func RenderReadme(dataDir string, now time.Time) (string, error) {
	power655, err := LoadDraws(filepath.Join(dataDir, "power655.jsonl"))
	if err != nil {
		power655 = nil
	}
	var b strings.Builder
	b.WriteString(readmeHeader)
	b.WriteString("\n\n")
	b.WriteString(readmeTOC)
	b.WriteString("\n\n## Predictions\n\nPrediction models are at [/src/machine_learning](./src/machine_learning/).\n\nFor background on these models, see the [Machine Learning README](./src/machine_learning/).\n\n## Data Statistics\n\n")
	b.WriteString(dataOverview(dataDir))
	b.WriteString("\n\n")
	b.WriteString(power655Analysis(power655, now))
	b.WriteString("\n\n")
	b.WriteString(readmeHowItWorks)
	b.WriteString("\n\n")
	b.WriteString(readmeInstall)
	b.WriteString("\n")
	return b.String(), nil
}

// WriteReadme renders and writes readme.md into root.
func WriteReadme(root string, now time.Time) error {
	content, err := RenderReadme(filepath.Join(root, "data"), now)
	if err != nil {
		return err
	}
	return os.WriteFile(filepath.Join(root, "readme.md"), []byte(content), 0o644)
}
