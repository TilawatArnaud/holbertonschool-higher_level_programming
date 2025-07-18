#!/usr/bin/env python3
from flask import Flask, render_template, request, g
import json
import csv
import sqlite3
import os
from contextlib import closing

app = Flask(__name__)
app.config['DATABASE'] = 'products.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with closing(get_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def home():
    return """
    <h1>Products API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><code>/products?source=json</code> - Get products from JSON</li>
        <li><code>/products?source=csv</code> - Get products from CSV</li>
        <li><code>/products?source=sql</code> - Get products from SQLite</li>
        <li>Add <code>&id=X</code> to any URL to get a specific product by ID</li>
    </ul>
    """

@app.route('/products')
def show_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json', 'csv', or 'sql'")
    
    try:
        if source == 'json':
            products = read_json_products()
        elif source == 'csv':
            products = read_csv_products()
        else:  # source == 'sql'
            products = read_sql_products()
        
        if product_id:
            try:
                product_id = int(product_id)
                product = next((p for p in products if p['id'] == product_id), None)
                if not product:
                    return render_template('product_display.html',
                                        error=f"Product with ID {product_id} not found")
                products = [product]
            except ValueError:
                return render_template('product_display.html',
                                    error="Invalid product ID. Must be a number.")
        
        return render_template('product_display.html', products=products)
        
    except Exception as e:
        return render_template('product_display.html',
                            error=f"Error processing request: {str(e)}")

def read_json_products():
    if not os.path.exists('products.json'):
        return []
    
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv_products():
    if not os.path.exists('products.csv'):
        return []
    
    products = []
    with open('products.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
            except (ValueError, KeyError):
                continue
    
    return products

def read_sql_products():
    db = get_db()
    cursor = db.execute('SELECT id, name, category, price FROM Products')
    products = []
    for row in cursor.fetchall():
        products.append(dict(row))
    return products

if __name__ == '__main__':
    # Create sample data files if they don't exist
    if not os.path.exists('products.json'):
        sample_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Notebook", "category": "Stationery", "price": 5.99}
        ]
        with open('products.json', 'w') as f:
            json.dump(sample_data, f, indent=2)
    
    if not os.path.exists('products.csv'):
        with open('products.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'category', 'price'])
            writer.writeheader()
            writer.writerow({"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99})
            writer.writerow({"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99})
            writer.writerow({"id": 3, "name": "Notebook", "category": "Stationery", "price": 5.99})
    
    # Ensure the database exists and has data
    if not os.path.exists('products.db'):
        from create_database import create_database
        create_database()
    
    app.run(debug=True, port=5003)
