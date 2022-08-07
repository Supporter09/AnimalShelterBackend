import enum
import time
from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from bson import json_util
import json
from bson.objectid import ObjectId
import os

app = Flask(__name__)
# For PyMongo
app.config['MONGO_URI'] = os.environ.get('DB_URI')

CORS(app, support_credentials=True)
uri = os.environ.get("DB_URI")
mongoClient = MongoClient(uri)
db = mongoClient.AnimalShelterDB

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return Response("AnimalShelter, 2022", mimetype="text/plain", status=200)

@app.route("/get-all-animal", methods=['GET'])
@cross_origin()
def getAllAnimal():
    data = db.AnimalSpecies
    resultCursor = data.find()
    json_docs = []
    for doc in resultCursor:
        json_docs.append(doc)
    return json.loads(json_util.dumps(json_docs))

@app.route("/animal-detail", methods=['GET'])
@cross_origin()
def animalDetail():
    data = db.AnimalSpecies
    key = request.args.get("key")
    
    resultCursor = data.find({"_id":ObjectId(key)})

    json_docs = []
    for doc in resultCursor:
        json_docs.append(doc)
    return json.loads(json_util.dumps(json_docs))

# Run server
if __name__ == "__main__":
    app.run(debug=True, port=8088)
