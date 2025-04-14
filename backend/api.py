from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data
products = [
    {"id": 1, "name": "Laptop", "price": 1200.00},
    {"id": 2, "name": "Smartphone", "price": 800.00},
    {"id": 3, "name": "Headphones", "price": 150.00},
]

carts = [
    {"id": 1, "items": []},
    {"id": 2, "items": []},
]

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/carts', methods=['GET'])
def get_carts():
    return jsonify(carts)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)