from flask import Flask, request, jsonify
from contact_manager import load_contacts, add_contact, delete_contact, edit_contact, view_contact   # replace with your actual file name

app = Flask(__name__)


@app.route("/")
def home():
    return "Contact Manager API Running"


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = load_contacts()
    data = view_contact(contacts)
    return jsonify(data)

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    
    contacts = load_contacts()
    
    msg = add_contact(
        contacts,
        data.get("name"),
        data.get("phone"),
        data.get("email")
    )
    
    return jsonify({"message": msg})

@app.route("/delete/<int:index>", methods=["DELETE"])
def delete(index):
    contacts = load_contacts()

    removed = delete_contact(contacts, index)
    
    if removed:
        return jsonify({"message": "Deleted successfully"})
    else:
        return jsonify({"error": "Invalid index"})

@app.route("/update/<int:index>", methods=["PUT"])
def update(index):
    data = request.json
    contacts = load_contacts()
    
    new_name = data.get("name")
    new_phone = data.get("phone")
    new_email = data.get("email")
    
    updated = edit_contact(contacts, index, new_name, new_phone, new_email)
    
    if updated:
        return jsonify({"message": "Updated successfully"})
    else:
        return jsonify({"error": "Invalid index"})

if __name__ == "__main__":
    app.run(debug=True)