from flask import Blueprint, request, jsonify
from laguinho.models.metadata import dataset_metadata
from marshmallow import ValidationError, EXCLUDE
from laguinho.extensions import mongo

datasets = Blueprint('datasets', __name__)
datasets_metadata = mongo.db.datasets


def dataset_exists(dataset):
    return datasets_metadata.find_one({
        '$or': [{
            'name': dataset['name']
        }, {
            'url': dataset['url'],
            'path': dataset['path']
        }]
    })


@datasets.route("/datasets", methods=['POST'], strict_slashes=False)
def publish():
    result = dataset_metadata.load(request.json, unknown=EXCLUDE)
    if dataset_exists(result):
        return jsonify('Dataset already exists'), 409
    datasets_metadata.insert_one(result)
    del result['_id']
    return jsonify(result), 201


@datasets.route("/datasets", methods=['GET'], strict_slashes=False)
def get_datasets():
    return jsonify(datasets_metadata.find())


@datasets.route("/datasets/<name>", methods=['GET'], strict_slashes=False)
def get_datasets_by_name(name):
    search_result = datasets_metadata.find_one_or_404({'name': name})
    return jsonify(search_result), 200
