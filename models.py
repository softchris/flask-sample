class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}


class Cart:
    def __init__(self, cart_id):
        self.id = cart_id
        self.items = []

    def to_dict(self):
        return {"id": self.id, "items": self.items}


# Sample data
products = [
    Product(1, "Laptop", 1200.00).to_dict(),
    Product(2, "Smartphone", 800.00).to_dict(),
    Product(3, "Headphones", 150.00).to_dict(),
]

carts = [
    Cart(1).to_dict(),
    Cart(2).to_dict(),
]
