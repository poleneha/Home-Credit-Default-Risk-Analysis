import pandas as pd
import sqlite3
from pathlib import Path

# Project folder and database
project_folder = Path(__file__).resolve().parent.parent
database_file = project_folder / "home_credit.db"

connection = sqlite3.connect(database_file)

# Load application data
application_file = project_folder / "application_train.csv"

print("Loading application_train.csv...")

df = pd.read_csv(application_file)

df.to_sql(
    "application_train",
    connection,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Application data loaded:", len(df), "rows")

del df

# Load bureau data in chunks
bureau_file = project_folder / "bureau.csv"

print("Loading bureau.csv...")

first_chunk = True
total_rows = 0

for chunk in pd.read_csv(bureau_file, chunksize=10000):
    chunk.to_sql(
        "bureau",
        connection,
        if_exists="replace" if first_chunk else "append",
        index=False,
        chunksize=2000
    )

    total_rows += len(chunk)
    first_chunk = False

print("Bureau data loaded:", total_rows, "rows")

connection.close()

print("Both tables loaded successfully!")