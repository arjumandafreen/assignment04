List Shortener Program
Description
This Python program allows users to input a list of elements and shortens the list to a maximum length of 3 (MAX_LENGTH = 3). If the user enters more than 3 elements, the program will remove the excess elements one by one from the end of the list, informing the user about each removal.

Features
Prompts the user to input a list of elements.

Automatically shortens the list to a predefined maximum length (MAX_LENGTH = 3).

Prints the removed elements as they are popped from the list.

Displays the final list after it has been shortened.

Usage
Run the script: Execute the Python file.

Enter elements: When prompted, enter the elements one by one. Press Enter without typing anything to stop the input.

Shortening the list: The program will check if the list exceeds the maximum allowed length (MAX_LENGTH = 3). If so, it will remove elements from the end of the list.

Display results: The program will show the original list, print each removed element, and display the final list.

Example
Input:
yaml
Copy
Edit
Enter element: apple
Enter element: banana
Enter element: cherry
Enter element: date
Enter element: fig
Enter element: 
Output:
less
Copy
Edit
Original list: ['apple', 'banana', 'cherry', 'date', 'fig']
Removed: fig
Removed: date
Final list: ['apple', 'banana', 'cherry']
Code Walkthrough
MAX_LENGTH: Defines the maximum allowed number of elements in the list.

shorten_list(input_list): This function reduces the list size by removing elements from the end if the list exceeds the maximum length. Each removed element is printed for the user to see.

get_user_input(): This function collects user input until the user presses Enter without entering anything. It stores all inputs in a list.

main(): This is the entry point of the program. It collects the user input, prints the original list, shortens the list if necessary, and prints the final list.

Requirements
Python 3.x

License
This project is licensed under the MIT License.