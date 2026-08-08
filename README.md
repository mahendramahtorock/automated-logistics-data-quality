# Automated Logistics Data Quality & QA Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL%20style-lightgrey)
![Power%20BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Data%20Quality](https://img.shields.io/badge/Data%20Quality-QA-green)

## 1. Business Problem

Logistics platforms depend on accurate shipment and container data. Missing fields, duplicate records, impossible dates, negative transit durations, or sudden changes in data volume can create incorrect operational decisions.

This project simulates a logistics data pipeline that receives shipment records and automatically:

- validates data completeness
- detects duplicates
- identifies invalid dates and impossible values
- calculates a data-quality score
- summarizes operational anomalies
- produces reusable SQL QA checks
- generates outputs that can feed a BI dashboard

The project is designed around a real-world **Data Analyst / Data Quality Analyst** workflow.

## 2. Architecture

```text
Raw Shipment CSV
       |
       v
Python Ingestion & Cleaning
       |
       v
Automated Data Quality Checks
       |
       +------> QA Report
       |
       +------> Anomaly Summary
       |
       v
SQL Validation & Business Analysis
       |
       v
Power BI Dashboard
```

## 3. Tech Stack

- Python
- Pandas
- NumPy
- SQL
- PostgreSQL-style queries
- Power BI
- Git / GitHub
- Jupyter Notebook

## 4. Data Quality Checks

### Completeness
- Missing shipment ID
- Missing carrier
- Missing origin
- Missing destination
- Missing arrival dates

### Uniqueness
- Duplicate shipment IDs

### Validity
- Arrival before shipment date
- Negative transit duration
- Invalid date parsing

### Operational anomaly analysis
- Delay rate by carrier
- Delay rate by route
- Average delay
- High-risk routes

## 5. Repository Structure

```text
automated_logistics_data_quality/
│
├── data/
│   ├── raw/
│   │   └── shipments.csv
│   └── processed/
│       └── shipments_clean.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── data_quality_checks.py
│   ├── anomaly_detection.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   ├── data_quality_checks.sql
│   └── business_analysis.sql
│
├── reports/
│   ├── data_quality_report.csv
│   ├── quality_summary.json
│   └── anomaly_summary.csv
│
├── dashboard/
│   └── README.md
│
├── notebooks/
├── requirements.txt
├── LICENSE
└── README.md
```

## 6. How to Run

### Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd automated-logistics-data-quality
```

### Create environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the complete pipeline

```bash
python python/run_pipeline.py
```

The pipeline creates:

- `reports/data_quality_report.csv`
- `reports/quality_summary.json`
- `reports/anomaly_summary.csv`

## 7. Example QA Output

The automated report contains:

| Check | Category | Status | Severity |
|---|---|---|---|
| Missing carrier | Completeness | FAIL | High |
| Duplicate shipment ID | Uniqueness | FAIL | Critical |
| Arrival before shipment | Validity | FAIL | Critical |
| Negative transit days | Validity | FAIL | Critical |
| Missing destination | Completeness | FAIL | High |

## 8. Business Value

The pipeline helps a logistics analytics team:

- detect bad records before they reach downstream dashboards
- reduce manual QA effort
- identify source-data problems earlier
- improve trust in operational KPIs
- prioritize high-impact data issues
- create reusable validation checks

For a production implementation, these checks could be scheduled daily and connected to alerting systems.

## 9. Power BI Dashboard

Recommended dashboard pages:

### Executive QA Overview
- Total records
- Data-quality score
- Failed checks
- Critical issues
- Missing-value rate

### Data Quality Details
- Issue type
- Severity
- Failure rate
- Affected records

### Logistics Performance
- Shipment volume
- On-time delivery %
- Delay rate
- Average delay
- Carrier performance

### Route Analysis
- Origin → Destination
- Shipment count
- Delay rate
- Average delay

## 10. Key Analyst Questions

The project is designed to answer:

1. Is the incoming data complete?
2. Are shipment identifiers unique?
3. Are the dates logically consistent?
4. Which data-quality issue is most severe?
5. Which carriers have the highest delay rate?
6. Which routes are most operationally risky?
7. Could an anomaly be caused by the source data rather than the logistics operation?

## 11. Future Improvements

- Add API ingestion
- Add PostgreSQL database
- Add scheduled execution
- Add email/Slack alerts
- Add Great Expectations or Soda
- Add unit tests with pytest
- Add Docker
- Add GitHub Actions CI
- Add real-time monitoring
- Connect Power BI directly to the SQL layer

## 12. Disclaimer

The shipment data included in this repository is **synthetically generated for portfolio and educational purposes**. It does not represent Portcast customer data or any confidential logistics data.

## Author

**Mahendra Kumar Mahto**

