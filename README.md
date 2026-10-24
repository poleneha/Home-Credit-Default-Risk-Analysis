Home Credit Default Risk Analysis

Project Overview

This project analyzes consumer loan application data to understand patterns associated with loan default risk. Using Python, SQL, SQLite, and Power BI, the project explores applicant characteristics and historical credit information to identify trends that can support data-driven lending decisions.

Business Problem

Financial institutions need to assess the risk that borrowers may have difficulty repaying loans. This project examines historical loan application data to identify default patterns across applicant groups and credit history categories.

Objectives

- Analyze overall loan default rates.
- Investigate default patterns across income and education groups.
- Examine employment and income-related risk factors.
- Analyze historical credit bureau information.
- Perform statistical analysis to explore relationships between applicant characteristics and defaults.
- Build an interactive Power BI dashboard to communicate findings.

Tools and Technologies

- Python: Pandas, NumPy, SciPy
- SQL: Data querying and aggregation
- SQLite: Local database storage and analysis
- Power BI: Interactive data visualization
- VS Code: Development environment
- Git and GitHub: Version control and project hosting

Dataset

The project uses the Home Credit Default Risk dataset, including loan application data and supporting credit history tables.

Key datasets include:

- "application_train.csv"
- "application_test.csv"
- "bureau.csv"
- "bureau_balance.csv"
- "previous_application.csv"
- "POS_CASH_balance.csv"
- "credit_card_balance.csv"
- "installments_payments.csv"

Note: The original datasets and local SQLite database are excluded from GitHub because of their size. Obtain the dataset from the official "Home Credit Default Risk competition on Kaggle" (https://www.kaggle.com/competitions/home-credit-default-risk/data).

Analysis Performed

- Overall default rate calculation.
- Default rate analysis by income group.
- Education-level risk analysis.
- Employment and income-type comparisons.
- Chi-square statistical test for income type and default status.
- Credit bureau history analysis.
- Applicant-level bureau data aggregation to avoid duplicate applicant counts.
- Export of analysis results to CSV for reporting and visualization.

Key Finding

The training dataset contains 307,511 loan applications, including 24,825 applications with a recorded default target of 1.

The overall default rate is approximately 8.07%.

This is a descriptive finding for the training dataset, not a prediction of future default rates. Further analysis is required to determine which characteristics are most strongly associated with default risk.

Power BI Dashboard

The Power BI dashboard contains two report pages:

1. Default Rate by Credit History — compares default rates across credit history groups.
2. Applicants by Credit History Group — displays the distribution of applicants across those groups.

Dashboard file: "powerbi/Home_Credit_Risk_Dashboard.pbix"

Project Structure

home-credit-default-risk/
├── powerbi/
│   └── Home_Credit_Risk_Dashboard.pbix
├── python/
│   ├── bureau_risk_analysis.py
│   ├── combined_risk_report.py
│   ├── default_rate.py
│   ├── education_risk.py
│   ├── employment_risk.py
│   ├── export_bureau_analysis.py
│   ├── income_risk.py
│   ├── load_data.py
│   ├── risk_summary.py
│   ├── run_sql.py
│   └── statistical_analysis.py
├── reports/
│   ├── bureau_risk_analysis.csv
│   ├── combined_risk_report.csv
│   ├── education_risk_summary.csv
│   └── project_report.md
├── sql/
│   └── 01_default_analysis.sql
├── .gitignore
└── README.md

How to Run

Clone this repository.

Download the dataset files from Kaggle and place the required CSV files in the project root directory.

Install the required Python packages:

pip install pandas numpy scipy

Run the relevant Python scripts from the project root, for example:

python python/default_rate.py

Open powerbi/Home_Credit_Risk_Dashboard.pbix in Power BI Desktop to explore the dashboard.

Note: Some scripts may require additional packages or the locally generated SQLite database. Run python/load_data.py first if your workflow requires database creation, and check individual scripts for their specific requirements.

Conclusion

This project demonstrates an end-to-end data analysis workflow involving data preparation, SQL querying, statistical analysis, risk segmentation, and dashboard development. It showcases practical skills in Python, SQL, SQLite, and Power BI for exploring consumer credit risk.

Author

Neha Pole

GitHub: poleneha