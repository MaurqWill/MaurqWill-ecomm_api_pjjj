from marshmallow import Schema, fields

class CustomerAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    customer_id = fields.Int(required=True)

    class Meta: 
        fields = ("id", "username", "password", "customer_id")


customer_account_schema = CustomerAccountSchema()
customers_account_schema = CustomerAccountSchema(many=True, exclude=["password"])
