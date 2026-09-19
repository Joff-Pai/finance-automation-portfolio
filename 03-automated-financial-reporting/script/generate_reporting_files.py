import os
from openpyxl import Workbook

# ============================================================
# CONFIGURATION
# ============================================================

output_folder = "../data"

os.makedirs(output_folder, exist_ok=True)

countries = [
    "France",
    "Germany",
    "Switzerland"
]

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

business_units = [
    "Services",
    "Industrial Solutions"
]

accounts = [
    "Revenue",
    "Personnel Costs",
    "External Costs",
    "Other Operating Costs"
]


# ============================================================
# COUNTRY PROFILES
# ============================================================

country_profiles = {
    "France": {
        "revenue_factor": 1.00,
        "budget_factor": 1.02,
        "cost_factor": 1.00
    },

    "Germany": {
        "revenue_factor": 1.15,
        "budget_factor": 1.12,
        "cost_factor": 1.08
    },

    "Switzerland": {
        "revenue_factor": 0.80,
        "budget_factor": 0.78,
        "cost_factor": 0.82
    }
}


# ============================================================
# NUMBER FORMATTING
# ============================================================

def format_amount(amount, country):

    if country == "France":
        return (
            f"{amount:,.2f}"
            .replace(",", " ")
            .replace(".", ",")
        )

    elif country == "Germany":
        return (
            f"{amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    elif country == "Switzerland":
        return f"{amount:,.2f}".replace(",", "'")

    return str(amount)


# ============================================================
# FINANCIAL CALCULATIONS
# ============================================================

def generate_amounts(country, business_unit, account, month_number):

    profile = country_profiles[country]

    # Month progression:
    # January = 0
    # February = 1
    # ...
    # December = 11

    month_index = month_number - 1

    if business_unit == "Services":

        if account == "Revenue":

            base_actual = 1_500_000
            base_budget = 1_450_000

            actual = (
                base_actual
                + month_index * 10_000
            ) * profile["revenue_factor"]

            budget = (
                base_budget
                + month_index * 8_000
            ) * profile["budget_factor"]

        elif account == "Personnel Costs":

            base_actual = -420_000
            base_budget = -400_000

            actual = (
                base_actual
                - month_index * 3_000
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 2_500
            ) * profile["cost_factor"]

        elif account == "External Costs":

            base_actual = -180_000
            base_budget = -175_000

            actual = (
                base_actual
                - month_index * 2_000
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 1_500
            ) * profile["cost_factor"]

        else:

            base_actual = -50_000
            base_budget = -45_000

            actual = (
                base_actual
                - month_index * 1_000
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 800
            ) * profile["cost_factor"]

    else:

        if account == "Revenue":

            base_actual = 2_200_000
            base_budget = 2_300_000

            actual = (
                base_actual
                + month_index * 15_000
            ) * profile["revenue_factor"]

            budget = (
                base_budget
                + month_index * 12_000
            ) * profile["budget_factor"]

        elif account == "Personnel Costs":

            base_actual = -600_000
            base_budget = -620_000

            actual = (
                base_actual
                - month_index * 4_000
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 3_500
            ) * profile["cost_factor"]

        elif account == "External Costs":

            base_actual = -850_000
            base_budget = -820_000

            actual = (
                base_actual
                - month_index * 5_000
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 4_500
            ) * profile["cost_factor"]

        else:

            base_actual = -120_000
            base_budget = -110_000

            actual = (
                base_actual
                - month_index * 1_500
            ) * profile["cost_factor"]

            budget = (
                base_budget
                - month_index * 1_200
            ) * profile["cost_factor"]

    return actual, budget


# ============================================================
# CREATE ROW
# ============================================================

def create_row(
    country,
    business_unit,
    account,
    month_number
):

    actual, budget = generate_amounts(
        country,
        business_unit,
        account,
        month_number
    )

    return [
        country,
        business_unit,
        account,
        format_amount(actual, country),
        format_amount(budget, country)
    ]


# ============================================================
# CREATE EXCEL FILE
# ============================================================

def create_excel_file(
    country,
    month,
    month_number
):

    file_name = f"{country}_{month}_2026.xlsx"

    file_path = os.path.join(
        output_folder,
        file_name
    )

    wb = Workbook()

    ws = wb.active
    ws.title = "Feuil1"

    headers = [
        "Country",
        "Business Unit",
        "Account",
        "Actual",
        "Budget"
    ]

    ws.append(headers)

    for business_unit in business_units:

        for account in accounts:

            row = create_row(
                country,
                business_unit,
                account,
                month_number
            )

            ws.append(row)

    # Store financial amounts as text
    # because each country uses a different
    # local number format.

    for row in ws.iter_rows(
        min_row=2,
        min_col=4,
        max_col=5
    ):

        for cell in row:
            cell.number_format = "@"

    wb.save(file_path)

    print(f"Created: {file_path}")


# ============================================================
# GENERATE ALL FILES
# ============================================================

for country in countries:

    for month_number, month in enumerate(
        months,
        start=1
    ):

        create_excel_file(
            country,
            month,
            month_number
        )

print()
print("===================================")
print("Reporting file generation complete")
print("Countries: 3")
print("Months: 12")
print("Files created: 36")
print("===================================")