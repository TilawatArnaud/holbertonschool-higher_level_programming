#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request
import json
import os
from pathlib import Path

app = Flask(__name__)

# Ensure the data directory exists
DATA_DIR = Path(__file__).parent
ITEMS_FILE = DATA_DIR / 'items.json'

def get_items():
    """Helper function to get items from the JSON file."""
    try:
        if not ITEMS_FILE.exists():
            return [], "Items file not found"
        
        with open(ITEMS_FILE, 'r') as f:
            data = json.load(f)
            
        items = data.get('items', [])
        if not isinstance(items, list):
            return [], "Invalid data format: items should be a list"
            
        return items, None
        
    except json.JSONDecodeError:
        return [], "Error: Invalid JSON format in items file"
    except Exception as e:
        return [], f"Error reading items: {str(e)}"

@app.route('/')
def home():
    """Home page that displays the items."""
    items, error = get_items()
    return render_template('items.html', 
                         items=items, 
                         error=error,
                         title="Home - Items List")

@app.route('/items')
def show_items():
    """Route to display all items."""
    items, error = get_items()
    return render_template('items.html', 
                         items=items, 
                         error=error,
                         title="All Items")

@app.route('/items/empty')
def show_empty_items():
    """Test route to show how the template handles an empty list."""
    return render_template('items.html', 
                         items=[], 
                         error=None,
                         title="Empty Items List")

@app.route('/api/items', methods=['GET'])
def api_get_items():
    """API endpoint to get items in JSON format."""
    items, error = get_items()
    if error:
        return jsonify({"status": "error", "message": error}), 500
    return jsonify({"status": "success", "items": items})

if __name__ == '__main__':
    # Create a sample items.json if it doesn't exist
    if not ITEMS_FILE.exists():
        sample_data = {
            "items": [
                "Python Book - Learn Python programming",
                "Flask Mug - For your coffee while coding",
                "Jinja Sticker - Show your template love",
                "Web Development Guide - Master the web",
                "Debugging Manual - Fix all the things"
            ]
        }
        with open(ITEMS_FILE, 'w') as f:
            json.dump(sample_data, f, indent=2)
    
    # Create a test file with an empty list
    empty_items_file = DATA_DIR / 'empty_items.json'
    if not empty_items_file.exists():
        with open(empty_items_file, 'w') as f:
            json.dump({"items": []}, f, indent=2)
    
    # Create a test file with invalid JSON
    invalid_json_file = DATA_DIR / 'invalid_items.json'
    if not invalid_json_file.exists():
        with open(invalid_json_file, 'w') as f:
            f.write('{"items": ["This is invalid JSON')
    
    print(f"Starting server on http://localhost:5001")
    print("Available routes:")
    print("  - /              : Home page with items")
    print("  - /items         : Display all items")
    print("  - /items/empty   : Test empty items list")
    print("  - /api/items     : Get items as JSON")
    
    app.run(debug=True, port=5001, use_reloader=True)
