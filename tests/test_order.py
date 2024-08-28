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

    def test_create_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        db.session.add(customer)
        db.session.add(product)
        db.session.commit()

        response = self.client.post('/orders/create', json={
            'order_date': '2024-08-24T00:00:00',
            'customer_id': customer.id,
            'products': [product.id]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_order(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        product = Product(name='Product A', price=29.99, description='Description of Product A')
        order = Order(order_date='2024-08-24T00:00:00', customer_id=customer.id)
        order.products.append(product)
        db.session.add(customer)
        db.session.add(product)
        db.session.add(order)
        db.session.commit()
        response = self.client.get(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['order_date'], '2024-08-24T00:00:00')