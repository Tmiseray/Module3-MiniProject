# Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.


import os


def create_contacts_backup(contacts):
    i = 0
    while os.path.exists(f"/Backups/ContactsBackup{i}.txt"):
        i +=1

    with open(f"/Backups/ContactsBackup{i}.txt", "w") as backup:
        for contact_id, info in contacts.items():
            backup.write(f"Contact ID: {contact_id}\n")
            for key, value in info.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        backup.write(f"{key} -> {sub_key}: {sub_value}\n")
                elif isinstance(value, list):
                    backup.write(f"{key}: {', '.join(value)}\n")
                else:
                    backup.write(f"{key}: {value}\n")
            backup.write("\n")
    print("Contacts' backup completed successfully!")
    print(f"Location: {backup}")


def find_latest_backup():
    i = 0
    while os.path.exists(f"/Backups/ContactsBackup{i}.txt"):
        i += 1
    return f"/Backups/ContactsBackup{i - 1}.txt" if i > 0 else None


def restore_contacts_backup(contacts):
    latest_backup = find_latest_backup()
    if latest_backup:
        contacts = {}
        contact_id = None
        info = {}
        with open(latest_backup, "r") as backup_file:
            for line in backup_file:
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
        print(f"Contacts restored from {latest_backup}")
        return contacts
    else:
        print("No backup files found.")
        return contacts

