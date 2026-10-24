import sqlite3
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
database = project_folder / "home_credit.db"
report_folder = project_folder / "reports"

report_folder.mkdir(exist_ok=True)

query = """
WITH bureau_summary AS (
    SELECT
        SK_ID_CURR,
        COUNT(*) AS bureau_record_count
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

with sqlite3.connect(database) as connection:
    results = pd.read_sql_query(query, connection)

output_file = report_folder / "bureau_risk_analysis.csv"
results.to_csv(output_file, index=False)

print("Bureau risk analysis exported successfully!")
print(results.to_string(index=False))
print(f"\nSaved to: {output_file}")