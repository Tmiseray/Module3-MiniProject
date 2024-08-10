# Display Welcome message
# Welcome to the Contact Management System! 

"""
No issues here.
There is a test version for 'contacts.txt' that I have been using to ensure things are functioning.
The 'create_contacts_backup' works great. I've been able to use it to help troubleshoot some of the initial issues.
"""

from ImportExportFunctions import import_contacts_from_text
from BackupFunctions import create_contacts_backup
from Menu import menu


def contact_management_system():
    print("\n* Welcome to the Contact Management System! *")
    contacts = {}
    try:
        contacts = import_contacts_from_text()
        menu(contacts)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if contacts:
            create_contacts_backup(contacts)
        print("\nExiting program...")

if __name__ == "__main__":
    contact_management_system()