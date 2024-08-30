from flask import Blueprint
from controllers.productController import create_product, get_products, search_products, get_product_by_id, update_product_by_id, delete_product_by_id

product_blueprint = Blueprint('product', __name__, url_prefix='/products')

product_blueprint.route('/', methods=['POST'])(create_product)
product_blueprint.route('/', methods=['GET'])(get_products)
product_blueprint.route('/search', methods=['GET'])(search_products)
product_blueprint.route('/<int:product_id>', methods=['GET'])(get_product_by_id)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update_product_by_id)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete_product_by_id)

