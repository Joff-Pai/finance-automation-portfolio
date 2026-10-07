-- ============================================================
-- SQL Financial Analysis
-- Management Analysis
-- ============================================================

-- Query 12: Revenue, open receivables and open ratio
-- Used to identify customers with a high level of outstanding
-- receivables relative to their total revenue.

SELECT
    c.customer_name,
    c.country,
    SUM(i.amount) AS total_revenue,
    SUM(
        CASE
            WHEN i.status = 'Open' THEN i.amount
            ELSE 0
        END
    ) AS open_receivables,
    ROUND(
        SUM(
            CASE
                WHEN i.status = 'Open' THEN i.amount
                ELSE 0
            END
        ) * 100.0 / SUM(i.amount),
        1
    ) AS open_ratio_pct
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
GROUP BY
    c.customer_name,
    c.country
ORDER BY open_receivables DESC;