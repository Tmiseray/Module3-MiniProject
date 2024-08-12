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
* Finally, the system provides the user with a confirmation message that the 'New Contact Added: ' and 'With Unique ID: '.