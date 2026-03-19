from flask import Blueprint, request, jsonify
from services.contact_service import (
    create_contact,
    get_all_contacts,
    delete_contact,
    update_contact,
    search_contacts
)

contact_bp = Blueprint("contacts", __name__)

@contact_bp.route("/contacts", methods=["POST"])
def create_contact_route():
        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "Invalid input"}), 400
        
        result, status = create_contact(data)
        return jsonify(result), status

@contact_bp.route("/contacts", methods=["GET"])
def get_contacts():
    name = request.args.get("name")
    phone = request.args.get("phone")

    result, status = get_all_contacts(name, phone)
    return jsonify(result), status

@contact_bp.route("/contacts/search", methods=["GET"])
def search():
    query = request.args.get("q")

    if not query:
        return jsonify({"status": "error", "message": "Query required"}), 400

    result, status = search_contacts(query)
    return jsonify(result), status

@contact_bp.route("/contacts/<contact_id>", methods=["DELETE"])
def delete(contact_id):
    result, status = delete_contact(contact_id)
    return jsonify(result), status

@contact_bp.route("/contacts/<contact_id>", methods=["PUT"])
def update(contact_id):
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Query required"}), 400

    result, status = update_contact(contact_id, data)
    return jsonify(result), status

