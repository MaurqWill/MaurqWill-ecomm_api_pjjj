from flask import Blueprint
from services.productService import save, find_all, get_product, update_product, delete_product, search_product

product_blueprint = Blueprint('product_bp', __name__)

product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/<int:product_id>', methods=['GET'])(get_product)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update_product)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete_product)
product_blueprint.route('/search', methods=['GET'])(search_product)
