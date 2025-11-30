#!/usr/bin/env python
"""
README Generator for Vietlott Data Project

This script generates a comprehensive README.md file for the GitHub repository
frontpage, including data statistics, predictions, and project information.
"""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import polars as pl
from loguru import logger

from vietlott.config.products import get_config
from vietlott.model.strategy.random_strategy import RandomModel


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
- [🔮 Prediction Models](#-prediction-models)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [📈 Power 5/35 Analysis](#-power-535-analysis)
  - [📅 Recent Results](#-recent-results-1)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time-1)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period-1)
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
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
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
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>
"""


class ReadmeGenerator:
    """Main class for generating the README.md file."""

    def __init__(self):
        self.templates = ReadmeTemplates()

    def _balance_long_df(self, df_: pl.DataFrame, n_splits: int = 20) -> pl.DataFrame:
        """Convert long dataframe to multiple columns for better display."""
        if df_.is_empty():
            return df_

        # Convert to pandas for this complex operation that's mainly for display
        import pandas as pd

        df_pd = df_.to_pandas()

        # reset_index may return a view in some edge-cases; work on an explicit copy
        df_pd = df_pd.reset_index().copy()
        # Create converted columns in a separate DataFrame and concat them back to
        # avoid assigning object-dtype data into existing numeric columns which
        # can trigger FutureWarnings about incompatible dtype setting.
        if "result" in df_pd.columns and "count" in df_pd.columns:
            converted = pd.DataFrame(
                {
                    "result": df_pd["result"].apply(lambda x: str(x)).astype(object),
                    "count": df_pd["count"].apply(lambda x: str(x)).astype(object),
                },
                index=df_pd.index,
            )
            # drop original columns then concat converted ones to preserve order
            left = df_pd.drop(columns=["result", "count"])
            df_pd = pd.concat([left, converted], axis=1)

        final = None

        for i in range(len(df_pd) // n_splits + 1):
            dd = df_pd.iloc[i * n_splits : (i + 1) * n_splits]

            if dd.empty:
                continue

            if final is None:
                final = dd
            else:
                final = pd.concat(
                    [
                        final.reset_index(drop=True),
                        pd.DataFrame([None] * len(dd), columns=["-"]).add_prefix(str(i)),
                        dd.reset_index(drop=True).add_prefix(str(i)),
                    ],
                    axis="columns",
                )

        if final is not None:
            # ensure we operate on an explicit copy before filling
            final = final.copy().fillna("")

            # Guarantee unique, string-based column names before conversion
            seen: dict[str, int] = {}
            renamed_columns = []
            for col in final.columns:
                col_str = str(col)
                if col_str in seen:
                    seen[col_str] += 1
                    col_str = f"{col_str}_{seen[col_str]}"
                else:
                    seen[col_str] = 0
                renamed_columns.append(col_str)
            final.columns = renamed_columns

            # Convert everything to string for display to avoid numeric columns with empty strings
            data = {}
            for col in final.columns:
                col_values = []
                for value in final[col].tolist():
                    if value == "":
                        col_values.append("")
                    else:
                        col_values.append(str(value))
                data[col] = col_values

            return pl.DataFrame(data)
        else:
            return pl.DataFrame()

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
        total_count = len(df_explode)
        stats = stats.with_columns(((pl.col("count") / total_count * 100).round(2)).alias("%"))
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
            import pandas as pd

            return pd.DataFrame(data_stats).to_markdown(index=False)
        return "No data available"

    def _generate_predictions_section(self, df: pl.DataFrame) -> str:
        """Generate predictions analysis section."""
        if df.is_empty():
            return "## 🔮 Prediction Models\n\n> No data available for predictions.\n"

        try:
            import pandas as pd

            # Convert to pandas for the model (if it expects pandas)
            df_pd = df.to_pandas()

            ticket_per_days = 20
            random_model = RandomModel(df_pd, ticket_per_days)
            random_model.backtest()
            random_model.evaluate()

            # Coerce `correct_num` to integer safely before applying threshold
            if "correct_num" in random_model.df_backtest_evaluate.columns:

                def _to_int(v):
                    try:
                        return int(v)
                    except Exception:
                        try:
                            return len(v)
                        except Exception:
                            return 0

                s_correct = random_model.df_backtest_evaluate["correct_num"].apply(_to_int)
                df_correct = random_model.df_backtest_evaluate[s_correct >= 5][["date", "result", "predicted"]]
            else:
                import pandas as _pd

                df_correct = _pd.DataFrame()

            cost_per_day = 10000 * ticket_per_days

            return f"""## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: {ticket_per_days}
- **Daily cost**: {cost_per_day:,} VND
- **Results with 5+ matches**:

{df_correct.to_markdown(index=False) if not df_correct.empty else "No significant matches found in backtest period."}

"""
        except Exception as e:
            logger.error(f"Error generating predictions: {e}")
            return "## 🔮 Prediction Models\n\n> Error generating prediction analysis.\n"

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

            # Convert to pandas for markdown display
            import pandas as pd

            recent_results_pd = recent_results.to_pandas()
            stats_all_pd = stats_all.to_pandas() if not stats_all.is_empty() else pd.DataFrame()
            stats_30d_pd = stats_30d.to_pandas() if not stats_30d.is_empty() else pd.DataFrame()
            stats_60d_pd = stats_60d.to_pandas() if not stats_60d.is_empty() else pd.DataFrame()
            stats_90d_pd = stats_90d.to_pandas() if not stats_90d.is_empty() else pd.DataFrame()

            return f"""## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
{recent_results_pd.to_markdown(index=False)}

### 🎲 Number Frequency (All Time)
{stats_all_pd.to_markdown(index=False) if not stats_all_pd.empty else "No data available"}

### 📊 Frequency Analysis by Period

#### Last 30 Days
{stats_30d_pd.to_markdown(index=False) if not stats_30d_pd.empty else "No data available"}

#### Last 60 Days
{stats_60d_pd.to_markdown(index=False) if not stats_60d_pd.empty else "No data available"}

#### Last 90 Days
{stats_90d_pd.to_markdown(index=False) if not stats_90d_pd.empty else "No data available"}

"""
        except Exception as e:
            logger.exception(f"EError generating Power 6/55 analysis: {e}")
            return "## 📈 Power 6/55 Analysis\n\n> Error generating analysis.\n"

    # Removed Power 5/35 Analysis section as requested.

    def generate_readme(self) -> str:
        """Generate the complete README content."""
        logger.info("Starting README generation...")

        # Load Power 6/55 data (main focus)
        df_power655 = self._load_lottery_data("power_655")

        # Generate all sections
        header = self.templates.get_header()
        toc = self.templates.get_toc()
        data_overview = self._get_data_overview()
        predictions = self._generate_predictions_section(df_power655)
        power655_analysis = self._generate_power655_analysis(df_power655)
        how_it_works = self.templates.get_how_it_works()
        install_section = self.templates.get_install_section()

        # Combine all sections
        readme_content = f"""{header}

{toc}

## 📊 Data Statistics

{data_overview}

{predictions}

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
