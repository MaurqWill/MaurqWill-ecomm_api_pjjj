from flask import request, jsonify, Blueprint
from services import customerAccountService  # Import your service module
from marshmallow import ValidationError
from models.schemas.customerAccountSchema import customer_account_schema, customer_accounts_schema
from utils.util import token_required, admin_required  # Import your role-based access decorators

# Define a Blueprint for customer account routes
customer_account_bp = Blueprint('customer_account', __name__)

@customer_account_bp.route('/accounts', methods=['POST'])
@admin_required
def create_account():
    """
    Endpoint to create a new customer account.
    Only accessible by admin users.
    """
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_account = customerAccountService.create_account(account_data)
    return customer_account_schema.jsonify(new_account), 201

@customer_account_bp.route('/accounts/<int:account_id>', methods=['GET'])
@token_required
def get_account(account_id):
    """
    Endpoint to retrieve a customer account by ID.
    Accessible by authenticated users.
    """
    account = customerAccountService.get_account(account_id)
    if account:
        return customer_account_schema.jsonify(account), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@customer_account_bp.route('/accounts/<int:account_id>', methods=['PUT'])
@admin_required
def update_account(account_id):
    """
    Endpoint to update customer account details by ID.
    Only accessible by admin users.
    """
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_account = customerAccountService.update_account(account_id, account_data)
    if updated_account:
        return customer_account_schema.jsonify(updated_account), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@customer_account_bp.route('/accounts/<int:account_id>', methods=['DELETE'])
@admin_required
def delete_account(account_id):
    """
    Endpoint to delete a customer account by ID.
    Only accessible by admin users.
    """
    customerAccountService.delete_account(account_id)
    return jsonify({'message': 'Account deleted successfully'}), 204

@customer_account_bp.route('/accounts', methods=['GET'])
@admin_required
def find_all_accounts():
    """
    Endpoint to retrieve all customer accounts.
    Only accessible by admin users.
    """
    accounts = customerAccountService.find_all_accounts()
    return customer_accounts_schema.jsonify(accounts), 200

@customer_account_bp.route('/accounts/paginate', methods=['GET'])
@admin_required
def find_all_accounts_paginate():
    """
    Endpoint to retrieve customer accounts with pagination.
    Only accessible by admin users.
    """
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    accounts = customerAccountService.find_all_accounts_paginate(page, per_page)
    return customer_accounts_schema.jsonify(accounts.items), 200
