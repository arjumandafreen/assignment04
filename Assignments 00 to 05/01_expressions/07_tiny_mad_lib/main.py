import colorama
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n🚀 Welcome to the Panaversity Sentence Builder! 🎉\n")

    # Ask for user inputs with styled prompts
    adjective = input(Fore.YELLOW + "👉 Please type an *adjective* and press enter: " + Style.RESET_ALL)
    noun = input(Fore.MAGENTA + "👉 Please type a *noun* and press enter: " + Style.RESET_ALL)
    verb = input(Fore.GREEN + "👉 Please type a *verb* and press enter: " + Style.RESET_ALL)

    # Construct and display the final sentence
    final_sentence = f"{SENTENCE_START} {Fore.BLUE + Style.BRIGHT}{adjective} {Fore.RED + noun} {Fore.GREEN + verb}{Style.RESET_ALL}!"
    
    print("\n✨ Here's your awesome sentence:")
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + final_sentence)
    print(Fore.LIGHTBLUE_EX + "\nThanks for playing with words at Panaversity! 🌟\n")

# Run the program
if __name__ == '__main__':
    main()
