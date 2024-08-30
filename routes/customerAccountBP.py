from flask import Blueprint
from controllers.customerAccountController import create_account, get_account, update_account, delete_account, find_all_accounts, find_all_accounts_paginate

customer_account_blueprint = Blueprint('customer_account_bp', __name__)

customer_account_blueprint.route('/', methods=['POST'])(create_account)
customer_account_blueprint.route('/<int:account_id>', methods=['GET'])(get_account)
customer_account_blueprint.route('/<int:account_id>', methods=['PUT'])(update_account)
customer_account_blueprint.route('/<int:account_id>', methods=['DELETE'])(delete_account)
customer_account_blueprint.route('/', methods=['GET'])(find_all_accounts)
customer_account_blueprint.route('/paginate', methods=['GET'])(find_all_accounts_paginate)
