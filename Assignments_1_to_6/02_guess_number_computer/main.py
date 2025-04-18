# Guess the number (computer)

import random

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

username = input(f"{CYAN}Enter your name: {RESET}")

print(f"\n{MAGENTA}Hello {username}! Welcome to the Guessing Number Game🔢🤔{RESET}\n")
print(f"{YELLOW}____________________________{RESET}")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"{BLUE}Guess a number between 1 to {x}: {RESET}"))
        if guess < random_number:
            print(f"{RED}Sorry {username}, guess again. Too Low!{RESET}")
        elif guess > random_number:
            print(f"{RED}Sorry {username}, guess again. Too High!{RESET}")

    print(f"{GREEN}Yay congrats {username}! You guessed the number {random_number} correctly!! 🎉{RESET}")      

guess(100)
