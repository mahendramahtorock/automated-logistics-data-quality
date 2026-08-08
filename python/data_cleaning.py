"""
Data cleaning and standardization for logistics shipment data.
Run: python python/data_cleaning.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/shipments.csv"
OUT = ROOT / "data/processed/shipments_clean.csv"

DATE_COLS = ["shipment_date", "expected_arrival", "actual_arrival"]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in DATE_COLS:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Standardize text fields
    text_cols = ["shipment_id", "container_id", "carrier", "origin",
                 "destination", "origin_country", "destination_country", "status"]
    for col in text_cols:
        df[col] = df[col].astype("string").str.strip()

    # Keep original records; fill only fields where a safe business default exists.
    # Missing values are retained for the QA report rather than silently hidden.
    return df

if __name__ == "__main__":
    df = pd.read_csv(RAW)
    clean = clean_data(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(OUT, index=False)
    print(f"Saved {len(clean):,} records to {OUT}")
