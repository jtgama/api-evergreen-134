from flask import Flask, jsonify, request
from flask_cors import CORS
from api.controllers.TipoCultivos import TipoCultivo

app = Flask(__name__)
CORS(app)

@app.route('/tipoCultivos', methods = ['GET'])
def getAll():
    return (TipoCultivo.list())

@app.route('/tipoCultivos', methods = ['POST'])
def postOne():
    body = request.json
    return (TipoCultivo.create(body))

app.run(port=3000,debug=True)