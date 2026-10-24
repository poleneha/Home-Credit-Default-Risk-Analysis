import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
SELECT
    NAME_INCOME_TYPE AS employment_type,
    COUNT(*) AS applicants,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM application_train
WHERE NAME_INCOME_TYPE IS NOT NULL
GROUP BY NAME_INCOME_TYPE
HAVING COUNT(*) >= 100
ORDER BY default_rate_pct DESC;
"""

results = connection.execute(query).fetchall()

print("Default Risk by Income/Employment Type")
print("--------------------------------------")

for row in results:
    print(
        f"Type: {row[0]}, "
        f"Applicants: {row[1]:,}, "
        f"Default rate: {row[2]}%"
    )

connection.close()