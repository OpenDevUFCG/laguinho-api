from flask import Blueprint, request, jsonify
from laguinho.models.metadata import MetadataSchema
from marshmallow import ValidationError, EXCLUDE

datasets = Blueprint('datasets', __name__)
datasets_metadata = []

@datasets.route("/datasets", methods=['POST'])
def publish():
    schema = MetadataSchema()
    result = schema.load(request.json, unknown=EXCLUDE)
    datasets_metadata.append(result)
    return result, 201

@datasets.route("/datasets", methods=['GET'])
def get_datasets():
    return jsonify(datasets_metadata)
