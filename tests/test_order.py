# import unittest
# from app import create_app
# from database import db
# from models.order import Order
# from models.customer import Customer
# from models.product import Product

# class OrderTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.app = create_app('ProductionConfig')
#         cls.client = cls.app.test_client()
#         with cls.app.app_context():
#             db.create_all()

#     @classmethod
#     def tearDownClass(cls):
#         with cls.app.app_context():
#             db.drop_all()

#     def test_create_order(self):
#         with self.app.app_context():
#             # Create a customer and a product
#             customer = Customer(name='Order Customer', email='ordercustomer@example.com', phone='1234567890', username='orderuser', password='password')
#             product = Product(name='Order Product', price=49.99, description='A product for order testing')
#             db.session.add(customer)
#             db.session.add(product)
#             db.session.commit()

#             # Send a POST request to create a new order
#             response = self.client.post('/orders/create', json={
#                 'order_date': '2024-08-24T00:00:00',
#                 'customer_id': customer.id,
#                 'products': [product.id]
#             })

#             # Assert that the order creation is successful
#             self.assertEqual(response.status_code, 201)
#             self.assertIn('id', response.json)

# if __name__ == '__main__':
#     unittest.main()
