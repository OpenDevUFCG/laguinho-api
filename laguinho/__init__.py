from flask import Flask
from .errors.handlers import errors
from .routes.datasets import datasets

def create_app(config_filename=None):
    app = Flask(__name__)

    app.register_blueprint(errors)
    app.register_blueprint(datasets)

    @app.route('/')
    def hello_world():
        return 'Laguinho API is up and running.'

    return app
