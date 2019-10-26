from marshmallow import Schema, fields, validate
from .error_messages import get_required_error


class DatasetMetadataSchema(Schema):
    name = fields.Str(required=True, error_messages=get_required_error("name"))
    url = fields.Str(required=True, error_messages=get_required_error("url"))
    path = fields.Str(required=True, error_messages=get_required_error("path"))
    maintainers = fields.List(fields.Str())
    format = fields.Str(validate=validate.OneOf(["json", "csv"]),
                        required=True,
                        error_messages=get_required_error("format"))
    contributable = fields.Bool()


dataset_metadata = DatasetMetadataSchema()
