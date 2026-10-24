Home Credit Default Risk Analysis

Project Overview

This project analyzes consumer loan application data to understand patterns associated with loan default risk. Using Python, SQL, SQLite, and Power BI, it explores applicant characteristics and historical credit information to support data-driven lending decisions.

Business Problem

Financial institutions need to assess the risk that borrowers may struggle to repay loans. This project investigates historical loan application data to identify default patterns across applicant groups and credit history categories.

Objectives

- Calculate the overall loan default rate.
- Analyze default patterns across income and education groups.
- Investigate employment and income-related risk factors.
- Explore historical credit bureau information.
- Apply statistical testing to examine relationships between applicant characteristics and defaults.
- Build an interactive Power BI dashboard to communicate findings.

Tools and Technologies

- Python: Pandas, NumPy, SciPy
- SQL: Data querying and aggregation
- SQLite: Database storage and analysis
- Power BI: Interactive dashboards and visualization
- VS Code: Development environment
- Git and GitHub: Version control and project hosting

Dataset

This project uses the "Home Credit Default Risk dataset on Kaggle" (https://www.kaggle.com/competitions/home-credit-default-risk/data).

Datasets used include:

- "application_train.csv"
- "application_test.csv"
- "bureau.csv"
- "bureau_balance.csv"
- "previous_application.csv"
- "POS_CASH_balance.csv"
- "credit_card_balance.csv"
- "installments_payments.csv"

Data availability: Raw datasets and the local SQLite database are excluded from this repository because of their size. Download the required files from Kaggle before running the analysis scripts.

Analysis Performed

- Overall default rate calculation.
- Default rate analysis by income group.
- Education-level risk analysis.
- Employment and income-type comparisons.
- Chi-square statistical testing.
- Credit bureau history analysis.
- Applicant-level aggregation of bureau records to avoid duplicate applicant counts.
- Export of analytical results to CSV for reporting and visualization.

Key Findings

The training dataset contains:

- Total applications: 307,511
- Applications with TARGET = 1: 24,825
- Overall default rate: Approximately 8.07%

These figures describe the training dataset. They should not be interpreted as a prediction of future loan defaults.

Power BI Dashboard

The Power BI report contains two pages:

1. Default Risk Analysis: Compares default rates across credit history groups.
2. Credit History Overview: Displays applicant counts across credit history groups.

Dashboard Preview

1. Default Risk Analysis

"Default Rate by Credit History" (screenshots/dashboard_default_risk.png)

2. Credit History Overview

"Applicants by Credit History Group" (screenshots/dashboard_credit_history.png)

Power BI file: "powerbi/Home_Credit_Risk_Dashboard.pbix"

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
├── screenshots/
│   ├── dashboard_default_risk.png
│   └── dashboard_credit_history.png
├── sql/
│   └── 01_default_analysis.sql
├── .gitignore
└── README.md

How to Run

1. Clone this repository:
   
   git clone https://github.com/poleneha/Home-Credit-Default-Risk-Analysis.git

2. Open the project folder:
   
   cd Home-Credit-Default-Risk-Analysis

3. Download the required datasets from Kaggle and place the CSV files in the project root directory.

4. Install the Python packages:
   
   pip install pandas numpy scipy

5. Run the required analysis script from the project root, for example:
   
   python python/default_rate.py

6. Open "powerbi/Home_Credit_Risk_Dashboard.pbix" in Power BI Desktop to explore the report.

Note: Individual scripts may require additional packages or a locally generated SQLite database. Check each script's requirements and run the data-loading script first when necessary.

Conclusion

This project demonstrates a practical data analytics workflow involving data preparation, SQL querying, statistical analysis, risk segmentation, and dashboard development. It showcases hands-on skills in Python, SQL, SQLite, and Power BI for exploring consumer credit risk.

Author

Neha Pole

- GitHub: "poleneha" (https://github.com/poleneha)
- Project Repository: "Home Credit Default Risk Analysis" (https://github.com/poleneha/Home-Credit-Default-Risk-Analysis)