# Display Functions
# Including:
    # Sort Key from User and if not Default
    # Sorting Contacts by User's Sort Key
    # Displaying Contacts with/without Sort
    # Recursively displays contact's info and applies indentations for nested info based on the level of nesting, making the display more user-friendly


# 5. Display All Contacts
# Display each contact and all details
# *BONUS* Implement sorting options to display contacts alphabetically or other criteria

def get_user_sort_key(contacts):
    # Generate sorting options dynamically based on the first contact's keys
    if contacts:
        example_contact = next(iter(contacts.values()))
    else:
        example_contact = {}

    print("\n* Sorting options: *")
    sort_keys = {}
    option_number = 1

    # Ensuring nested dictionary keys are being used for sort options
    for outer_key, inner_dict in example_contact.items():
        if isinstance(inner_dict, dict):
            for inner_key in inner_dict.keys():
                print(f"{option_number}. {outer_key} -> {inner_key}")
                sort_keys[str(option_number)] = (outer_key, inner_key)
                option_number += 1
        else:
            print(f"{option_number}. {outer_key}")
            sort_keys[str(option_number)] = outer_key
            option_number += 1

    choice = input("Enter the number associated with the sorting option: ").strip()

    return sort_keys.get(choice, 'Name')


def sort_contacts_by_key(contacts, sort_key):
    contact_items = list(contacts.items())

    # Handle sorting by a nested key if 'sort_key' is a tuple
    if isinstance(sort_key, tuple):
        outer_key, inner_key = sort_key
        sorted_contacts = dict(sorted(contact_items, key=lambda item: item[1].get(outer_key, {}).get)(inner_key, ''))
    else:
        sorted_contacts = dict(sorted(contact_items, key=lambda item: item[1].get(sort_key, '')))

    return sorted_contacts


def display_contacts(contacts):
    sort = input("Would you like to sort the contacts? (yes/no): ").lower()
    if sort == 'yes':
        sort_key = get_user_sort_key(contacts)
        sorted_contacts = sort_contacts_by_key(contacts, sort_key)
        print("\n.~* Full Contacts List: *~.")
        print(f"* Sorted By: {sort_key} *")
        for contact_id, info in sorted_contacts.items():
            print(f"\nContact ID: {contact_id}")
            display_contact_info(info)
    else:
        print("\n.~* Full Contacts List: *~.")
        for contact_id, info in contacts.items():
            print(f"\nContact ID: {contact_id}")
            display_contact_info(info)


def display_contact_info(info, indent_level = 0):
    # recursively display contact info
    # Adjust indentation based on level of nesting
    indent = "    " * indent_level

    for key, value in info.items():
        if isinstance(value, dict):
            # Display key for nested dictionary
            print(f"{indent}{key}: ")
            display_contact_info(value, indent_level + 1)
        elif isinstance(value, list):
            # Display list values as comma-separated items
            print(f"{indent}{key}: {', '.join(value)}")
        else:
            # Only display the key if there is a value
            print(f"{indent}{key}: {value}")
