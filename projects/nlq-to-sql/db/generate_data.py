import duckdb
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
con = duckdb.connect("analytics.db")

# ---------- Tabellen ----------
con.execute("""
CREATE TABLE IF NOT EXISTS regions (
    id INTEGER,
    name TEXT
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER,
    name TEXT,
    region_id INTEGER
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER,
    name TEXT,
    category TEXT,
    price FLOAT
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER,
    customer_id INTEGER,
    order_date DATE
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER
)
""")

# ---------- Daten ----------
regions = ["EU", "US", "APAC"]
for i, r in enumerate(regions):
    con.execute("INSERT INTO regions VALUES (?, ?)", [i+1, r])

NUM_CUSTOMERS = 500
NUM_PRODUCTS = 200
NUM_ORDERS = 10_000

# Customers
for i in range(1, NUM_CUSTOMERS + 1):
    con.execute(
        "INSERT INTO customers VALUES (?, ?, ?)",
        [i, fake.name(), random.randint(1, len(regions))]
    )

# Products
for i in range(1, NUM_PRODUCTS + 1):
    con.execute(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        [i, fake.word(), fake.word(), round(random.uniform(10, 500), 2)]
    )

# Orders + Items
start_date = datetime(2023, 1, 1)

for order_id in range(1, NUM_ORDERS + 1):
    customer_id = random.randint(1, NUM_CUSTOMERS)
    date = start_date + timedelta(days=random.randint(0, 500))

    con.execute(
        "INSERT INTO orders VALUES (?, ?, ?)",
        [order_id, customer_id, date.date()]
    )

    for _ in range(random.randint(1, 5)):
        con.execute(
            "INSERT INTO order_items VALUES (?, ?, ?)",
            [
                order_id,
                random.randint(1, NUM_PRODUCTS),
                random.randint(1, 3)
            ]
        )

con.close()
print("✅ Large analytics database generated.")
