# Mad Libs Game

# Getting user input
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
food = input("Enter a food item: ")

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Story template with colored text
story = f"""
Once upon a time, {GREEN}{name}{RESET} went to {BLUE}{place}{RESET}. 
There, they saw a {YELLOW}{adjective}{RESET} {MAGENTA}{animal}{RESET} that was {CYAN}{verb}{RESET} happily. 
Surprised, {GREEN}{name}{RESET} decided to feed it some {RED}{food}{RESET}, and they became best friends forever!
"""

# Display the final story
print("\nYour Mad Libs story:\n")
print(story)
