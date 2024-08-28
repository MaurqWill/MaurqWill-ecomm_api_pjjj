from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from marshmallow import ValidationError
from services import orderService
from utils.util import token_required, admin_required, user_token_wrapper

@admin_required
def save():
    """
    Create a new order.
    Only accessible by admin users.
    """
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

@admin_required
def find_all():
    """
    Retrieve all orders.
    Only accessible by admin users.
    """
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

@token_required
def find_by_id(id):
    """
    Retrieve an order by ID.
    Accessible by authenticated users.
    """
    order = orderService.find_by_id(id)
    if order:
        return order_schema.jsonify(order), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

@user_token_wrapper
def find_by_customer_id(id, token_id):
    """
    Retrieve orders by customer ID.
    Accessible by the authenticated customer.
    """
    if id == token_id:
        orders = orderService.find_by_customer_id(id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "You can't view other people's orders."}), 403

@admin_required
def find_by_customer_email():
    """
    Retrieve orders by customer email.
    Only accessible by admin users.
    """
    try:
        email = request.json['email']
    except KeyError:
        return jsonify({'message': 'Email is required'}), 400

    orders = orderService.find_by_customer_email(email)
    return orders_schema.jsonify(orders), 200

@admin_required
def update_order(order_id):
    """
    Update an order by ID.
    Only accessible by admin users.
    """
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
    """
    Delete an order by ID.
    Only accessible by admin users.
    """
    orderService.delete_order(order_id)
    return jsonify({'message': 'Order deleted successfully'}), 204
