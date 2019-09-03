from flask import Flask, jsonify

def create_app(config_filename):
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
    return jsonify({'status': 'running'})
  
  return app
