# Contact Management System Project

Contact Management System is a command-line-based application to simplify the management of your contacts. This program was built using Python Programming Language and made to be user-friendly. It allows for you to add, edit, delete, search for contacts, and more! Detailed descriptions of each feature and function are below in the Features section.

## Requirements:
* This project requires the following modules:
    - Python [Python Downloads](https://www.python.org/downloads/)
    - OS (`import os`)
    - REGEX (`import re`)

## Installation:
*** Cloning Option ***
* If you have Git Bash installed, you can clone the repository using the URL
1. Create a 'Clone' Folder
2. Within the folder, right-click for Git Bash
3. From the GitHub Repository, click on the '<> Code' button and copy the link provided
4. Paste the link into your Git Bash and click 'Enter'
* If you have GitHub Desktop, when you click on the '<> Code' button you will have an option to 'Open with GitHub Desktop'
* If you have Visual Studio Code, when you click on the '<> Code' button you will have an option to 'Open with Visual Studio'
*** Download Option ***
1. From the GitHub Repository, click on the '<> Code' button
2. Click on 'Download Zip'
3. Extract contents of Zip file

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
* `menu(contacts)`
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
* `add_new_contact(contacts)`
* Each contact has a unique identifier (Contact ID) that is established. When Adding anew contact, the system will automatically generate the next Contact ID in sequence based on the current Contacts.
* The system generates prompts for user input based on the other contacts' current fields available.
* There are special handling scenarios for additional nested dictionaries, fields that can contain multiple values, and optional values (when the user leaves blank, the system registers 'None')
* Once every available field has been entered, the system gives the user an option for 'Custom Field'. If the user would like to add a custom field for the new contact, they will be prompted for the name of the field and the value. It automatically creates the field for the other existing contacts, ensuring functionality throughout the application.
* Finally, the system provides the user with a confirmation message that the 'New Contact Added: {new_contact.get('Name', 'Unnamed Contact')}' and 'With Unique ID: {new_contact_ID}'.

### Edit an Existing Contact & Delete a Contact(EditContact.py):
* There are 3 parts to this feature:
    - **Editing Options Menu**
    - **Edit an Existing Contact**
    - **Delete a Contact**
1. Editing Options Menu:
    * `get_user_edit_key(contact_info)`
    * This provides a user-friendly, formatted menu to the user for editing options
    * The options are based on the user's selected contact's current fields and lastly a 'Custom Field'.
    * It also has special handling for any nested dictionary keys and ensures they are being used for editing options as well.
    * Asks for user input of the editing option and returns the choice into the edit_contact function
2. Edit an Existing Contact:
    * `edit_contact(contacts)`
    * Asks for user input of the name of the contact they would like to edit and iterates through the contacts dictionary for a match
    * If the contact is found, a formatted message ('* Editing Contact: *') is provided to the user and provides the user the 'Editing Options Menu'.
    * Once the user's choice has been returned, it will iterate through the contact's dictionary for the 'edit_key' they chose and ask for another user input of 'Enter the new information for {edit_key}: '
    * There are special handling statments for:
        - *Nested Dictionaries:* Provides 'Enter the new information for {outer_key}: -> {inner_key}: '
        - *Custom Fields:* 'Enter the name of the custom field: ' and 'Enter the information for {custom_key}: '. When a custom field is added, it automatically creates a default value of 'None' for the field in every other existing contact. This ensures functionality throughout the application.
    * Within this feature, depending on the edit key, there are additional validation and formatting checks for:
        - *Phone Number:* (XXX) XXX-XXXX
        - *Email Address:* email@example.com
        - *Birthday:* YYYY-MM-DD
            * These features will be discussed in detail further in the README under *** Validation and Formatting ***
    * Finally, the application provides a confirmation message 'Contact '{info['Name']}' has been updated.' or if the contact was not found provides 'Contact not found.'
3. Delete a Contact:
    * `delete_contact(contacts)`
    * Asks for user input 'Enter the name of the contact you would like to delete: '
    * If the contact is found, the contact is deleted and the user is provided a confirmation message 'Contact: {user_input} has been deleted from contacts.'
    * If the contact is not found, the user is provided another message 'Contact: {user_input} does not exist in contacts.'

### Search for a Contact (Search.py):
* There are 2 parts to this feature:
    - **Search Options Menu**
    - **Search for a Contact**
1. Search Options Menu:
    * `get_user_search_key(contacts)`
    * Generates search options based on the first contact's keys
    * Provides the user a formatted menu for search options to choose from
    * Special handling for nested dictionaries
    * Asks for user input 'Enter the number associated with the search option: '
    * If no option is selected, the function will provide a default search option for 'Name'
2. Search for a Contact:
    * `search_contacts(contacts)`
    * Collects the 'search_key' from the `get_user_search_key` function, then prompts the user to 'Enter the value to search for: '
    * The function iterates through all contacts' keys for the value the user provided
    * If the value is found, the contact associated with the value is appended to a 'found_contacts' list
        - Once the function has processed all contacts, the 'found_contacts' list is then provided to the user in a user-friendly format using the `display_contact_info` function (this is discussed in detail further in the README)
    * If the value is not found, the user is provided a message 'No contacts found matching your search criteria.'

### Display All Contacts (DisplayContacts.py):
* There are 4 parts to this feature:
    - **Sorting Options Menu**
    - **Sorting Contacts by Key**
    - **Display Contacts**
    - **Display Contact Info**
1. Sorting Options Menu:
    * `get_user_sort_key(contacts)`
    * Generates sorting options based on the first contact's keys and values
    * Handles any key-value pairs that have nested dictionaries
    * Provides a user-friendly menu for the user to select sorting options from
    * Asks for user input for the number associated with the sorting option
    * Returns the user's choice or if nothing input, gives a default option of 'Name'
2. Sorting Contacts by Key:
    * `sort_contacts_by_key(contacts, sort_key)`
    * Takes the 'sort_key' the user selected from `get_user_sort_key` and sorts the contacts based on the user's 'sort_key'
    * Returns the 'sorted_contacts' for the next function
3. Display Contacts:
    * `display_contacts(contacts)`
    * Asks the user if they would like the contacts sorted
    * If 'yes':
        - Calls to the `get_user_sort_key` function for the user's 'sort_key' and assigns it to a variable
        - Calls to the `sort_contacts_by_key` function with the user's 'sort_key' and 'contacts' as parameters to get the sorted contacts dictionary based on the user's sorting option chosen
        - Displays a user-friendly, formatted title with the sorting option chosen. Then for each contact's 'info' in the 'contacts' dictionary, calls to the `display_contact_info` function for formatting and special handling
3. Display Contact Info:
    * `display_contact_info(info, indent_level = 0)`
    * Recursively displays contact information in a user-friendly format including:
        - Indentation based on the level of nesting within the dictionary
        - Comma-separated items from list values
    * This function is also used in the `search_contacts(contacts)` function

### Export/Import Contacts to a Text File (ImportExport.py):
* There are 3 parts to this feature:
    - **Export Contacts to a Text File**
    - **Import Contacts from a Text File**
    - **Merge Contact Information**
1. Export Contacts to a Text File:
    * `export_contacts_to_text(contacts)`
    * Exports 'contacts' to a text file (Contacts.txt) in a structured, user-friendly format
    * Ensures to 'write' vs 'append' the file so there are no duplicated contacts
2. Import Contacts from a Text File:
    * `import_contacts_from_text(contacts = None)`
    * Imports contacts from a text file (Contacts.txt) and adds them to the system
    * Uses *REGEX* for patterns to match for proper import into 'contacts' dictionary
    * Uses an additional merge function (`merge_contacts`) to ensure there are no duplicated contacts or values
    * Exceptions for error handling with user-friendly messages indicating what went wrong
    * Returns the 'contacts' dictionary and provides a confirmation message to the user when the import was successful
3. Merge Contact Information:
    * `merge_contacts(existing_contact, new_info)`
    * Handles any existing contacts and new information
        - Adds new information if it does not exist
        - Merges any existing fields with new information
    * Returns the contact's information once completed

### Backup Files (Backup.py):
* There are 3 parts to this feature:
    - *Create a Backup File*
    - *Find the Latest Backup File*
    - *Restore Contacts from Backup File*
* All 3 use the OS Module for file handling
1. Create a Backup File:
    * `create_contacts_backup(contacts)`
    * Creates a new backup file within the 'Backups' directory based on the existing 'ContactsBackup.txt' file
    * Ensures the backup file is in a user-friendly format
    * Provides the user with a confirmation message when the bakcup is successful including the location of the new backup
2. Find the Latest Backup File:
    * `find_latest_backup()`
    * Checks if the directory 'Backups' exists
        - If not, provides a message to the user
        - If exists, joins the backup directory and file name and increments the number at the end of the file until the file does not exist. Once the last increment has taken place, creates a variable for the backup with the file decremented by 1
    * If a 'latest_backup' variable exists, provides the user with a confirmation message of the found backup with the file name and returns the 'latest_backup'
    * If no 'latest_backup' variable exists, provides the user with a message indicating it was not found and returns None
3. Restore Contacts from Backup File:
    * `restore_contacts_backup()`
    * Calls the `find_latest_backup` function and 'reads' the file information
    * For each line in the file, the function strips and splits upon specified parameters. Ensuring the 'contacts' dictionary is updated with the contents from the backup file properly
    * When successful, provides the usesr with a message indicating Contacts was restored and from what backup file. Returns the 'contacts' dictionary after restoration
    * If no backup file found, provides a message to the user indicating no backup files were found. Returns an empty dicitonary.

### Validation and Formatting (ValidateFormat.py):
* There are 6 parts to this feature:
    - *Validation for Phone Numbers*
    - *Validation for Email Addresses*
    - *Validation for Birthdays*
    - *Formatting for Phone Numbers*
    - *Formatting for Birthdays*
    - *Validate and Format User Input*
* Most of these functions use the REGEX Module for pattern matching, besides the 'Validate and Format User Inputs' which calls to the functions
1. Validation for Phone Numbers:
    * `validate_phone_number(phone_number)`
    * Matches the inputted phone number to a REGEX pattern
2. Validation for Email Addresses:
    * `validate_email(email)`
    * Matches the inputted email address to a REGEX pattern
3. Validation for Birthdays:
    * `validate_birthday(birthday)`
    * Matches the inputted birthday to a REGEX pattern
4. Formatting for Phone Numbers:
    * `format_phone_number(phone_number)`
    * Matches elements within the substring to a REGEX pattern and replaces them
    * Searches for another REGEX pattern and creates a group from it
    * Slices the 'group' from the number variable
    * Creates a formatted phone number using the group variable and slicing from the number variable
5. Formatting for Birthdays:
    * `format_birthday(birthday)`
    * Matches the inputted birthday to a REGEX pattern3
    * If it matches the pattern, formats to a standard date format and returns the formatted birthday
    * Matches the inputted birthday to a REGEX pattern2
    * If it matches the pattern, formats to a standard date format and returns the formatted birthday
    * Anything else will just return the birthday
6. Validate and Format User Input:
    * `validate_and_format_input(key, value)`
    * This will take a key-value pair from other functions to validate and format based on the key
    * If any of the validations or formatting fails, provides a message to the user indicating invalid format and a standard format they should use

