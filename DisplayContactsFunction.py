# Display Functions
# Including:
    # Sort Key from User and if not Default
    # Sorting Contacts by User's Sort Key
    # Displaying Contacts with/without Sort


import re
import os


# 5. Display All Contacts
# Display each contact and all details
# *BONUS* Implement sorting options to display contacts alphabetically or other criteria

def get_user_sort_key():
    print("\n* Sorting options: *")
    print("1. Name")
    print("2. Phone Number")
    print("3. Email Address")
    print("4. Birthday")
    print("5. Category")
    choice = input("Enter the number associated with the sorting option: ").strip()

    sort_keys = {
        '1': 'Name',
        '2': 'Phone Number',
        '3': 'Email Address',
        '4': 'Birthday',
        '5': 'Category'
    }

    return sort_keys.get(choice, 'Name')

def sort_contacts_by_key(contacts, sort_key):
    contact_items = list(contacts.items())
    sorted_contacts = sorted(contact_items, key=lambda item: item[1].get(sort_key, ''))
    return sorted_contacts

def display_contacts(contacts):
    sort = input("Would you like to sort the contacts? (yes/no): ").lower()
    if sort == 'yes':
        sort_key = get_user_sort_key()
        sorted_contacts = sort_contacts_by_key(contacts, sort_key)
        print("\n.~* Full Contacts List: *~.")
        print(f"* Sorted By: {sort_key} *")
        for contact_id, info in sorted_contacts.items():
            print(f"\nContact ID: {contact_id}")
            print(f"Name: {info['Name']}")
            print(f"Phone Number: {info['Phone Number']}")
            print(f"Email Address: {info['Email Address']}")
            print(f"Birthday: {info['Birthday']}")
            print(f"Category: {info['Category']}")
    else:
        print("\n.~* Full Contacts List: *~.")
        for contact_id, info in contacts.items():
            print(f"\nContact ID: {contact_id}")
            print(f"Name: {info['Name']}")
            print(f"Phone Number: {info['Phone Number']}")
            print(f"Email Address: {info['Email Address']}")
            print(f"Birthday: {info['Birthday']}")
            print(f"Category: {info['Category']}")
