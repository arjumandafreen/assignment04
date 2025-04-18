import random

# Constants
NUM_SIDES = 6

# ANSI Color Codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def roll_dice():
    """🎲 Simulates rolling two dice and prints their total 🎲"""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"{CYAN}🎲 Rolled: {YELLOW}{die1}{CYAN} and {YELLOW}{die2} {MAGENTA}- Total: {GREEN}{BOLD}{total}{RESET}")

def main():
    die1 = 10
    print(f"{MAGENTA}✨ Initial value of 'die1' in main(): {YELLOW}{die1}{RESET}\n")

    print(f"{BOLD}--- Rolling the dice 3 times ---{RESET}\n")
    for i in range(3):
        print(f"{BOLD}👉 Roll {i + 1}:{RESET}")
        roll_dice()
        print()  # Newline for spacing

    print(f"{MAGENTA}🔒 Final value of 'die1' in main() remains unchanged: {YELLOW}{die1}{RESET}")

if __name__ == '__main__':
    print(f"{BOLD}{GREEN}🎉 Welcome to the Colorful Dice Roller! 🎉{RESET}\n")
    main()
    print(f"\n{BOLD}{CYAN}🎯 Thanks for playing! 🎯{RESET}")
