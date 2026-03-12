#!/usr/bin/env python
"""
Docs HTML Generator for Vietlott Data Project

This script updates the docs/index.html file with current data statistics
from the data folder, keeping the HTML structure and styling intact.
"""

import re
from pathlib import Path

import polars as pl
from loguru import logger

from vietlott.config.products import get_config

BLOG_POST_URL = "https://open.substack.com/pub/vietvudanh/p/minh-a-tao-repo-vietlott-data-the"
BLOG_POST_BADGE = f"""
                    <a
                        href="{BLOG_POST_URL}"
                        class="badge"
                        target="_blank"
                    >
                        <span
                            data-vi="📝 Bài viết Blog"
                            data-en="📝 Blog Post"
                            >📝 Bài viết Blog</span
                        >
                    </a>"""

ML_README_URL = "https://github.com/vietvudanh/vietlott-data/blob/main/src/machine_learning"


class DocsRenderer:
    """Main class for updating the docs/index.html file with current data."""

    def _load_lottery_data(self, product: str) -> pl.DataFrame:
        """Load and prepare lottery data for analysis."""
        try:
            df = pl.read_ndjson(get_config(product).raw_path)

            # Normalize/parse date column which can be in multiple formats
            if "date" in df.columns:
                # Try to parse the date column
                try:
                    # Check if it's already a date type
                    if df["date"].dtype in [pl.Date, pl.Datetime]:
                        df = df.with_columns(pl.col("date").cast(pl.Date))
                    # Check if it's numeric (epoch time)
                    elif df["date"].dtype in [pl.Int64, pl.Int32, pl.Float64]:
                        # Check if values are in milliseconds or seconds
                        max_val = df["date"].max()
                        if max_val > 1_000_000_000_000:
                            # milliseconds
                            df = df.with_columns(
                                (pl.col("date").cast(pl.Int64) / 1000).cast(pl.Datetime("ms")).cast(pl.Date)
                            )
                        else:
                            # seconds
                            df = df.with_columns(pl.col("date").cast(pl.Int64).cast(pl.Datetime("s")).cast(pl.Date))
                    else:
                        # String date - try to parse
                        df = df.with_columns(pl.col("date").str.to_date(strict=False))
                except Exception as e:
                    logger.warning(f"Could not parse date column: {e}")
                    # Fallback: try string parsing
                    df = df.with_columns(pl.col("date").str.to_date(strict=False))

            df = df.sort(["date", "id"], descending=True)
            return df
        except Exception as e:
            logger.error(f"Error loading data for {product}: {e}")
            return pl.DataFrame()

    def _get_data_stats(self):
        """Generate overview statistics for all products."""
        products = ["power_655", "power_645", "power_535", "keno", "3d", "3d_pro", "bingo18"]
        data_stats = []

        for product in products:
            try:
                df = self._load_lottery_data(product)
                if not df.is_empty():
                    data_stats.append(
                        {
                            "product": product,
                            "name": product.replace("_", " ").title(),
                            "total_draws": df["date"].n_unique(),
                            "start_date": str(df["date"].min()),
                            "end_date": str(df["date"].max()),
                            "total_records": df["id"].n_unique(),
                        }
                    )
            except Exception as e:
                logger.warning(f"Could not load stats for {product}: {e}")

        return data_stats

    def _calculate_days_since_last_appearance(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculate days since last appearance for each number."""
        if df.is_empty():
            return pl.DataFrame()

        latest_date = df["date"].max()
        df_explode = df.explode("result")
        last_appearance = df_explode.group_by("result").agg(pl.col("date").max().alias("last_date"))
        last_appearance = last_appearance.with_columns(
            (pl.lit(latest_date) - pl.col("last_date")).dt.total_days().alias("days_since")
        )
        last_appearance = last_appearance.sort("days_since", descending=True)
        return last_appearance

    def _format_number(self, num: int) -> str:
        """Format number with thousand separators."""
        return f"{num:,}"

    def _generate_table_rows(self, stats_list) -> str:
        """Generate HTML table rows from stats."""
        rows = []
        product_name_map = {
            "Power 655": "Power 655",
            "Power 645": "Power 645",
            "Power 535": "Power 535",
            "Keno": "Keno",
            "3D": "3D",
            "3D Pro": "3D Pro",
            "Bingo18": "Bingo18",
        }

        for stat in stats_list:
            name = product_name_map.get(stat["name"], stat["name"])
            row = f"""                                <tr>
                                    <td><strong>{name}</strong></td>
                                    <td>{self._format_number(stat["total_draws"])}</td>
                                    <td>{stat["start_date"]}</td>
                                    <td>{stat["end_date"]}</td>
                                    <td>{self._format_number(stat["total_records"])}</td>
                                </tr>"""
            rows.append(row)

        return "\n".join(rows)

    def _generate_days_since_rows(self, days_since_df: pl.DataFrame) -> str:
        """Generate HTML table rows for days-since-last-appearance data."""
        rows = []
        for row in days_since_df.iter_rows(named=True):
            rows.append(
                f"""                                <tr>
                                    <td><strong>{row["result"]}</strong></td>
                                    <td>{row["last_date"]}</td>
                                    <td>{row["days_since"]}</td>
                                </tr>"""
            )
        return "\n".join(rows)

    def _generate_days_since_section(self, df: pl.DataFrame) -> str:
        """Generate the full HTML section for days-since-last-appearance analysis."""
        if df.is_empty():
            return ""

        days_since = self._calculate_days_since_last_appearance(df)
        top10 = days_since.head(10)
        all_numbers = days_since.sort("result")

        top10_rows = self._generate_days_since_rows(top10)
        all_rows = self._generate_days_since_rows(all_numbers)

        return f"""<!-- BEGIN_DAYS_SINCE_SECTION -->
            <section class="section">
                <h2
                    class="section-title"
                    data-vi="⏳ Phân tích Power 6/55 - Số ngày vắng mặt"
                    data-en="⏳ Power 6/55 - Days Since Last Appearance"
                >
                    ⏳ Power 6/55 - Days Since Last Appearance
                </h2>
                <div class="card">
                    <h3
                        data-vi="🔟 Top 10 số lâu chưa xuất hiện"
                        data-en="🔟 Top 10 Numbers by Days Since Last Appearance"
                    >
                        🔟 Top 10 số lâu chưa xuất hiện
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
{top10_rows}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="card" style="margin-top:1rem">
                    <h3
                        data-vi="📆 Số ngày từ lần xuất hiện cuối cùng (tất cả các số)"
                        data-en="📆 Days Since Last Appearance (All Numbers)"
                    >
                        📆 Số ngày từ lần xuất hiện cuối cùng (tất cả các số)
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
{all_rows}
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
            <!-- END_DAYS_SINCE_SECTION -->"""

    def update_docs_html(self, html_path: Path = None) -> None:
        """Update the docs/index.html file with current data."""
        if html_path is None:
            html_path = Path("./docs/index.html")

        try:
            logger.info(f"Reading HTML from {html_path}")
            with html_path.open("r", encoding="utf-8") as f:
                html_content = f.read()

            # Get current stats
            logger.info("Fetching current data statistics...")
            stats = self._get_data_stats()

            # Generate new table rows
            new_rows = self._generate_table_rows(stats)

            # Find and replace the tbody content
            # Look for <tbody> ... </tbody> pattern
            pattern = r"(<tbody>).*?(</tbody>)"
            replacement = f"\\1\n{new_rows}\n                            \\2"

            updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

            # Update days-since-last-appearance section for Power 6/55
            logger.info("Generating days-since-last-appearance analysis for Power 6/55...")
            df_power655 = self._load_lottery_data("power_655")
            days_since_section = self._generate_days_since_section(df_power655)
            days_since_pattern = r"<!-- BEGIN_DAYS_SINCE_SECTION -->.*?<!-- END_DAYS_SINCE_SECTION -->"
            updated_html = re.sub(days_since_pattern, days_since_section, updated_html, flags=re.DOTALL)

            # Ensure blog post badge is present in the badges section
            if BLOG_POST_URL not in updated_html:
                badges_pattern = r'(<div class="badges">.*?)(</div>)'
                updated_html = re.sub(
                    badges_pattern,
                    f"\\1{BLOG_POST_BADGE}\n                \\2",
                    updated_html,
                    flags=re.DOTALL,
                )

            ml_section = f"""<!-- BEGIN_MACHINE_LEARNING_SECTION -->
            <section class="section">
                <h2
                    class="section-title"
                    data-vi="🔮 Phân tích Machine Learning"
                    data-en="🔮 Machine Learning Predictions"
                >
                    🔮 Phân tích Machine Learning
                </h2>
                <div class="card">
                    <p
                        data-vi="Các dự đoán máy học chi tiết nằm trong README Machine Learning."
                        data-en="Detailed machine learning predictions live in the Machine Learning README."
                    >
                        Các dự đoán máy học chi tiết nằm trong
                        <a href="{ML_README_URL}" target="_blank" rel="noreferrer"
                            >README Machine Learning</a
                        >.
                    </p>
                </div>
            </section>
            <!-- END_MACHINE_LEARNING_SECTION -->"""
            ml_pattern = r"<!-- BEGIN_MACHINE_LEARNING_SECTION -->.*?<!-- END_MACHINE_LEARNING_SECTION -->"
            if re.search(ml_pattern, updated_html, flags=re.DOTALL):
                updated_html = re.sub(ml_pattern, ml_section, updated_html, flags=re.DOTALL)

            # Save the updated HTML
            with html_path.open("w", encoding="utf-8") as f:
                f.write(updated_html)

            logger.info(f"Successfully updated {html_path}")
            logger.info("Data statistics updated:")
            for stat in stats:
                logger.info(
                    f"  {stat['name']}: {stat['total_draws']} draws, "
                    f"{stat['start_date']} to {stat['end_date']}, "
                    f"{stat['total_records']} records"
                )

        except Exception as e:
            logger.error(f"Error updating docs HTML: {e}")
            raise


def main():
    """Main entry point for docs HTML generation."""
    try:
        renderer = DocsRenderer()
        renderer.update_docs_html()
        logger.info("Docs HTML update completed successfully!")
    except Exception as e:
        logger.error(f"Failed to update docs HTML: {e}")
        raise


if __name__ == "__main__":
    main()
