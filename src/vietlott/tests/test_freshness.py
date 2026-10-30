"""Tests for dataset freshness, SEO metadata, schema documentation, and sitemap consistency."""

import json
import re
from pathlib import Path

import polars as pl

from vietlott.config.products import get_config

REPO_ROOT = Path(__file__).resolve().parents[3]


def _compute_expected_stats() -> list[dict[str, str | int]]:
    """Compute expected statistics directly from the raw NDJSON files in data/."""
    products = [
        ("power_655", "Power 655"),
        ("power_645", "Power 645"),
        ("power_535", "Power 535"),
        ("keno", "Keno"),
        ("3d", "3D"),
        ("3d_pro", "3D Pro"),
        ("bingo18", "Bingo18"),
    ]
    stats: list[dict[str, str | int]] = []
    for key, label in products:
        df = pl.read_ndjson(get_config(key).raw_path)
        dates = df["date"].cast(pl.Utf8)
        stats.append(
            {
                "key": key,
                "label": label,
                "total_draws": dates.n_unique(),
                "start_date": str(dates.min()),
                "end_date": str(dates.max()),
                "total_records": df["id"].n_unique(),
            }
        )
    return stats


def test_docs_and_readme_statistics_match_data() -> None:
    """Verify that docs/index.html, docs/en/index.html, and readme.md match data/*.jsonl."""
    stats = _compute_expected_stats()
    docs_html = (REPO_ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    en_html = (REPO_ROOT / "docs" / "en" / "index.html").read_text(encoding="utf-8")
    readme_md = (REPO_ROOT / "readme.md").read_text(encoding="utf-8")

    for item in stats:
        label = str(item["label"])
        draws_fmt = f"{int(item['total_draws']):,}"
        records_fmt = f"{int(item['total_records']):,}"
        start_date = str(item["start_date"])
        end_date = str(item["end_date"])

        expected_row_snippet = (
            f"<td><strong>{label}</strong></td>\n"
            f"                                    <td>{draws_fmt}</td>\n"
            f"                                    <td>{start_date}</td>\n"
            f"                                    <td>{end_date}</td>\n"
            f"                                    <td>{records_fmt}</td>"
        )
        assert expected_row_snippet in docs_html, f"Stale stats in docs/index.html for {label}"
        assert expected_row_snippet in en_html, f"Stale stats in docs/en/index.html for {label}"

        readme_row = f"| {label} | {item['total_draws']} | {start_date} | {end_date} | {item['total_records']} |"
        assert readme_row in readme_md, f"Stale stats in readme.md for {label}"

    print("Verified docs/index.html, docs/en/index.html, and readme.md statistics match data/*.jsonl.")


def test_jsonld_and_freshness_badge_synchronized() -> None:
    """Verify JSON-LD Dataset schema validity and synchronization with latest draw date."""
    stats = _compute_expected_stats()
    latest_date = max(str(item["end_date"]) for item in stats)
    docs_html = (REPO_ROOT / "docs" / "index.html").read_text(encoding="utf-8")

    assert f"Data last updated: {latest_date}" in docs_html
    assert f"Dữ liệu mới nhất: {latest_date}" in docs_html

    match = re.search(
        r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
        docs_html,
        flags=re.DOTALL,
    )
    assert match is not None, "Missing JSON-LD script block in docs/index.html"
    payload = json.loads(match.group(1))
    graph = payload.get("@graph", [])
    datasets = [node for node in graph if node.get("@type") == "Dataset"]
    assert len(datasets) == 1, "Expected exactly 1 Dataset node in JSON-LD @graph"

    dataset = datasets[0]
    assert dataset.get("identifier") == "https://github.com/vietvudanh/vietlott-data"
    assert dataset.get("datePublished") == "2021-04-01"
    assert dataset.get("dateModified") == latest_date
    assert dataset.get("temporalCoverage") == f"2017-08-01/{latest_date}"
    assert len(dataset.get("distribution", [])) == 7
    print("Verified JSON-LD Dataset schema and freshness badge synchronization.")


def test_mega645_and_product_schema_accuracy() -> None:
    """Verify that Mega 6/45 is documented with 6 numbers (no bonus) in data and docs."""
    mega_df = pl.read_ndjson(get_config("power_645").raw_path)
    lengths = mega_df["result"].list.len().unique().to_list()
    assert lengths == [6], f"Expected Mega 6/45 result arrays to have length 6, got {lengths}"

    p655_df = pl.read_ndjson(get_config("power_655").raw_path)
    assert int(p655_df["result"].list.len().mode()[0]) == 7

    p535_df = pl.read_ndjson(get_config("power_535").raw_path)
    assert p535_df["result"].list.len().unique().to_list() == [6]

    llms_txt = (REPO_ROOT / "docs" / "llms.txt").read_text(encoding="utf-8")
    assert "Power 6/55 / Mega 6/45 / Power 5/35 the last number" not in llms_txt
    assert "mega 6/45 has no bonus/special number" in llms_txt.lower()

    schema_html = (REPO_ROOT / "docs" / "data-schema" / "index.html").read_text(encoding="utf-8")
    assert "Mega 6/45 has NO bonus/special number" in schema_html
    print("Verified Mega 6/45 and Power 6/55 schema documentation accuracy.")


def test_sitemap_and_dedicated_pages_exist() -> None:
    """Verify all URLs in docs/sitemap.xml exist as HTML pages and llms.txt is excluded."""
    sitemap_xml = (REPO_ROOT / "docs" / "sitemap.xml").read_text(encoding="utf-8")
    assert "llms.txt" not in sitemap_xml, "llms.txt should not be in sitemap.xml"

    urls = re.findall(r"<loc>(https://vietvudanh\.github\.io/vietlott-data/[^<]*)</loc>", sitemap_xml)
    assert len(urls) == 11, f"Expected 11 canonical URLs in sitemap.xml, found {len(urls)}"

    prefix = "https://vietvudanh.github.io/vietlott-data/"
    for url in urls:
        rel_dir = url.removeprefix(prefix).strip("/")
        target_html = REPO_ROOT / "docs" / rel_dir / "index.html" if rel_dir else REPO_ROOT / "docs" / "index.html"
        assert target_html.is_file(), f"Missing HTML file for sitemap URL {url}: {target_html}"
        html_text = target_html.read_text(encoding="utf-8")
        assert f'<link rel="canonical" href="{url}"' in re.sub(r"\s+", " ", html_text)

    root_index = (REPO_ROOT / "index.html").read_text(encoding="utf-8")
    assert "noindex, nofollow" in root_index
    print("Verified all 11 sitemap pages exist with self-referential canonicals.")
