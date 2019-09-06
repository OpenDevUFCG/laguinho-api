from flask import Blueprint, jsonify
from marshmallow import ValidationError

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify(e.messages), 422