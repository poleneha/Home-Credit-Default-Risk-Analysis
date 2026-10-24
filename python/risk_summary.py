import sqlite3
from pathlib import Path
import csv

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"
report_folder = project_folder / "reports"

report_folder.mkdir(exist_ok=True)

connection = sqlite3.connect(database)

query = """
SELECT
    NAME_EDUCATION_TYPE AS education_level,
    COUNT(*) AS applicants,
    SUM(TARGET) AS defaulters,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM application_train
WHERE NAME_EDUCATION_TYPE IS NOT NULL
GROUP BY NAME_EDUCATION_TYPE
ORDER BY default_rate_pct DESC;
"""

results = connection.execute(query).fetchall()

output_file = report_folder / "education_risk_summary.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Education Level",
        "Applicants",
        "Defaulters",
        "Default Rate (%)"
    ])
    writer.writerows(results)

connection.close()

print("Education risk report created successfully!")
print(f"Saved to: {output_file}")
print(f"Education categories analyzed: {len(results)}")