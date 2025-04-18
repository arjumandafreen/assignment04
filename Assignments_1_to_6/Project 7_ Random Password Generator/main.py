import random
import string

def generate_password(numbers=1, length=12, use_special_chars=True, use_numbers=True):
    # Generates random passwords based on user preferences.

    passwords = []

    for _ in range(numbers):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        char_pool = lower_case + upper_case

        if use_numbers:
            char_pool += digits
        if use_special_chars:
            char_pool += special_chars

        password = "".join(random.choice(char_pool) for _ in range(length))
        passwords.append(password)

    return passwords


def main():
    print("\033[95m\n🔐 Welcome to Password Generator\033[0m")
    print("\033[94m===============================\033[0m")

    try:
        numbers = int(input("\033[96m\n💬 How many passwords do you want to generate? \033[0m"))
        length = int(input("\033[96m📏 Enter the desired password length: \033[0m"))

        if numbers < 1 or length < 1:
            print("\033[91m\n⚠️ Error: Please enter positive values for password count and length.\033[0m")
            return

        include_numbers = input("\033[93m🔢 Include numbers? (y/n): \033[0m").strip().lower() == 'y'
        include_special = input("\033[93m❗ Include special characters? (y/n): \033[0m").strip().lower() == 'y'

        passwords = generate_password(numbers, length, include_special, include_numbers)

        print("\033[92m\n✅ Your generated password(s):\n\033[0m")
        for idx, password in enumerate(passwords, start=1):
            print(f"\033[94m{idx}. \033[92m{password}\033[0m")
        print(" ")

    except ValueError:
        print("\033[91m\n❌ Error: Please enter a valid number for password count and length.\033[0m\n")
    
    except Exception as e:
        print(f"\033[91m\n💥 An unexpected error occurred: {e}\033[0m\n")


if __name__ == "__main__":
    main()
