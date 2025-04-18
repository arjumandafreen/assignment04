def get_first_element(lst):
    """
    Prints the first element of the provided list.
    If the list is empty, it informs the user.
    """
    if lst:  # Check if the list is not empty
        print(f"\n✅ The first element in your list is: **{lst[0]}**")
    else:
        print("\n⚠️ The list is empty. No elements to display.")


def get_lst():
    """
    Prompts the user to input elements for a list until they press Enter with no input.
    Returns the created list.
    """
    print("📝 Let's build your list!")
    print("Enter elements one by one. Press [Enter] to finish.\n")

    lst = []
    count = 1

    while True:
        elem = input(f"Enter element #{count}: ")
        if not elem:  # Stop if the input is empty (Enter pressed without typing)
            break
        lst.append(elem)
        count += 1

    print(f"\n📦 Your final list: {lst}")
    return lst


def main():
    """
    The main function that orchestrates the creation of the list
    and prints the first element.
    """
    lst = get_lst()           # Get the list from user input
    get_first_element(lst)    # Print the first element (if any)


if __name__ == '__main__':
    print("🔹 Welcome to the List Element Viewer 🔹\n")
    main()
    print("\n👋 Thanks for using the program!")
