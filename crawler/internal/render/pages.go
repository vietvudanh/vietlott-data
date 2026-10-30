package render

import (
	"fmt"
	"html"
	"os"
	"path/filepath"
)

type productPageConfig struct {
	slug        string
	key         string
	file        string
	title       string
	h1          string
	subtitle    string
	description string
	schedule    string
	officialURL string
	schemaDesc  string
	notes       string
	hasFreq     bool
}

var productPageConfigs = []productPageConfig{
	{
		slug:        "power-6-55",
		key:         "power_655",
		file:        "power655.jsonl",
		title:       "Vietlott Power 6/55 Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Power 6/55 — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Power 6/55 draw history since 2017-08-01 (6 main numbers + 1 bonus number), updated daily.",
		description: "Download complete historical Vietlott Power 6/55 lottery results in NDJSON format. Includes every draw since August 2017, 6 main numbers (1–55) plus 1 bonus number, frequency statistics, and Python examples.",
		schedule:    "Tuesday, Thursday, Saturday (18:00–18:30 ICT)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655",
		schemaDesc:  "<code>result</code> is an array of <strong>7 integers</strong>: the first 6 integers (<code>result[0:6]</code>) are the sorted main winning numbers (drawn from 1 to 55), and the 7th integer (<code>result[6]</code>) is the special/bonus number (used for Jackpot 2).",
		notes:       "Power 6/55 has two cumulative jackpot tiers: Jackpot 1 (matching all 6 main numbers) and Jackpot 2 (matching 5 main numbers plus the 7th special number). When computing main-number vs. bonus-number frequencies separately, slice <code>result[:6]</code> for main balls and <code>result[6]</code> for the special ball.",
		hasFreq:     true,
	},
	{
		slug:        "mega-6-45",
		key:         "power_645",
		file:        "power645.jsonl",
		title:       "Vietlott Mega 6/45 Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Mega 6/45 — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Mega 6/45 draw history (6 winning numbers from 1–45, no bonus number), updated daily.",
		description: "Free NDJSON dataset of Vietlott Mega 6/45 historical draw results (power645.jsonl). Features 6 winning numbers per draw (no bonus number), draw dates, IDs, and number frequency analytics.",
		schedule:    "Wednesday, Friday, Sunday (18:00–18:30 ICT)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645",
		schemaDesc:  "<code>result</code> is an array of <strong>6 integers</strong>: the 6 sorted winning numbers drawn from 1 to 45. <strong>Mega 6/45 does NOT have a bonus or special number</strong>.",
		notes:       "Unlike Power 6/55 and Power 5/35, Mega 6/45 draws exactly 6 numbers with no 7th bonus ball. The raw filename is <code>data/power645.jsonl</code> for historical compatibility with the internal product config (<code>power_645</code>).",
		hasFreq:     true,
	},
	{
		slug:        "power-5-35",
		key:         "power_535",
		file:        "power535.jsonl",
		title:       "Vietlott Power 5/35 Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Power 5/35 — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Power 5/35 draw history since 2025-06-29 (5 main numbers + 1 special number), updated daily.",
		description: "Download complete historical Vietlott Power 5/35 results in NDJSON format (power535.jsonl). Contains 5 main numbers (1–35) plus 1 special number per draw, updated daily.",
		schedule:    "Daily (twice daily draws)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535",
		schemaDesc:  "<code>result</code> is an array of <strong>6 integers</strong>: the first 5 integers (<code>result[0:5]</code>) are the main winning numbers (drawn from 1 to 35), and the 6th integer (<code>result[5]</code>) is the special number.",
		notes:       "Power 5/35 runs multiple draws per day (so <code>Total Records</code> exceeds <code>Total Draws</code> counted by unique calendar dates). Always separate <code>result[:5]</code> (main numbers) from <code>result[5]</code> (special number) when modeling main vs. special pools.",
		hasFreq:     true,
	},
	{
		slug:        "keno",
		key:         "keno",
		file:        "keno.jsonl",
		title:       "Vietlott Keno Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Keno — High-Frequency Historical Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Keno high-frequency draw dataset (20 winning numbers from 1–80 every 10 minutes), updated daily.",
		description: "Download 90,000+ historical Vietlott Keno lottery draws in NDJSON format (keno.jsonl). Each record includes 20 numbers (1–80), big/small, and odd/even summaries.",
		schedule:    "Daily every 10 minutes (06:00–21:50 ICT, up to 96 draws/day)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno",
		schemaDesc:  "<code>result</code> is an array of <strong>20 integers</strong> drawn from 1 to 80. Each record also includes <code>big_small</code> (Chẵn/Lẻ/Hòa parity or Big/Small summary as labeled on Vietlott) and <code>odd_even</code>, and <code>id</code> is prefixed with <code>#</code> (e.g., <code>#0301098</code>).",
		notes:       "Because Keno draws every 10 minutes, <code>data/keno.jsonl</code> is the largest file (~14 MB, 90,000+ records). Use streaming or columnar readers like <code>polars.scan_ndjson('data/keno.jsonl')</code> rather than loading the entire file into a list of dicts.",
		hasFreq:     false,
	},
	{
		slug:        "max-3d",
		key:         "3d",
		file:        "3d.jsonl",
		title:       "Vietlott Max 3D Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Max 3D — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Max 3D draw history since 2019-04-22 (20 three-digit triplets across 4 prize tiers), updated daily.",
		description: "Download historical Vietlott Max 3D lottery results in NDJSON format (3d.jsonl). Each draw maps 4 Vietnamese prize tiers to 20 3-digit string triplets.",
		schedule:    "Monday, Wednesday, Friday (18:00–18:30 ICT)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d",
		schemaDesc:  "<code>result</code> is a <strong>JSON object</strong> mapping 4 prize tier keys to arrays of 3-digit strings (<code>\"000\"</code>–<code>\"999\"</code>): <code>\"Giải Đặc biệt\"</code> (2 triplets), <code>\"Giải Nhất\"</code> (4 triplets), <code>\"Giải Nhì\"</code> (6 triplets), and <code>\"Giải ba\"</code> (8 triplets) — 20 triplets total per draw.",
		notes:       "Triplets are stored as zero-padded 3-character strings (e.g., <code>\"005\"</code>) to preserve leading zeros. In Polars or Pandas, unnest or normalize the <code>result</code> struct/dict to analyze specific prize tiers.",
		hasFreq:     false,
	},
	{
		slug:        "max-3d-pro",
		key:         "3d_pro",
		file:        "3d_pro.jsonl",
		title:       "Vietlott Max 3D Pro Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Max 3D Pro — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Max 3D Pro draw history since 2021-09-14 (20 three-digit triplets across 4 prize tiers), updated daily.",
		description: "Download historical Vietlott Max 3D Pro lottery results in NDJSON format (3d_pro.jsonl). Includes every draw since September 2021 with full prize-tier triplet mappings.",
		schedule:    "Tuesday, Thursday, Saturday (18:00–18:30 ICT)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro",
		schemaDesc:  "<code>result</code> is a <strong>JSON object</strong> with the same 4 prize tier keys as Max 3D: <code>\"Giải Đặc biệt\"</code> (2 triplets), <code>\"Giải Nhất\"</code> (4 triplets), <code>\"Giải Nhì\"</code> (6 triplets), and <code>\"Giải ba\"</code> (8 triplets).",
		notes:       "Max 3D Pro is drawn on Tuesday, Thursday, and Saturday, complementing Max 3D (Monday, Wednesday, Friday). Leading zeros are preserved as 3-digit strings.",
		hasFreq:     false,
	},
	{
		slug:        "bingo18",
		key:         "bingo18",
		file:        "bingo18.jsonl",
		title:       "Vietlott Bingo18 Historical Dataset & Results (NDJSON) — Vietlott Data",
		h1:          "Bingo18 — Historical Results & Dataset (NDJSON)",
		subtitle:    "Complete Vietlott Bingo18 fast-draw history (3 numbers from 1–6, sum 3–18), updated daily.",
		description: "Download 97,000+ historical Vietlott Bingo18 draws in NDJSON format (bingo18.jsonl). Each record includes 3 dice numbers (1–6), total sum (3–18), and large/small classification.",
		schedule:    "Daily every 10 minutes (06:00–21:53 ICT)",
		officialURL: "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18",
		schemaDesc:  "<code>result</code> is an array of <strong>3 integers</strong> (each 1–6, representing three dice/numbers), accompanied by <code>total</code> (integer sum 3–18), <code>large_small</code> (<code>\"Nhỏ\"</code>, <code>\"Hòa\"</code>, or <code>\"Lớn\"</code>), and <code>process_time</code>.",
		notes:       "With 3 independent numbers from 1 to 6, there are 6³ = 216 possible ordered outcomes per draw. Use <code>polars.scan_ndjson('data/bingo18.jsonl')</code> for fast aggregations over all 97,000+ records.",
		hasFreq:     false,
	},
}

func pageHeaderHTML(title, description, canonicalPath, lang, altHrefVi, altHrefEn string) string {
	canonicalURL := "https://vietvudanh.github.io/vietlott-data/" + canonicalPath
	ogLocale := "en_US"
	if lang == "vi" {
		ogLocale = "vi_VN"
	}
	hreflangBlock := fmt.Sprintf(`        <link rel="canonical" href="%s" />`, canonicalURL)
	if altHrefVi != "" && altHrefEn != "" {
		hreflangBlock += fmt.Sprintf(`
        <link rel="alternate" hreflang="vi" href="%s" />
        <link rel="alternate" hreflang="en" href="%s" />
        <link rel="alternate" hreflang="x-default" href="%s" />`, altHrefVi, altHrefEn, altHrefVi)
	}
	return fmt.Sprintf(`<!doctype html>
<html lang="%s" data-theme="light">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>%s</title>
        <meta name="description" content="%s" />
        <meta name="author" content="vietvudanh" />
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
        <link rel="alternate" type="text/plain" href="https://vietvudanh.github.io/vietlott-data/llms.txt" title="LLM-readable summary" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="%s" />
        <meta property="og:title" content="%s" />
        <meta property="og:description" content="%s" />
        <meta property="og:image" content="https://vietvudanh.github.io/vietlott-data/assets/screenshot.png" />
        <meta property="og:locale" content="%s" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="%s" />
        <meta name="twitter:description" content="%s" />
        <meta name="twitter:image" content="https://vietvudanh.github.io/vietlott-data/assets/screenshot.png" />
%s
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="../styles.css" />
        <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%%22http://www.w3.org/2000/svg%%22 viewBox=%%220 0 100 100%%22><text y=%%22.9em%%22 font-size=%%2290%%22>V</text></svg>" />
    </head>
    <body>
        <div class="ambient-glow" aria-hidden="true"></div>
        <header class="top-nav-wrapper">
            <div class="container">
                <nav class="top-nav" aria-label="Main Navigation">
                    <a href="../" class="brand-link">
                        <div class="brand-icon" aria-hidden="true">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z" />
                            </svg>
                        </div>
                        <span>Vietlott Data</span>
                        <span class="brand-version">v0.3.0</span>
                    </a>
                    <ul class="nav-menu">
                        <li><a href="../" class="nav-link">Home (VI)</a></li>
                        <li><a href="../en/" class="nav-link">Home (EN)</a></li>
                        <li><a href="../power-6-55/" class="nav-link">Power 6/55</a></li>
                        <li><a href="../mega-6-45/" class="nav-link">Mega 6/45</a></li>
                        <li><a href="../power-5-35/" class="nav-link">Power 5/35</a></li>
                        <li><a href="../keno/" class="nav-link">Keno</a></li>
                        <li><a href="../data-schema/" class="nav-link">Schema</a></li>
                        <li><a href="../python-examples/" class="nav-link">Python</a></li>
                    </ul>
                    <div class="nav-actions">
                        <button class="icon-btn theme-toggle-btn" id="themeToggleBtn" aria-label="Toggle dark mode">
                            <svg class="theme-icon-moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg>
                            <svg class="theme-icon-sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path></svg>
                        </button>
                        <a href="https://github.com/vietvudanh/vietlott-data" target="_blank" rel="noreferrer" class="icon-btn" aria-label="GitHub Repository">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12Z" /></svg>
                        </a>
                    </div>
                </nav>
            </div>
        </header>
`, lang, html.EscapeString(title), html.EscapeString(description), canonicalURL, html.EscapeString(title), html.EscapeString(description), ogLocale, html.EscapeString(title), html.EscapeString(description), hreflangBlock)
}

const pageFooterHTML = `        <footer class="footer">
            <div class="container footer-content">
                <div>
                    <strong>Vietlott Data</strong> &copy; 2026. Open source under MIT License.
                </div>
                <div class="footer-links">
                    <a href="../">Tiếng Việt</a>
                    <a href="../en/">English</a>
                    <a href="../data-schema/">Data Schema</a>
                    <a href="../python-examples/">Python Examples</a>
                    <a href="https://github.com/vietvudanh/vietlott-data" target="_blank" rel="noreferrer">GitHub</a>
                    <a href="https://vietlott.vn" target="_blank" rel="noreferrer">vietlott.vn</a>
                </div>
            </div>
        </footer>
        <script>
            function getPreferredTheme() {
                const stored = localStorage.getItem("vietlott-theme");
                if (stored) return stored;
                return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
            }
            function setTheme(theme) {
                document.documentElement.setAttribute("data-theme", theme);
                localStorage.setItem("vietlott-theme", theme);
            }
            setTheme(getPreferredTheme());
            const btn = document.getElementById("themeToggleBtn");
            if (btn) {
                btn.addEventListener("click", function () {
                    const current = document.documentElement.getAttribute("data-theme") || "light";
                    setTheme(current === "dark" ? "light" : "dark");
                });
            }
        </script>
    </body>
</html>
`

func renderProductPage(cfg productPageConfig, draws []Draw, stat productStat) string {
	rawURL := "https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/" + cfg.file
	sampleLine := `{}`
	latestID := ""
	if len(draws) > 0 {
		sampleLine = draws[0].RawLine
		latestID = draws[0].ID
	}

	recent := draws
	if len(recent) > 10 {
		recent = recent[:10]
	}
	var recentRows string
	for _, d := range recent {
		res := d.RawResult
		if len(res) > 120 {
			res = res[:117] + "..."
		}
		recentRows += fmt.Sprintf(`                                <tr>
                                    <td>%s</td>
                                    <td><strong>%s</strong></td>
                                    <td><code>%s</code></td>
                                </tr>
`, formatDate(d.Date), html.EscapeString(d.ID), html.EscapeString(res))
	}

	var extraStats string
	if cfg.hasFreq && len(draws) > 0 {
		days := DaysSince(draws)
		top10 := days
		if len(top10) > 10 {
			top10 = top10[:10]
		}
		extraStats = fmt.Sprintf(`            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 1rem;">Top 10 Numbers by Days Since Last Appearance</h2>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Number</th>
                                    <th>Last Appearance</th>
                                    <th>Days Since</th>
                                </tr>
                            </thead>
                            <tbody>
%s
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
`, daysSinceRows(top10))
	}

	header := pageHeaderHTML(cfg.title, cfg.description, cfg.slug+"/", "en", "", "")
	return header + fmt.Sprintf(`        <main class="container">
            <section class="hero-section">
                <div class="hero-pill">
                    <span class="status-dot"></span>
                    <span>Dataset &amp; Historical Statistics</span>
                </div>
                <h1 class="hero-title">%s</h1>
                <p class="hero-subtitle">%s</p>
                <div class="badges">
                    <span class="badge badge-green"><span>Latest Draw: %s (ID %s)</span></span>
                    <span class="badge"><span>Total Draws: %s</span></span>
                    <span class="badge"><span>Total Records: %s</span></span>
                    <span class="badge"><span>Coverage: %s to %s</span></span>
                </div>
                <div class="hero-actions">
                    <a href="%s" class="btn btn-primary" target="_blank" rel="noreferrer">
                        <span>Download %s (Raw NDJSON)</span>
                    </a>
                    <a href="%s" class="btn btn-secondary" target="_blank" rel="noreferrer">
                        <span>Official Vietlott Page</span>
                    </a>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Dataset Overview &amp; Record Schema</h2>
                    <p style="margin-bottom: 0.75rem;"><strong>Draw Schedule:</strong> %s</p>
                    <p style="margin-bottom: 0.75rem;"><strong>Result Schema:</strong> %s</p>
                    <p style="margin-bottom: 1rem;"><strong>Technical Notes:</strong> %s</p>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header">
                            <span class="code-card-title">Latest Sample Record (data/%s)</span>
                        </div>
                        <pre class="code-block"><code>%s</code></pre>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 1rem;">Recent 10 Draws</h2>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Draw Date</th>
                                    <th>Draw ID</th>
                                    <th>Winning Result</th>
                                </tr>
                            </thead>
                            <tbody>
%s                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

%s            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Load in Python (Polars &amp; Pandas)</h2>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header">
                            <span class="code-card-title">python</span>
                        </div>
                        <pre class="code-block"><code>import polars as pl

url = "%s"
df = pl.read_ndjson(url)
print(df.head(5))</code></pre>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Explore Related Datasets &amp; Guides</h2>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.6rem;">
                        <a href="../power-6-55/" class="btn btn-secondary btn-sm">Power 6/55</a>
                        <a href="../mega-6-45/" class="btn btn-secondary btn-sm">Mega 6/45</a>
                        <a href="../power-5-35/" class="btn btn-secondary btn-sm">Power 5/35</a>
                        <a href="../keno/" class="btn btn-secondary btn-sm">Keno</a>
                        <a href="../max-3d/" class="btn btn-secondary btn-sm">Max 3D</a>
                        <a href="../max-3d-pro/" class="btn btn-secondary btn-sm">Max 3D Pro</a>
                        <a href="../bingo18/" class="btn btn-secondary btn-sm">Bingo18</a>
                        <a href="../data-schema/" class="btn btn-secondary btn-sm">Data Schema</a>
                        <a href="../python-examples/" class="btn btn-secondary btn-sm">Python Examples</a>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="disclaimer">
                    <div>
                        <h4>Methodology &amp; Randomness Disclaimer</h4>
                        <p>Data is collected automatically from official Vietlott results pages and verified by draw ID. Lottery draws are independent random events; past frequencies do not influence future draws. Provided strictly for educational and statistical research under the MIT License.</p>
                    </div>
                </div>
            </section>
        </main>
`, html.EscapeString(cfg.h1), html.EscapeString(cfg.subtitle),
		stat.endDate, html.EscapeString(latestID),
		formatThousands(stat.totalDraws), formatThousands(stat.totalRecords),
		stat.startDate, stat.endDate,
		rawURL, cfg.file, cfg.officialURL,
		html.EscapeString(cfg.schedule), cfg.schemaDesc, cfg.notes,
		cfg.file, html.EscapeString(sampleLine),
		recentRows, extraStats, rawURL) + pageFooterHTML
}

func renderEnglishHomePage(stats []productStat, latestDate string, power655Draws []Draw) string {
	title := "Vietlott Historical Lottery Dataset — Free NDJSON Downloads & Statistics"
	desc := "Download historical Vietlott lottery results for Power 6/55, Mega 6/45, Power 5/35, Keno, Max 3D, Max 3D Pro and Bingo18. Free NDJSON data, daily updates, statistics and Python/Go tools."
	header := pageHeaderHTML(title, desc, "en/", "en", "https://vietvudanh.github.io/vietlott-data/", "https://vietvudanh.github.io/vietlott-data/en/")

	rows := statsTableRows(stats)
	daysSection := ""
	if len(power655Draws) > 0 {
		days := DaysSince(power655Draws)
		top10 := days
		if len(top10) > 10 {
			top10 = top10[:10]
		}
		daysSection = fmt.Sprintf(`            <section class="section" id="analysis">
                <div class="section-header">
                    <span class="section-eyebrow">Statistical Analysis</span>
                    <h2 class="section-title">Power 6/55 — Top 10 Numbers by Days Since Last Appearance</h2>
                </div>
                <div class="card">
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Number</th>
                                    <th>Last Appearance</th>
                                    <th>Days Since</th>
                                </tr>
                            </thead>
                            <tbody>
%s
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
`, daysSinceRows(top10))
	}

	return header + fmt.Sprintf(`        <main class="container">
            <section class="hero-section">
                <div class="hero-pill">
                    <span class="status-dot"></span>
                    <span>Open Vietnamese Lottery Data Platform</span>
                </div>
                <h1 class="hero-title">Vietlott Historical Lottery Dataset</h1>
                <p class="hero-subtitle">Free, daily-updated NDJSON datasets and statistical analysis for all seven official Vietlott games: Power 6/55, Mega 6/45, Power 5/35, Keno, Max 3D, Max 3D Pro, and Bingo18.</p>
                <div class="badges">
                    <span class="badge badge-green"><span>Data last updated: %s</span></span>
                    <a href="https://go.dev/" class="badge" target="_blank"><span>Go 1.27+ Crawler</span></a>
                    <a href="https://pypi.org/project/vietlott-data/" class="badge" target="_blank"><span>Python 3.11+ Package</span></a>
                    <a href="https://github.com/vietvudanh/vietlott-data/blob/main/LICENSE" class="badge" target="_blank"><span>MIT License</span></a>
                    <a href="../" class="badge"><span>Tiếng Việt (Vietnamese) →</span></a>
                </div>
                <div class="hero-actions">
                    <a href="#statistics" class="btn btn-primary"><span>Explore Dataset Statistics</span></a>
                    <a href="../data-schema/" class="btn btn-secondary"><span>Data Schema Reference</span></a>
                    <a href="../python-examples/" class="btn btn-secondary"><span>Python &amp; Polars Examples</span></a>
                </div>
            </section>

            <section class="section" id="statistics">
                <div class="section-header">
                    <span class="section-eyebrow">Dataset Coverage</span>
                    <h2 class="section-title">All 7 Vietlott Lottery Datasets</h2>
                    <p class="section-description">Automatically synchronized with the repository NDJSON files in <code>data/*.jsonl</code></p>
                </div>
                <div class="card" style="padding: 0; overflow: hidden;">
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Product</th>
                                    <th>Total Draws (Days)</th>
                                    <th>Start Date</th>
                                    <th>Latest Date</th>
                                    <th>Total Records</th>
                                </tr>
                            </thead>
                            <tbody>
%s
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <section class="section" id="products">
                <div class="section-header">
                    <span class="section-eyebrow">Individual Product Pages</span>
                    <h2 class="section-title">Dedicated Dataset Pages &amp; Raw Downloads</h2>
                </div>
                <div class="stats-table">
                    <table>
                        <thead>
                            <tr>
                                <th>Product</th>
                                <th>Result Structure</th>
                                <th>Dedicated Page</th>
                                <th>Raw NDJSON</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Power 6/55</strong></td><td>7 ints: 6 main numbers (1–55) + 1 bonus number (7th element)</td><td><a href="../power-6-55/">/power-6-55/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/power655.jsonl">power655.jsonl</a></td></tr>
                            <tr><td><strong>Mega 6/45</strong></td><td>6 ints: 6 winning numbers (1–45), <strong>no bonus number</strong></td><td><a href="../mega-6-45/">/mega-6-45/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/power645.jsonl">power645.jsonl</a></td></tr>
                            <tr><td><strong>Power 5/35</strong></td><td>6 ints: 5 main numbers (1–35) + 1 special number (6th element)</td><td><a href="../power-5-35/">/power-5-35/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/power535.jsonl">power535.jsonl</a></td></tr>
                            <tr><td><strong>Keno</strong></td><td>20 ints (1–80), plus <code>big_small</code> and <code>odd_even</code></td><td><a href="../keno/">/keno/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/keno.jsonl">keno.jsonl</a></td></tr>
                            <tr><td><strong>Max 3D</strong></td><td>JSON object mapping 4 prize tiers to 20 3-digit strings</td><td><a href="../max-3d/">/max-3d/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/3d.jsonl">3d.jsonl</a></td></tr>
                            <tr><td><strong>Max 3D Pro</strong></td><td>JSON object mapping 4 prize tiers to 20 3-digit strings</td><td><a href="../max-3d-pro/">/max-3d-pro/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/3d_pro.jsonl">3d_pro.jsonl</a></td></tr>
                            <tr><td><strong>Bingo18</strong></td><td>3 ints (1–6), plus <code>total</code> (3–18) and <code>large_small</code></td><td><a href="../bingo18/">/bingo18/</a></td><td><a href="https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/bingo18.jsonl">bingo18.jsonl</a></td></tr>
                        </tbody>
                    </table>
                </div>
            </section>

%s            <section class="section" id="cli">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Crawler &amp; Tooling: Go (Recommended) vs Python</h2>
                    <p style="margin-bottom: 1rem;"><strong>Go Crawler (Recommended):</strong> Production crawling and rendering run on the standalone Go binary (<code>bin/vietlott-crawler</code>), which is ~1.7&times; faster and uses &lt;2 MB RAM. Because Vietlott geo-blocks non-Vietnam IP addresses, crawling runs on a local runner in Vietnam and commits daily updates to GitHub.</p>
                    <p><strong>Python Package:</strong> The <code>vietlott-data</code> package on PyPI provides Python schemas and legacy CLI commands (<code>vietlott-crawl</code>, <code>vietlott-missing</code>) for Python workflows.</p>
                </div>
            </section>
        </main>
`, latestDate, rows, daysSection) + pageFooterHTML
}

func renderDataSchemaPage() string {
	title := "Vietlott Data Schema Reference — NDJSON Field Definitions & Examples"
	desc := "Complete schema specification for all 7 Vietlott NDJSON datasets: Power 6/55, Mega 6/45, Power 5/35, Keno, Max 3D, Max 3D Pro, and Bingo18."
	header := pageHeaderHTML(title, desc, "data-schema/", "en", "", "")

	return header + `        <main class="container">
            <section class="hero-section">
                <div class="hero-pill">
                    <span class="status-dot"></span>
                    <span>Technical Specification</span>
                </div>
                <h1 class="hero-title">NDJSON Data Schema Reference</h1>
                <p class="hero-subtitle">Exact field definitions, data types, and winning-number semantics for all seven Vietlott lottery datasets in <code>data/*.jsonl</code>.</p>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Common Record Fields</h2>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Field</th>
                                    <th>Type</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><code>date</code></td><td><code>string (YYYY-MM-DD)</code></td><td>Official draw date in Vietnam time (ICT, UTC+7).</td></tr>
                                <tr><td><code>id</code></td><td><code>string</code></td><td>Zero-padded draw identifier (5 digits for Power/Max3D, 7 digits for Bingo18, <code>#</code> + 7 digits for Keno).</td></tr>
                                <tr><td><code>result</code></td><td><code>array&lt;int&gt; | object</code></td><td>Winning numbers for the draw. Structure depends on the specific game (detailed below).</td></tr>
                                <tr><td><code>process_time</code></td><td><code>string (ISO-8601)</code></td><td>Timestamp when the record was crawled/processed (present on Power 6/55, Mega 6/45, Power 5/35, Bingo18).</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 1rem;">Per-Product <code>result</code> Semantics</h2>
                    <div class="stats-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Product</th>
                                    <th>File</th>
                                    <th><code>result</code> Type</th>
                                    <th>Exact Semantics &amp; Bonus Number Rules</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong><a href="../power-6-55/">Power 6/55</a></strong></td>
                                    <td><code>data/power655.jsonl</code></td>
                                    <td><code>int[7]</code></td>
                                    <td>First 6 elements (<code>result[0:6]</code>) are main numbers (1–55). The <strong>7th element (<code>result[6]</code>) is the special/bonus number</strong> (Jackpot 2).</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../mega-6-45/">Mega 6/45</a></strong></td>
                                    <td><code>data/power645.jsonl</code></td>
                                    <td><code>int[6]</code></td>
                                    <td>6 main winning numbers (1–45). <strong>Mega 6/45 has NO bonus/special number.</strong> All 6 elements are main numbers.</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../power-5-35/">Power 5/35</a></strong></td>
                                    <td><code>data/power535.jsonl</code></td>
                                    <td><code>int[6]</code></td>
                                    <td>First 5 elements (<code>result[0:5]</code>) are main numbers (1–35). The <strong>6th element (<code>result[5]</code>) is the special number</strong>.</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../keno/">Keno</a></strong></td>
                                    <td><code>data/keno.jsonl</code></td>
                                    <td><code>int[20]</code></td>
                                    <td>20 winning numbers drawn from 1–80. Also includes top-level <code>big_small</code> and <code>odd_even</code> strings.</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../max-3d/">Max 3D</a></strong></td>
                                    <td><code>data/3d.jsonl</code></td>
                                    <td><code>map&lt;string, string[]&gt;</code></td>
                                    <td>Object with 4 prize keys: <code>"Giải Đặc biệt"</code> (2 triplets), <code>"Giải Nhất"</code> (4), <code>"Giải Nhì"</code> (6), <code>"Giải ba"</code> (8) — 20 zero-padded 3-digit strings total.</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../max-3d-pro/">Max 3D Pro</a></strong></td>
                                    <td><code>data/3d_pro.jsonl</code></td>
                                    <td><code>map&lt;string, string[]&gt;</code></td>
                                    <td>Same 4 prize keys and 20 3-digit string triplets as Max 3D.</td>
                                </tr>
                                <tr>
                                    <td><strong><a href="../bingo18/">Bingo18</a></strong></td>
                                    <td><code>data/bingo18.jsonl</code></td>
                                    <td><code>int[3]</code></td>
                                    <td>3 numbers from 1–6, accompanied by top-level <code>total</code> (sum 3–18) and <code>large_small</code> (<code>"Nhỏ"</code>, <code>"Hòa"</code>, <code>"Lớn"</code>).</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">Sample Records (All 7 Games)</h2>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header"><span class="code-card-title">jsonl</span></div>
                        <pre class="code-block"><code>// Power 6/55 (6 main + 1 bonus)
{"date":"2026-10-29","id":"01417","result":[9,29,33,38,45,46,53],"process_time":"2026-10-29T12:00:05Z"}

// Mega 6/45 (6 main, NO bonus)
{"date":"2026-10-28","id":"01581","result":[1,9,11,28,33,42],"process_time":"2026-10-28T12:00:07Z"}

// Power 5/35 (5 main + 1 special)
{"date":"2026-10-29","id":"00976","result":[5,13,22,26,35,3],"process_time":"2026-10-30T00:00:07Z"}

// Keno (20 numbers from 1-80)
{"date":"2026-10-30","id":"#0301098","result":[1,4,5,6,8,13,18,20,23,24,25,29,34,41,42,49,57,75,79,80],"big_small":"Lẻ (11)","odd_even":"Nhỏ (13)"}

// Max 3D &amp; Max 3D Pro (4 prize tiers -> 20 3-digit strings)
{"date":"2026-10-28","id":"01151","result":{"Giải Nhì":["335","265","268","222","917","484"],"Giải Nhất":["621","118","707","412"],"Giải ba":["099","875","590","161","801","076","841","957"],"Giải Đặc biệt":["692","005"]}}

// Bingo18 (3 numbers 1-6 + sum)
{"date":"2026-10-30","id":"0193681","result":[3,5,5],"total":13,"large_small":"Lớn","process_time":"2026-10-30T00:00:28Z"}</code></pre>
                    </div>
                </div>
            </section>
        </main>
` + pageFooterHTML
}

func renderPythonExamplesPage() string {
	title := "Analyze Vietlott Data with Python, Polars & Pandas — Vietlott Data"
	desc := "Code examples for loading and analyzing Vietlott NDJSON lottery datasets using Python, Polars, Pandas, and DuckDB."
	header := pageHeaderHTML(title, desc, "python-examples/", "en", "", "")

	return header + `        <main class="container">
            <section class="hero-section">
                <div class="hero-pill">
                    <span class="status-dot"></span>
                    <span>Developer Guide</span>
                </div>
                <h1 class="hero-title">Python, Polars &amp; Pandas Examples</h1>
                <p class="hero-subtitle">Practical recipes for loading Vietlott NDJSON files, separating main vs. bonus numbers, streaming large Keno datasets, and detecting missing draw IDs.</p>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">1. Load Power 6/55 &amp; Separate Main vs. Bonus Numbers (Polars)</h2>
                    <p style="margin-bottom: 0.75rem;">In Power 6/55, <code>result</code> has 7 elements (6 main numbers + 1 bonus number). In Mega 6/45, all 6 elements are main numbers.</p>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header"><span class="code-card-title">python (polars)</span></div>
                        <pre class="code-block"><code>import polars as pl

df = pl.read_ndjson("https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/power655.jsonl")
df = df.with_columns([
    pl.col("date").str.to_date(),
    pl.col("result").list.slice(0, 6).alias("main_numbers"),
    pl.col("result").list.get(6).alias("bonus_number"),
])

# Main number frequency (excluding the 7th bonus ball)
main_freq = (
    df.explode("main_numbers")
    .group_by("main_numbers")
    .len()
    .sort("len", descending=True)
)
print(main_freq.head(10))</code></pre>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">2. Stream High-Volume Keno Data Without Memory Spikes</h2>
                    <p style="margin-bottom: 0.75rem;">Keno has over 90,000 draws. Use Polars lazy scanning (<code>pl.scan_ndjson</code>) or DuckDB to filter and aggregate in streaming fashion:</p>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header"><span class="code-card-title">python (polars lazy scan)</span></div>
                        <pre class="code-block"><code>import polars as pl

keno_lazy = pl.scan_ndjson("data/keno.jsonl")
recent_freq = (
    keno_lazy
    .filter(pl.col("date") &gt;= "2026-01-01")
    .explode("result")
    .group_by("result")
    .len()
    .sort("len", descending=True)
    .collect()
)
print(recent_freq.head(10))</code></pre>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">3. Analyze Mega 6/45 with Pandas</h2>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header"><span class="code-card-title">python (pandas)</span></div>
                        <pre class="code-block"><code>import pandas as pd

url = "https://raw.githubusercontent.com/vietvudanh/vietlott-data/main/data/power645.jsonl"
df = pd.read_json(url, lines=True)
df["date"] = pd.to_datetime(df["date"])

# Mega 6/45 has 6 main numbers and no bonus number
freq = df.explode("result")["result"].value_counts()
print(freq.head(10))</code></pre>
                    </div>
                </div>
            </section>

            <section class="section">
                <div class="card">
                    <h2 class="section-title" style="margin-bottom: 0.75rem;">4. Detect Missing Draw IDs</h2>
                    <div class="code-card" style="margin-bottom: 0;">
                        <div class="code-card-header"><span class="code-card-title">python</span></div>
                        <pre class="code-block"><code>import polars as pl

df = pl.read_ndjson("data/power655.jsonl")
ids = set(df["id"].str.strip_chars("#").cast(pl.Int64).to_list())
expected = set(range(min(ids), max(ids) + 1))
missing = sorted(expected - ids)
print(f"Missing draws: {missing}")</code></pre>
                    </div>
                </div>
            </section>
        </main>
` + pageFooterHTML
}

func writePageFile(root, relDir, content string) error {
	dir := filepath.Join(root, "docs", relDir)
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return err
	}
	return os.WriteFile(filepath.Join(dir, "index.html"), []byte(content), 0o644)
}
