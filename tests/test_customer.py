import unittest
from app import create_app
from database import db
from models.customer import Customer

class CustomerTests(unittest.TestCase):
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

    def test_create_customer(self):
        response = self.client.post('/customers/create', json={
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'username': 'janedoe',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_customer(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        db.session.add(customer)
        db.session.commit()
        response = self.client.get(f'/customers/{customer.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Jane Doe')

    def test_update_customer(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        db.session.add(customer)
        db.session.commit()
        response = self.client.put(f'/customers/{customer.id}', json={'name': 'Jane Smith'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Jane Smith')

    def test_delete_customer(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        db.session.add(customer)
        db.session.commit()
        response = self.client.delete(f'/customers/{customer.id}')
        self.assertEqual(response.status_code, 204)