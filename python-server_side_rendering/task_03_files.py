#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Products API. Use /products?source=json or /products?source=csv"

@app.route('/products')
def show_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json' or 'csv'")
    
    try:
        if source == 'json':
            products = read_json_products()
        else:  # source == 'csv'
            products = read_csv_products()
        
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
        # Create sample JSON data if file doesn't exist
        sample_data = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Notebook", "category": "Stationery", "price": 5.99}
        ]
        with open('products.json', 'w') as f:
            json.dump(sample_data, f, indent=2)
    
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv_products():
    csv_file = 'products.csv'
    if not os.path.exists(csv_file):
        # Create sample CSV data if file doesn't exist
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'category', 'price'])
            writer.writeheader()
            writer.writerow({"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99})
            writer.writerow({"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99})
            writer.writerow({"id": 3, "name": "Notebook", "category": "Stationery", "price": 5.99})
    
    products = []
    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert string values to appropriate types
            product = {
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            }
            products.append(product)
    
    return products

if __name__ == '__main__':
    # Ensure the data files exist with sample data
    if not os.path.exists('products.json'):
        read_json_products()
    if not os.path.exists('products.csv'):
        read_csv_products()
    
    app.run(debug=True, port=5002)
