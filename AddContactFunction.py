# Add New Contact Function
# Includes:
# 


from ValidateFormatFunctions import *


# 1. Add a New Contact
# unique  identifier: {{Name: name}, {Phone Number: number}, {Email Address: email@example.com}, {Additional Info: info here}}
# *BONUS* category groups (friends, family, work) can belong to multiple groups {Category: [cat1, cat2]}
# *BONUS* Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.


def add_new_contact(contacts):
    new_contact_ID = str(len(contacts) + 1).zfill(3)
    new_contact = {}

    print("\n* Adding New Contact *")

    for contact_id, info in contacts.items():
        for outer_key, inner_value in info.items():
            if isinstance(inner_value, dict):
                # Nested dictionary handling (e.g., Phone Number -> Mobile, Work)
                new_contact[outer_key] = {}
                for sub_key in inner_value.keys():
                    sub_value = input(f"\nEnter the {outer_key} -> {sub_key} (or leave blank): ").strip()
                    if sub_value:
                        sub_value = validate_and_format_input(outer_key, sub_value)
                        new_contact[outer_key][sub_key] = sub_value
            elif isinstance(inner_value, list):
                # Handling categories or other list-based fields
                values = input(f"\nEnter {outer_key} (comma-separated, or leave blank for none): ").split(',')
                unique_values = list(set(val.strip() for val in values if val.strip()))
                new_contact[outer_key] = unique_values if unique_values else None
            else:
                # Single value field
                new_value = input(f"\nEnter the information for {outer_key} (or leave blank): ").strip()
                if new_value:
                    new_value = validate_and_format_input(outer_key, new_value)
                    new_contact[outer_key] = new_value

    # # Handle any custom fields
    # for existing_contact in contacts.values():
    #     for key in existing_contact.keys():
    #         if key not in new_contact:
    #             if isinstance(existing_contact[key], list):
    #                 values = input(f"\nEnter {key} (comma-separated, or leave blank for none): ").split(',')
    #                 unique_values = list(set(val.strip() for val in values if val.strip()))
    #                 new_contact[key] = unique_values if unique_values else None
    #             elif isinstance(existing_contact[key], dict):
    #                 new_contact[key] = {}
    #                 for sub_key in existing_contact[key].keys():
    #                     sub_value = input(f"\nEnter {key} -> {sub_key} (or leave blank): ").strip()
    #                     if sub_value:
    #                         sub_value = validate_and_format_input(key, sub_value)
    #                         new_contact[key][sub_key] = sub_value
    #             else:
    #                 value = input(f"Enter {key} information (or leave blank for none): ").strip()
    #                 new_contact[key] = value if value else None

    contacts[new_contact_ID] = new_contact
    print(f"\nNew Contact Added: '{new_contact.get('Name', 'Unnamed Contact')}'")
    print(f"With Unique ID: {new_contact_ID}")


# def add_new_contact(contacts):
#     new_contact_ID = str(len(contacts) + 1).zfill(3)
#     new_contact = {}

#     print("\n* Adding New Contact *")

#     # Directly prompt for the information without iterating over existing contacts
#     name = input("Enter the Name: ").strip()
#     if name:
#         new_contact['Name'] = name

#     phone_numbers = {}
#     for phone_type in ['Mobile', 'Work', 'Home']:
#         phone_number = input(f"Enter {phone_type} Phone Number (or leave blank): ").strip()
#         if phone_number:
#             phone_numbers[phone_type] = phone_number
#     if phone_numbers:
#         new_contact['Phone Number'] = phone_numbers

#     email = input("Enter Email Address: ").strip()
#     if email:
#         new_contact['Email Address'] = email

#     birthday = input("Enter Birthday (YYYY-MM-DD): ").strip()
#     if birthday:
#         new_contact['Birthday'] = birthday

#     categories = input("Enter Categories (comma-separated, or leave blank): ").strip().split(',')
#     unique_categories = list(set(val.strip() for val in categories if val.strip()))
#     if unique_categories:
#         new_contact['Category'] = unique_categories


### TODO Need to create better functionality for creating Key: Value pair for custom field
### TODO Maybe have a loop to ask if they would like to add another custom field and if so, recursively do so until the user input is 'no' or 'None' or 'done'


#     # Handling custom fields
#     favorite_color = input("Enter Favorite Color: ").strip()
#     if favorite_color:
#         new_contact['Favorite Color'] = favorite_color

#     anniversary = input("Enter Anniversary (YYYY-MM-DD): ").strip()
#     if anniversary:
#         new_contact['Anniversary'] = anniversary

#     notes = input("Enter Notes (comma-separated, or leave blank): ").strip().split(',')
#     unique_notes = list(set(val.strip() for val in notes if val.strip()))
#     if unique_notes:
#         new_contact['Notes'] = unique_notes

#     # Add the new contact to the contacts dictionary
#     contacts[new_contact_ID] = new_contact

#     print(f"\nNew Contact Added: '{new_contact.get('Name', 'Unnamed Contact')}'")
#     print(f"With Unique ID: {new_contact_ID}")
