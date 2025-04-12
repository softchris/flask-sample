from flask import Flask, jsonify, request

app = Flask(__name__)

# Static data
products = [
    {"id": 1, "name": "Laptop", "price": 1000, "stock": 10},
    {"id": 2, "name": "Phone", "price": 500, "stock": 20},
]

carts = [
    {"id": 1, "items": [{"product_id": 1, "quantity": 1}]},
]

# Products CRUD
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product.update(request.json)
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

# Carts CRUD
@app.route('/carts', methods=['GET'])
def get_carts():
    return jsonify(carts)

@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    cart = next((c for c in carts if c["id"] == cart_id), None)
    if cart:
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts', methods=['POST'])
def create_cart():
    new_cart = {"id": len(carts) + 1, "items": []}
    carts.append(new_cart)
    return jsonify(new_cart), 201

@app.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    cart = next((c for c in carts if c["id"] == cart_id), None)
    if cart:
        cart.update(request.json)
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    global carts
    carts = [c for c in carts if c["id"] != cart_id]
    return jsonify({"message": "Cart deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)