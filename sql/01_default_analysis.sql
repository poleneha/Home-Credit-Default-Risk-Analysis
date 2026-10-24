-- Query 1: Count applicants by default status
SELECT
    TARGET,
    COUNT(*) AS applicant_count
FROM application_train
GROUP BY TARGET
ORDER BY TARGET;