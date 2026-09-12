import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# 1. CONFIGURATION
# ============================================================

np.random.seed(42)

START_DATE = "2025-01-01"
END_DATE = "2026-12-01"

countries = [
    "Austria",
    "Germany",
    "France",
    "Italy",
    "Switzerland"
]

business_units = [
    "Industrial Solutions",
    "Services",
    "Equipment"
]


# ============================================================
# 2. PARAMETRES FINANCIERS PAR PAYS
# ============================================================
#
# Ces paramètres permettent de créer des profils de
# Working Capital différents.
#
# DSO  = délai de paiement clients
# DIO  = durée d'immobilisation des stocks
# DPO  = délai de paiement fournisseurs
#
# France :
#   DSO élevé -> cash immobilisé chez les clients
#
# Austria :
#   DIO élevé -> cash immobilisé dans les stocks
#
# Italy :
#   DPO élevé -> fournisseurs financent davantage le cycle
#
# Germany / Switzerland :
#   profil plus équilibré
#


country_profiles = {
    "Austria": {
        "dso": 48,
        "dio": 78,
        "dpo": 48,
        "revenue_factor": 1.00
    },

    "Germany": {
        "dso": 38,
        "dio": 52,
        "dpo": 42,
        "revenue_factor": 1.15
    },

    "France": {
        "dso": 65,
        "dio": 58,
        "dpo": 38,
        "revenue_factor": 1.10
    },

    "Italy": {
        "dso": 55,
        "dio": 65,
        "dpo": 72,
        "revenue_factor": 0.90
    },

    "Switzerland": {
        "dso": 32,
        "dio": 45,
        "dpo": 40,
        "revenue_factor": 0.80
    }
}


# ============================================================
# 3. BUSINESS UNIT PARAMETERS
# ============================================================

business_unit_profiles = {
    "Industrial Solutions": {
        "revenue_factor": 1.30,
        "cogs_ratio": 0.68
    },

    "Services": {
        "revenue_factor": 0.90,
        "cogs_ratio": 0.55
    },

    "Equipment": {
        "revenue_factor": 1.00,
        "cogs_ratio": 0.72
    }
}


# ============================================================
# 4. CREATION DES PERIODES
# ============================================================

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="MS"
)


# ============================================================
# 5. GENERATION DES DONNEES
# ============================================================

data = []

for date in dates:

    month_number = date.month
    year = date.year

    # Facteur de saisonnalité
    seasonal_factor = {
        1: 0.92,
        2: 0.95,
        3: 1.00,
        4: 1.02,
        5: 1.05,
        6: 1.08,
        7: 0.95,
        8: 0.82,
        9: 1.08,
        10: 1.10,
        11: 1.05,
        12: 1.15
    }[month_number]

    # Croissance progressive entre 2025 et 2026
    if year == 2025:
        growth_factor = 1.00
    else:
        growth_factor = 1.08


    for country in countries:

        country_profile = country_profiles[country]

        for business_unit in business_units:

            bu_profile = business_unit_profiles[business_unit]


            # ------------------------------------------------
            # REVENUE
            # ------------------------------------------------

            base_revenue = (
                8_000_000
                * country_profile["revenue_factor"]
                * bu_profile["revenue_factor"]
            )

            revenue = (
                base_revenue
                * seasonal_factor
                * growth_factor
                * np.random.uniform(0.94, 1.06)
            )


            # ------------------------------------------------
            # COGS
            # ------------------------------------------------

            cogs_ratio = bu_profile["cogs_ratio"]

            cogs = (
                revenue
                * cogs_ratio
                * np.random.uniform(0.97, 1.03)
            )


            # ------------------------------------------------
            # WORKING CAPITAL DAYS
            # ------------------------------------------------

            dso = country_profile["dso"]
            dio = country_profile["dio"]
            dpo = country_profile["dpo"]


            # ------------------------------------------------
            # DELIBERATE BUSINESS STORY
            # ------------------------------------------------
            #
            # France:
            # DSO gradually deteriorates in 2026
            #
            # Austria:
            # DIO gradually deteriorates in 2026
            #
            # Italy:
            # DPO gradually increases in 2026
            #
            # This creates changes in cash conversion over time.
            #

            if country == "France" and year == 2026:
                dso += 10

            if country == "Austria" and year == 2026:
                dio += 15

            if country == "Italy" and year == 2026:
                dpo += 8


            # Small business-unit variation
            if business_unit == "Services":
                dso += 3

            elif business_unit == "Equipment":
                dio += 5


            # Random variation
            dso *= np.random.uniform(0.97, 1.03)
            dio *= np.random.uniform(0.97, 1.03)
            dpo *= np.random.uniform(0.97, 1.03)


            # ------------------------------------------------
            # DAYS IN MONTH
            # ------------------------------------------------

            days_in_month = date.days_in_month


            # ------------------------------------------------
            # ACCOUNTS RECEIVABLE
            # ------------------------------------------------

            accounts_receivable = (
                revenue
                / days_in_month
                * dso
            )


            # ------------------------------------------------
            # INVENTORY
            # ------------------------------------------------

            inventory = (
                cogs
                / days_in_month
                * dio
            )


            # ------------------------------------------------
            # ACCOUNTS PAYABLE
            # ------------------------------------------------

            accounts_payable = (
                cogs
                / days_in_month
                * dpo
            )


            # ------------------------------------------------
            # OPERATING WORKING CAPITAL
            # ------------------------------------------------

            operating_working_capital = (
                accounts_receivable
                + inventory
                - accounts_payable
            )


            # ------------------------------------------------
            # CASH CONVERSION CYCLE
            # ------------------------------------------------

            cash_conversion_cycle = (
                dso
                + dio
                - dpo
            )


            # ------------------------------------------------
            # AJOUT DE LA LIGNE
            # ------------------------------------------------

            data.append({
                "Date": date,
                "Country": country,
                "Business Unit": business_unit,

                "Revenue": round(revenue, 2),
                "COGS": round(cogs, 2),

                "Accounts Receivable": round(
                    accounts_receivable, 2
                ),

                "Inventory": round(
                    inventory, 2
                ),

                "Accounts Payable": round(
                    accounts_payable, 2
                ),

                "Operating Working Capital": round(
                    operating_working_capital, 2
                ),

                "DSO": round(dso, 2),
                "DIO": round(dio, 2),
                "DPO": round(dpo, 2),

                "CCC": round(
                    cash_conversion_cycle, 2
                )
            })


# ============================================================
# 6. CREATION DU DATAFRAME
# ============================================================

df = pd.DataFrame(data)


# ============================================================
# 7. CONTROLES DE QUALITE
# ============================================================

print("\n==========================================")
print("WORKING CAPITAL DATASET VALIDATION")
print("==========================================")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print(
    f"Date range: "
    f"{df['Date'].min().date()} → "
    f"{df['Date'].max().date()}"
)

print(
    f"Countries: "
    f"{df['Country'].nunique()}"
)

print(
    f"Business Units: "
    f"{df['Business Unit'].nunique()}"
)


# Vérification des valeurs négatives
negative_values = df[
    [
        "Revenue",
        "COGS",
        "Accounts Receivable",
        "Inventory",
        "Accounts Payable"
    ]
] < 0

if negative_values.any().any():
    print("WARNING: Negative values detected.")
else:
    print("Check 1 - Negative values: PASSED")


# Vérification des valeurs manquantes
missing_values = df.isnull().sum().sum()

if missing_values > 0:
    print(
        f"WARNING: {missing_values} missing values detected."
    )
else:
    print("Check 2 - Missing values: PASSED")


# Vérification de la formule Working Capital
wc_check = np.isclose(
    df["Operating Working Capital"],
    (
        df["Accounts Receivable"]
        + df["Inventory"]
        - df["Accounts Payable"]
    ),
    atol=0.10
)

if wc_check.all():
    print(
        "Check 3 - Working Capital formula: PASSED"
    )
else:
    print(
        "WARNING: Working Capital calculation issue."
    )


# Vérification de la formule CCC
ccc_check = np.isclose(
    df["CCC"],
    (
        df["DSO"]
        + df["DIO"]
        - df["DPO"]
    ),
    atol=0.10
)

if ccc_check.all():
    print(
        "Check 4 - CCC formula: PASSED"
    )
else:
    print(
        "WARNING: CCC calculation issue."
    )


# ============================================================
# 8. APERCU DES DONNEES
# ============================================================

print("\n==========================================")
print("DATA PREVIEW")
print("==========================================")

print(
    df.head(10).to_string(index=False)
)


# ============================================================
# 9. ANALYSE RAPIDE PAR PAYS
# ============================================================

print("\n==========================================")
print("AVERAGE WORKING CAPITAL METRICS BY COUNTRY")
print("==========================================")

country_summary = (
    df
    .groupby("Country")[
        [
            "DSO",
            "DIO",
            "DPO",
            "CCC",
            "Operating Working Capital"
        ]
    ]
    .mean()
    .round(1)
)

print(country_summary)


# ============================================================
# 10. EXPORT CSV
# ============================================================

output_directory = (
    Path(__file__).resolve().parent.parent / "data"
)

output_directory.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_directory / "working_capital_data.csv"
)

df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 11. FINAL MESSAGE
# ============================================================

print("\n==========================================")
print("DATASET GENERATED SUCCESSFULLY")
print("==========================================")

print(f"Output file: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nAll validation checks completed.")