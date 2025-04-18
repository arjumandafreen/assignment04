from termcolor import colored, cprint
import pyfiglet

def square_number():
    # Cool ASCII banner
    banner = pyfiglet.figlet_format("Square Program")
    cprint(banner, "cyan")

    # Welcome Message
    print(colored("🌟 Welcome to the Square Number Program by Arjumand! 🌟", "cyan", attrs=["bold", "underline"]))
    print("-" * 60)

    while True:
        try:
            number = int(input(colored("🔢 Enter a number to square: ", "light_magenta", attrs=["bold"])))
            break
        except ValueError:
            print(colored("❌ Oops! That’s not a valid number. Try again.", "red", attrs=["bold"]))

    square = number ** 2
    print(colored(f"\n✅ The square of {number} is: {square}", "yellow", attrs=["bold", "underline"]))
    
    print(colored("\n🎉 Thank you for using the Square Number Program! Have a great day! 🎉", "green", attrs=["bold"]))
    print("-" * 60)

if __name__ == '__main__':
    square_number()
