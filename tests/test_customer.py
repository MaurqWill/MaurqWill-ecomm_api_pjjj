import unittest
from app import create_app
from database import db
from models.customer import Customer

class CustomerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('ProductionConfig')
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_get_customer(self):
        # Create a new customer in the database
        customer = Customer(name='Test Customer', email='test@example.com', phone='1234567890', username='testuser', password='password')
        with self.app.app_context():
            db.session.add(customer)
            db.session.commit()

        # Send a GET request to retrieve the customer
        response = self.client.get(f'/customers/{customer.id}')
        
        # Assert that the retrieval is successful
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['email'], 'test@example.com')

if __name__ == '__main__':
    unittest.main()
