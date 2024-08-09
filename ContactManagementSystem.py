# Display Welcome message
# Welcome to the Contact Management System! 

import re
from MenuFunctions import *
from Menu import *
import Menu

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