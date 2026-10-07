-- ============================================================
-- SQL Financial Analysis
-- Revenue Analysis
-- ============================================================

-- Query 1: Revenue by customer
SELECT
    c.customer_name,
    c.country,
    c.business_unit,
    SUM(i.amount) AS total_revenue
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
GROUP BY
    c.customer_name,
    c.country,
    c.business_unit
ORDER BY total_revenue DESC;


-- Query 2: Revenue by country
SELECT
    c.country,
    SUM(i.amount) AS total_revenue
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_revenue DESC;


-- Query 8: Monthly revenue evolution
SELECT
    substr(i.invoice_date, 1, 7) AS revenue_month,
    SUM(i.amount) AS total_revenue
FROM invoices i
GROUP BY revenue_month
ORDER BY revenue_month;


-- Query 10: Customer revenue concentration
SELECT
    c.customer_name,
    c.country,
    SUM(i.amount) AS total_revenue,
    COUNT(i.invoice_id) AS invoice_count,
    ROUND(
        SUM(i.amount) * 100.0 /
        (SELECT SUM(amount) FROM invoices),
        1
    ) AS revenue_share_pct
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
GROUP BY
    c.customer_name,
    c.country
ORDER BY total_revenue DESC;