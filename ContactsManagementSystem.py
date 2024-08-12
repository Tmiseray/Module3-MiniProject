# Welcome to the Contact Management System! 


from ImportExport import import_contacts_from_text
from Menu import menu


def contact_management_system():
    print("\n* Welcome to the Contact Management System! *")
    contacts = {}
    try:
        contacts = import_contacts_from_text(contacts)
        menu(contacts)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nExiting program...")

if __name__ == "__main__":
    contact_management_system()