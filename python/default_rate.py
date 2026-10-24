import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
SELECT
    COUNT(*) AS total_applicants,
    SUM(TARGET) AS defaulted_applicants,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM application_train;
"""

result = connection.execute(query).fetchone()

print("Overall Default Rate Analysis")
print("-----------------------------")
print("Total applicants:", f"{result[0]:,}")
print("Applicants with TARGET = 1:", f"{result[1]:,}")
print("Default rate:", str(result[2]) + "%")

connection.close()