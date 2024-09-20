from database import db
from models.customer import Customer
from utils.util import encode_token
from sqlalchemy import select, update, delete
from flask import jsonify

def login(username, password):
    """
    Log in a customer by username and password.
    """
    try:
        query = select(Customer).where(Customer.username == username)
        customer = db.session.execute(query).scalar_one_or_none()

        if customer and customer.password == password:
            auth_token = encode_token(customer.id, customer.role.role_name)
            # customer_data = customer.to_dict()  # Convert to dictionary

            response = {
                "status": "success",
                "message": "Successfully Logged In",
                "auth_token": auth_token,
                # "customer": customer_data  # Include customer data in the response
            }
        else:
            response = {
                "status": "fail",
                "message": "Invalid username or password"
            }

        return response
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def save(customer_data):

    try:
        new_customer = Customer(
            name=customer_data['name'],
            email=customer_data['email'],
            password=customer_data['password'],
            phone=customer_data['phone'],
            username=customer_data['username']
        )
        db.session.add(new_customer)
        db.session.commit()
        db.session.refresh(new_customer)
        return new_customer.to_dict()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_customer(customer_id):
 
    try:
        query = select(Customer).where(Customer.id == customer_id)
        customer = db.session.execute(query).scalar_one_or_none()
        return customer.to_dict() if customer else None
    except Exception as e:
        return {"status": "error", "message": str(e)}

def update_customer(customer_id, customer_data):

    try:
        query = (
            update(Customer)
            .where(Customer.id == customer_id)
            .values(
                name=customer_data.get('name'),
                email=customer_data.get('email'),
                password=customer_data.get('password'),
                phone=customer_data.get('phone'),
                username=customer_data.get('username'),
                role_id=customer_data.get('role_id')  
            )
        )
        db.session.execute(query)
        db.session.commit()
        return get_customer(customer_id)
    except Exception as e:
      
        return {"status": "error", "message": str(e)}

def delete_customer(customer_id):

    try:
        query = delete(Customer).where(Customer.id == customer_id)
        db.session.execute(query)
        db.session.commit()
        return {"status": "success", "message": "Customer deleted successfully"}
    except Exception as e:
    
        return {"status": "error", "message": str(e)}

def find_all():

    try:
        query = select(Customer)
        all_customers = db.session.execute(query).scalars().all()
        return [customer.to_dict() for customer in all_customers]
    except Exception as e:
        
        return {"status": "error", "message": str(e)}

def find_all_paginate(page, per_page):

    try:
        offset = (page - 1) * per_page
        query = select(Customer).offset(offset).limit(per_page)
        customers = db.session.execute(query).scalars().all()
        return [customer.to_dict() for customer in customers]
    except Exception as e:
        
        return {"status": "error", "message": str(e)}