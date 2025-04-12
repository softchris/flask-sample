import unittest
from flask import json
from api import app

# test_api-test.py

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Products Tests
    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_product_success(self):
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", json.loads(response.data))

    def test_get_product_not_found(self):
        response = self.app.get('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

    def test_create_product(self):
        new_product = {"name": "Tablet", "price": 300, "stock": 15}
        response = self.app.post(
            '/products',
            data=json.dumps(new_product),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", json.loads(response.data))

    def test_update_product_success(self):
        updated_data = {"name": "Updated Laptop", "price": 1200, "stock": 8}
        response = self.app.put(
            '/products/1',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["name"], "Updated Laptop")

    def test_update_product_not_found(self):
        updated_data = {"name": "Non-existent Product", "price": 100, "stock": 0}
        response = self.app.put(
            '/products/999',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

    def test_delete_product_success(self):
        response = self.app.delete('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", json.loads(response.data))

    def test_delete_product_not_found(self):
        response = self.app.delete('/products/999')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", json.loads(response.data))

    # Carts Tests
    def test_get_carts(self):
        response = self.app.get('/carts')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_cart_success(self):
        response = self.app.get('/carts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", json.loads(response.data))

    def test_get_cart_not_found(self):
        response = self.app.get('/carts/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

    def test_create_cart(self):
        response = self.app.post('/carts')
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", json.loads(response.data))

    def test_update_cart_success(self):
        updated_data = {"items": [{"product_id": 2, "quantity": 3}]}
        response = self.app.put(
            '/carts/1',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["items"], updated_data["items"])

    def test_update_cart_not_found(self):
        updated_data = {"items": [{"product_id": 2, "quantity": 3}]}
        response = self.app.put(
            '/carts/999',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", json.loads(response.data))

    def test_delete_cart_success(self):
        response = self.app.delete('/carts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", json.loads(response.data))

    def test_delete_cart_not_found(self):
        response = self.app.delete('/carts/999')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", json.loads(response.data))

if __name__ == '__main__':
    unittest.main()