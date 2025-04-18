import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

NUM_SIDES = 6

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n🎲 Welcome to the Magical Dice Roller! 🎲\n")

    # Simulate rolling two dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(Fore.YELLOW + f"🎯 Each dice has {NUM_SIDES} sides.\n")
    
    print(Fore.GREEN + f"🎲 First dice roll:  {Style.BRIGHT}{die1}")
    print(Fore.MAGENTA + f"🎲 Second dice roll: {Style.BRIGHT}{die2}")
    
    print(Fore.BLUE + Style.BRIGHT + f"\n✨ Total of both dice: {total} ✨")

    # Reactions based on the total
    if total == 2:
        print(Fore.RED + "😲 Snake Eyes! Tough luck.")
    elif total == 12:
        print(Fore.GREEN + "🎉 Double sixes! Jackpot!")
    elif total in [7, 11]:
        print(Fore.CYAN + "🍀 Lucky number!")
    else:
        print(Fore.WHITE + "🔁 Roll again and test your luck!")

    print(Fore.LIGHTBLUE_EX + "\nThanks for rolling! 🎉")

if __name__ == '__main__':
    main()
