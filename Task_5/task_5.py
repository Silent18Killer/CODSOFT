                            # Contact Book

'''
    Contact Information: Store name, phone number, email, and address for each contact.
    Add Contact: Allow users to add new contacts with their details.
    View Contact List: Display a list of all saved contacts with names and phone numbers.
    Search Contact: Implement a search function to find contacts by name or phone number.
    Update Contact: Enable users to update contact details.
    Delete Contact: Provide an option to delete a contact.
    User Interface: Design a user-friendly interface for easy interaction.
'''

def add_contact(contacts):
    """Add a new contact to the book."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")


def view_contact_list(contacts):
    """Display all saved contacts."""
    if not contacts:
        print("No contacts found.")
        return
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter contact name or phone number to search: ")

    for name, details in contacts.items():
        if name == search_term:
            print(f"Contact Name: '{name}', Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return

    for name, details in contacts.items():
        if details['phone'] == search_term:
            print(f"Contact Name: '{name}', Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return

    print(f"No contact found for '{search_term}'.")


def update_contact(contacts):
    """Update contact details."""
    name = input("Enter contact name to update: ")
    phone = input("Enter new phone number (leave blank to skip): ")
    email = input("Enter new email address (leave blank to skip): ")
    address = input("Enter new address (leave blank to skip): ")
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")


def main():
    contacts = {}

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
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()