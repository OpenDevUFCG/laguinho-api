from marshmallow import Schema, fields, pprint, validate

def get_required_error(attribute):
        return {"required": {"message": attribute + " is required"}}

class DatasetMetadataSchema(Schema):
    name = fields.Str(
        required=True, 
        error_messages=get_required_error("name"))
    url = fields.Str(
        required=True, 
        error_messages=get_required_error("url"))
    path = fields.Str(
        required=True, 
        error_messages=get_required_error("path"))
    maintainers = fields.List(fields.Str())
    format = fields.Str(
        validate=validate.OneOf(["json", "csv"]), 
        required=True, 
        error_messages=get_required_error("format"))
    contributable = fields.Bool()
