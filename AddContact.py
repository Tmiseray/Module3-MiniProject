# Add New Contact Function
# Includes:
    # Creating a new contact ID (unique identifier) based on the existing contacts data
    # Gives the user field options based on the existing contacts information/data
    # Gives the user an additonal option for a custom field they can title and add input value for
    # Handles validation and formatting for user inputs that are phone numbers, emails, and birthdates



from ValidateFormat import *


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
                    if sub_key in new_contact[outer_key].keys():
                        break
                    else:
                        sub_value = input(f"\nEnter the {outer_key} -> {sub_key} (or leave blank): ").strip()
                        if sub_value:
                            sub_value = validate_and_format_input(outer_key, sub_value)
                            new_contact[outer_key][sub_key] = sub_value
                        else:
                            new_contact[outer_key][sub_key] = 'None'
            elif isinstance(inner_value, list):
                # Handling categories or other list-based fields
                if outer_key in new_contact.keys():
                    break
                else:
                    values = input(f"\nEnter {outer_key} (comma-separated, or leave blank for none): ").split(',')
                    unique_values = list(set(val.strip() for val in values if val.strip()))
                    new_contact[outer_key] = unique_values if unique_values else None

            else:
                # Single value field
                if outer_key in new_contact.keys():
                    break
                else:
                    new_value = input(f"\nEnter the information for {outer_key} (or leave blank): ").strip()
                    if new_value:
                        new_value = validate_and_format_input(outer_key, new_value)
                        new_contact[outer_key] = new_value
                    else:
                        new_contact[outer_key] = 'None'
        custom_choice = input("Would you like to add a custom field? (yes/no): ")
        if custom_choice == 'yes':
            custom_field = input("Enter the name for the custom field: ").strip()
            custom_value = input(f"Enter the value for {custom_field}: ").strip()
            new_contact[custom_field] = custom_value

        else:
            break

    contacts[new_contact_ID] = new_contact
    print(f"\nNew Contact Added: '{new_contact.get('Name', 'Unnamed Contact')}'")
    print(f"With Unique ID: {new_contact_ID}")
    return contacts

# TODO Attempt to add custom field, if so add custom field with default None to all other contacts