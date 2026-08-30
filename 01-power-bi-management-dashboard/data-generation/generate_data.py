import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# 1. CONFIGURATION
# ============================================================

SEED = 42
np.random.seed(SEED)

START_DATE = "2025-01-01"
END_DATE = "2026-12-01"

countries = {
    "Austria": "DACH",
    "Germany": "DACH",
    "France": "Western Europe",
    "Italy": "Southern Europe",
    "Switzerland": "DACH",
}

business_units = [
    "Industrial Solutions",
    "Services",
    "Equipment",
]

accounts = [
    "Revenue",
    "Material Costs",
    "Production Costs",
    "Personnel Costs",
    "External Services",
    "Travel Expenses",
    "IT Expenses",
    "Other Operating Expenses",
    "Depreciation",
    "Other Operating Income",
]

scenarios = [
    "Actual",
    "Budget",
    "Forecast",
]


# ============================================================
# 2. GENERATE MONTHS
# ============================================================

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="MS"
)


# ============================================================
# 3. BUSINESS ASSUMPTIONS
# ============================================================

country_factor = {
    "Austria": 1.00,
    "Germany": 1.35,
    "France": 1.10,
    "Italy": 0.80,
    "Switzerland": 0.75,
}

business_unit_revenue = {
    "Industrial Solutions": 2_400_000,
    "Services": 1_500_000,
    "Equipment": 1_900_000,
}

seasonality = {
    1: 0.90,
    2: 0.92,
    3: 1.00,
    4: 1.02,
    5: 1.04,
    6: 1.06,
    7: 0.88,
    8: 0.82,
    9: 1.05,
    10: 1.08,
    11: 1.10,
    12: 0.98,
}


# ============================================================
# 4. COST STRUCTURE
# ============================================================

material_rate = {
    "Industrial Solutions": 0.37,
    "Services": 0.18,
    "Equipment": 0.43,
}

production_rate = {
    "Industrial Solutions": 0.12,
    "Services": 0.08,
    "Equipment": 0.15,
}

personnel_rate = {
    "Industrial Solutions": 0.145,
    "Services": 0.235,
    "Equipment": 0.120,
}

external_services_rate = {
    "Industrial Solutions": 0.050,
    "Services": 0.075,
    "Equipment": 0.040,
}

depreciation_rate = {
    "Industrial Solutions": 0.035,
    "Services": 0.020,
    "Equipment": 0.045,
}


# ============================================================
# 5. BUILD FINANCIAL DATA
# ============================================================

rows = []


for date in dates:

    month = date.month

    # Moderate growth between 2025 and 2026
    year_growth = 1 + 0.035 * (date.year - 2025)

    # Slight monthly trend
    monthly_trend = 1 + (month - 1) * 0.0015

    for country, region in countries.items():

        for business_unit in business_units:

            base_revenue = (
                business_unit_revenue[business_unit]
                * country_factor[country]
            )

            underlying_revenue = (
                base_revenue
                * seasonality[month]
                * year_growth
                * monthly_trend
            )

            # ------------------------------------------------
            # Budget
            # ------------------------------------------------

            budget_revenue = underlying_revenue * np.random.normal(
                1.00,
                0.012
            )

            # ------------------------------------------------
            # Actual
            # ------------------------------------------------

            actual_factor = np.random.normal(
                1.00,
                0.035
            )

            # Business story:
            # Germany / Services performs strongly on revenue
            if (
                country == "Germany"
                and business_unit == "Services"
            ):
                actual_factor *= 1.045

            # Business story:
            # France / Equipment underperforms
            if (
                country == "France"
                and business_unit == "Equipment"
            ):
                actual_factor *= 0.935

            actual_revenue = (
                underlying_revenue
                * actual_factor
            )

            # ------------------------------------------------
            # Forecast
            # ------------------------------------------------

            forecast_revenue = (
                0.55 * actual_revenue
                + 0.45 * budget_revenue
            ) * np.random.normal(1.00, 0.008)


            revenues = {
                "Actual": actual_revenue,
                "Budget": budget_revenue,
                "Forecast": forecast_revenue,
            }


            # =================================================
            # 6. CREATE P&L ACCOUNTS
            # =================================================

            for scenario, revenue in revenues.items():

                cost_factor = 1.00

                if scenario == "Actual":

                    cost_factor *= np.random.normal(
                        1.00,
                        0.025
                    )

                    # Business story:
                    # Germany Services has personnel cost pressure
                    if (
                        country == "Germany"
                        and business_unit == "Services"
                    ):
                        cost_factor *= 1.06

                    # Business story:
                    # Austria Industrial Solutions has
                    # slightly higher production costs
                    if (
                        country == "Austria"
                        and business_unit == "Industrial Solutions"
                    ):
                        cost_factor *= 1.035

                elif scenario == "Forecast":

                    cost_factor *= np.random.normal(
                        1.00,
                        0.012
                    )


                material_costs = (
                    revenue
                    * material_rate[business_unit]
                    * cost_factor
                )

                production_costs = (
                    revenue
                    * production_rate[business_unit]
                    * cost_factor
                )

                personnel_costs = (
                    revenue
                    * personnel_rate[business_unit]
                    * cost_factor
                )

                external_services = (
                    revenue
                    * external_services_rate[business_unit]
                    * cost_factor
                )

                travel_expenses = (
                    revenue
                    * 0.012
                    * np.random.normal(1.00, 0.03)
                )

                it_expenses = (
                    revenue
                    * 0.010
                    * np.random.normal(1.00, 0.02)
                )

                other_opex = (
                    revenue
                    * 0.018
                    * np.random.normal(1.00, 0.025)
                )

                depreciation = (
                    revenue
                    * depreciation_rate[business_unit]
                )

                other_operating_income = (
                    revenue
                    * 0.004
                    * np.random.normal(1.00, 0.04)
                )


                # Costs are negative
                amounts = {

                    "Revenue":
                        revenue,

                    "Material Costs":
                        -material_costs,

                    "Production Costs":
                        -production_costs,

                    "Personnel Costs":
                        -personnel_costs,

                    "External Services":
                        -external_services,

                    "Travel Expenses":
                        -travel_expenses,

                    "IT Expenses":
                        -it_expenses,

                    "Other Operating Expenses":
                        -other_opex,

                    "Depreciation":
                        -depreciation,

                    "Other Operating Income":
                        other_operating_income,
                }


                for account, amount in amounts.items():

                    rows.append({

                        "Date": date,

                        "Country":
                            country,

                        "Region":
                            region,

                        "Business Unit":
                            business_unit,

                        "Account":
                            account,

                        "Scenario":
                            scenario,

                        "Amount EUR":
                            round(amount, 2),
                    })


# ============================================================
# 7. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(rows)


# ============================================================
# 8. VALIDATION CHECKS
# ============================================================

expected_rows = (
    len(dates)
    * len(countries)
    * len(business_units)
    * len(accounts)
    * len(scenarios)
)

assert len(df) == expected_rows

assert df["Amount EUR"].notna().all()

assert df.duplicated(
    [
        "Date",
        "Country",
        "Business Unit",
        "Account",
        "Scenario",
    ]
).sum() == 0


# ============================================================
# 9. EXPORT CSV
# ============================================================

project_folder = Path(__file__).resolve().parent.parent

data_folder = project_folder / "data"

data_folder.mkdir(
    exist_ok=True
)

output_file = data_folder / "financial_data.csv"

df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 10. DATA DICTIONARY
# ============================================================

data_dictionary = pd.DataFrame({

    "Field": [
        "Date",
        "Country",
        "Region",
        "Business Unit",
        "Account",
        "Scenario",
        "Amount EUR",
    ],

    "Description": [

        "Monthly reporting date",

        "Reporting country",

        "Geographical region",

        "Operating business unit",

        "P&L account",

        "Actual, Budget or Forecast",

        "Financial amount in EUR. "
        "Revenue and income are positive; "
        "costs are negative.",
    ],

    "Type": [

        "Date",
        "Dimension",
        "Dimension",
        "Dimension",
        "Dimension",
        "Scenario",
        "Measure",
    ],
})


dictionary_file = (
    data_folder
    / "data_dictionary.csv"
)

data_dictionary.to_csv(
    dictionary_file,
    index=False
)


# ============================================================
# 11. SUMMARY
# ============================================================

print()
print("==============================================")
print("Financial dataset successfully generated")
print("==============================================")
print()

print(f"Rows: {len(df):,}")

print(f"Columns: {len(df.columns)}")

print()

print("Date range:")
print(
    f"{df['Date'].min().date()} "
    f"→ "
    f"{df['Date'].max().date()}"
)

print()

print("Countries:")
print(
    ", ".join(df["Country"].unique())
)

print()

print("Business Units:")
print(
    ", ".join(df["Business Unit"].unique())
)

print()

print("Scenarios:")
print(
    ", ".join(df["Scenario"].unique())
)

print()

print(f"Output file:")
print(output_file)

print()

print("Data validation: PASSED")
print()