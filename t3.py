# Define a dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    
    if name in contacts:
        print("A contact with this name already exists. Use the update function to modify it.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search in details['phone']:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            found = True
            break
    if not found:
        print("No contact found with the given details.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Current details:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        print("\nEnter new details (leave blank to keep current value):")
        phone = input("New phone number: ") or contacts[name]['phone']
        email = input("New email: ") or contacts[name]['email']
        address = input("New address: ") or contacts[name]['address']
        
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main_menu():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the Contact Book
main_menu()
