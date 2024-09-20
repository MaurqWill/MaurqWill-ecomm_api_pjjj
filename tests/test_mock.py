import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from app import app
from services import customerService

class TestCustomerService(unittest.TestCase):

    @patch('services.customerService.db.session.execute')
    def test_login_customer(self, mock_customer):
        
        faker = Faker()
        mock_user = MagicMock()  
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

            if response:
                self.assertEqual(response['id'], mock_customer.id)
                self.assertEqual(response['username'], mock_customer.username)
                self.assertEqual(response['email'], mock_customer.email)
            else:
                self.fail("Expected customer data but received None")

if __name__ == '__main__':
    unittest.main()
