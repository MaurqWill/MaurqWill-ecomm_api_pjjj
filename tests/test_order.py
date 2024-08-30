# import unittest
# from app import create_app
# from database import db
# from models.order import Order
# from models.product import Product
# from models.customer import Customer

# class OrderTests(unittest.TestCase):
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

#     def test_create_order(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         db.session.add(customer)
#         db.session.add(product)
#         db.session.commit()

#         response = self.client.post('/orders/create', json={
#             'order_date': '2024-08-24T00:00:00',
#             'customer_id': customer.id,
#             'products': [product.id]
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)

#     def test_get_order(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         product = Product(name='Product A', price=29.99, description='Description of Product A')
#         order = Order(order_date='2024-08-24T00:00:00', customer_id=customer.id)
#         order.products.append(product)
#         db.session.add(customer)
#         db.session.add(product)
#         db.session.add(order)
#         db.session.commit()
#         response = self.client.get(f'/orders/{order.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['order_date'], '2024-08-24T00:00:00')

import unittest
from app import create_app
from database import db
from models.order import Order
from models.product import Product
from models.customer import Customer

class OrderTests(unittest.TestCase):
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

    def test_create_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        db.session.add(customer)
        db.session.add(product)
        db.session.commit()

        response = self.client.post('/orders/', json={
            'order_date': '2024-08-24',
            'customer_id': customer.id,
            'products_ids': [product.id]  # Ensure the key matches your implementation
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        order = Order(order_date='2024-08-24', customer_id=customer.id)
        order.products.append(product)
        db.session.add(customer)
        db.session.add(product)
        db.session.add(order)
        db.session.commit()
        response = self.client.get(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['order_date'], '2024-08-24')

    def test_update_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        order = Order(order_date='2024-08-24', customer_id=customer.id)
        order.products.append(product)
        db.session.add(customer)
        db.session.add(product)
        db.session.add(order)
        db.session.commit()
        response = self.client.put(f'/orders/{order.id}', json={'order_date': '2024-08-25'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['order_date'], '2024-08-25')

    def test_delete_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        order = Order(order_date='2024-08-24', customer_id=customer.id)
        order.products.append(product)
        db.session.add(customer)
        db.session.add(product)
        db.session.add(order)
        db.session.commit()
        response = self.client.delete(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
