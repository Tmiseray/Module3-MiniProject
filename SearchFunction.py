# Search Functions
# Including:
    # Search Key from User and if not Default
    # Search Contacts by User's Search Key
    # Displaying Contacts Matching User's Search Criteria


import re
import os
from MenuFunctions import *
from ValidateFormatFunctions import *

# 4. Search for a Contact
# Search for contact and display details
# *BONUS* allow options for search by name, phone number, email, or additional information

def get_user_search_key():
    print("\n* Search Criteria: *")
    print("1. Name")
    print("2. Phone Number")
    print("3. Email Address")
    print("4. Birthday")
    print("5. Category")
    choice = input("Enter the number associated with the criteria to search by: ").strip()

    search_keys = {
        '1': 'Name',
        '2': 'Phone Number',
        '3': 'Email Address',
        '4': 'Birthday',
        '5': 'Category'
    }

    return search_keys.get(choice, 'Name')


def search_contacts(contacts):
    search_key = get_user_search_key()
    if search_key == 'Phone Number':
        search_number = input("Enter the phone number to search for: ")
        if validate_phone_number(search_number):
            print("\n.~* Contacts Matching Search: *~.")
            print(f"* Criteria: {search_number} *")
            for contact_id, info in contacts:
                if info['Phone Number'] == search_number:
                    print(f"\nContact ID: {contact_id}")
                    print(f"Name: {info['Name']}")
                    print(f"Email Address: {info['Email Address']}")
                    print(f"Birthday: {info['Birthday']}")
                    print(f"Category: {info['Category']}")
                else:
                    print("No matches found.")
        else:
            phone_number = format_phone_number(search_number)
            print("\n.~* Contacts Matching Search: *~.")
            print(f"* Criteria: {phone_number} *")
            for contact_id, info in contacts:
                if info['Phone Number'] == phone_number:
                    print(f"\nContact ID: {contact_id}")
                    print(f"Name: {info['Name']}")
                    print(f"Email Address: {info['Email Address']}")
                    print(f"Birthday: {info['Birthday']}")
                    print(f"Category: {info['Category']}")
                else:
                    print("No matches found.")
    elif search_key == 'Email Address':
        search_email = input("Enter the email address to search for: ")
        if validate_email(search_email):
            print("\n.~* Contacts Matching Search: *~.")
            print(f"* Criteria: {search_email} *")
            for contact_id, info in contacts:
                if info['Email Address'] == search_email:
                    print(f"\nContact ID: {contact_id}")
                    print(f"Name: {info['Name']}")
                    print(f"Phone Number: {info['Phone Number']}")
                    print(f"Birthday: {info['Birthday']}")
                    print(f"Category: {info['Category']}")
                else:
                    print("No matches found.")
        else:
            print(f"\nInvalid format for search criteria: {search_key}.")
            print("Please try again or choose another criteria.")
            get_user_search_key()
    elif search_key == 'Birthday':
        search_birthday = input("Enter the birthday to search for: ")
        if validate_birthday(search_birthday):
            print("\n.~* Contacts Matching Search: *~.")
            print(f"* Criteria: {search_birthday} *")
            for contact_id, info in contacts:
                if info['Birthday'] == search_birthday:
                    print(f"\nContact ID: {contact_id}")
                    print(f"Name: {info['Name']}")
                    print(f"Phone Number: {info['Phone Number']}")
                    print(f"Email Address: {info['Email Address']}")
                    print(f"Category: {info['Category']}")
                else:
                    print("No matches found.")
        else:
            formatted_birthday = format_birthday(search_birthday)
            if validate_birthday(formatted_birthday):
                print("\n.~* Contacts Matching Search: *~.")
                print(f"* Criteria: {formatted_birthday} *")
                for contact_id, info in contacts:
                    if info['Birthday'] == formatted_birthday:
                        print(f"\nContact ID: {contact_id}")
                        print(f"Name: {info['Name']}")
                        print(f"Phone Number: {info['Phone Number']}")
                        print(f"Email Address: {info['Email Address']}")
                        print(f"Birthday: {info['Birthday']}")
                        print(f"Category: {info['Category']}")
                    else:
                        print("No matches found.")
            else:
                print(f"\nInvalid format for search criteria: {search_key}.")
                print("Please provide a valid date in DD.MM.YYYY, DD/MM/YYYY, or YYYY-MM-DD format.")
                print("Or choose another criteria.")
                get_user_search_key()
    elif search_key == 'Category':
        search_category = input("Enter the category to search for: (Friends/Family/Work) ")
        print("\n.~* Contacts Matching Search: *~.")
        print(f"* Criteria: {search_category} *")
        for contact_id, info in contacts:
            if info['Category'].lower() == search_category.lower():
                print(f"\nContact ID: {contact_id}")
                print(f"Name: {info['Name']}")
                print(f"Phone Number: {info['Phone Number']}")
                print(f"Email Address: {info['Email Address']}")
                print(f"Birthday: {info['Birthday']}")
            else:
                print("No matches found.")
    elif search_key == 'Name':
        search_name = input("Enter the name to search for: ")
        print("\n.~* Contacts Matching Search: *~.")
        print(f"* Criteria: {search_name} *")
        for contact_id, info in contacts:
            if info['Name'].lower() == search_name.lower():
                print(f"\nContact ID: {contact_id}")
                print(f"Name: {info['Name']}")
                print(f"Phone Number: {info['Phone Number']}")
                print(f"Email Address: {info['Email Address']}")
                print(f"Birthday: {info['Birthday']}")
                print(f"Category: {info['Category']}")
            else:
                print("No matches found.")
    else:
        print("Invalid criteria. Please choose another search option.")
        get_user_search_key()
        
    pass