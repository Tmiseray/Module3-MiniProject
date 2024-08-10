# Import/Export Functions
"""
import function works great. I had a couple issues with it at first. It kept giving an error without an actual error that took place. Should be fixed.

export has not been attempted due to issues with add/edit contact
"""

import re

# 6. Export Contacts to a Text File
# Export to text file in a structured format
def export_contacts_to_text(contacts):
    try:
        with open('Contacts.txt', 'a') as file:
            for contact_id, info in contacts.items():
                file.write(f"Contact ID: {contact_id}\n")
                for key, value in info.items():
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            file.write(f"{key}: -> {sub_key}: {sub_value}\n")
                    elif isinstance(value, list):
                        file.write(f"{key}: {', '.join(value)}\n")
                    else:
                        file.write(f"{key}: {value}\n")
                file.write("\n")
        print("Contacts successfully exported to 'Contacts.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")



# 7. Import Contacts from a Text File *BONUS*
# Import contacts from a text file and add them to the system

def import_contacts_from_text(contacts = None):
    if contacts is None:
        contacts = {}

    contact_id_pattern = re.compile(r"^Contact ID:\s*(\S+)$")
    nested_key_pattern = re.compile(r"^(\w[\w\s]+):\s*->\s*(\w[\w\s]+):\s*(.*)$")
    key_value_pattern = re.compile(r"^(\w[\w\s]+):\s(.+)$")

    try:
        with open('Contacts.txt', 'r') as file:
            contact_id = None
            info = {}
            for line in file:
                line = line.strip()

                # Match "Contact ID: <ID>"
                match = contact_id_pattern.match(line)
                if match:
                    if contact_id is not None:
                        contacts[contact_id] = info
                        info = {}
                    contact_id = match.group(1)
                    continue

                # Match "Outer Key: -> Sub Key: Value"
                match = nested_key_pattern.match(line)
                if match:
                    outer_key, sub_key, sub_value = match.groups()
                    if outer_key not in info:
                        info[outer_key] = {}
                    info[outer_key][sub_key] = sub_value.strip()
                    continue

                # Match "Key: Value"
                match = key_value_pattern.match(line)
                if match:
                    key, value = match.groups()
                    if "," in value:
                        # Handling lists
                        info[key.strip()] = [val.strip() for val in value.split(',')]
                    else:
                        info[key.strip()] = value.strip()
                    continue

            if contact_id is not None:
                contacts[contact_id] = info

        print("Contacts successfully imported from 'Contacts.txt'.")
    except FileNotFoundError:
        print("The file 'Contacts.txt' was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    return contacts