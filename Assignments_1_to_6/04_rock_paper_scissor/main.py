import random

def play():
    options = ["rock", "paper", "scissors"]
    user_choice = input("\033[94mChoose rock, paper, or scissors:\033[0m ").lower()
    
    if user_choice not in options:
        print("\033[91mInvalid choice! Please select rock, paper, or scissors.\033[0m")
        return play()

    computer_choice = random.choice(options)
    
    print(f"\033[96mYou chose:\033[0m {user_choice}")
    print(f"\033[95mComputer chose:\033[0m {computer_choice}")

    if user_choice == computer_choice:
        print("\033[93mIt's a tie! 🤝\033[0m")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("\033[92mYou win! 🎉\033[0m")
    else:
        print("\033[91mComputer wins! 😢\033[0m")

play()
