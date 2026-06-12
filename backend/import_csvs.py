import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
SAMPLE_DATA_DIR = BASE_DIR / "sample_data"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "lensprime.db"


def import_csv_files():
    DATABASE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    csv_files = list(SAMPLE_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in sample_data.")
        return

    for csv_file in csv_files:
        table_name = csv_file.stem

        df = pd.read_csv(csv_file)
        df.to_sql(table_name, connection, if_exists="replace", index=False)

        print(f"Imported {csv_file.name} as table '{table_name}'")

    connection.close()
    print(f"\nDatabase created at: {DATABASE_PATH}")


def show_database_structure():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("\nTables found:")

    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")

        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        for column in columns:
            column_name = column[1]
            column_type = column[2]
            print(f"  - {column_name} ({column_type})")

    connection.close()


if __name__ == "__main__":
    import_csv_files()
    show_database_structure()