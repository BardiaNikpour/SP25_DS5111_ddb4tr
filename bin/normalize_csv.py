import os
import sys
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

COLUMN_MAPPING = {
    'Symbol': 'symbol',
    'Price': 'price',
    'Change': 'price_change',
    'Change %': 'price_percent_change'
}

def normalize_csv(input_csv_path):
    assert isinstance(input_csv_path, str), "Input path must be a string"
    assert os.path.exists(input_csv_path), f"File does not exist: {input_csv_path}"
    assert input_csv_path.endswith('.csv'), "Input file must be a CSV"

    try:
        df = pd.read_csv(input_csv_path)
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        sys.exit(1)

    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Rename columns based on mapping
    df.rename(columns=COLUMN_MAPPING, inplace=True)

    # Check if all required columns exist
    missing_columns = set(COLUMN_MAPPING.values()) - set(df.columns)
    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        sys.exit(1)

    output_csv_path = input_csv_path.replace('.csv', '_norm.csv')
    df[list(COLUMN_MAPPING.values())].to_csv(output_csv_path, index=False)

    logging.info(f"Normalized CSV saved to: {output_csv_path}")
    return output_csv_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python3 bin/normalize_csv.py <path to raw gainers csv>")
        sys.exit(1)

    input_csv_path = sys.argv[1]
    normalize_csv(input_csv_path)

