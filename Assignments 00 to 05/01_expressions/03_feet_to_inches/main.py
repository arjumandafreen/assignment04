from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

INCHES_IN_FOOT = 12

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n📏 Feet to Inches Converter 📏\n")
    
    try:
        feet = float(input(Fore.YELLOW + "👉 Enter number of feet: "))

        # Convert feet to inches
        inches = feet * INCHES_IN_FOOT

        print(Fore.GREEN + f"\n✅ {feet} feet is equal to {inches} inches.\n")
        print(Fore.MAGENTA + "✨ Conversion completed successfully! ✨")
    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter a numeric value.")

if __name__ == '__main__':
    main()
