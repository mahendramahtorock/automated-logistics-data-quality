"""
Root-cause-oriented anomaly analysis.
Run: python python/anomaly_detection.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/shipments_clean.csv"
OUT = ROOT / "reports/anomaly_summary.csv"

df = pd.read_csv(INPUT, parse_dates=[
    "shipment_date", "expected_arrival", "actual_arrival"
])

df["delay_days"] = (
    df["actual_arrival"] - df["expected_arrival"]
).dt.days

df["is_delay"] = (df["delay_days"] > 0).astype("Int64")

carrier_summary = (
    df.groupby("carrier", dropna=False)
      .agg(
          shipments=("shipment_id", "count"),
          delayed_shipments=("is_delay", "sum"),
          avg_delay_days=("delay_days", "mean")
      )
      .reset_index()
)

carrier_summary["delay_rate"] = (
    carrier_summary["delayed_shipments"] / carrier_summary["shipments"]
)

route_summary = (
    df.groupby(["origin", "destination"], dropna=False)
      .agg(
          shipments=("shipment_id", "count"),
          avg_delay_days=("delay_days", "mean")
      )
      .reset_index()
)

route_summary["delay_rate"] = (
    df.groupby(["origin", "destination"], dropna=False)["is_delay"].mean()
      .values
)

carrier_summary.to_csv(OUT, index=False)

print("Carrier-level anomaly / delay summary:")
print(carrier_summary.sort_values("delay_rate", ascending=False).head(10).to_string(index=False))
print("\nHighest-risk routes:")
print(route_summary.sort_values("delay_rate", ascending=False).head(10).to_string(index=False))
