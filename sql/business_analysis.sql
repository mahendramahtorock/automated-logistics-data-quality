-- Business analysis queries

-- On-time delivery rate by carrier
SELECT
    carrier,
    COUNT(*) AS shipments,
    ROUND(
        100.0 * AVG(
            CASE WHEN actual_arrival <= expected_arrival THEN 1.0 ELSE 0.0 END
        ), 2
    ) AS on_time_rate
FROM shipments
WHERE carrier IS NOT NULL
GROUP BY carrier
ORDER BY on_time_rate DESC;

-- Highest-risk routes
SELECT
    origin,
    destination,
    COUNT(*) AS shipments,
    ROUND(
        100.0 * AVG(
            CASE WHEN actual_arrival > expected_arrival THEN 1.0 ELSE 0.0 END
        ), 2
    ) AS delay_rate
FROM shipments
GROUP BY origin, destination
HAVING COUNT(*) >= 50
ORDER BY delay_rate DESC;

-- Average delay by carrier
SELECT
    carrier,
    ROUND(
        AVG(
            CASE
                WHEN actual_arrival > expected_arrival
                THEN actual_arrival - expected_arrival
            END
        ), 2
    ) AS avg_delay_days
FROM shipments
WHERE carrier IS NOT NULL
GROUP BY carrier
ORDER BY avg_delay_days DESC;
