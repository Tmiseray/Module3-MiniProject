# Menu Function
# Includes:
    # CLI Menu with a user-friendly format
    # Error handling for user input
    # Based on user input, calls to functions in other modules
    # Once user selects 'Quit', provides a friendly closing and automatically creates a backup file for the contacts


from AddContact import *
from Search import search_contacts
from DisplayContacts import display_contacts
from ImportExport import import_contacts_from_text, export_contacts_to_text
from Backup import *
from EditContact import edit_contact, delete_contact


def menu(contacts):
    title = ".~* Menu: *~."
    while True:
        print(f"\n{title.center(25)}") # centered 25 chars
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
            continue
        except TypeError:
            print("\nAn unexpected type error occurred. Please try again.")
            continue
        else:
            if choice == 1:
                add_new_contact(contacts)
            elif choice == 2:
                edit_contact(contacts)
            elif choice == 3:
                delete_contact(contacts)
            elif choice == 4:
                search_contacts(contacts)
            elif choice == 5:
                display_contacts(contacts)
            elif choice == 6:
                contacts = export_contacts_to_text(contacts)
            elif choice == 7:
                contacts = import_contacts_from_text(contacts)
            elif choice == 8:
                contacts = restore_contacts_backup()
            elif choice == 9:
                print("\nThank you for using Contact Management System!")
                if contacts:
                    create_contacts_backup(contacts)
                    break
                return
            else:
                print("\nInvalid choice. Please try again.")
    return

