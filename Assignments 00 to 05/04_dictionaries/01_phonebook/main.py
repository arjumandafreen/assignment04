def main():
    phone_book = {}

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. View all contacts")
        print("4. Exit")
        print("----------------------")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            phone_book[name] = f"+92{phone_number}"
            print(f"\n✅ {name} added successfully!")

        elif choice == "2":
            search_name = input("Enter the name to search: ")
            if search_name in phone_book:
                print(f"\n📞 {search_name}: {phone_book[search_name]} ✅")
            else:
                print("\n😔 Contact not found.")

        elif choice == "3":
            if phone_book:
                print("\nPhonebook Contacts:")
                for name, number in phone_book.items():
                    print(f"📘 {name}: {number}")
            else:
                print("\n📓 Phonebook is empty!")

        elif choice == "4":
            print("\n📴 Exiting the phonebook.")
            break

        else:
            print("\n⚠️ Invalid choice, try again.")

# Run the main function if this file is executed directly
if __name__ == '__main__':
    main()
