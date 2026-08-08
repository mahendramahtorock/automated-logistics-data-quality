# Power BI Dashboard Guide

Create a Power BI report using:

`data/processed/shipments_clean.csv`

## Page 1 — Data Quality Overview
Cards:
- Total Records
- Quality Score
- Failed Checks
- Critical Issues

Charts:
- Issues by Category
- Issues by Severity
- Failure Rate by Check

## Page 2 — Logistics Performance
Cards:
- Total Shipments
- On-Time %
- Delay %
- Average Delay Days

Charts:
- Delay Rate by Carrier
- Delay Rate by Route
- Monthly Shipment Volume

## Page 3 — Root Cause Analysis
Use slicers:
- Carrier
- Origin
- Destination
- Status

Visuals:
- Average Delay by Carrier
- Average Delay by Route
- Transit Days vs Expected Transit Days

## Suggested Power BI measures

```DAX
Total Shipments = COUNTROWS(shipments_clean)

Delayed Shipments =
CALCULATE(
    [Total Shipments],
    shipments_clean[actual_arrival] > shipments_clean[expected_arrival]
)

Delay Rate =
DIVIDE([Delayed Shipments], [Total Shipments])

On Time Shipments =
CALCULATE(
    [Total Shipments],
    shipments_clean[actual_arrival] <= shipments_clean[expected_arrival]
)

On Time Rate =
DIVIDE([On Time Shipments], [Total Shipments])
```

Add a screenshot of the finished dashboard to the main README after building it.
