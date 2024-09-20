from flask import Blueprint
from controllers.customerController import save, find_all, find_all_paginate, login, get_customer, update_customer, delete_customer

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
customer_blueprint.route('/login', methods=['POST'])(login)
customer_blueprint.route('/<int:customer_id>', methods=['GET'])(get_customer)
customer_blueprint.route('/<int:customer_id>', methods=['PUT'])(update_customer)
customer_blueprint.route('/<int:customer_id>', methods=['DELETE'])(delete_customer)
