# Month-End Closing Automation

## Business Problem

Month-end closing processes often require finance teams to consolidate data from multiple sources, perform manual validation checks, investigate exceptions and prepare management reporting.

These activities can be time-consuming and may create operational risks when data quality issues are not identified early.

This project simulates an automated month-end closing process designed to improve:

- Data quality
- Control reliability
- Exception detection
- Closing efficiency
- Financial reporting readiness

All data used in this project is synthetic and created for demonstration purposes.

---

## Objective

The objective is to build a simplified month-end closing workflow that automatically:

1. Consolidates financial data from multiple sources
2. Performs validation and account mapping checks
3. Identifies potential exceptions
4. Summarizes the control results
5. Provides a management-oriented closing status
6. Allows the process to be triggered through a single `RUN MONTH-END` button

The project combines financial controlling, internal controls, data transformation and process automation.

---

## Solution

The automated workflow follows this structure:

```text
Trial Balance
Accruals
Prepayments
Invoices
       ↓
   Power Query
       ↓
Data transformation
       ↓
Validation controls
       ↓
Exception detection
       ↓
Closing Control
       ↓
Month-End Control Center
       ↓
PASS / WARNING