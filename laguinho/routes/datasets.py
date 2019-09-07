from flask import Blueprint, request, jsonify
from laguinho.models.metadata import dataset_metadata
from marshmallow import ValidationError, EXCLUDE

datasets = Blueprint('datasets', __name__)
datasets_metadata = []

@datasets.route("/datasets", methods=['POST'])
def publish():
    result = dataset_metadata.load(request.json, unknown=EXCLUDE)
    datasets_metadata.append(result)
    return result, 201

@datasets.route("/datasets", methods=['GET'])
def get_datasets():
    return dataset_metadata.dumps(datasets_metadata, many=True)
