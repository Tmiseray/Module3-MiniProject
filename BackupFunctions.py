# Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.

import re
import os


def create_contacts_backup(contacts):
    i = 0
    while os.path.exists("/Backups/ContactsBackup%s.txt" % i):
        i +=1
        with open("/Backups/ContactsBackup%s.txt" % i, "w") as backup:
            for contact_id, info in contacts.items():
                backup.write(f"Contact ID: {contact_id}\n")
                backup.write(f"Name: {info['Name']}\n")
                backup.write(f"Phone Number : {info['Phone Number']}\n")
                backup.write(f"Email Address: {info['Email Address']}\n")
                backup.write(f"Birthday: {info['Birthday']}\n")
                backup.write(f"Category: {info['Category']}\n")
                backup.write("\n")


def find_latest_backup():
    i = 0
    while os.path.exists(f"ContactsBackup{i}.txt"):
        i += 1
    return f"ContactsBackup{i - 1}.txt" if i > 0 else None


def restore_contacts_backup(contacts):
    latest_backup = find_latest_backup()
    if latest_backup:
        contacts = {}
        with open(latest_backup, "r") as backup_file:
            for line in backup_file:
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
        print(f"Contacts restored from {latest_backup}")
    else:
        print("No backup files found.")

