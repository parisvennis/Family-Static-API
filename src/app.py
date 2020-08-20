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
def get_all_members():
             # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    if members is None or len(members) < 1:
        raise APIException("Record is Not Found", status_code=400)

    return jsonify({"family_members" : members}), 200


    # GET ONE SINGLE MEMBER

@app.route('/members/<int:id>', methods=['GET'])
def get_one_member(id):
    member = jackson_family.get_member()
    if id > len(member) -1:
        raise APIException("Record is Not Found", status_code=500)
    if member is None or len(member) <1 or id > len(member)-1:
        return jsonify(member)
    return jsonify({"message":"Member Not Found"})

#  ADD MEMBER
@app.route('/members/', methods=['POST'])
def add_member():
    member = request.data
    text_data = json.loads(member)
    jackson_family.add_member(text_data)
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
