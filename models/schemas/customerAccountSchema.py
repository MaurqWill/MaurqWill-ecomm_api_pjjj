from marshmallow import Schema, fields
from . import ma

class CustomerAccountSchema(ma.Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    customer_id = fields.Int(required=True)

    class Meta: 
        fields = ("id", "username", "password", "customer_id")


customer_account_schema = CustomerAccountSchema()
customer_accounts_schema = CustomerAccountSchema(many=True, exclude=["password"])
