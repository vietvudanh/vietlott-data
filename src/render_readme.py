#!/usr/bin/env python
"""
README Generator for Vietlott Data Project

This script generates a comprehensive README.md file for the GitHub repository
frontpage, including data statistics and project information.
"""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import polars as pl
from loguru import logger

from vietlott.config.products import get_config


class ReadmeTemplates:
    """Container for README template strings and formatting."""

    @staticmethod
    def get_header() -> str:
        """Get the main header with badges and description."""
        return """# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/vietvudanh/vietlott-data/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://vietvudanh.github.io/vietlott-data/)

> 📊 **Automated Vietnamese Lottery Data Collection & Analysis**
>
> This project automatically crawls and analyzes Vietnamese lottery data from [vietlott.vn](https://vietlott.vn/), providing comprehensive statistics and insights for all major lottery products.

## 🎯 Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Power 5/35** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535) | Choose 5 numbers from 1-35 |
| **Keno** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |
| **Bingo18** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18) | 3 numbers from 0-9 game |
"""

    @staticmethod
    def get_toc() -> str:
        """Get table of contents."""
        return """## 📋 Table of Contents

- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [📊 Data Statistics](#-data-statistics)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)
"""

    @staticmethod
    def get_how_it_works() -> str:
        """Get how it works section."""
        return """## ⚙️ How It Works

### 🤖 Automated Data Collection

This project runs completely automatically using **GitHub Actions** - no server required!

- **⏰ Schedule**: Runs daily via [GitHub Actions workflow](.github/workflows/crawl.yaml)
- **🔄 Process**: Fetches latest results → Processes data → Commits to repository
- **📊 Analysis**: Generates statistics and updates README automatically

### 🕵️ Data Crawling Method

The data collection works by:
1. **🔍 Network Analysis**: Inspecting browser-server communication
2. **🐍 Python Replication**: Recreating the data fetch logic in Python
3. **📋 Structured Storage**: Saving results in JSONL format for easy analysis
4. **🔄 Continuous Updates**: Daily automated runs ensure fresh data

> **Note**: This is purely for educational and research purposes. No gambling advice is provided.
"""

    @staticmethod
    def get_install_section() -> str:
        """Get installation section."""
        return """## 🚀 Installation & Usage

### 📦 Install via pip

```bash
pip install -i vietlott-data
```

### 💻 Command Line Interface

#### 🔍 Crawl Data

```bash
vietlott-crawl [OPTIONS] PRODUCT

# Options:
#   --run-date TEXT       Specific date to crawl (default: current date)
#   --index-from INTEGER  Starting page index (default: 0)
#   --index-to INTEGER    Ending page index (default: None)
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process (default: 20)
#   --help          Show help message
```

> **Available Products**: power_655, power_645, power_535, keno, 3d, 3d_pro, bingo18

### 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/vietvudanh/vietlott-data.git ; cd vietlott-data

# Install dependencies (recommend using uv and virtual environment)
uv sync --dev

# Run tests
uv run pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>
"""


def df_to_markdown(df: pl.DataFrame) -> str:
    """Convert Polars DataFrame to Markdown table format."""
    if df.is_empty():
        return "No data available"

    # Get column names
    columns = df.columns

    # Build header
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"

    # Build rows
    rows = []
    for row in df.iter_rows(named=False):
        row_str = "| " + " | ".join(str(val) if val is not None else "" for val in row) + " |"
        rows.append(row_str)

    return "\n".join([header, separator] + rows)


class ReadmeGenerator:
    """Main class for generating the README.md file."""

    def __init__(self):
        self.templates = ReadmeTemplates()

    def _balance_long_df(self, df_: pl.DataFrame, n_splits: int = 20) -> pl.DataFrame:
        """Convert long dataframe to multiple columns for better display."""
        if df_.is_empty():
            return df_

        # Convert all columns to string for display
        df_ = df_.with_columns([pl.col(c).cast(pl.Utf8) for c in df_.columns])

        total_rows = df_.height
        num_chunks = (total_rows // n_splits) + (1 if total_rows % n_splits else 0)

        if num_chunks <= 1:
            return df_

        # Create chunks
        result_frames = []

        for i in range(num_chunks):
            start_idx = i * n_splits
            end_idx = min((i + 1) * n_splits, total_rows)
            chunk = df_.slice(start_idx, end_idx - start_idx)

            if i == 0:
                result_frames.append(chunk)
            else:
                # Add separator column
                separator = pl.DataFrame({f"-{i}": [""] * chunk.height})
                # Rename chunk columns to add prefix
                chunk_renamed = chunk.select([pl.col(c).alias(f"{i}{c}") for c in chunk.columns])
                result_frames.extend([separator, chunk_renamed])

        # Combine horizontally - pad shorter frames with empty strings
        max_height = max(frame.height for frame in result_frames)

        padded_frames = []
        for frame in result_frames:
            if frame.height < max_height:
                # Create padding rows
                padding_rows = max_height - frame.height
                padding_data = {col: [""] * padding_rows for col in frame.columns}
                padding_df = pl.DataFrame(padding_data)
                frame = pl.concat([frame, padding_df])
            padded_frames.append(frame)

        # Concatenate horizontally
        result = pl.concat(padded_frames, how="horizontal")

        return result

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

    def _calculate_stats(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculate number frequency statistics."""
        if df.is_empty():
            return pl.DataFrame()

        df_explode = df.explode("result")
        stats = df_explode.group_by("result").agg(pl.count("id").alias("count"))
        total_count = df_explode.height
        stats = stats.with_columns(((pl.col("count") / total_count * 100).round(2)).alias("%"))
        stats = stats.sort("result")
        return stats

    def _get_data_overview(self) -> str:
        """Generate overview statistics for all products."""
        products = ["power_655", "power_645", "power_535", "keno", "3d", "3d_pro", "bingo18"]
        data_stats = []

        for product in products:
            try:
                df = self._load_lottery_data(product)
                if not df.is_empty():
                    data_stats.append(
                        {
                            "Product": product.replace("_", " ").title(),
                            "Total Draws": df["date"].n_unique(),
                            "Start Date": str(df["date"].min()),
                            "End Date": str(df["date"].max()),
                            "Total Records": df["id"].n_unique(),
                            "First ID": str(df["id"].min()),
                            "Latest ID": str(df["id"].max()),
                        }
                    )
            except Exception as e:
                logger.warning(f"Could not load stats for {product}: {e}")

        if data_stats:
            df_stats = pl.DataFrame(data_stats)
            return df_to_markdown(df_stats)
        return "No data available"

    def _generate_power655_analysis(self, df: pl.DataFrame) -> str:
        """Generate detailed Power 6/55 analysis section."""
        if df.is_empty():
            return "## 📈 Power 6/55 Analysis\n\n> No data available for analysis.\n"

        try:
            # Calculate stats for different periods
            stats_all = self._balance_long_df(self._calculate_stats(df))

            current_date = datetime.now().date()
            stats_30d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=30))))
            )
            stats_60d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=60))))
            )
            stats_90d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=90))))
            )

            recent_results = df.head(10)

            # Convert to markdown
            recent_results_md = df_to_markdown(recent_results)
            stats_all_md = df_to_markdown(stats_all)
            stats_30d_md = df_to_markdown(stats_30d)
            stats_60d_md = df_to_markdown(stats_60d)
            stats_90d_md = df_to_markdown(stats_90d)

            return f"""## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
{recent_results_md}

### 🎲 Number Frequency (All Time)
{stats_all_md}

### 📊 Frequency Analysis by Period

#### Last 30 Days
{stats_30d_md}

#### Last 60 Days
{stats_60d_md}

#### Last 90 Days
{stats_90d_md}

"""
        except Exception as e:
            logger.exception(f"Error generating Power 6/55 analysis: {e}")
            return "## 📈 Power 6/55 Analysis\n\n> Error generating analysis.\n"

    def generate_readme(self) -> str:
        """Generate the complete README content."""
        logger.info("Starting README generation...")

        # Load Power 6/55 data (main focus)
        df_power655 = self._load_lottery_data("power_655")

        # Generate all sections
        header = self.templates.get_header()
        toc = self.templates.get_toc()
        data_overview = self._get_data_overview()
        power655_analysis = self._generate_power655_analysis(df_power655)
        how_it_works = self.templates.get_how_it_works()
        install_section = self.templates.get_install_section()

        # Combine all sections
        readme_content = f"""{header}

{toc}

## 📊 Data Statistics

{data_overview}

{power655_analysis}

{how_it_works}

{install_section}
"""

        return readme_content

    def save_readme(self, output_path: Optional[Path] = None) -> None:
        """Generate and save README to file."""
        if output_path is None:
            output_path = Path("./readme.md")

        try:
            readme_content = self.generate_readme()

            with output_path.open("w", encoding="utf-8") as ofile:
                ofile.write(readme_content)

            logger.info(f"README successfully written to {output_path.absolute()}")
        except Exception as e:
            logger.error(f"Error saving README: {e}")
            raise


def main():
    """Main entry point for README generation."""
    try:
        generator = ReadmeGenerator()
        generator.save_readme()
        logger.info("README generation completed successfully!")
    except Exception as e:
        logger.error(f"Failed to generate README: {e}")
        raise


if __name__ == "__main__":
    main()
