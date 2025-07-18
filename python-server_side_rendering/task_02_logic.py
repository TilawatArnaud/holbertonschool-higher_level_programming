#!/usr/bin/env python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('items.html', items=[])

@app.route('/items')
def show_items():
    try:
        # Check if items.json exists
        if not os.path.exists('items.json'):
            return render_template('items.html', items=[], error="Items file not found")
        
        # Read items from JSON file
        with open('items.json', 'r') as f:
            data = json.load(f)
            
        return render_template('items.html', items=data.get('items', []))
        
    except json.JSONDecodeError:
        return render_template('items.html', items=[], error="Error reading items file")
    except Exception as e:
        return render_template('items.html', items=[], error=str(e))

if __name__ == '__main__':
    # Create a sample items.json if it doesn't exist
    if not os.path.exists('items.json'):
        sample_data = {
            "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
        }
        with open('items.json', 'w') as f:
            json.dump(sample_data, f)
    
    app.run(debug=True, port=5001)
