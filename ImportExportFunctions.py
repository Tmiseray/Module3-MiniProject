# Import/Export Functions



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
                            file.write(f"{key} -> {sub_key}: {sub_value}\n")
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
                elif " -> " in line:
                    outer_key, rest = line.split(" -> ")
                    sub_key, sub_value = rest.split(": ", 1)
                    if outer_key not in info:
                        info[outer_key] = {}
                    info[outer_key][sub_key] = sub_value
                elif ": " in line:
                    key, value = line.split(": ", 1)
                    if "," in value:
                        # Handling lists
                        info[key] = [val.strip() for val in value.split(',')]
                    else:
                        info[key] = value
            if contact_id is not None:
                contacts[contact_id] = info
        print("Contacts successfully imported from 'Contacts.txt'.")
    except FileNotFoundError:
        print("The file 'Contacts.txt' was not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    return contacts
