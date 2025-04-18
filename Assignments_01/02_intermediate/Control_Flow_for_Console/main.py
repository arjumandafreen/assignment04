import random

NUM_ROUNDS = 5

# ANSI escape sequences for text colors
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def main():
    print(f"{YELLOW}Welcome to the High-Low Game!{RESET}")
    print('--------------------------------')

    score = 0
    
    for i in range(NUM_ROUNDS):
        computer_num = random.randint(1,100)
        user_num = random.randint(1,100)

        print(f"{BLUE}Round {i + 1}{RESET}")

        print(f"{GREEN}Your number is {user_num}{RESET}")

        user_input = input(f"{YELLOW}Do you think your number is higher or lower than the computer's?: {RESET}").lower()
        if ((user_num < computer_num) and (user_input == "lower")) or ((user_num > computer_num) and (user_input == "higher")):
            print(f"{GREEN}You were right! The computer's number was {computer_num}{RESET}")
            score += 1
            print(f"{GREEN}Your score is now {score}{RESET}")
        else:
            print(f"{RED}Aww, that's incorrect. The computer's number was {computer_num}{RESET}")
            print(f"{RED}Your score is now {score}{RESET}")
        print(" ")
    
    if score == 5:
        print(f"{GREEN}Wow! You played perfectly!{RESET}")
        print(" ")    
    elif score >= 2:
        print(f"{YELLOW}Good job, you played really well!{RESET}")
        print(" ") 
    else:
        print(f"{RED}Better luck next time!{RESET}")
        print(" ")

if __name__ == "__main__":
    main()
