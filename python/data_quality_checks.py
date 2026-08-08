"""
Automated logistics data-quality checks.
Run: python python/data_quality_checks.py
"""
from pathlib import Path
import pandas as pd
import json

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/shipments_clean.csv"
REPORT_DIR = ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

def run_checks(df):
    checks = []

    def add(name, category, failed, total, severity):
        rate = failed / total if total else 0
        checks.append({
            "check_name": name,
            "category": category,
            "failed_records": int(failed),
            "total_records": int(total),
            "failure_rate": round(rate, 4),
            "severity": severity,
            "status": "FAIL" if failed else "PASS"
        })

    total = len(df)

    add("Missing shipment_id", "Completeness",
        df["shipment_id"].isna().sum(), total, "Critical")
    add("Missing carrier", "Completeness",
        df["carrier"].isna().sum(), total, "High")
    add("Missing origin", "Completeness",
        df["origin"].isna().sum(), total, "High")
    add("Missing destination", "Completeness",
        df["destination"].isna().sum(), total, "High")
    add("Duplicate shipment_id", "Uniqueness",
        df["shipment_id"].duplicated(keep=False).sum(), total, "Critical")
    add("Arrival before shipment", "Validity",
        (df["actual_arrival"] < df["shipment_date"]).fillna(False).sum(), total, "Critical")
    add("Negative transit days", "Validity",
        (df["actual_transit_days"] < 0).fillna(False).sum(), total, "Critical")
    add("Missing expected arrival", "Completeness",
        df["expected_arrival"].isna().sum(), total, "Medium")
    add("Missing actual arrival", "Completeness",
        df["actual_arrival"].isna().sum(), total, "Medium")

    return pd.DataFrame(checks)

def quality_score(results):
    # Weighted score: completeness/validity/uniqueness failures reduce the score.
    weighted_failure = results["failure_rate"].mean()
    return round(max(0, 100 * (1 - weighted_failure)), 2)

if __name__ == "__main__":
    df = pd.read_csv(INPUT, parse_dates=[
        "shipment_date", "expected_arrival", "actual_arrival"
    ])
    results = run_checks(df)
    score = quality_score(results)

    results.to_csv(REPORT_DIR / "data_quality_report.csv", index=False)

    summary = {
        "total_records": len(df),
        "failed_checks": int((results["status"] == "FAIL").sum()),
        "quality_score": score
    }
    with open(REPORT_DIR / "quality_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(results.to_string(index=False))
    print(f"\nData Quality Score: {score}%")
