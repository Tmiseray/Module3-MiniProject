# Contact Management System Project

Contact Management System is a command-line-based application to simplify the management of your contacts. This program was built using Python Programming Language and made to be user-friendly.

## Features

### User Interface (UI):
* User-friendly command-line-interface (CLI)
* Formatted menus with detailed options to choose from
* Informative messages throughout the application for welcoming the user, successful completions and/or errors that occur, thankful message upon quiting, and a closing/exiting message

### Initializing the System (ContactsManagementSystem.py):
* Provides an initial welcoming message to the user
* Before calling the initial menu, attempts to import contacts from a text file (if Contacts.txt exists, if not initializes an empty dictionary for input)
* Exception handling for errors that may occur and provides a user-friendly format of the error
* Automatic Backup File: If the contacts dictionary exists, creates a back up file (ContactsBackup{i}.txt) within the appropriate directory (Backups). This file is based on whether the path already exists and increments the backup file number {i} by 1, ensuring to create the next backup file in sequence. 
* Finally, the system provides the user with a closing message ('Exiting the program...').

### Initial Menu (Menu.py) & Actions:
* User-friendly formatted menu with detailed options to choose from including:
1. Add a New Contact
2. Edit an Existing Contact
3. Delete a Contact
4. Search for a Contact
5. Display All Contacts
6. Export Contacts to a Text File
7. Import Contacts from a Text File
8. Restore Contacts from Backup File
9. Quit
* This menu has exception handling for user inputs including ValueError and TypeError
* Within each action, the program calls to the appropriate function for the task
* When the user decides to 'Quit' the program, there is a thankful message presented ('Thank you for using Contact Management System!)

### Add a New Contact (AddContact.py):
* Each contact has a unique identifier (Contact ID) that is established. When Adding anew contact, the system will automatically generate the next Contact ID in sequence based on the current Contacts.
* The system generates prompts for user input based on the other contacts' current fields available.
* There are special handling scenarios for additional nested dictionaries, fields that can contain multiple values, and optional values (when the user leaves blank, the system registers 'None')
* Once every available field has been entered, the system gives the user an option for 'Custom Field'. If the user would like to add a custom field for the new contact, they will be prompted for the name of the field and the value. It automatically creates the field for the other existing contacts, ensuring functionality throughout the application.
* Finally, the system provides the user with a confirmation message that the 'New Contact Added: {new_contact.get('Name', 'Unnamed Contact')}' and 'With Unique ID: {new_contact_ID}'.

### Edit an Existing Contact & Delete a Contact(EditContact.py):
* There are 3 parts to this feature:
    - Editing Options Menu
    - Edit an Existing Contact
    - Delete a Contact
1. Editing Options Menu:
    * get_user_edit_key
    * This provides a user-friendly, formatted menu to the user for editing options
    * The options are based on the user's selected contact's current fields and lastly a 'Custom Field'.
    * It also has special handling for any nested dictionary keys and ensures they are being used for editing options as well.
    * Asks for user input of the editing option and returns the choice into the edit_contact function
2. Edit an Existing Contact:
    * edit_contact
    * Asks for user input of the name of the contact they would like to edit and iterates through the contacts dictionary for a match
    * If the contact is found, a formatted message ('* Editing Contact: *') is provided to the user and provides the user the 'Editing Options Menu'.
    * Once the user's choice has been returned, it will iterate through the contact's dictionary for the 'edit_key' they chose and ask for another user input of 'Enter the new information for {edit_key}: '
    * There are special handling statments for:
        - Nested Dictionaries: Provides 'Enter the new information for {outer_key}: -> {inner_key}: '
        - Custom Fields: 'Enter the name of the custom field: ' and 'Enter the information for {custom_key}: '. When a custom field is added, it automatically creates a default value of 'None' for the field in every other existing contact. This ensures functionality throughout the application.
    * Within this feature, depending on the edit key, there are additional validation and formatting checks for:
        - Phone Number: (XXX) XXX-XXXX
        - Email Address: email@example.com
        - Birthday: YYYY-MM-DD
            * These features will be discussed in detail further in the README
    * Finally, the application provides a confirmation message 'Contact '{info['Name']}' has been updated.' or if the contact was not found provides 'Contact not found.'
3. Delete a Contact:
    * delete_contact
    * Asks for user input 'Enter the name of the contact you would like to delete: '
    * If the contact is found, the contact is deleted and the user is provided a confirmation message 'Contact: {user_input} has been deleted from contacts.'
    * If the contact is not found, the user is provided another message 'Contact: {user_input} does not exist in contacts.'

### Search for a Contact (Search.py):
* There are 2 parts to this feature:
    - Search Options Menu
    - Search for a Contact
1. Search Options Menu:
    * get_user_search_key
    * Generates search options based on the first contact's keys
    * Provides the user a formatted menu for search options to choose from
    * Special handling for nested dictionaries
    * Asks for user input 'Enter the number associated with the search option: '
    * If no option is selected, the function will provide a default search option for 'Name'
2. Search for a Contact:
    * search_contacts
    * Collects the search_key from the get_user_search_key function, then prompts the user to 'Enter the value to search for: '
    * The function iterates through all contacts' keys for the value the user provided
    * If the value is found, the contact associated with the value is appended to a 'found_contacts' list
        - Once the function has processed all contacts, the 'found_contacts' list is then provided to the user in a user-friendly format using the 'display_contact_info' function (this is discussed in detail further in the README)
    * If the value is not found, the user is provided a message 'No contacts found matching your search criteria.'

### Display All Contacts (DisplayContacts.py):
* There are 4 parts to this feature:
    - Sorting Options Menu
    - Sorting Contacts by Key
    - Display Contacts
    - Display Contact Info
1. Sorting Options Menu:
    * get_user_sort_key
    * 
2. Sorting Contacts by Key:
    * sort_contacts_by_key
    * 
3. Display Contacts:
    * display_contacts
    * 
3. Display Contact Info:
    * display_contact_info
    * Recursively displays contact information in a user-friendly format including:
        - Indentation based on the level of nesting within the dictionary
        - Comma-separated items from list values

### Export/Import Contacts to a Text File (ImportExport.py):
* 

### Backup Files (Backup.py):
* 

### Validation and Formatting (ValidateFormat.py):
* 

