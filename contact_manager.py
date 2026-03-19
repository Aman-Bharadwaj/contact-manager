import os
import json
import csv

    
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
    
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts(contacts)
    return "Contact added"


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

    return {"status": "success", "data": results}


def delete_contact(contacts, index):
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        save_contacts(contacts)
        return removed
    return None

def view_contact(contacts):
    if not contacts:
        return[]
    
    return contacts

def edit_contact(contacts, index, new_name, new_phone, new_email):
    if 0 <= index < len(contacts):
        contact = contacts[index]
        
        if new_name:
            contact["name"] = new_name
        if new_phone:
            contact["phone"] = new_phone
        if new_email:
            contact["email"] = new_email
        
        save_contacts(contacts)
        return contact
    
    return None


def export_to_csv(contacts, mode, index=None):
    if not contacts:
        return "No contacts"
    
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        
        if mode == "one" and index is not None:
            contact = contacts[index]
            writer.writerow([
                contact["name"],
                contact["phone"],
                contact["email"]
            ])
        
        elif mode == "all":
            for contact in contacts:
                writer.writerow([
                    contact["name"],
                    contact["phone"],
                    contact["email"]
                ])
    
    return "Exported successfully"
        
    
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("=" * 30)
        print("      CONTACT MANAGER")
        print("=" * 30)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")
        print("7. Export to CSV")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            
            contacts = contacts[index]
            
            msg = add_contact(contacts, name, phone, email)
            print(msg)
            
        elif choice == "2":
            contacts_list = view_contact(contacts)

            if not contacts_list:
                print("No contact yet")
            else:
                for i, contact in enumerate(contacts_list, start=1):
                    print(f"{i}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
            

        elif choice == "3":
            query = input("Enter name: ")
            results = search_contact(contacts, query)
        
            if results:
                for i, c in enumerate(results, 1):
                    print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
            else:
                print("No match")

        elif choice == "4":
            view_contact(contacts)
            index = int(input("Enter index: ")) - 1
            
            removed = delete_contact(contacts, index)
            if removed:
                print("Deleted:", removed["name"])
            else:
                print("Invalid index")

            try:
                index = int(input("Enter index: ")) - 1
            except ValueError:
                print("Invalid input")
            continue
        elif choice == "5":
            view_contact(contacts)
            index = int(input("Enter index: ")) - 1
            
            new_name = input("New name: ")
            new_phone = input("New phone: ")
            new_email = input("New email: ")
            
            updated = edit_contact(contacts, index, new_name, new_phone, new_email)
            
            if updated:
                print("Updated")
            else:
                print("Invalid index")
                
        elif choice == "6":
            print("Exiting...")
            break

        elif choice == "7":
            mode = input("1. One\n2. All\nChoice: ")
            
            if mode == "1":
                view_contact(contacts)
                index = int(input("Enter index: ")) - 1
                msg = export_to_csv(contacts, "one", index)
            else:
                msg = export_to_csv(contacts, "all")
            
            print(msg)
        
        input("\nPress Enter to continue...")
        
if __name__ == "__main__":
    main()
            