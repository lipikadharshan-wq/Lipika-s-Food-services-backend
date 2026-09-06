import sqlite3

connection = sqlite3.connect("food_services.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone TEXT,
    food_item TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL
)
""")

connection.commit()
connection.close()
