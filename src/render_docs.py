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
                                    <td>{self._format_number(stat['total_draws'])}</td>
                                    <td>{stat['start_date']}</td>
                                    <td>{stat['end_date']}</td>
                                    <td>{self._format_number(stat['total_records'])}</td>
                                </tr>"""
            rows.append(row)

        return "\n".join(rows)

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
