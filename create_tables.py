import sqlite3
import random
from datetime import datetime, timedelta

db_name = "database.db"
# Проверка: если база уже существует — выходим
if os.path.exists(db_name):
    print("❌ База данных уже существует. Работа программы остановлена.")
    sys.exit(1)

# Подключаемся к базе (или создаём её)
conn = sqlite3.connect("database.db")

# Создаём курсор
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    region TEXT,
    registration_date DATE
);
""")

cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    category TEXT,
    price REAL
);
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

""")

# Generate datas

# customers
regions = ["North", "South", "East", "West"]
for i in range(1, 101):
    cursor.execute(
        "INSERT INTO customers VALUES (?, ?, ?)",
        (i, random.choice(regions), "2023-01-01")
    )

# products
categories = ["Electronics", "Clothing", "Food"]
for i in range(1, 11):
    cursor.execute(
        "INSERT INTO products VALUES (?, ?, ?)",
        (i, random.choice(categories), random.randint(10, 500))
    )

# orders
for i in range(1, 500):
    cursor.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
        (
            i,
            random.randint(1, 100),
            random.randint(1, 10),
            random.randint(1, 5),
            (datetime.now() - timedelta(days=random.randint(1, 365))).date()
        )
    )

conn.commit()
conn.close()
