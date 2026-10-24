import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
SELECT
    a.TARGET,
    COUNT(DISTINCT a.SK_ID_CURR) AS applicants,
    COUNT(b.SK_ID_BUREAU) AS bureau_records,
    ROUND(AVG(b.DAYS_CREDIT), 2) AS avg_days_since_credit
FROM application_train AS a
LEFT JOIN bureau AS b
    ON a.SK_ID_CURR = b.SK_ID_CURR
GROUP BY a.TARGET
ORDER BY a.TARGET;
"""

print("Credit Bureau Analysis")
print("----------------------")

try:
    results = connection.execute(query).fetchall()

    for row in results:
        print(f"TARGET: {row[0]}")
        print(f"Applicants: {row[1]:,}")
        print(f"Bureau records: {row[2]:,}")
        print(f"Average DAYS_CREDIT: {row[3]}")
        print("----------------------")

except sqlite3.Error as error:
    print("SQL error:", error)

finally:
    connection.close()