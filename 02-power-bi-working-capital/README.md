# Working Capital Dashboard

Interactive Power BI dashboard designed to analyse working capital, cash conversion and the operational drivers of cash immobilisation across countries and business units.

The project complements the Management P&L Dashboard by moving from **profitability analysis to cash generation**.

> **Business perspective: Revenue and EBITDA growth do not necessarily translate into cash generation.**

---

## 1. Business Problem

A company can generate strong revenue growth and remain profitable while significant amounts of cash are tied up in:

* Accounts Receivable
* Inventory
* Accounts Payable dynamics

Management therefore needs to understand not only profitability, but also how efficiently operational performance is converted into cash.

The key management question addressed by this dashboard is:

> **Where is cash currently tied up, and what is driving it?**

---

## 2. Objective

The objective of this project is to provide management with a consolidated view of working capital and cash conversion performance.

The dashboard is designed to:

* Monitor Operating Working Capital
* Analyse Accounts Receivable, Inventory and Accounts Payable
* Monitor collection performance
* Analyse inventory efficiency
* Monitor supplier payment timing
* Measure the Cash Conversion Cycle
* Compare working capital performance across countries
* Identify the main drivers of cash immobilisation

---

## 3. Key Financial Concepts

### Operating Working Capital

Operating Working Capital is calculated as:

**Accounts Receivable + Inventory − Accounts Payable**

It represents the amount of cash invested in the operating cycle.

### DSO — Days Sales Outstanding

Measures the average number of days required to collect customer receivables.

**Higher DSO → more cash tied up in receivables.**

### DIO — Days Inventory Outstanding

Measures how long inventory remains tied up before being sold or consumed.

**Higher DIO → more cash tied up in inventory.**

### DPO — Days Payable Outstanding

Measures the average time taken to pay suppliers.

**Higher DPO → more supplier financing and lower immediate cash requirements.**

### CCC — Cash Conversion Cycle

The Cash Conversion Cycle combines the three operational drivers:

**CCC = DSO + DIO − DPO**

A higher CCC generally means that cash remains tied up in the operating cycle for longer.

---

## 4. Solution

The project follows a finance-oriented data workflow:

**Synthetic Financial Data → Power Query → Data Model → DAX Measures → Power BI Dashboard → Financial Analysis**

The focus is not on visualisation alone, but on transforming financial data into management information.

---

## 5. Dataset

The dataset is fully synthetic and was created specifically for demonstration purposes.

It contains:

* 24 monthly periods
* 5 countries
* 3 business units
* Revenue and COGS
* Accounts Receivable
* Inventory
* Accounts Payable
* Operating Working Capital
* DSO
* DIO
* DPO
* CCC

Countries:

* Austria
* Germany
* France
* Italy
* Switzerland

Business Units:

* Industrial Solutions
* Services
* Equipment

The dataset was generated and validated using Python and pandas.

---

## 6. Key KPIs

The dashboard includes:

### Working Capital Position

* Closing Accounts Receivable
* Closing Inventory
* Closing Accounts Payable
* Closing Operating Working Capital

### Cash Conversion

* Closing DSO
* Closing DIO
* Closing DPO
* Closing CCC

The dashboard distinguishes between **flow measures** and **balance-sheet positions**.

For example, revenue is accumulated over the selected period, while inventory is a balance measured at a specific point in time. Inventory is therefore analysed using closing or average balances rather than by summing monthly inventory balances.

---

## 7. Dashboard Structure

### Page 1 — Working Capital Overview

Provides a high-level view of the working capital position and cash conversion metrics.

Key KPIs:

* Accounts Receivable
* Inventory
* Accounts Payable
* Operating Working Capital
* DSO
* DIO
* DPO
* CCC

---

### Page 2 — Working Capital Evolution

Focuses on the evolution of working capital over time.

Includes:

* Country slicer
* Closing Operating Working Capital over time
* Accounts Receivable / Inventory / Accounts Payable over time

This page helps identify changes in working capital and understand which balance-sheet components are driving the movement.

---

### Page 3 — Cash Drivers Analysis

Focuses on the operational drivers of cash conversion.

Includes:

* DSO by Country
* DIO by Country
* DPO by Country
* CCC by Country
* Country and period analysis

This page helps identify where cash is tied up and which operational driver requires management attention.

---

## 8. Key Insights

The synthetic dataset was designed to illustrate different working capital profiles across countries.

Examples identified through the dashboard include:

* **France:** highest DSO, indicating slower customer collections and greater cash immobilisation in receivables.
* **Austria:** highest DIO, indicating a significant amount of cash tied up in inventory.
* **Italy:** highest DPO, indicating greater reliance on supplier financing.
* **Switzerland:** strongest overall cash conversion profile.
* **France:** highest CCC, reflecting a less efficient overall cash conversion cycle.

The dashboard therefore moves beyond reporting KPIs to identify potential operational areas requiring attention.

---

## 9. Architecture

```text
Synthetic Financial Dataset
            ↓
       Power Query
            ↓
      Data Transformation
            ↓
       Power BI Model
            ↓
        DAX Measures
            ↓
    Working Capital Dashboard
            ↓
     Financial Analysis
            ↓
     Management Insights
```

---

## 10. Tools

* Power BI
* Power Query
* DAX
* Python
* pandas
* CSV

Python was used primarily to generate and validate the synthetic financial dataset.

---

## 11. Business Impact

This project demonstrates how a Financial Controller can use data and automation tools to improve financial analysis and management reporting.

The dashboard provides:

* Improved visibility over working capital
* Identification of cash immobilisation drivers
* Country-level performance comparison
* More structured working capital analysis
* Consistent KPI calculation
* Support for management decision-making

The key objective is to connect:

**Financial Data → Operational Drivers → Cash Impact → Management Action**

---

## 12. Data Disclaimer

All data used in this project is synthetic and was created for demonstration purposes.

No confidential, proprietary or client data from previous employers or professional engagements has been used.

> **Synthetic financial dataset created for demonstration purposes.**
