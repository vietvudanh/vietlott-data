#!/usr/bin/env python
"""
Adhoc script to convert date fields from timestamp integers to date strings (YYYY-MM-DD format)
in all JSONL data files.
"""

import polars as pl
from pathlib import Path
from loguru import logger


def convert_file(file_path: Path):
    """Convert a single JSONL file's date column from timestamp to string."""
    logger.info(f"Processing {file_path.name}...")
    
    try:
        # Read the file
        df = pl.read_ndjson(file_path)
        
        # Check if date column exists
        if "date" not in df.columns:
            logger.warning(f"{file_path.name}: No 'date' column found, skipping")
            return
        
        # Check current date format
        date_dtype = df["date"].dtype
        logger.info(f"{file_path.name}: Current date dtype: {date_dtype}")
        
        # Show sample before conversion
        logger.info(f"{file_path.name}: Sample before - {df.select(['id', 'date']).head(2)}")
        
        # Convert based on current type
        if date_dtype in [pl.Int64, pl.Int32]:
            # It's a timestamp in milliseconds, convert to date string
            logger.info(f"{file_path.name}: Converting from timestamp to date string...")
            df = df.with_columns(
                pl.from_epoch(pl.col("date"), time_unit="ms").dt.strftime("%Y-%m-%d").alias("date")
            )
        elif date_dtype in [pl.Date, pl.Datetime]:
            # It's already a date/datetime type, convert to string
            logger.info(f"{file_path.name}: Converting from Date/Datetime to string...")
            df = df.with_columns(
                pl.col("date").dt.strftime("%Y-%m-%d").alias("date")
            )
        elif date_dtype == pl.Utf8:
            logger.info(f"{file_path.name}: Already string format, checking if valid...")
            # Verify it's in correct format by trying to parse
            sample = df["date"][0]
            if len(str(sample)) != 10 or '-' not in str(sample):
                logger.warning(f"{file_path.name}: String format looks incorrect: {sample}")
            else:
                logger.info(f"{file_path.name}: Already in correct format, skipping")
                return
        else:
            logger.warning(f"{file_path.name}: Unknown date dtype {date_dtype}, skipping")
            return
        
        # Show sample after conversion
        logger.info(f"{file_path.name}: Sample after - {df.select(['id', 'date']).head(2)}")
        
        # Create backup
        backup_path = file_path.with_suffix(file_path.suffix + '.backup')
        logger.info(f"{file_path.name}: Creating backup at {backup_path}")
        file_path.rename(backup_path)
        
        # Write converted data
        df.write_ndjson(file_path)
        logger.info(f"{file_path.name}: Successfully converted {len(df)} records")
        logger.info(f"{file_path.name}: Date range: {df['date'].min()} to {df['date'].max()}")
        
    except Exception as e:
        logger.error(f"{file_path.name}: Error converting file: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Convert all JSONL files in the data directory."""
    data_dir = Path(__file__).parent / "data"
    
    if not data_dir.exists():
        logger.error(f"Data directory not found: {data_dir}")
        return
    
    # Find all JSONL files
    jsonl_files = list(data_dir.glob("*.jsonl"))
    
    if not jsonl_files:
        logger.warning("No JSONL files found in data directory")
        return
    
    logger.info(f"Found {len(jsonl_files)} JSONL files to process")
    
    for file_path in sorted(jsonl_files):
        convert_file(file_path)
        logger.info("-" * 80)
    
    logger.info("Conversion complete!")
    logger.info("Backup files created with .backup extension")
    logger.info("If everything looks good, you can remove backup files with: rm data/*.backup")


if __name__ == "__main__":
    main()
