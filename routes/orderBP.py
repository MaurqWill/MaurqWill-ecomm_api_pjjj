from flask import Blueprint
from controllers.orderController import save, find_all, find_by_id, find_by_customer_id, find_by_customer_email, update_order, delete_order

order_blueprint = Blueprint('order_bp', __name__)

order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/', methods=['GET'])(find_all)
order_blueprint.route('/<int:order_id>', methods=['GET'])(find_by_id)
order_blueprint.route('/customer/<int:customer_id>', methods=['GET'])(find_by_customer_id)
order_blueprint.route('/customer/email', methods=['POST'])(find_by_customer_email)
order_blueprint.route('/<int:order_id>', methods=['PUT'])(update_order)
order_blueprint.route('/<int:order_id>', methods=['DELETE'])(delete_order)
