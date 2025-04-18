import random

def computer_guess(x):
    print("\n\033[92m_____________________________\033[0m\n")
    print("\033[92mWelcome to 'Guess the Number'! 🤖\033[0m")
    print("\033[92mThink of a number, and I'll try to guess it.\033[0m")
    print("\033[92mType 'H' if my guess is too high.\033[0m")
    print("\033[92mType 'L' if my guess is too low.\033[0m")
    print("\033[92mType 'C' if I guessed correctly.\033[0m")
    print("\n\033[92m_____________________________\033[0m\n")
    
    low = 1
    high = x
    guess_count = 0  # Keep track of the number of guesses
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # If only one number is left, it must be the answer!

        feedback = input(f"\033[92mIs {guess} too high (H), too low (L), or correct (C)? \033[0m").lower()

        # Validate user input
        while feedback not in ["h", "l", "c"]:
            feedback = input("\033[92mInvalid input! Please enter H (high), L (low), or C (correct): \033[0m").lower()

        guess_count += 1

        if feedback == "h":
            high = guess - 1  # Reduce the high range
        elif feedback == "l":
            low = guess + 1  # Increase the low range

    responses = [
        "I'm a genius! 🤖",
        "That was easy! 😎",
        "I should work for the FBI! 🚀",
        "Took me a while, but I got it! 😉"
    ]

    print(f"\033[92m🎉 Yay! I guessed your number, {guess}, correctly in {guess_count} attempts! {random.choice(responses)}\033[0m")

    # Ask if the user wants to play again
    play_again = input("\033[92mDo you want to play again? (yes/no): \033[0m").lower()
    if play_again == "yes":
        x = int(input("\033[92mEnter the maximum number I should guess up to: \033[0m"))
        computer_guess(x)
    else:
        print("\033[92mThanks for playing! 🎮\033[0m")


# Start the game
x = int(input("\033[92mEnter the maximum number I should guess up to: \033[0m"))
computer_guess(x)
