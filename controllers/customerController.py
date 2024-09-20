from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService  
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, admin_required 

def login():
    """
    Handles customer login by generating a JWT token.
    """
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'message': 'Invalid payload, expecting username and password'}), 401

    if token:
        return jsonify(token), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

def save():

    try:
        # Validate and deserialize the incoming data
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_saved), 201

@cache.cached(timeout=60)
@admin_required
def find_all():

    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200

@admin_required
def find_all_paginate():

    try:
        page = int(request.args.get('page', 1))  # Default to page 1 if not provided
        per_page = int(request.args.get('per_page', 10))  # Default to 10 per page if not provided
    except ValueError:
        return jsonify({'message': 'Page and per_page must be integers'}), 400

    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers.items), 200

@token_required
def get_customer(customer_id):

    customer = customerService.get_customer(customer_id)
    if customer:
        return customer_schema.jsonify(customer), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404

@admin_required
def update_customer(customer_id):

    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_customer = customerService.update(customer_id, customer_data)
    if updated_customer:
        return customer_schema.jsonify(updated_customer), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404

@admin_required
def delete_customer(customer_id):

    customerService.delete(customer_id)
    return jsonify({'message': 'Customer deleted successfully'}), 204
