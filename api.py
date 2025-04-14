from flask import Flask, request, jsonify
from models import carts  # Ensure this is the same `carts` list used in the test
from services import (
    get_all_products, get_product_by_id, create_product, update_product, delete_product,
    get_all_carts, get_cart_by_id, create_cart, update_cart, delete_cart,
    get_all_users, get_user_by_id, create_user, update_user, delete_user
)

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product_route():
    new_product = create_product(request.json)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    updated_product = update_product(product_id, request.json)
    if updated_product:
        return jsonify(updated_product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    delete_product(product_id)
    return jsonify({"message": "Product deleted"}), 200

@app.route('/carts', methods=['GET'])
def get_carts():
    return jsonify(get_all_carts())

@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    print(f"Getting cart {cart_id}")  # Debugging statement
    cart = get_cart_by_id(cart_id)
    if cart:
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts', methods=['POST'])
def create_cart_route():
    new_cart = create_cart()
    return jsonify(new_cart), 201

@app.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart_route(cart_id):
    updated_cart = update_cart(cart_id, request.json)
    if updated_cart:
        return jsonify(updated_cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart_route(cart_id):
    delete_cart(cart_id)
    return jsonify({"message": "Cart deleted"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(get_all_users())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user_route():
    new_user = create_user(request.json)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    updated_user = update_user(user_id, request.json)
    if updated_user:
        return jsonify(updated_user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    delete_user(user_id)
    return jsonify({"message": "User deleted"}), 200

@app.route('/routes', methods=['GET'])
def list_routes():
    """
    List all registered routes in the application.

    Returns:
        Response: A JSON response containing all routes.
    """
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            "endpoint": rule.endpoint,
            "methods": list(rule.methods),
            "url": str(rule)
        })
    return jsonify(routes)

if __name__ == "__main__":
    app.run(debug=True)