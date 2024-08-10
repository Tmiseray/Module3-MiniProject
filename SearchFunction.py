# Search Functions
# Including:
    # Search Key from User and if not Default
    # Search Contacts by User's Search Key
    # Displaying Contacts Matching User's Search Criteria

"""
Have not tested this one due to being stuck on the 'add/edit' issues. But I have used similar logic in other places and may not be a problem.
"""

from AddContactFunction import *
from ValidateFormatFunctions import *


# 4. Search for a Contact
# Search for contact and display details
# *BONUS* allow options for search by name, phone number, email, or additional information

def get_user_search_key(contacts):
    # Generate search options dynamically based on the first contact's keys
    if contacts:
        example_contact = next(iter(contacts.values()))
    else:
        example_contact = {}

    print("\n* Search options: *")
    search_keys = {}
    option_number = 1

    # Ensuring nested dictionary keys are being used for search options
    for outer_key, inner_dict in example_contact.items():
        if isinstance(inner_dict, dict):
            for inner_key in inner_dict.keys():
                print(f"{option_number}. {outer_key} -> {inner_key}")
                search_keys[str(option_number)] = (outer_key, inner_key)
                option_number += 1
        else:
            print(f"{option_number}. {outer_key}")
            search_keys[str(option_number)] = outer_key
            option_number += 1

    choice = input("Enter the number associated with the search option: ").strip()

    return search_keys.get(choice, 'Name')


def search_contacts(contacts):
    search_key = get_user_search_key(contacts)
    search_value = input("\nEnter the value to search for: ").strip().lower()

    found_contacts = []

    for contact_id, info in contacts.items():
        if isinstance(search_key, tuple):
            outer_key, inner_key = search_key
            if search_value in str(info.get(outer_key, {}).get(inner_key, '')).lower():
                found_contacts.append((contact_id, info))
        else:
            if search_value in str(info.get(search_key, '')).lower():
                found_contacts.append((contact_id, info))

    if found_contacts:
        print(f"\n.~* Search Results for '{search_value}' in '{search_key}': *~.")
        for contact_id, info in found_contacts:
            print(f"\nContact ID: {contact_id}")
            display_contact_info(info)
    else:
        print("\nNo contacts found matching your search criteria.")


def display_contact_info(info):
    # Recursively display contact info, handling nested dictionaries
    for key, value in info.items():
        if isinstance(value, dict):
            print(f"{key}:")
            display_contact_info(value)
        else:
            print(f"{key}: {value}")
