# E-Commerce Backend Service

## Description

This project is a backend service for managing an e-commerce platform. It includes features for managing products, orders, customers, and customer accounts. The service is built using Flask and SQLAlchemy, and includes unit tests to ensure functionality.

## Features

- **Product Management**:
  - Save new products
  - Retrieve product details by ID
  - Retrieve all products
  - Search products by name
  - Update product details
  - Delete products

- **Order Management**:
  - Save new orders
  - Retrieve all orders
  - Retrieve order details by ID
  - Retrieve orders by customer ID
  - Retrieve orders by customer email
  - Update order details
  - Delete orders

- **Customer Management**:
  - Customer login
  - Save new customers
  - Retrieve customer details by ID
  - Update customer details
  - Delete customers
  - Retrieve all customers
  - Paginate customer retrieval

- **Customer Account Management**:
  - Create new customer accounts
  - Retrieve customer account details by ID
  - Update customer account details
  - Delete customer accounts
  - Retrieve all customer accounts
  - Paginate customer account retrieval

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- MySQL server
- Git

### Clone the Repository

```sh
git clone https://github.com/MaurqWill/MaurqWill-ecomm_api_pjjj
cd MaurqWill-ecomm_api_pjjj
```

### Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Set Up the Database

1. **Install MySQL Server**:
   - On Ubuntu:
     ```sh
     sudo apt-get install mysql-server
     sudo service mysql start
     ```
   - On Windows, download and install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/installer/).

2. **Create Database and User**:
   ```sh
   mysql -u root -p
   CREATE DATABASE IF NOT EXISTS bes_ecomm;
   CREATE USER 'root'@'localhost' IDENTIFIED BY 'C0dingTemp012!';
   GRANT ALL PRIVILEGES ON bes_ecomm.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```



### Configure Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:C0dingTemp012!@localhost/bes_ecomm
CACHE_TYPE=simple
RATELIMIT_DEFAULT=100 per day
```

### Run the Application

```sh
flask run
```

### Running Tests

To run the unit tests, use the following command:

```sh
python -m unittest discover -s tests -p 'test_*.py'
```

## Usage

### Product Management

- **Save Product**:
  - Endpoint: `/products`
  - Method: `POST`
  - Payload:
    ```json
    {
      "name": "Product Name",
      "price": 100.0
    }
    ```

- **Get Product**:
  - Endpoint: `/products/<product_id>`
  - Method: `GET`

- **Find All Products**:
  - Endpoint: `/products`
  - Method: `GET`

- **Search Product**:
  - Endpoint: `/products/search`
  - Method: `GET`
  - Query Parameter: [`search_term`]

- **Update Product**:
  - Endpoint: `/products/<product_id>`
  - Method: `PUT`
  - Payload:
    ```json
    {
      "name": "Updated Product Name",
      "price": 150.0
    }
    ```

- **Delete Product**:
  - Endpoint: `/products/<product_id>`
  - Method: `DELETE`

### Order Management

- **Save Order**:
  - Endpoint: `/orders`
  - Method: `POST`
  - Payload:
    ```json
    {
      "customer_id": 1,
      "products_ids": [1, 2, 3]
    }
    ```

- **Get Order**:
  - Endpoint: `/orders/<order_id>`
  - Method: `GET`

- **Find All Orders**:
  - Endpoint: `/orders`
  - Method: `GET`

- **Find Orders by Customer ID**:
  - Endpoint: `/orders/customer/<customer_id>`
  - Method: `GET`

- **Find Orders by Customer Email**:
  - Endpoint: `/orders/customer/email`
  - Method: `GET`
  - Query Parameter: `email`

- **Update Order**:
  - Endpoint: `/orders/<order_id>`
  - Method: `PUT`
  - Payload:
    ```json
    {
      "customer_id": 1,
      "products_ids": [1, 2, 3]
    }
    ```

- **Delete Order**:
  - Endpoint: `/orders/<order_id>`
  - Method: `DELETE`

### Customer Management

- **Login**:
  - Endpoint: `/login`
  - Method: `POST`
  - Payload:
    ```json
    {
      "username": "example_user",
      "password": "example_password"
    }
    ```

- **Save Customer**:
  - Endpoint: `/customers`
  - Method: `POST`
  - Payload:
    ```json
    {
      "name": "Customer Name",
      "email": "customer@example.com",
      "password": "password",
      "phone": "1234567890",
      "username": "customer_username"
    }
    ```

- **Get Customer**:
  - Endpoint: `/customers/<customer_id>`
  - Method: `GET`

- **Find All Customers**:
  - Endpoint: `/customers`
  - Method: `GET`

- **Update Customer**:
  - Endpoint: `/customers/<customer_id>`
  - Method: `PUT`
  - Payload:
    ```json
    {
      "name": "Updated Customer Name",
      "email": "updated@example.com",
      "password": "newpassword",
      "phone": "0987654321",
      "username": "updated_username",
      "role_id": 2
    }
    ```

- **Delete Customer**:
  - Endpoint: `/customers/<customer_id>`
  - Method: `DELETE`

### Customer Account Management

- **Create Account**:
  - Endpoint: /accounts
  - Method: POST
  - Payload:
    ```json
    {
      "username": "john_doe",
      "password": "securepassword",
      "customer_id": 1
    }
    ```

- **Get Account**:
  - Endpoint: /accounts/<account_id>
  - Method: GET

- **Find All Accounts**:
  - Endpoint: /accounts
  - Method: GET

- **Find All Accounts with Pagination**:
  - Endpoint: /accounts/paginate?page=<page>&per_page=<per_page>
  - Method: GET

- **Update Account**:
  - Endpoint: /accounts/<account_id>
  - Method: PUT
  - Payload:
    ```JSON
    {
      "username": "john_doe_updated",
      "password": "newsecurepassword",
      "customer_id": 1
    }
    ```
    
- **Delete Account**:
  - Endpoint: /accounts/<account_id>
  - Method: DELETE



## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes ([`git commit -m 'Add some feature'`].
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
