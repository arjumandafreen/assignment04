from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    Anton: int = 21
    Beth: int = Anton + 6
    Chen: int = Beth + 20
    Drew: int = Chen + Anton
    Ethan: int = Chen

    print(Fore.RED + f"🎈 Anton is {Anton} years old.")
    print(Fore.MAGENTA + f"🌸 Beth is {Beth} years old.")     
    print(Fore.CYAN + f"🐉🎯 Chen is {Chen} years old.")
    print(Fore.YELLOW + f"🚀 Drew is {Drew} years old.")
    print(Fore.GREEN + f"🌿 Ethan is {Ethan} years old.")

if __name__ == '__main__':
    main()
