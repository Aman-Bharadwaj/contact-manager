from utils.file_handler import load_contacts, save_contacts
import uuid

def get_all_contacts(name=None, phone=None):
    contacts = load_contacts()

    if name:
        contacts = [c for c in contacts if name.lower() in c["name"].lower()]

    if phone:
        contacts = [c for c in contacts if phone in c["phone"]]

    return {"status": "success", "data": contacts}, 200

def search_contacts(query):
    contacts = load_contacts()

    results = []
    for contact in contacts:
        if (
            query.lower() in contact["name"].lower()
            or query.lower() in contact["phone"]
            or (contact["email"] and query.lower() in contact["email"].lower())
        ):
            results.append(contact)

    return {"status": "success", "data": results}, 200

def delete_contact(contact_id):
    contacts = load_contacts()

    new_contacts = [c for c in contacts if c["id"] != contact_id]

    if len(new_contacts) == len(contacts):
        return {"error": "Contact not found"}, 404

    save_contacts(new_contacts)
    return {"message": "Deleted successfully"}, 200

def create_contact(data):
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    
    if not name or not phone:
        return{"error": "Name and phone are required"}, 400
    
    contacts = load_contacts()
    
    if not phone.isdigit() or len(phone) != 10:
        return {"error": "Invalid phone number"}, 400
    
    for contact in contacts:
        if contact["phone"] == phone:
            return {"error": "Contact already exists"}, 400
    new_contact = {
        "id": str(uuid.uuid4()),
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    
    return new_contact, 201

def update_contact(contact_id, data):
    contacts = load_contacts()

    for contact in contacts:
        if contact["id"] == contact_id:
            # update only provided fields
            if "name" in data:
                contact["name"] = data["name"]               
            if "phone" in data:
                if not data["phone"].isdigit() or len(data["phone"]) != 10:
                    return {"error": "Invalid phone"}, 400
                contact["phone"] = data["phone"]
            if "email" in data:
                contact["email"] = data["email"]

            save_contacts(contacts)
            return contact, 200

    return {"error": "Contact not found"}, 404