#!/usr/bin/python3
"""
Flask API for user management.
Users are stored in memory using a dictionary with username as the key.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return a JSON response containing all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """Return a JSON response containing the status of the API."""
    return "OK"

@app.route('/users/<username>')
def get_user(username): 
    """Return the details of a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the API."""
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
        
    data = request.get_json()
    
    username = data.get('username')
    if not username:
        return jsonify({"error": "Missing username"}), 400
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    required_fields = ['name', 'age', 'city']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400
    
    try:
        age = int(data['age'])
    except (ValueError, TypeError):
        return jsonify({"error": "age must be an integer"}), 400
    
    users[username] = {
        "username": username,
        "name": data['name'],
        "age": age,
        "city": data['city']
    }
    return jsonify({"message": "User added successfully", "user": users[username]}), 201
    
if __name__ == "__main__":
    app.run()
