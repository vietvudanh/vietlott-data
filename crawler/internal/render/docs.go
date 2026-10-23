package render

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

const blogPostURL = "https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the"

const blogPostBadge = `
                    <a
                        href="` + blogPostURL + `"
                        class="badge"
                        target="_blank"
                    >
                        <span
                            data-vi="Bài viết Blog"
                            data-en="Blog Post"
                            >Bài viết Blog</span
                        >
                    </a>`

const mlReadmeURL = "https://github.com/vietvudanh/vietlott-data/blob/main/src/machine_learning"

const mlSection = `<!-- BEGIN_MACHINE_LEARNING_SECTION -->
            <section class="section">
                <a
                    href="` + mlReadmeURL + `"
                    target="_blank"
                    rel="noreferrer"
                    class="ml-card-banner"
                >
                    <div class="ml-card-content">
                        <div class="ml-card-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
                        </div>
                        <div class="ml-card-text">
                            <h3 data-vi="Phân tích Machine Learning →" data-en="Machine Learning Analysis →">Phân tích Machine Learning →</h3>
                            <p data-vi="Khám phá các mô hình dự đoán và backtest dữ liệu xổ số Vietlott" data-en="Explore prediction models and backtesting for Vietlott lottery data">Khám phá các mô hình dự đoán và backtest dữ liệu xổ số Vietlott</p>
                        </div>
                    </div>
                    <div class="ml-card-arrow">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </div>
                </a>
            </section>
            <!-- END_MACHINE_LEARNING_SECTION -->`

const daysSinceSectionTemplate = `<!-- BEGIN_DAYS_SINCE_SECTION -->
            <section class="section" id="analysis">
                <div class="section-header">
                    <span class="section-eyebrow" data-vi="Phân tích Thống kê" data-en="Statistical Analysis">Phân tích Thống kê</span>
                    <h2
                        class="section-title"
                        data-vi="Phân tích Power 6/55 - Số ngày vắng mặt"
                        data-en="Power 6/55 - Days Since Last Appearance"
                    >
                        Power 6/55 - Days Since Last Appearance
                    </h2>
                </div>
                <div class="card">
                    <h3
                        style="margin-bottom: 1rem"
                        data-vi="Top 10 số lâu chưa xuất hiện"
                        data-en="Top 10 Numbers by Days Since Last Appearance"
                    >
                        Top 10 số lâu chưa xuất hiện
                    </h3>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th data-vi="Số" data-en="Number">Số</th>
                                    <th data-vi="Lần xuất hiện cuối" data-en="Last Appearance">Lần xuất hiện cuối</th>
                                    <th data-vi="Số ngày vắng mặt" data-en="Days Since">Số ngày vắng mặt</th>
                                </tr>
                            </thead>
                            <tbody>
%s
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="card" style="margin-top: 1.25rem">
                    <h3
                        style="margin-bottom: 1rem"
                        data-vi="Số ngày từ lần xuất hiện cuối cùng (tất cả các số)"
                        data-en="Days Since Last Appearance (All Numbers)"
                    >
                        Số ngày từ lần xuất hiện cuối cùng (tất cả các số)
                    </h3>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th data-vi="Số" data-en="Number">Số</th>
                                    <th data-vi="Lần xuất hiện cuối" data-en="Last Appearance">Lần xuất hiện cuối</th>
                                    <th data-vi="Số ngày vắng mặt" data-en="Days Since">Số ngày vắng mặt</th>
                                </tr>
                            </thead>
                            <tbody>
%s
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
            <!-- END_DAYS_SINCE_SECTION -->`

var productNameMap = map[string]string{
	"Power 655": "Power 655",
	"Power 645": "Power 645",
	"Power 535": "Power 535",
	"Keno":      "Keno",
	"3D":        "3D",
	"3D Pro":    "3D Pro",
	"Bingo18":   "Bingo18",
}

type productStat struct {
	name         string
	totalDraws   int
	startDate    string
	endDate      string
	totalRecords int
}

func dataStats(dataDir string) []productStat {
	var stats []productStat
	for _, p := range products {
		draws, err := LoadDraws(filepath.Join(dataDir, p.file))
		if err != nil || len(draws) == 0 {
			continue
		}
		dates := map[string]struct{}{}
		ids := map[string]struct{}{}
		var loDate, hiDate string
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
			first = false
		}
		stats = append(stats, productStat{
			name:         pythonTitle(p.key),
			totalDraws:   len(dates),
			startDate:    loDate,
			endDate:      hiDate,
			totalRecords: len(ids),
		})
	}
	return stats
}

func statsTableRows(stats []productStat) string {
	rows := make([]string, 0, len(stats))
	for _, s := range stats {
		name := s.name
		if mapped, ok := productNameMap[name]; ok {
			name = mapped
		}
		rows = append(rows, fmt.Sprintf(`                                <tr>
                                    <td><strong>%s</strong></td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                </tr>`, name, formatThousands(s.totalDraws), s.startDate, s.endDate, formatThousands(s.totalRecords)))
	}
	return strings.Join(rows, "\n")
}

func daysSinceRows(rows []DaysRow) string {
	out := make([]string, 0, len(rows))
	for _, r := range rows {
		out = append(out, fmt.Sprintf(`                                <tr>
                                    <td><strong>%d</strong></td>
                                    <td>%s</td>
                                    <td>%d</td>
                                </tr>`, r.Result, formatDate(r.LastDate), r.Days))
	}
	return strings.Join(out, "\n")
}

func daysSinceSection(draws []Draw) string {
	if len(draws) == 0 {
		return ""
	}
	days := DaysSince(draws)
	top10 := days
	if len(top10) > 10 {
		top10 = top10[:10]
	}
	byResult := append([]DaysRow{}, days...)
	sortByResult(byResult)
	return fmt.Sprintf(daysSinceSectionTemplate, daysSinceRows(top10), daysSinceRows(byResult))
}

// replaceInner substitutes every match of pattern (which must wrap the
// replaceable region in its second capture group) with newContent,
// preserving the surrounding markers. It mirrors the Python re.sub calls
// that keep surrounding markers via backreferences.
func replaceInner(html, pattern, newContent string) string {
	re := regexp.MustCompile(pattern)
	var b strings.Builder
	prev := 0
	for _, loc := range re.FindAllStringSubmatchIndex(html, -1) {
		b.WriteString(html[prev:loc[4]])
		b.WriteString(newContent)
		prev = loc[5]
	}
	b.WriteString(html[prev:])
	return b.String()
}

// replaceWhole substitutes whole matches of pattern with newContent.
func replaceWhole(html, pattern, newContent string) string {
	return regexp.MustCompile(pattern).ReplaceAllString(html, newContent)
}

// UpdateDocsHTML regenerates the statistics inside docs/index.html.
func UpdateDocsHTML(root string) error {
	dataDir := filepath.Join(root, "data")
	htmlPath := filepath.Join(root, "docs", "index.html")
	raw, err := os.ReadFile(htmlPath)
	if err != nil {
		return err
	}
	html := string(raw)

	stats := dataStats(dataDir)
	rows := statsTableRows(stats)
	html = replaceInner(html, `(?s)(<tbody>)(.*?)(</tbody>)`, "\n"+rows+"\n                            ")

	power655, err := LoadDraws(filepath.Join(dataDir, "power655.jsonl"))
	if err != nil {
		power655 = nil
	}
	section := daysSinceSection(power655)
	html = replaceWhole(html, `(?s)<!-- BEGIN_DAYS_SINCE_SECTION -->.*?<!-- END_DAYS_SINCE_SECTION -->`, section)

	if !strings.Contains(html, blogPostURL) {
		badges := regexp.MustCompile(`(?s)(<div class="badges">.*?)(</div>)`)
		loc := badges.FindStringSubmatchIndex(html)
		if loc != nil {
			html = html[:loc[2]] + blogPostBadge + "\n                " + html[loc[3]:]
		}
	}

	ml := regexp.MustCompile(`(?s)<!-- BEGIN_MACHINE_LEARNING_SECTION -->.*?<!-- END_MACHINE_LEARNING_SECTION -->`)
	if ml.FindString(html) != "" {
		html = replaceWhole(html, `(?s)<!-- BEGIN_MACHINE_LEARNING_SECTION -->.*?<!-- END_MACHINE_LEARNING_SECTION -->`, mlSection)
	}

	return os.WriteFile(htmlPath, []byte(html), 0o644)
}
