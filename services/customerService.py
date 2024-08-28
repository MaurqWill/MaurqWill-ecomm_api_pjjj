from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to create Customer Objects
from utils.util import encode_token

from sqlalchemy import select

def login(username, password): #Login using unique info so we don't query multiple users
    query = select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalar_one_or_none() #Query customer table for a customer with the password and username

    if customer and customer.password == password:#if we have a customer associated with the username, validated the password
        auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status":"success",
            "message":"Successfully Logged In",
            "auth_token": auth_token
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "Invalid username or password"
        }
        return response


def save(customer_data):
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], password=customer_data['password'], phone=customer_data['phone'], username=customer_data['username'])
    db.session.add(new_customer)
    db.session.commit()

    db.session.refresh(new_customer)
    return new_customer

def get_customer(customer_id):
    """
    Retrieve a customer by ID.
    """
    query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(query).scalar_one_or_none()
    return customer

def update_customer(customer_id, customer_data):
    """
    Update customer details based on their ID.
    """
    query = (
        update_customer(Customer)
        .where(Customer.id == customer_id)
        .values(
            name=customer_data.get('name'),
            email=customer_data.get('email'),
            password=customer_data.get('password'),
            phone=customer_data.get('phone'),
            username=customer_data.get('username'),
            role_id=customer_data.get('role_id')  # Optional, if you have role_id in your data
        )
    )
    db.session.execute(query)
    db.session.commit()
    return get_customer(customer_id)

def delete_customer(customer_id):
    """
    Delete a customer from the database based on their ID.
    """
    query = delete_customer(Customer).where(Customer.id == customer_id)
    db.session.execute(query)
    db.session.commit()



def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    customers = db.paginate(select(Customer), page = page, per_page = per_page)
    return customers