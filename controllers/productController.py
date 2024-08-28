from flask import jsonify, request
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services import productService
from utils.util import token_required, admin_required

@admin_required
def save():
    """
    Create a new product.
    Only accessible by admin users.
    """
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@token_required
def find_all():
    """
    Retrieve all products.
    Accessible by authenticated users.
    """
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

@token_required
def search_product():
    """
    Search for products by name.
    Accessible by authenticated users.
    """
    search_term = request.args.get("search")
    if not search_term:
        return jsonify({"message": "Search term is required"}), 400

    searched_items = productService.search_product(search_term)
    return products_schema.jsonify(searched_items), 200

@admin_required
def update_product(product_id):
    """
    Update a product by ID.
    Only accessible by admin users.
    """
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_product = productService.update_product(product_id, product_data)
    if updated_product:
        return product_schema.jsonify(updated_product), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

@admin_required
def delete_product(product_id):
    """
    Delete a product by ID.
    Only accessible by admin users.
    """
    productService.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'}), 204
