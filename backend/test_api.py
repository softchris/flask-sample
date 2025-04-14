import unittest
from models import Product, Cart, User

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Laptop", 1200.00)

    def test_to_dict(self):
        self.assertEqual(self.product.to_dict(), {"id": 1, "name": "Laptop", "price": 1200.00})

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart(1)

    def test_to_dict(self):
        self.assertEqual(self.cart.to_dict(), {"id": 1, "items": []})

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Alice", "alice@example.com")

    def test_to_dict(self):
        self.assertEqual(self.user.to_dict(), {"id": 1, "name": "Alice", "email": "alice@example.com"})

if __name__ == "__main__":
    unittest.main()