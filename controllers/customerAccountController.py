from flask import request, jsonify
from marshmallow import ValidationError
from models.schemas.customerAccountSchema import customer_account_schema, customer_accounts_schema
from services import customerAccountService

from utils.util import token_required, admin_required

@admin_required
def create_account():
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_account = customerAccountService.create_account(account_data)
    return customer_account_schema.jsonify(new_account), 201

@token_required
def get_account(account_id):
    account = customerAccountService.get_account(account_id)
    if account:
        return customer_account_schema.jsonify(account), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@admin_required
def update_account(account_id):
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_account = customerAccountService.update_account(account_id, account_data)
    if updated_account:
        return customer_account_schema.jsonify(updated_account), 200
    else:
        return jsonify({'message': 'Account not found'}), 404

@admin_required
def delete_account(account_id):
    customerAccountService.delete_account(account_id)
    return jsonify({'message': 'Account deleted successfully'}), 204

@admin_required
def find_all_accounts():
    accounts = customerAccountService.find_all_accounts()
    return customer_accounts_schema.jsonify(accounts), 200

@admin_required
def find_all_accounts_paginate():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    accounts = customerAccountService.find_all_accounts_paginate(page, per_page)
    return customer_accounts_schema.jsonify(accounts.items), 200