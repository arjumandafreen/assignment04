List Element Finder
# **📌 Get Last Element - Python List Handling 🚀**  

This script retrieves and prints the **last element** from a user-inputted list. It demonstrates **basic list operations, user input handling, and function structuring** in Python.  
Description
This Python program allows users to input elements into a list and then displays the last element entered into the list. If the list is empty, it will notify the user. The program stops collecting inputs when the user presses Enter without typing anything.

Features
Allows the user to input multiple elements into a list.

Displays the last element in the list when the user chooses to stop input.

Handles edge cases (e.g., when the list is empty).

Requirements
Python 3.x

How to Use
Clone the repository or copy the code into a .py file.

Run the Python file.

You will be prompted to enter elements for the list. To stop entering elements, simply press Enter without typing anything.

Once you stop, the program will display the last element entered into the list. If no elements were entered, it will notify you that the list is empty.


Please enter elements of the list. Press Enter without typing anything to stop.
Enter an element: apple
Enter an element: banana
Enter an element: cherry
Enter an element: 

The last element in the list is: cherry
Edge Case:
If no elements are entered, the program will output:


You have not added any elements to the list.
Functions
get_lst(): This function handles the user input, appending each inputted element into a list until the user presses Enter without typing anything.

get_last_element(lst): This function takes a list as input and prints the last element. If the list is empty, it prints a message indicating no last element is available.

main(): The main function where the list is created and the last element is displayed.

License
This project is open-source and available under the MIT License.