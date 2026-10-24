import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
SELECT
    CASE
        WHEN AMT_INCOME_TOTAL < 100000 THEN 'Low Income'
        WHEN AMT_INCOME_TOTAL < 250000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_band,
    COUNT(*) AS applicants,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM application_train
WHERE AMT_INCOME_TOTAL IS NOT NULL
GROUP BY income_band
ORDER BY default_rate_pct DESC;
"""

results = connection.execute(query).fetchall()

print("Default Rate by Income Group")
print("----------------------------")

for row in results:
    print(
        f"Income: {row[0]}, "
        f"Applicants: {row[1]:,}, "
        f"Default rate: {row[2]}%"
    )

connection.close()