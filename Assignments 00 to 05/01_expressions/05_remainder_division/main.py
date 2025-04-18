from colorama import Fore, Style, init

def main():
    init(autoreset=True)

    print(Fore.CYAN + Style.BRIGHT + "\n🚀 Welcome to the Cool Divider Program! 🚀\n")

    try:
        dividend = int(input(Fore.YELLOW + "🔢 Please enter an integer to be divided: "))
        divisor = int(input(Fore.YELLOW + "➗ Please enter an integer to divide by: "))

        quotient = dividend // divisor
        remainder = dividend % divisor

        print(Fore.GREEN + f"\n✅ The result of this division is:")
        print(Fore.MAGENTA + f"   👉 Quotient : {quotient}")
        print(Fore.MAGENTA + f"   👉 Remainder: {remainder}\n")
        print(Fore.CYAN + "🎉 Division complete! You're awesome! 🎉")

    except ZeroDivisionError:
        print(Fore.RED + "🚫 Error: You cannot divide by zero!")
    except ValueError:
        print(Fore.RED + "🚫 Error: Please enter valid integers!")

if __name__ == '__main__':
    main()
