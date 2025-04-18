AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Prompt the user to type the affirmation
    print(f"Please type the following affirmation: {AFFIRMATION}")

    # Get user's input
    user_feedback = input()
    
    # Keep asking the user until the input matches the affirmation
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print(f"Please type the following affirmation: {AFFIRMATION}")
        user_feedback = input()

    # Acknowledge the correct affirmation
    print("That's right! :)")

# Main entry point
if __name__ == '__main__':
    main()
