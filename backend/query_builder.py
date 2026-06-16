import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "lensprime.db"


METRICS = {
    "1": {
        "label": "Total Sales",
        "sql": "ROUND(SUM(orders.quantity * products.price), 2)",
        "alias": "total_sales",
    },
    "2": {
        "label": "Quantity Sold",
        "sql": "SUM(orders.quantity)",
        "alias": "quantity_sold",
    },
    "3": {
        "label": "Order Count",
        "sql": "COUNT(orders.order_id)",
        "alias": "order_count",
    },
}


GROUP_BY_OPTIONS = {
    "1": {
        "label": "State",
        "sql": "customers.state",
        "alias": "state",
    },
    "2": {
        "label": "Category",
        "sql": "products.category",
        "alias": "category",
    },
    "3": {
        "label": "Customer",
        "sql": "customers.first_name || ' ' || customers.last_name",
        "alias": "customer_name",
    },
}


SORT_OPTIONS = {
    "1": {
        "label": "Highest First",
        "sql": "DESC",
    },
    "2": {
        "label": "Lowest First",
        "sql": "ASC",
    },
}


def run_query(sql):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(sql)

    column_names = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    connection.close()

    return column_names, rows


def get_user_choice(title, options):
    print(f"\n{title}")

    for key, option in options.items():
        print(f"{key}. {option['label']}")

    choice = input("\nEnter choice: ")

    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input("Enter choice: ")

    return options[choice]


def get_limit():
    limit = input("\nLimit results? Enter a number or press Enter for no limit: ")

    if limit.strip() == "":
        return None

    while not limit.isdigit() or int(limit) <= 0:
        print("Please enter a positive number.")
        limit = input("Limit results? Enter a number or press Enter for no limit: ")

        if limit.strip() == "":
            return None

    return int(limit)


def build_query(metric, group_by, sort, limit):
    sql = f"""
    SELECT
        {group_by['sql']} AS {group_by['alias']},
        {metric['sql']} AS {metric['alias']}
    FROM orders
    JOIN customers
        ON orders.customer_id = customers.customer_id
    JOIN products
        ON orders.product_id = products.product_id
    GROUP BY {group_by['sql']}
    ORDER BY {metric['alias']} {sort['sql']}
    """

    if limit:
        sql += f"LIMIT {limit}\n"

    sql += ";"

    return sql


def print_results(column_names, rows):
    print("\nResults:")
    print(" | ".join(column_names))
    print("-" * 50)

    for row in rows:
        print(" | ".join(str(value) for value in row))


def main():
    print("LensPrime Dynamic Query Builder")

    metric = get_user_choice("Choose a metric:", METRICS)
    group_by = get_user_choice("Choose how to group the results:", GROUP_BY_OPTIONS)
    sort = get_user_choice("Choose sort order:", SORT_OPTIONS)
    limit = get_limit()

    sql = build_query(metric, group_by, sort, limit)

    print("\nGenerated SQL:")
    print(sql)

    column_names, rows = run_query(sql)
    print_results(column_names, rows)


if __name__ == "__main__":
    main()