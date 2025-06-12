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
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username): 
    """Return the details of a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user')
def add_user():
    """Add a new user to the API."""
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Missing username"}), 400
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {
        "username": username,
        "name": request.args.get('name'),
        "age": int(request.args.get('age')),
        "city": request.args.get('city')
    }
    return jsonify({"message": "User added successfully"}), 201
    
if __name__ == "__main__":
    app.run()
