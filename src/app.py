"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person


         #from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

#                                                                            create the jackson family object
jackson_family = FamilyStructure("Jackson")

            # Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

     # endpoint for google to generate a map 
@app.route('/')
def sitemap():
    return generate_sitemap(app)


    # GET ALL MEMBERS

@app.route('/members', methods=['GET'])


@app.route('/members', methods=['GET'])
def get_all_members():

    response = jackson_family.get_all_members()
    if  response is None or len(response) < 1: 
      raise APIException("Record is not found", status_code=500)

    return jsonify({"family": jackson_family.get_all_members()}), 200



    # GET ONE SINGLE MEMBER

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member()

    if member is None:
        raise APIException("Bad Request", status_code=500)
    return jsonify({"family": member(id)

#  ADD MEMBER
@app.route('/members/<int:id>', methods=['POST'])
def add_member():
    member = request.data
    text_data = json.loads(member)
    jackson_family.get_member(text_data)
    return jsonify({"family_members":member(id)}), 200

# DELETE MEMBER
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member()
    jackson_family.delete_member(id)
    return jsonify({"family_members":member(id)}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
