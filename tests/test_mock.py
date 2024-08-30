# import sys
# import os
# import unittest
# from unittest.mock import MagicMock, patch
# from faker import Faker
# from werkzeug.security import generate_password_hash
# from app import app


# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from services import customerService

# class TestLoginCustomer(unittest.TestCase):

#     @patch('services.customerService.db.session.execute')
#     def test_login_customer(self, mock_customer):
#         #set up the return value for our mock object
#         faker           = Faker()
#         mock_user       = MagicMock() #simulate a user retrieved from the database
#         mock_user.id    = 1
#         mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
#         password = faker.password()
#         mock_user.username = faker.user_name()
#         mock_user.password = generate_password_hash(password)
#         mock_customer.return_value.scalar_one_or_none.return_value = mock_user
        
#         with app.app_context():
            
#             response = customerService.login(mock_user.username, password)
#             response_data = response.get_json()

#         self.assertEqual(response_data['status'], 'fail')


#     @patch('services.customerService.db.session.add')
#     @patch('services.customerService.db.session.commit')
#     @patch('services.customerService.Customer')
#     def test_register_customer(self, mock_customer_class, mock_commit, mock_add):
#         faker = Faker()
#         mock_customer = MagicMock()
#         mock_customer.id = 1
#         mock_customer.username = faker.user_name()
#         mock_customer.email = faker.email()
#         mock_customer.password = generate_password_hash(faker.password())
#         mock_customer_class.return_value = mock_customer

#         with app.app_context():
#             response = customerService.register(mock_customer.username, mock_customer.email, mock_customer.password)
#             response_data = response.get_json()

#         self.assertEqual(response_data['status'], 'success')
#         self.assertEqual(response_data['message'], 'Customer registered successfully')

#     @patch('services.customerService.db.session.execute')
#     def test_get_customer_details(self, mock_execute):
#         faker = Faker()
#         mock_user = MagicMock()
#         mock_user.id = 1
#         mock_user.username = faker.user_name()
#         mock_user.email = faker.email()
#         mock_execute.return_value.scalar_one_or_none.return_value = mock_user

#         with app.app_context():
#             response = customerService.get_customer_details(mock_user.id)
#             response_data = response.get_json()

#         self.assertEqual(response_data['status'], 'success')
#         self.assertEqual(response_data['data']['username'], mock_user.username)
#         self.assertEqual(response_data['data']['email'], mock_user.email)


# if __name__ == '__main__':
#     unittest.main()  






import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from app import app
from services import customerService

class TestCustomerService(unittest.TestCase):

    @patch('services.customerService.db.session.execute')
    def test_login_customer(self, mock_customer):
        # Set up the return value for our mock object
        faker = Faker()
        mock_user = MagicMock()  # Simulate a user retrieved from the database
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user
        
        with app.app_context():
            response = customerService.login(mock_user.username, password)
            response_data = response.get_json()

        self.assertEqual(response_data['status'], 'fail')

    @patch('services.customerService.db.session.execute')
    def test_delete_customer(self, mock_execute):
        # Set up the return value for our mock object
        mock_execute.return_value = MagicMock()  # Simulate successful deletion
        
        with app.app_context():
            response = customerService.delete_customer(1)
            response_data = response

        # Check if the response is successful
        self.assertEqual(response_data['status'], 'success')
        self.assertEqual(response_data['message'], 'Customer deleted successfully')

    @patch('services.customerService.db.session.execute')
    def test_get_customer(self, mock_execute):
        faker = Faker()
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.username = faker.user_name()
        mock_customer.email = faker.email()
        mock_customer.to_dict.return_value = {'id': mock_customer.id, 'username': mock_customer.username, 'email': mock_customer.email}
        
        mock_execute.return_value.scalar_one_or_none.return_value = mock_customer

        with app.app_context():
            response = customerService.get_customer(1)
            # Since the function can return a dictionary with customer data or None, handle both cases
            if response:
                self.assertEqual(response['id'], mock_customer.id)
                self.assertEqual(response['username'], mock_customer.username)
                self.assertEqual(response['email'], mock_customer.email)
            else:
                self.fail("Expected customer data but received None")

if __name__ == '__main__':
    unittest.main()
