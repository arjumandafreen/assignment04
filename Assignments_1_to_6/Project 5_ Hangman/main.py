import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("\033[95m🎩 Welcome to Hangman! 💀\033[0m")
    
    while attempts > 0:
        print("\n\033[96mWord:\033[0m", display_word(word, guessed_letters))
        guess = input("\033[94mGuess a letter:\033[0m ").lower()

        if guess in guessed_letters:
            print("\033[93mYou already guessed that letter! Try again.\033[0m")
        elif guess in word:
            guessed_letters.add(guess)
            print("\033[92m✅ Correct guess!\033[0m")
        else:
            attempts -= 1
            print(f"\033[91m❌ Wrong guess! {attempts} attempts left.\033[0m")
        
        if set(word) == guessed_letters:
            print(f"\n\033[92m🎉 Congratulations! You guessed the word: {word}\033[0m")
            return

    print(f"\n\033[91m💀 Game Over! The word was: {word}\033[0m")

hangman()
