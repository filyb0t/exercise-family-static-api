import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False

CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ENDPOINTS

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.json
    if not new_member.get('first_name') or not new_member.get('age') or not new_member.get('lucky_numbers'):
        return jsonify({"msg": "Datos incompletos para agregar un miembro"}), 400

    
    jackson_family.add_member(new_member)

    return jsonify(new_member), 200


@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    miembro_encontrado = jackson_family.get_member(member_id)
    if not miembro_encontrado:
        return jsonify({"msg": "Miembro no encontrado"}), 404
    return jsonify(miembro_encontrado), 200


@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if not deleted:
        return jsonify({"msg": "Miembro no encontrado"}), 404
    return jsonify({"done": True}), 200


@app.route('/members/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    updated_member_data = request.json
    updated = jackson_family.update_member(member_id, updated_member_data)
    if not updated:
        return jsonify({"msg": "Miembro no encontrado"}), 404
    return jsonify({"done": True}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
