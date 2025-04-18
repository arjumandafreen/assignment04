def get_last_element(lst):
    # Check if the list is not empty
    if lst:
        print(f"The last element in the list is: {lst[-1]}")
    else:
        print("The list is empty, no last element to display.")

def get_lst():
    lst = []
    print("Please enter elements of the list. Press Enter without typing anything to stop.")
    
    while True:
        elem = input("Enter an element: ").strip()
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    if lst:
        get_last_element(lst)  # Print last element
    else:
        print("You have not added any elements to the list.")

if __name__ == '__main__':
    main()
