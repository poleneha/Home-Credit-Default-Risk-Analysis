import sqlite3
from pathlib import Path
from scipy.stats import chi2_contingency

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
SELECT
    CASE
        WHEN AMT_INCOME_TOTAL < 100000 THEN 'Low Income'
        WHEN AMT_INCOME_TOTAL < 250000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_group,
    TARGET
FROM application_train
WHERE AMT_INCOME_TOTAL IS NOT NULL;
"""

rows = connection.execute(query).fetchall()
connection.close()

# Build a contingency table
groups = {}

for income_group, target in rows:
    if income_group not in groups:
        groups[income_group] = [0, 0]

    groups[income_group][int(target)] += 1

categories = sorted(groups)

# Columns: TARGET = 0 and TARGET = 1
table = [groups[group] for group in categories]

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(table)

print("Statistical Analysis: Income vs Default")
print("---------------------------------------")

for group in categories:
    no_default, defaulted = groups[group]
    total = no_default + defaulted
    rate = defaulted / total * 100

    print(
        f"{group}: Applicants={total:,}, "
        f"Defaulters={defaulted:,}, "
        f"Default rate={rate:.2f}%"
    )

print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.6f}")

if p_value < 0.05:
    print("Conclusion: Default rates differ statistically across income groups.")
else:
    print("Conclusion: Insufficient evidence of a difference across income groups.")

print("Note: Association does not establish causation.")