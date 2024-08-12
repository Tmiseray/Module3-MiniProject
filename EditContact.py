# Edit Functions
# Including:
    # Edit key based on the contact's information keys(including nested keys) and providing an additional option for a custom field
    # Handles validation based on edit key and formatting for phone numbers, emails, and birthdates
    # Handling nested dictionary keys/tuples to ensure values are updated for the proper nested type
    # Delete contact function


from ValidateFormat import *


# 2. Edit an existing Contact
# (name, phone number, email, etc.)
# *BONUS* Categories (friends, family, work)
# *BONUS* Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

def get_user_edit_key(contact_info):
    print(f"\n* Editing Options: *")
    edit_keys = {}
    option_number = 1

    # Ensuring nested dictionary keys are being used for sort options
    for outer_key, inner_dict in contact_info.items():
        if isinstance(inner_dict, dict):
            for inner_key in inner_dict.keys():
                print(f"{option_number}. {outer_key}: -> {inner_key}")
                edit_keys[str(option_number)] = (outer_key, inner_key)
                option_number += 1
        else:
            print(f"{option_number}. {outer_key}")
            edit_keys[str(option_number)] = outer_key
            option_number += 1
    print(f"{option_number}. Custom Field")

    choice = input("Enter the number associated with the editing option: ").strip()

    return edit_keys.get(choice)


def edit_contact(contacts):
    user_input = input("\nEnter the name of the contact to edit: ").strip()
    contact_found = False

    for contact_id, info in contacts.items():
        if info['Name'].lower() == user_input.lower():
            contact_found = True
            print(f"\n* Editing Contact: {user_input} *")
            edit_key = get_user_edit_key(info)

            if isinstance(edit_key, tuple):
                outer_key, inner_key = edit_key
                new_value = input(f"Enter the new information for {outer_key} -> {inner_key}: ").strip()
                # Validate and Format input based on 'edit_key'
                if outer_key == 'Phone Number':
                    if validate_phone_number(new_value):
                        info[outer_key][inner_key] = new_value
                    else:
                        formatted_number = format_phone_number(new_value)
                        if validate_phone_number(formatted_number):
                            info[outer_key][inner_key] = formatted_number
                        else:
                            print("\nInvalid phone number format.")
                            print("Please use (XXX) XXX-XXXX.")
                            return
                else:
                    info[outer_key][inner_key] = new_value
            elif edit_key not in info:
                custom_key = input("Enter the name of the custom field: ").strip()
                custom_value = input(f"Enter the information for {custom_key}: ").strip()
                # TODO when adding custom field, ensure all other ocntacts are updated with field and None as default value
                for contact in contacts.values():
                    if custom_key not in contact:
                        contact[custom_key] = 'None'

                info[custom_key] = custom_value
            else:
                new_value = input(f"Enter the new information for {edit_key}: ").strip()
                # Validate and Format input based on 'edit_key'
                if edit_key == 'Phone Number':
                    if validate_phone_number(new_value):
                        info[edit_key] = new_value
                    else:
                        formatted_number = format_phone_number(new_value)
                        if validate_phone_number(formatted_number):
                            info[edit_key] = formatted_number
                        else:
                            print("\nInvalid phone number format.")
                            print("Please use (XXX) XXX-XXXX.")
                            return
                elif edit_key == 'Email Address':
                    if validate_email(new_value):
                        info[edit_key] = new_value
                    else:
                        print("\nInvalid email address format.")
                        print("Please try again.")
                        return
                elif edit_key == 'Birthday':
                    if validate_birthday(new_value):
                        info[edit_key] = new_value
                    else:
                        formatted_birthday = format_birthday(new_value)
                        if validate_birthday(formatted_birthday):
                            info[edit_key] = formatted_birthday
                        else:
                            print("\nInvalid birthday format.")
                            print("Please use YYYY-MM-DD.")
                            return
                else:
                    info[edit_key] = new_value

            print(f"\nContact '{info['Name']}' has been updated.")
            break

    if not contact_found:
            print("\nContact not found.")
    return contacts


# 3. Delete a Contact
def delete_contact(contacts):
    user_input = input("\nEnter the name of the contact you would like to delete: ")
    for contact_id, info in contacts.items():
        if info['Name'].lower() == user_input.lower():
            del contacts[contact_id]
            print(f"\nContact: {user_input} has been deleted from contacts.")
            return contacts
        else:
            print(f"\nContact: {user_input} does not exist in contacts.")
            return



