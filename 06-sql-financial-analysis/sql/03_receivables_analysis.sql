-- ============================================================
-- SQL Financial Analysis
-- Receivables Analysis
-- ============================================================

-- Query 3: Open receivables by customer
SELECT
    c.customer_name,
    c.country,
    SUM(i.amount) AS open_receivables
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
WHERE i.status = 'Open'
GROUP BY
    c.customer_name,
    c.country
ORDER BY open_receivables DESC;


-- Query 4: Open receivables by country
SELECT
    c.country,
    SUM(i.amount) AS open_receivables
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
WHERE i.status = 'Open'
GROUP BY c.country
ORDER BY open_receivables DESC;


-- Query 5: Overdue open invoices as of 2026-09-30
SELECT
    i.invoice_id,
    c.customer_name,
    c.country,
    i.invoice_date,
    i.due_date,
    i.amount
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
WHERE i.status = 'Open'
  AND i.due_date < '2026-09-30'
ORDER BY i.due_date;


-- Query 9: Paid vs Open invoices
SELECT
    status,
    COUNT(*) AS invoice_count,
    SUM(amount) AS total_amount
FROM invoices
GROUP BY status
ORDER BY total_amount DESC;