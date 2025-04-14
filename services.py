from models import products, carts

def get_all_products():
    return products

def get_product_by_id(product_id):
    return next((p for p in products if p["id"] == product_id), None)

def create_product(data):
    new_product = data
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return new_product

def update_product(product_id, data):
    product = get_product_by_id(product_id)
    if product:
        product.update(data)
    return product

def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]

def get_all_carts():
    return carts

def get_cart_by_id(cart_id):
    return next((c for c in carts if c["id"] == cart_id), None)

def create_cart():
    new_cart = {"id": len(carts) + 1, "items": []}
    carts.append(new_cart)
    return new_cart

def update_cart(cart_id, data):
    cart = get_cart_by_id(cart_id)
    if cart:
        cart.update(data)
    return cart

def delete_cart(cart_id):
    global carts
    carts = [c for c in carts if c["id"] != cart_id]
