from flask import Blueprint, request, jsonify
from laguinho.models.metadata import dataset_metadata
from marshmallow import ValidationError, EXCLUDE

datasets = Blueprint('datasets', __name__)
datasets_metadata = []

def equals(dataset1, dataset2):
    return (dataset1['name'] == dataset2['name'] or
            dataset1['url'] == dataset2['url'] and
            dataset1['path'] == dataset2['path'])

def dataset_exists(incoming_dataset):
    compare_datasets = lambda dataset: equals(dataset, incoming_dataset)
    filtered = list(filter(compare_datasets, datasets_metadata))
    return len(filtered) > 0

@datasets.route("/datasets", methods=['POST'], strict_slashes=False)
def publish():
    result = dataset_metadata.load(request.json, unknown=EXCLUDE)
    if dataset_exists(result):
        return jsonify('Dataset already exists'), 409
    datasets_metadata.append(result)
    return jsonify(result), 201

@datasets.route("/datasets", methods=['GET'], strict_slashes=False)
def get_datasets():
    return jsonify(datasets_metadata)

@datasets.route("/datasets/<name>", methods=['GET'], strict_slashes=False)
def get_datasets_by_name(name):
  search_result = list(
    filter(lambda dataset: dataset['name'] == name, datasets_metadata))

  if len(search_result) > 0:
    # A busca encontrou resultado.
    return jsonify(search_result[0]), 200
  
  return jsonify({"error": 'Dataset not found!'}), 404
