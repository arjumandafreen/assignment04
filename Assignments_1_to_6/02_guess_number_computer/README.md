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
🌈 What’s Colored:
CYAN for input prompts

MAGENTA and YELLOW for welcoming visuals

RED for incorrect guesses

GREEN for success

BLUE for number input guidance

Let me know if you’d like a matching README.md file for this too!







You said:
make readme file for it


ChatGPT said:
Sure! Here's a colorful and well-structured README.md file for your "Guess the Number (Computer)" game:

markdown
Copy
Edit
# 🎯 Guess the Number (Computer Edition)

A fun terminal-based number guessing game in Python where **you** try to guess the number the **computer** is thinking of!

---

## 💡 Features

- 🎮 Interactive gameplay
- 🎨 Colorful terminal output using ANSI escape codes
- 💬 Personalized messages using your name
- 🔢 Random number generated each time for fresh fun

---

## 🚀 How to Run the Game

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Open your terminal and navigate to the folder.
4. Run the Python file:

```bash
python guess_number.py
🖼️ Example Gameplay
pgsql
Copy
Edit
Enter your name: Sam

Hello Sam! Welcome to the Guessing Number Game🔢🤔
____________________________
Guess a number between 1 to 100: 50
Sorry Sam, guess again. Too Low!
Guess a number between 1 to 100: 75
Sorry Sam, guess again. Too High!
Guess a number between 1 to 100: 63
Yay congrats Sam! You guessed the number 63 correctly!! 🎉
🎨 Terminal Colors
The script uses ANSI escape codes for colorful output:

🟢 Green – for success

🔴 Red – for wrong guesses

🔵 Blue – for inputs

🟣 Magenta & 🟡 Yellow – for fun UI messages

Note: Colors display best in modern terminals (like VS Code Terminal, macOS Terminal, Linux Shell, or Windows Terminal).
CMD or older PowerShell may not fully support ANSI codes.

📄 License
This project is free and open-source. Feel free to use and customize it!

Made with ❤️ and Python 🐍