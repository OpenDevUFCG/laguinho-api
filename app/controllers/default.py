from app import app
from flask import jsonify

@app.route("/")
def hello():
  return jsonify({
    "message": "Servidor funcionando"
  })
