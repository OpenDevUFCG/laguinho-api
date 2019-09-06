from flask import Blueprint, request, jsonify
from laguinho.models.metadata import MetadataSchema
from marshmallow import ValidationError, EXCLUDE

datasets = Blueprint('datasets',__name__,url_prefix="/datasets")
metadata = []

@datasets.route("/publish", methods=['POST'])
def publish():
    schema = MetadataSchema()
    result = schema.load(request.json, unknown=EXCLUDE)
    metadata.append(result)
    return result

@datasets.route("/metadata", methods=['GET'])
def get_metadata():
    return jsonify(metadata)