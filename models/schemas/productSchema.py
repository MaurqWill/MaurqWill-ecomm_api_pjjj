from marshmallow import fields, validate
from . import ma


class ProductSchema(ma.Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

    class Meta: 
        fields = ("id", "name", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
