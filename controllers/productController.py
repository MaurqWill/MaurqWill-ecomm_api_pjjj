from flask import jsonify, request
from marshmallow import ValidationError
from models.schemas.productSchema import product_schema, products_schema
from services.productService import (
    save_product,
    get_product,
    find_all_products,
    search_product,
    update_product,
    delete_product
)
from utils.util import token_required, admin_required

@admin_required
def create_product():

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        product = save_product(product_data)
        return product_schema.jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@token_required
def get_products():

    products = find_all_products()
    return products_schema.jsonify(products), 200

@token_required
def search_products():

    search_term = request.args.get("search")
    if not search_term:
        return jsonify({"message": "Search term is required"}), 400

    products = search_product(search_term)
    return products_schema.jsonify(products), 200

@token_required
def get_product_by_id(product_id):

    product = get_product(product_id)
    if product:
        return product_schema.jsonify(product), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

@admin_required
def update_product_by_id(product_id):

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    try:
        updated_product = update_product(product_id, product_data)
        return product_schema.jsonify(updated_product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@admin_required
def delete_product_by_id(product_id):

    try:
        delete_product(product_id)
        return jsonify({'message': 'Product deleted successfully'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

