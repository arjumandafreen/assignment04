import random
from termcolor import colored

def main():
    try:
        secret_number: int = random.randint(1, 99)
        print(colored("I am thinking of a number between 1 and 99...", "magenta"))
        
        guess = int(input(colored("Enter a guess: ", "cyan")))
        
        while guess != secret_number:
            if guess < secret_number:
                print(colored("Your guess is too low", "light_red"))
            else:
                print(colored("Your guess is too high", "light_blue"))
                
            print()
            guess = int(input(colored("Enter a new guess: ", "cyan")))
            
        print(colored("Congrats! The number was: " + str(secret_number), "light_green"))
    
    except ValueError:
        print(colored("Please enter a valid integer as your guess.", "light_red"))

if __name__ == '__main__':
    main()
