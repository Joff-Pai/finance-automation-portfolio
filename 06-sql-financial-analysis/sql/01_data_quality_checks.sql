-- ============================================================
-- SQL Financial Analysis
-- Data Quality Checks
-- ============================================================

-- Check 1: Invalid or non-positive invoice amounts
SELECT
    'Invalid amount' AS check_type,
    COUNT(*) AS issue_count
FROM invoices
WHERE amount <= 0

UNION ALL

-- Check 2: Due date before invoice date
SELECT
    'Due date before invoice date' AS check_type,
    COUNT(*) AS issue_count
FROM invoices
WHERE due_date < invoice_date

UNION ALL

-- Check 3: Invalid invoice status
SELECT
    'Invalid status' AS check_type,
    COUNT(*) AS issue_count
FROM invoices
WHERE status NOT IN ('Paid', 'Open');