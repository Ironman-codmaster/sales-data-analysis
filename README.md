📊 Sales Data Analysis (SQL + Python)
🧠 Project Overview
This project demonstrates a complete data analysis workflow using a relational database, SQL queries, and Python data analysis tools.
The goal is to analyze sales performance and extract business insights from transactional data.
The project simulates a real-world scenario where a company stores its sales data in a database and wants to understand:

Revenue trends
Top-performing product categories
Customer and regional performance

💼 Business Problem
Company management needs answers to the following questions:
How does total revenue change over time?
Which product categories generate the most revenue?
Which regions contribute most to sales?
What insights can help improve business decisions?

🛠 Technologies Used
Python
SQLite
SQL
pandas
matplotlib
Jupyter Notebook

🗂 Project Structure
sales-data-analysis/

│

├── database.db             # SQLite database

├── create_tables.py        # Script to create database tables

├── analysis_2.py           # Main analysis script

└── README.md               # Project description

🗄 Database Schema

customers
| Column            | Type    |
| ----------------- | ------- |
| customer_id       | INTEGER |
| region            | TEXT    |
| registration_date | DATE    |

products
| Column     | Type    |
| ---------- | ------- |
| product_id | INTEGER |
| category   | TEXT    |
| price      | REAL    |

orders
| Column      | Type    |
| ----------- | ------- |
| order_id    | INTEGER |
| customer_id | INTEGER |
| product_id  | INTEGER |
| quantity    | INTEGER |
| order_date  | DATE    |

📈 Analysis Performed
Database creation with create_tables.py
Data generation and storage in database.db
SQL queries for revenue analysis
Analysis using Python (analysis_2.py) with pandas and matplotlib
Revenue analysis by:
Product category
Daily revenue
Monthly revenue
Data visualization using matplotlib

🔍 Example SQL Query
SELECT
    p.category,
    SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category;

📊 Visualization
Daily revenue trends (line plot)
Monthly revenue comparison (bar chart)
All charts generated in Python script analysis_2.py

🧠 Key Insights
Certain product categories generate significantly higher revenue
Sales patterns show seasonal trends
Regional performance varies and can guide marketing strategy

▶️ How to Run the Project
Run create_tables.py to create the database tables or use database.db.
Run analysis_2.py to generate data, run analysis, and produce charts.
Explore the generated plots for insights.

📌 Author
Data Analyst
Portfolio project

🔗 Links
GitHub repository:
LinkedIn profile:
