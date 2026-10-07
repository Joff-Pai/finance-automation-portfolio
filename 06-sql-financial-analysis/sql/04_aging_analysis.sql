-- ============================================================
-- SQL Financial Analysis
-- Accounts Receivable Aging
-- ============================================================

-- Query 6: Invoice-level aging analysis
SELECT
    i.invoice_id,
    c.customer_name,
    c.country,
    i.due_date,
    i.amount,
    CASE
        WHEN i.due_date >= '2026-09-30' THEN 'Current'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 30
            THEN '1-30 days overdue'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 60
            THEN '31-60 days overdue'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 90
            THEN '61-90 days overdue'
        ELSE '>90 days overdue'
    END AS aging_bucket
FROM invoices i
JOIN customers c
    ON i.customer_id = c.customer_id
WHERE i.status = 'Open'
ORDER BY i.due_date;


-- Query 7: Aging summary
SELECT
    CASE
        WHEN i.due_date >= '2026-09-30' THEN 'Current'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 30
            THEN '1-30 days overdue'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 60
            THEN '31-60 days overdue'
        WHEN julianday('2026-09-30') - julianday(i.due_date) <= 90
            THEN '61-90 days overdue'
        ELSE '>90 days overdue'
    END AS aging_bucket,
    COUNT(*) AS invoice_count,
    SUM(i.amount) AS total_amount
FROM invoices i
WHERE i.status = 'Open'
GROUP BY aging_bucket
ORDER BY
    CASE aging_bucket
        WHEN 'Current' THEN 1
        WHEN '1-30 days overdue' THEN 2
        WHEN '31-60 days overdue' THEN 3
        WHEN '61-90 days overdue' THEN 4
        WHEN '>90 days overdue' THEN 5
    END;