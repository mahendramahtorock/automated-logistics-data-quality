-- Automated SQL QA checks
-- Compatible with PostgreSQL-style SQL

-- 1. Missing critical fields
SELECT
    COUNT(*) FILTER (WHERE shipment_id IS NULL) AS missing_shipment_id,
    COUNT(*) FILTER (WHERE carrier IS NULL) AS missing_carrier,
    COUNT(*) FILTER (WHERE origin IS NULL) AS missing_origin,
    COUNT(*) FILTER (WHERE destination IS NULL) AS missing_destination
FROM shipments;

-- 2. Duplicate shipment IDs
SELECT shipment_id, COUNT(*) AS record_count
FROM shipments
GROUP BY shipment_id
HAVING COUNT(*) > 1
ORDER BY record_count DESC;

-- 3. Impossible dates
SELECT *
FROM shipments
WHERE actual_arrival < shipment_date;

-- 4. Negative transit duration
SELECT *
FROM shipments
WHERE actual_transit_days < 0;

-- 5. Route-level data quality
SELECT
    origin,
    destination,
    COUNT(*) AS shipments,
    COUNT(*) FILTER (WHERE carrier IS NULL) AS missing_carrier,
    COUNT(*) FILTER (WHERE actual_arrival < shipment_date) AS invalid_dates
FROM shipments
GROUP BY origin, destination
ORDER BY invalid_dates DESC;
