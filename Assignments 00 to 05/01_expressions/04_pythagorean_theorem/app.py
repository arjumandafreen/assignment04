import math
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n🔺 Welcome to the Hypotenuse Calculator! 🔺\n")
    
    try:
        ab = float(input(Fore.CYAN + "📏 Enter the length of side AB: "))
        ac = float(input(Fore.CYAN + "📐 Enter the length of side AC: "))

        # Calculate the hypotenuse using Pythagorean theorem
        bc = math.sqrt(ab**2 + ac**2)

        print(Fore.GREEN + f"\n✅ The length of BC (the hypotenuse) is: {bc:.2f}")
        print(Fore.YELLOW + "✨ Calculation Complete! ✨\n")
    
    except ValueError:
        print(Fore.RED + "❌ Please enter valid numbers for the side lengths!")

if __name__ == '__main__':
    main()
