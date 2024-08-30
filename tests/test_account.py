# import unittest
# from app import create_app
# from database import db
# from models.customerAccount import CustomerAccount
# from models.customer import Customer

# class AccountTests(unittest.TestCase):
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

#     def test_create_account(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         db.session.add(customer)
#         db.session.commit()

#         response = self.client.post('/accounts/create', json={
#             'username': 'janedoe',
#             'password': 'password123',
#             'customer_id': customer.id
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)

#     def test_get_account(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
#         db.session.add(customer)
#         db.session.add(account)
#         db.session.commit()
#         response = self.client.get(f'/accounts/{account.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['username'], 'janedoe')

#     def test_update_account(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
#         db.session.add(customer)
#         db.session.add(account)
#         db.session.commit()
#         response = self.client.put(f'/accounts/{account.id}', json={'username': 'janedoe_updated'})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['username'], 'janedoe_updated')

#     def test_delete_account(self):
#         customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
#         account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
#         db.session.add(customer)
#         db.session.add(account)
#         db.session.commit()
#         response = self.client.delete(f'/accounts/{account.id}')
#         self.assertEqual(response.status_code, 204)




import unittest
from app import create_app
from database import db
from models.customerAccount import CustomerAccount
from models.customer import Customer

class AccountTests(unittest.TestCase):
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

    def test_create_account(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        db.session.add(customer)
        db.session.commit()

        response = self.client.post('/accounts/', json={
            'username': 'janedoe',
            'password': 'password123',
            'customer_id': customer.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_account(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
        db.session.add(customer)
        db.session.add(account)
        db.session.commit()
        response = self.client.get(f'/accounts/{account.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], 'janedoe')

    def test_update_account(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
        db.session.add(customer)
        db.session.add(account)
        db.session.commit()
        response = self.client.put(f'/accounts/{account.id}', json={'username': 'janedoe_updated'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], 'janedoe_updated')

    def test_delete_account(self):
        customer = Customer(name='Jane Doe', email='jane@example.com', phone='0987654321', username='janedoe', password='password123')
        account = CustomerAccount(username='janedoe', password='password123', customer_id=customer.id)
        db.session.add(customer)
        db.session.add(account)
        db.session.commit()
        response = self.client.delete(f'/accounts/{account.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
