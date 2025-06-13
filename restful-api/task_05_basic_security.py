#!/usr/bin/python3
"""
Flask API with Basic Auth and JWT Authentication
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
import werkzeug.security

app = Flask(__name__)

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": werkzeug.security.generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": werkzeug.security.generate_password_hash("password"),
        "role": "admin"
    }
}


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


@auth.verify_password
def verify_password(username, password):
    if username in users and werkzeug.security.check_password_hash(
            users[username]["password"], password):
        return username
    return None


def admin_required(f):
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_jwt_identity()
        user_role = users.get(current_user, {}).get('role')
        if user_role != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return f(*args, **kwargs)
    return decorated_function


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = verify_password(username, password)
    if not user:
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": access_token})


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@admin_required
def admin_only():
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
