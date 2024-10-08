# Import/Export Functions
# Including:
    # Exporting to a text file in a structured, user-friendly format
        # Ensures to 'write' the file vs 'append' ensuring there are no duplicated contacts
    # Importing contacts from a text file and adding them to the system
        # Using REGEX for patterns to match for proper import into contacts
        # Using an additonal merge function to ensure there are not duplicated contacts
        # Exceptions for error handling that may occur
        # Returns full contacts after the import
    # Merge function that handles any existing contacts and new information to be added to the contact
        # Adds any new information and merges any existing fields with new data
        # Returns the existing contact information


import re


def export_contacts_to_text(contacts):
    try:
        with open('Contacts.txt', 'w') as file:
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
        print("\nContacts successfully exported to 'Contacts.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return contacts


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
                        # Update or add new contact
                        if contact_id in contacts:
                            contacts[contact_id] = merge_contacts(contacts[contact_id], info)
                        else:
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
                    # Avoid duplicating values
                    if sub_key in info[outer_key] and info[outer_key][sub_key] == sub_value.strip():
                        continue
                    info[outer_key][sub_key] = sub_value.strip()
                    continue

                # Match "Key: Value"
                match = key_value_pattern.match(line)
                if match:
                    key, value = match.groups()
                    if "," in value:
                        # Handling lists and avoiding duplicates
                        values = [val.strip() for val in value.split(',')]
                        if key in info:
                            info[key].extend([v for v in values if v not in info[key]])
                        else:
                            info[key] = values
                    else:
                        # Update or add single value fields
                        info[key.strip()] = value.strip()
                    continue

            if contact_id is not None:
                # Handling final contact
                if contact_id in contacts:
                    contacts[contact_id] = merge_contacts(contacts[contact_id], info)
                else:
                    contacts[contact_id] = info

        print("Contacts successfully imported from 'Contacts.txt'.")
    except FileNotFoundError:
        print("The file 'Contacts.txt' was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    return contacts


def merge_contacts(existing_contact, new_info):
    # Merges new contact info into the existing contact
    for key, value in new_info.items():
        if isinstance(value, dict):
            if key not in existing_contact:
                existing_contact[key] = value
            else:
                for sub_key, sub_value in value.items():
                    existing_contact[key][sub_key] = sub_value
        elif isinstance(value, list):
            if key not in existing_contact:
                existing_contact[key] = value
            else:
                existing_contact[key].extend([v for v in value if v not in existing_contact[key]])
        else:
            if key in existing_contact and existing_contact[key] is None:
                existing_contact[key] = value
            else:
                return

    return existing_contact        
