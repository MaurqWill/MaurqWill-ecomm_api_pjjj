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
#         # Send a POST request to create a new product
#         response = self.client.post('/products/create', json={
#             'name': 'Test Product',
#             'price': 99.99,
#             'description': 'A product for testing purposes'
#         })
        
#         # Assert that the product creation is successful
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)
#         self.assertEqual(response.json['name'], 'Test Product')

# if __name__ == '__main__':
#     unittest.main()





# # test_product.py
# import unittest
# from app import create_app
# from database import db
# from models.product import Product

# class ProductTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.app = create_app('TestingConfig')  # Using the TestingConfig
#         cls.client = cls.app.test_client()
#         with cls.app.app_context():
#             db.create_all()
    
#     @classmethod
#     def tearDownClass(cls):
#         with cls.app.app_context():
#             db.drop_all()

#     def setUp(self):
#         """Set up a new database for each test."""
#         self.app = ProductTests.app
#         self.client = ProductTests.client
#         with self.app.app_context():
#             db.session.begin(subtransactions=True)

#     def tearDown(self):
#         """Rollback any changes to the database."""
#         with self.app.app_context():
#             db.session.rollback()

#     def test_create_product(self):
#         """Test creating a new product."""
#         response = self.client.post('/products/create', json={
#             'name': 'Product A',
#             'price': 29.99,
#             'description': 'Description of Product A'
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)
#         self.assertEqual(response.json['name'], 'Product A')

#     def test_get_product(self):
#         """Test retrieving a product by ID."""
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         with self.app.app_context():
#             db.session.add(product)
#             db.session.commit()

#         response = self.client.get(f'/products/{product.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['name'], 'Product A')

#     def test_update_product(self):
#         """Test updating a product."""
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         with self.app.app_context():
#             db.session.add(product)
#             db.session.commit()

#         response = self.client.put(f'/products/{product.id}', json={'name': 'Product B'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['name'], 'Product B')

# if __name__ == '__main__':
#     unittest.main()
