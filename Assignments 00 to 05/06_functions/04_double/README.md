📄 Description
This is a simple Python program that doubles a number entered by the user. It demonstrates the use of:

Functions

Input handling

Basic error checking using try-except

🚀 How It Works
The user is prompted to enter a number.

The input is passed to a function called double() which multiplies it by 2.

The result is printed back to the user.

If the user enters invalid input (e.g., letters), the program displays an error message.

🧠 Functions
double(num)
Takes a number as input.

Returns the number multiplied by 2.

main()
Handles user input.

Calls the double() function.

Displays the result or an error message if the input is invalid.

▶️ Usage
Run the script using:

bash
Copy
Edit
python filename.py
Example:

vbnet
Copy
Edit
Enter a number to double it: 5

Double of 5 is 10
⚠️ Error Handling
If a user enters a non-integer value:


Enter a number to double it: abc

Invalid input! Please enter a valid number.