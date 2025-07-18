#!/usr/bin/env python3
import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create Products table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        # Insert sample data
        sample_products = [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Notebook', 'Stationery', 5.99),
            (4, 'Wireless Mouse', 'Electronics', 24.99),
            (5, 'Desk Lamp', 'Home Goods', 29.99)
        ]
        cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?)', sample_products)
    
    conn.commit()
    conn.close()
    print("Database setup complete!")

if __name__ == '__main__':
    create_database()
