import sqlite3

products = [
    ("Telefon", 1200, "images/phone.jpg"),
    ("Laptop", 3500, "images/laptop.jpg"),
    ("Ceas Inteligent", 800, "images/watch.jpg")
]

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        image TEXT NOT NULL
    )
""")

cursor.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)
conn.commit()
conn.close()

print("Baza de date a fost populată.")