import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_name = "database.db"

with sqlite3.connect(db_name) as conn:
    # Доход по категориям
    query_cat = """
    SELECT
        p.category,
        SUM(o.quantity * p.price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category
    """
    df_cat = pd.read_sql(query_cat, conn)

    # Доход по датам
    query_date = """
    SELECT 
        order_date,
        p.category,
        SUM(o.quantity * p.price) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY order_date, p.category
    ORDER BY order_date
    """
    df_date = pd.read_sql(query_date, conn)
    df_date['order_date'] = pd.to_datetime(df_date['order_date'])
    df_date['month'] = df_date['order_date'].dt.to_period('M')

# Проверки
if df_cat.empty:
    print("⚠️ Данные по категориям пусты")
if df_date.empty:
    print("⚠️ Данные по датам пусты")

# Визуализация
fig, axes = plt.subplots(3, 1, figsize=(14,14))  # теперь 3 графика

# 1️⃣ Верхний график — доход по категориям (столбцы)
axes[0].bar(df_cat['category'], df_cat['revenue'], color='blue')
axes[0].set_title('Revenue by Product Category (Total)')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Revenue')
axes[0].grid(True)

# 2️⃣ Средний график — доход по месяцам
monthly_revenue = df_date.groupby('month')['revenue'].sum()
axes[1].bar(monthly_revenue.index.astype(str), monthly_revenue.values, color='green')
axes[1].set_title('Monthly Revenue')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Revenue')
axes[1].grid(True)

# 3️⃣ Нижний график — доход по категориям **каждый в отдельной линии**
categories = df_date['category'].unique()
for cat in categories:
    cat_data = df_date[df_date['category'] == cat]
    # группируем по дате и суммируем
    cat_daily = cat_data.groupby('order_date')['revenue'].sum()
    axes[2].plot(cat_daily.index, cat_daily.values, marker='o', label=cat)

axes[2].set_title('Daily Revenue by Category (Line Chart)')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Revenue')
axes[2].grid(True)
axes[2].legend()  # подписи для каждой категории

plt.tight_layout()
plt.show()
