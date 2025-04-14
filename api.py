from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the products and carts lists
products = []
carts = []

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve all products.

    This endpoint handles GET requests to fetch a list of all available products.
    The products are returned in JSON format.

    Returns:
        Response: A JSON response containing a list of all products.
    """
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a product by its ID.

    This endpoint handles GET requests to fetch details of a specific product
    based on the provided product ID. If the product exists, its details are
    returned in JSON format. If the product is not found, a 404 error response
    is returned with an appropriate error message.

    Args:
        product_id (int): The unique identifier of the product to retrieve.

    Returns:
        Response: A JSON response containing the product details if found,
        or an error message with a 404 status code if the product does not exist.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product.

    This endpoint handles POST requests to create a new product. It expects a JSON
    payload containing the product details. A unique ID is assigned to the new product,
    which is then added to the `products` list.

    Returns:
        Response: A JSON response containing the newly created product and a 201 status code.
    """
    new_product = request.json
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product.

    This endpoint handles PUT requests to update the details of an existing product
    identified by its ID. The updated details are provided in the JSON payload.

    Args:
        product_id (int): The unique identifier of the product to update.

    Returns:
        Response: A JSON response containing the updated product details if found,
        or an error message with a 404 status code if the product does not exist.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product.update(request.json)
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product.

    This endpoint handles DELETE requests to remove a product identified by its ID
    from the `products` list.

    Args:
        product_id (int): The unique identifier of the product to delete.

    Returns:
        Response: A JSON response with a success message and a 200 status code.
    """
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

@app.route('/carts', methods=['GET'])
def get_carts():
    """
    Retrieve all shopping carts.

    This endpoint handles GET requests to fetch a list of all shopping carts.
    The carts are returned in JSON format.

    Returns:
        Response: A JSON response containing a list of all shopping carts.
    """
    return jsonify(carts)

@app.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    """
    Retrieve a shopping cart by its ID.

    This endpoint handles GET requests to fetch details of a specific shopping cart
    based on the provided cart ID. If the cart exists, its details are returned in
    JSON format. If the cart is not found, a 404 error response is returned.

    Args:
        cart_id (int): The unique identifier of the cart to retrieve.

    Returns:
        Response: A JSON response containing the cart details if found,
        or an error message with a 404 status code if the cart does not exist.
    """
    cart = next((c for c in carts if c["id"] == cart_id), None)
    if cart:
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts', methods=['POST'])
def create_cart():
    """
    Create a new shopping cart.

    This endpoint handles POST requests to create a new shopping cart. A unique ID
    is assigned to the new cart, which is then added to the `carts` list.

    Returns:
        Response: A JSON response containing the newly created cart and a 201 status code.
    """
    new_cart = {"id": len(carts) + 1, "items": []}
    carts.append(new_cart)
    return jsonify(new_cart), 201

@app.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    """
    Update an existing shopping cart.

    This endpoint handles PUT requests to update the details of an existing shopping cart
    identified by its ID. The updated details are provided in the JSON payload.

    Args:
        cart_id (int): The unique identifier of the cart to update.

    Returns:
        Response: A JSON response containing the updated cart details if found,
        or an error message with a 404 status code if the cart does not exist.
    """
    cart = next((c for c in carts if c["id"] == cart_id), None)
    if cart:
        cart.update(request.json)
        return jsonify(cart)
    return jsonify({"error": "Cart not found"}), 404

@app.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    """
    Delete a shopping cart.

    This endpoint handles DELETE requests to remove a shopping cart identified by its ID
    from the `carts` list.

    Args:
        cart_id (int): The unique identifier of the cart to delete.

    Returns:
        Response: A JSON response with a success message and a 200 status code.
    """
    global carts
    carts = [c for c in carts if c["id"] != cart_id]
    return jsonify({"message": "Cart deleted"}), 200