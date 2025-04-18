def get_user_input():
    """
    Prompts the user to enter values to be added to a list.
    Continues until the user presses Enter without typing anything.
    Returns the list of user inputs.
    """
    lst = []  # Initialize an empty list to store user inputs
    
    print("Enter values to add to the list. Press Enter without typing anything to stop.")
    while True:
        value = input("Enter a value: ").strip()  # Get user input and strip any extra spaces
        if not value:  # If the input is empty, stop the loop
            break
        lst.append(value)  # Add the non-empty input to the list
    
    return lst

def display_list(lst):
    """
    Displays the list of values entered by the user.
    """
    print("\nHere's the list you entered:")
    print(lst)

def main():
    """
    Main function that coordinates the user input and display of the list.
    """
    user_list = get_user_input()  # Get the list of user inputs
    display_list(user_list)  # Display the final list

if __name__ == '__main__':
    main()
