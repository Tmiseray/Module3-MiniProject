# Display Welcome message
# Welcome to the Contact Management System! 


from Menu import menu
import Menu
from BackupFunctions import create_contacts_backup


def contact_management_system():
    print("\n* Welcome to the Contact Management System! *")
    try:
        menu()
    finally:
        contacts = Menu.contacts
        create_contacts_backup(contacts)
        print("Exiting program...")

if __name__ == "__main__":
    contact_management_system()