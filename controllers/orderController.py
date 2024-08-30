from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from marshmallow import ValidationError
from services import orderService
from utils.util import token_required, admin_required, user_token_wrapper

@admin_required
def save():

    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

@admin_required
def find_all():

    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

@token_required
def find_by_id(id):

    order = orderService.find_by_id(id)
    if order:
        return order_schema.jsonify(order), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

@user_token_wrapper
def find_by_customer_id(id, token_id):

    if id == token_id:
        orders = orderService.find_by_customer_id(id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "You can't view other people's orders."}), 403

@admin_required
def find_by_customer_email():

    try:
        email = request.json['email']
    except KeyError:
        return jsonify({'message': 'Email is required'}), 400

    orders = orderService.find_by_customer_email(email)
    return orders_schema.jsonify(orders), 200

@admin_required
def update_order(order_id):
 
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_order = orderService.update_order(order_id, order_data)
    if updated_order:
        return order_schema.jsonify(updated_order), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

@admin_required
def delete_order(order_id):

    orderService.delete_order(order_id)
    return jsonify({'message': 'Order deleted successfully'}), 204
