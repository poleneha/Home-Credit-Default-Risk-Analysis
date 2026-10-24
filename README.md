Home Credit Default Risk Analysis

Project Overview

An end-to-end data analytics project exploring factors associated with loan repayment difficulties using the Home Credit Default Risk dataset.

Objectives

- Analyze historical loan repayment patterns.
- Calculate the overall default rate.
- Compare risk across income groups, education levels, and income types.
- Explore the relationship between credit bureau history and repayment difficulties.
- Present findings through a Power BI dashboard.

Tools & Technologies

- Python: Pandas, NumPy, SciPy
- Database: SQLite
- Query Language: SQL
- Visualization: Power BI
- Development Environment: Visual Studio Code

Dataset

The project uses the Home Credit Default Risk dataset.

- Application training data: 307,511 records
- Target variable: "TARGET"
- "TARGET = 1": repayment difficulties
- "TARGET = 0": no recorded repayment difficulties

Analysis Performed

- Overall default rate analysis
- Income group risk analysis
- Income type analysis
- Education-level risk analysis
- Statistical association testing
- Credit bureau history analysis

Project Structure

Home_Credit_Default_Risk_Analysis/
├── python/
├── sql/
├── powerbi/
│   └── Home_Credit_Risk_Dashboard.pbix
├── reports/
│   ├── project_report.md
│   └── bureau_risk_analysis.csv
├── home_credit.db
└── README.md

Initial Finding

In the training dataset, 24,825 out of 307,511 applicants have "TARGET = 1", giving an overall rate of approximately 8.07%.

Dashboard

The Power BI dashboard visualizes default rates and applicant counts by credit history group.

Conclusion

This project demonstrates practical skills in data preparation, exploratory analysis, statistical testing, database management, and dashboard development.

Note: Findings describe historical associations and do not establish causation or constitute a production-ready credit scoring model.