# Display Welcome message
# Welcome to the Contact Management System! 


from Menu import menu
from BackupFunctions import create_contacts_backup


def contact_management_system():
    print("\n* Welcome to the Contact Management System! *")
    contacts = {}
    try:
        contacts = menu()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if contacts:
            create_contacts_backup(contacts)
        print("Exiting program...")

if __name__ == "__main__":
    contact_management_system()