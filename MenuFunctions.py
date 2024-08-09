# Utilize input() to enable users to select additional menu options and provide contact details
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues during execution

import re
import os

# 1. Add a New Contact
# unique  identifier: {{Name: name}, {Phone Number: number}, {Email Address: email@example.com}, {Additional Info: info here}}
# *BONUS* category groups (friends, family, work) can belong to multiple groups {Category: [cat1, cat2]}
# *BONUS* Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.
def add_new_contact():
    pass

# 2. Edit an existing Contact
# (name, phone number, email, etc.)
# *BONUS* Categories (friends, family, work)
# *BONUS* Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.
def edit_contact(contacts):
    user_input = input("\nEnter the name of the contact to edit: ")
    for contact_id, info in contacts.items():
        if info['Name'].lower() == user_input.lower():
            print("\n* Editing Options: *")
            print("1. Name")
            print("2. Phone Number")
            print("3. Email Address")
            print("4. Birthday")
            print("5. Category")
            print("6. Custom Field")
            info_input = input("Enter the edit option number: ")
            
    pass

# 3. Delete a Contact
def delete_contact(contacts):
    user_input = input("\nEnter the name of the contact you would like to delete: ")
    for contact_id, info in contacts.items():
        if info['Name'].lower() == user_input.lower():
            del contacts[contact_id]
            print(f"\nContact: {user_input} has been deleted from contacts.")
        else:
            print(f"\nContact: {user_input} does not exist in contacts.")
    pass



