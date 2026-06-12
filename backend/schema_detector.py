import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "lensprime.db"


def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]


def get_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    return [column[1] for column in cursor.fetchall()]


def detect_primary_keys(tables, table_columns):
    primary_keys = {}

    for table in tables:
        for column in table_columns[table]:
            if column == "id" or column == f"{table[:-1]}_id" or column == f"{table}_id":
                primary_keys[table] = column

    return primary_keys


def detect_foreign_keys(tables, table_columns, primary_keys):
    relationships = []

    for table in tables:
        for column in table_columns[table]:
            for parent_table, primary_key in primary_keys.items():
                if table != parent_table and column == primary_key:
                    relationships.append({
                        "from_table": table,
                        "from_column": column,
                        "to_table": parent_table,
                        "to_column": primary_key
                    })

    return relationships


def main():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    tables = get_tables(cursor)
    table_columns = {table: get_columns(cursor, table) for table in tables}

    primary_keys = detect_primary_keys(tables, table_columns)
    relationships = detect_foreign_keys(tables, table_columns, primary_keys)

    print("Detected Primary Keys:")
    for table, key in primary_keys.items():
        print(f"  {table}.{key}")

    print("\nDetected Relationships:")
    for relationship in relationships:
        print(
            f"  {relationship['from_table']}.{relationship['from_column']} "
            f"→ {relationship['to_table']}.{relationship['to_column']}"
        )

    connection.close()


if __name__ == "__main__":
    main()