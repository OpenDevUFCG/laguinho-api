from flask import Blueprint, request, jsonify
from laguinho.models.metadata import dataset_metadata
from marshmallow import ValidationError, EXCLUDE

datasets = Blueprint('datasets', __name__)
datasets_metadata = []

@datasets.route("/datasets", methods=['POST'])
def publish():
    result = dataset_metadata.load(request.json, unknown=EXCLUDE)
    datasets_metadata.append(result)
    return jsonify(result), 201

@datasets.route("/datasets/", methods=['GET'])
def get_datasets():
    return jsonify(datasets_metadata)

@datasets.route("/datasets/<name>", methods=['GET'])
def get_datasets_by_name(name):
  search_result = list(
    filter(lambda dataset: dataset['name'] == name, datasets_metadata))
  
  result = search_result[0] if len(search_result) > 0 else None
  return jsonify({"dataset": result}), 200
