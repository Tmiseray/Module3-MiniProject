# Menu with the following options:
# Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Import contacts from a text file *BONUS*
# 8. Quit

# Utilize input() to enable users to select menu options and provide contact details
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues during execution

import re
import os
from MenuFunctions import *
from SearchFunction import *
from DisplayContactsFunction import *
from ImportExportFunctions import *
from BackupFunctions import *



def menu():
    contacts = import_contacts_from_text('Contacts.txt')
    title = ".~* Menu: *~."
    while True:
        print(f"\n{title.center(45)}") # 45
        print("1. Add a New Contact")
        print("2. Edit an Existing Contact")
        print("3. Delete a Contact")
        print("4. Search for a Contact")
        print("5. Display All Contacts")
        print("6. Export Contacts to a Text File")
        print("7. Import Contacts from a Text File")
        print("8. Restore Contacts from Backup File")
        print("9. Quit")
        user_input = input("Enter your choice: ")
        try:
            choice = int(user_input)
        except ValueError:
            print("\nNot a valid choice. Please enter the digit that corresponds with your selection.")
            menu()
        except TypeError:
            print("\nAn unexpected type error occurred. Please try again.")
            menu()
        else:
            if choice == 1:
                add_new_contact(contacts)
                menu()
                pass
            elif choice == 2:
                edit_contact(contacts)
                menu()
                pass
            elif choice == 3:
                delete_contact(contacts)
                menu()
                pass
            elif choice == 4:
                search_contacts(contacts)
                menu()
                pass
            elif choice == 5:
                display_contacts(contacts)
                menu()
                pass
            elif choice == 6:
                export_contacts_to_text(contacts)
                menu()
                pass
            elif choice == 7:
                import_contacts_from_text(contacts)
                menu()
                pass
            elif choice == 8:
                restore_contacts_backup(contacts)
                menu()
                pass
            elif choice == 9:
                print("Thank you for using Contact Management System!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                menu()
