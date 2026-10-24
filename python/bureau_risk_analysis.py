import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"

connection = sqlite3.connect(database)

query = """
WITH bureau_summary AS (
    SELECT
        SK_ID_CURR,
        COUNT(*) AS bureau_record_count,
        AVG(DAYS_CREDIT) AS avg_days_credit
    FROM bureau
    GROUP BY SK_ID_CURR
),
applicant_data AS (
    SELECT
        a.SK_ID_CURR,
        a.TARGET,
        COALESCE(b.bureau_record_count, 0) AS bureau_record_count
    FROM application_train AS a
    LEFT JOIN bureau_summary AS b
        ON a.SK_ID_CURR = b.SK_ID_CURR
)
SELECT
    CASE
        WHEN bureau_record_count = 0 THEN 'No bureau records'
        WHEN bureau_record_count = 1 THEN '1 record'
        WHEN bureau_record_count BETWEEN 2 AND 4 THEN '2-4 records'
        ELSE '5+ records'
    END AS credit_history_group,
    COUNT(*) AS applicants,
    SUM(TARGET) AS defaulters,
    ROUND(AVG(TARGET) * 100, 2) AS default_rate_pct
FROM applicant_data
GROUP BY credit_history_group
ORDER BY default_rate_pct DESC;
"""

try:
    results = connection.execute(query).fetchall()

    print("Default Risk by Credit History")
    print("--------------------------------")

    for row in results:
        print(
            f"Group: {row[0]}, "
            f"Applicants: {row[1]:,}, "
            f"Defaulters: {row[2]:,}, "
            f"Default rate: {row[3]}%"
        )

finally:
    connection.close()