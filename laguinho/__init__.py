from flask import Flask

def create_app(config_filename=None):
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Laguinho API is up and running.'

    return app
