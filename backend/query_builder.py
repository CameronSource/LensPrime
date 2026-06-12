import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "lensprime.db"


def run_query(sql):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(sql)

    column_names = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    connection.close()

    return column_names, rows


def total_sales_by_state_query():
    return """
    SELECT
        customers.state,
        ROUND(SUM(orders.quantity * products.price), 2) AS total_sales
    FROM orders
    JOIN customers
        ON orders.customer_id = customers.customer_id
    JOIN products
        ON orders.product_id = products.product_id
    GROUP BY customers.state
    ORDER BY total_sales DESC;
    """


def quantity_sold_by_category_query():
    return """
    SELECT
        products.category,
        SUM(orders.quantity) AS total_quantity_sold
    FROM orders
    JOIN products
        ON orders.product_id = products.product_id
    GROUP BY products.category
    ORDER BY total_quantity_sold DESC;
    """


def customer_purchase_totals_query():
    return """
    SELECT
        customers.first_name || ' ' || customers.last_name AS customer_name,
        ROUND(SUM(orders.quantity * products.price), 2) AS total_spent
    FROM orders
    JOIN customers
        ON orders.customer_id = customers.customer_id
    JOIN products
        ON orders.product_id = products.product_id
    GROUP BY customers.customer_id
    ORDER BY total_spent DESC;
    """


def print_results(column_names, rows):
    print("\nResults:")
    print(" | ".join(column_names))
    print("-" * 50)

    for row in rows:
        print(" | ".join(str(value) for value in row))


def main():
    print("LensPrime Query Builder")
    print("\nChoose a question:")
    print("1. Total sales by state")
    print("2. Quantity sold by product category")
    print("3. Customer purchase totals")

    choice = input("\nEnter choice: ")

    if choice == "1":
        sql = total_sales_by_state_query()
    elif choice == "2":
        sql = quantity_sold_by_category_query()
    elif choice == "3":
        sql = customer_purchase_totals_query()
    else:
        print("Invalid choice.")
        return

    print("\nGenerated SQL:")
    print(sql)

    column_names, rows = run_query(sql)
    print_results(column_names, rows)


if __name__ == "__main__":
    main()