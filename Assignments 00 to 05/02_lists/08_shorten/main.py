
MAX_LENGTH = 3  # Maximum allowed length of the list

def shorten_list(input_list):
    """Shortens the list to MAX_LENGTH by removing excess elements."""
    # Create a copy of the list so the original one remains unchanged
    shortened_list = input_list[:]
    while len(shortened_list) > MAX_LENGTH:
        removed_element = shortened_list.pop()  # Remove the last element
        print(f"Removed: {removed_element}")  # Inform the user of the removed element
    
    return shortened_list  # Return the shortened list

def get_user_input():
    """Collects a list of elements from the user until they press enter without input."""
    user_list = []
    print("Please enter elements for the list. Press Enter without input to stop.")
    
    while True:
        element = input("Enter element: ")
        if not element:  # Stop if the input is empty
            break
        user_list.append(element)
    
    return user_list

def main():
    user_list = get_user_input()  # Get the list of elements from the user
    print(f"Original list: {user_list}")
    user_list = shorten_list(user_list)  # Shorten the list if it's longer than MAX_LENGTH
    print(f"Final list: {user_list}")  # Display the final list after modification

if __name__ == '__main__':
    main()
