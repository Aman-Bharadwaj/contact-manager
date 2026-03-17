import os
import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileExistsError:
    contacts = []
    
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
        
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    
    print("Contact added!")
    
def view_contact(contacts):
    if not contacts:
        print("No contacts yet")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

def search_contact(contacts):
    query = input("Enter name to search: ").lower()
    
    found = False
    
    for i, contact in enumerate(contacts, start=1):
        if query in contact["name"].lower():
            print(f"{i}.{contact['name']} | {contact['phone']} | {contact['email']}")
            found = True
            
    if not found:
        print("No matching contact found")
        
def edit_contact(contacts):
    if not contacts:
        print("No contacts to edit")
        return
    
    view_contact(contacts)
    
    index = get_valid_index(contacts, "Enter contact number to edit: ")
    
    contact = contacts[index]
    
    print("\nLeave blank to keep old value")
    
    new_name = input(f"Enter new name ({contact['name']}): ")
    new_phone = input(f"Enter new phone ({contact['phone']}): ")
    new_email = input(f"Enter new email ({contact['email']}): ")
    
    if new_name:
        contact["name"] = new_name
            
    if new_phone:
        contact["phone"] = new_phone
        
    if new_email:
        contact["email"]  = new_email
        
    print("Contact updated")
    save_contacts(contacts)
    
def get_valid_index(contacts, message):
    while True:
        try:
            index = int(input(message)) -1
            
            if 0 <= index < len(contacts):
                return index
            else:
                print("Invalid index")
                
        except ValueError:
            print("Please enter a valid number")
            
def delete_contact(contacts):
    if not contacts:
        print("No contact yet")
        return
    
    view_contact(contacts)
    
    index = get_valid_index(contacts, "Enter contact number to delete: ")
    
    removed = contacts.pop(index)
    save_contacts(contacts)
    
    print(f"Deleted: {removed['name']}")
    
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
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            print("Exiting....")
            break
        
        else:
            print("Invalid choice")
            
        input("\nPress Enter to continue...")
        
if __name__ == "__main__":
    main()
            