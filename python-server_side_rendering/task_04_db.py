from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading JSON file: {str(e)}"

def read_csv():
    try:
        products = []
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError as e:
        return f"Error reading CSV file: {str(e)}"

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    except sqlite3.Error as e:
        return f"Error reading from database: {str(e)}"

@app.route('/')
def home():
    return '<h1>Welcome to the Flask App</h1>'

@app.route('/products')
def products():
    source = request.args.get('source', 'json')  # Default source to JSON
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if isinstance(products, str):  # Check if an error message was returned
        return render_template('product_display.html', error=products)

    if product_id:
        try:
            product_id = int(product_id)  # Convert product_id to integer
            products = [p for p in products if int(p['id']) == product_id]
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID format")
        
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port if necessary