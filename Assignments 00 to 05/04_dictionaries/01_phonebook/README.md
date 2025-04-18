# Phonebook CLI Application

This is a simple command-line phonebook application written in Python. It allows users to store contact names with their phone numbers, display all entries, and look up phone numbers by name.

## Features

- Add multiple name and phone number pairs.
- Automatically stops when a blank name is entered.
- Displays all saved contacts.
- Search for a contact's number by entering their name.
- Graceful handling of unknown names.

## How to Use

1. Make sure Python (version 3.x) is installed on your system.
2. Run the program using a terminal or command prompt:

```bash
python phonebook.py
Follow the on-screen prompts:

Enter a name and number to add to the phonebook.

Press Enter on an empty name to stop adding entries.

All saved contacts will be displayed.

Then you can look up contacts by name.

Press Enter on an empty line to stop the lookup process.

Example
plaintext
Copy
Edit
Name: Alice
Number: 1234567890
Name: Bob
Number: 0987654321
Name:

Phonebook Entries:
Alice -> 1234567890
Bob -> 0987654321

Enter name to lookup: Alice
1234567890
Enter name to lookup: Charlie
Charlie is not in the phonebook
Enter name to lookup:
Files
phonebook.py — The main Python script.

README.md — Instructions and details about the program.

License
This project is open source and free to use.