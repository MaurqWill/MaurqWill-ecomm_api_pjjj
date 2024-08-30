# import unittest
# from app import create_app
# from database import db
# from models.product import Product

# class ProductTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.app = create_app('TestingConfig')
#         cls.client = cls.app.test_client()
#         with cls.app.app_context():
#             db.create_all()
    
#     @classmethod
#     def tearDownClass(cls):
#         with cls.app.app_context():
#             db.drop_all()

#     def test_create_product(self):
#         response = self.client.post('/products/create', json={
#             'name': 'Product A',
#             'price': 29.99,
#             'description': 'Description of Product A'
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)

#     def test_get_product(self):
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         db.session.add(product)
#         db.session.commit()
#         response = self.client.get(f'/products/{product.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['name'], 'Product A')

#     def test_update_product(self):
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         db.session.add(product)
#         db.session.commit()
#         response = self.client.put(f'/products/{product.id}', json={'name': 'Product B'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['name'], 'Product B')

#     def test_delete_product(self):
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         db.session.add(product)
#         db.session.commit()
#         response = self.client.delete(f'/products/{product.id}')
#         self.assertEqual(response.status_code, 204)



import unittest
from app import create_app
from database import db
from models.product import Product

class ProductTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('TestingConfig')
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def setUp(self):
        """Create a fresh database session for each test."""
        with self.app.app_context():
            db.session.remove()
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        response = self.client.post('/products/', json={
            'name': 'Product A',
            'price': 29.99,
            'description': 'Description of Product A'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_product(self):
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        db.session.add(product)
        db.session.commit()
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Product A')

    def test_update_product(self):
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        db.session.add(product)
        db.session.commit()
        response = self.client.put(f'/products/{product.id}', json={'name': 'Product B'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Product B')

    def test_delete_product(self):
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        db.session.add(product)
        db.session.commit()
        response = self.client.delete(f'/products/{product.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
