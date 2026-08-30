# Management P&L Dashboard

Interactive Power BI dashboard designed to provide management with a consolidated view of financial performance across countries and business units.

The dashboard focuses on Actual vs Budget vs Forecast analysis, profitability monitoring and variance analysis.

---

## 1. Business Problem

Management reporting often requires Finance teams to consolidate financial information across multiple countries, business units and reporting periods.

A management dashboard should allow Finance and business stakeholders to quickly answer questions such as:

* Are we on track against Budget?
* How is performance evolving compared with Forecast?
* Which countries or business units are driving the variance?
* Is EBITDA performance driven by revenue, costs or both?
* Where should management focus its attention?

The objective is therefore not only to present financial data, but to transform it into actionable management information.

---

## 2. Objective

Build an interactive management P&L dashboard enabling Finance and management to:

* monitor financial performance;
* compare Actual, Budget and Forecast;
* analyse revenue and profitability;
* identify significant variances;
* drill down by country and business unit;
* understand the main drivers of performance.

---

## 3. Management Questions

The dashboard is designed around four main questions:

1. **Are we achieving our financial plan?**
2. **Where are the largest variances?**
3. **What are the main drivers behind these variances?**
4. **Which countries or business units require management attention?**

---

## 4. Solution

The solution combines:

**Synthetic financial data → Data preparation → Data model → DAX measures → Interactive Power BI dashboard**

The dashboard will provide management-level KPIs together with the ability to drill down into the underlying performance drivers.

---

## 5. Dataset

The project uses a fully synthetic financial dataset created specifically for demonstration purposes.

The dataset covers:

* 24 months of financial data;
* 5 countries;
* 3 business units;
* 3 reporting scenarios;
* multiple P&L accounts.

### Countries

* Austria
* Germany
* France
* Italy
* Switzerland

### Business Units

* Industrial Solutions
* Services
* Equipment

### Scenarios

* Actual
* Budget
* Forecast

### P&L Accounts

The dataset includes revenue and operating cost categories used to calculate Gross Profit and EBITDA.

The dataset was generated using Python and validated before being used in Power BI.

---

## 6. Key KPIs

The dashboard will focus on the following management KPIs:

### Revenue

Total revenue generated across the selected reporting scope.

### Gross Profit

Revenue after material and production costs.

### EBITDA

Operating profitability before depreciation, amortisation, interest and taxes.

### EBITDA Margin

EBITDA as a percentage of Revenue.

### Actual vs Budget

Absolute and percentage variance between Actual results and Budget.

### Actual vs Forecast

Absolute and percentage variance between Actual results and Forecast.

### YTD Performance

Year-to-date financial performance based on the selected reporting period.

---

## 7. Dashboard Structure

### Page 1 — Management Overview

Executive-level view of financial performance.

Main elements:

* Revenue;
* Gross Profit;
* EBITDA;
* EBITDA Margin;
* Actual vs Budget;
* Actual vs Forecast;
* monthly performance trend.

### Page 2 — Variance Analysis

Detailed analysis of performance deviations.

Analysis dimensions:

* Country;
* Business Unit;
* P&L Account;
* Month.

The objective is to identify where the largest positive and negative variances occur.

### Page 3 — Business Unit Analysis

Detailed profitability analysis by business unit.

Focus areas:

* Revenue;
* EBITDA;
* EBITDA Margin;
* Actual vs Budget;
* monthly evolution;
* comparison between business units.

---

## 8. Architecture

```text
Synthetic Financial Dataset
          │
          ▼
      Power Query
          │
          ▼
   Data Transformation
          │
          ▼
    Power BI Data Model
          │
          ▼
       DAX Measures
          │
          ▼
   Management Dashboard
          │
          ▼
    Variance Analysis
```

---

## 9. Tools & Technologies

* Power BI
* Power Query
* DAX
* Python
* Excel / CSV

Python is used to generate and validate the synthetic financial dataset.

Power BI is used for data modelling, calculations, visualisation and management reporting.

---

## 10. Key Insights

*To be completed after the dashboard has been built and the analysis performed.*

The final analysis will highlight the main financial performance drivers identified through the dashboard.

---

## 11. Business Impact

*To be completed after the dashboard has been built.*

The project will assess how the solution can improve:

* management visibility;
* variance analysis;
* reporting efficiency;
* identification of performance drivers;
* decision-making.

---

## 12. Technical Details

Detailed technical documentation will cover:

* data preparation;
* Power Query transformations;
* data modelling;
* DAX measures;
* KPI calculations;
* variance analysis;
* dashboard design.

Technical details are intentionally presented after the business context to reflect a Finance-oriented approach.

---

## 13. Data Disclaimer

> **Synthetic financial dataset created for demonstration purposes.**

No confidential, proprietary or client data is used in this project.

The financial scenarios and figures are entirely fictional and have been created to demonstrate financial reporting, variance analysis and Business Intelligence capabilities.
