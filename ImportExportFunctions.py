# Import/Export Functions


import re
import os


# 6. Export Contacts to a Text File
# Export to text file in a structured format
def export_contacts_to_text(contacts):
    try:
        with open('Contacts.txt', 'a') as file:
            for contact_id, info in contacts.items():
                file.write(f"Contact ID: {contact_id}\n")
                file.write(f"Name: {info['Name']}\n")
                file.write(f"Phone Number : {info['Phone Number']}\n")
                file.write(f"Email Address: {info['Email Address']}\n")
                file.write(f"Birthday: {info['Birthday']}\n")
                file.write(f"Category: {info['Category']}\n")
                file.write("\n")
    except Exception as e:
        print(f"An error occurred: {e}")



# 7. Import Contacts from a Text File *BONUS*
# Import contacts from a text file and add them to the system
def import_contacts_from_text(contacts = None):
    if contacts is None:
        contacts = {}
        try:
            with open('Contacts.txt', 'r') as file:
                contact_id = None
                info = {}
                for line in file:
                    line = line.strip()
                    if line.startswith("Contact ID:"):
                        if contact_id is not None:
                            contacts[contact_id] = info
                            info = {}
                        contact_id = line.split(": ", 1)[1]
                    elif line.startswith("Name:"):
                        info['Name'] = line.split(": ", 1)[1]
                    elif line.startswith("Phone Number:"):
                        info['Phone Number'] = line.split(": ", 1)[1]
                    elif line.startswith("Email Address:"):
                        info['Email Address'] = line.split(": ", 1)[1]
                    elif line.startswith("Birthday:"):
                        info['Birthday'] = line.split(": ", 1)[1]
                    elif line.startswith("Category:"):
                        info['Category'] = line.split(": ", 1)[1]
                if contact_id is not None:
                    contacts[contact_id] = info
        except FileNotFoundError:
            print("The file 'Contacts.txt' was not found")
        except Exception as e:
            print(f"An error occurred: {e}")
