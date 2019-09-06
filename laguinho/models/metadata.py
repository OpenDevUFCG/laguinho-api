from marshmallow import Schema, fields, pprint, validate

class MetadataSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": {"message": "Name is required."}})
    url = fields.Str(required=True, error_messages={"required": {"message": "URL is required."}})
    path = fields.Str(required=True, error_messages={"required": {"message": "Path is required."}})
    maintainers = fields.List(fields.Str())
    format = fields.Str(validate=validate.OneOf(["json", "csv"]), required=True, error_messages={"required": {"message": "Format is required."}})
    contributable = fields.Bool()
