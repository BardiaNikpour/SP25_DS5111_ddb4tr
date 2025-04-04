"""
normalize_csv.py

This script normalizes stock gainer CSV files by:
- Removing unnamed columns
- Renaming specific columns to a consistent format
- Validating required data presence
- Writing a cleaned version to a new CSV file
"""

import os
import sys
import logging
import pandas as pd  # third-party imports go after standard lib

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

COLUMN_MAPPING = {
    'Symbol': 'symbol',
    'Price': 'price',
    'Change': 'price_change',
    'Change %': 'price_percent_change'
}

def normalize_csv(file_path):
    """Normalize CSV by renaming columns and removing unnamed ones."""
    assert isinstance(file_path, str), "Input path must be a string"
    assert os.path.exists(file_path), f"File does not exist: {file_path}"
    assert file_path.endswith('.csv'), "Input file must be a CSV"

    try:
        df = pd.read_csv(file_path)
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as exc:
        logging.error("Error reading CSV file: %s", exc)
        sys.exit(1)

    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Rename columns based on mapping
    df.rename(columns=COLUMN_MAPPING, inplace=True)

    # Check if all required columns exist
    missing_columns = set(COLUMN_MAPPING.values()) - set(df.columns)
    if missing_columns:
        logging.error("Missing required columns: %s", missing_columns)
        sys.exit(1)

    output_csv_path = file_path.replace('.csv', '_norm.csv')
    df[list(COLUMN_MAPPING.values())].to_csv(output_csv_path, index=False)

    logging.info("Normalized CSV saved to: %s", output_csv_path)
    return output_csv_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python3 bin/normalize_csv.py <path to raw gainers csv>")
        sys.exit(1)

    path = sys.argv[1]
    normalize_csv(path)
