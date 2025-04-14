from models import products, carts, users

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
        print(f"Updating product: {product}")  # Debugging statement
        for key in data:
            if key in product:
                product[key] = data[key]
        print(f"Updated product: {product}")  # Debugging statement
        return product
    print(f"Product with ID {product_id} not found")  # Debugging statement
    return None

def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]

def get_all_carts():
    return carts

def get_cart_by_id(cart_id):
    print(f"Current carts: {carts}")  # Debugging statement
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

def get_all_users():
    return users

def get_user_by_id(user_id):
    return next((u for u in users if u["id"] == user_id), None)

def create_user(data):
    new_user = {"id": len(users) + 1, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return new_user

def update_user(user_id, data):
    user = get_user_by_id(user_id)
    if user:
        user.update(data)
    return user

def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
