import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

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

print("Default Risk by Education Level")
print("--------------------------------")

for row in results:
    print(
        f"Education: {row[0]}, "
        f"Applicants: {row[1]:,}, "
        f"Defaulters: {row[2]:,}, "
        f"Default rate: {row[3]}%"
    )

connection.close()