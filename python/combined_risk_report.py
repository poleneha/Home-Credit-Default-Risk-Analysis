import sqlite3
import csv
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"
report_folder = project_folder / "reports"
report_folder.mkdir(exist_ok=True)

connection = sqlite3.connect(database)

query = """
SELECT
    CASE
        WHEN AMT_INCOME_TOTAL < 100000 THEN 'Low Income'
        WHEN AMT_INCOME_TOTAL < 250000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_group,
    COUNT(*) AS applicants,
    SUM(TARGET) AS defaulters,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM application_train
WHERE AMT_INCOME_TOTAL IS NOT NULL
GROUP BY income_group
ORDER BY default_rate_pct DESC;
"""

results = connection.execute(query).fetchall()

output_file = report_folder / "combined_risk_report.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Income Group",
        "Applicants",
        "Defaulters",
        "Default Rate (%)"
    ])
    writer.writerows(results)

connection.close()

print("Combined risk report created!")
print("Report saved to:", output_file)