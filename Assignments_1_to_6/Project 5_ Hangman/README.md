🎩 Hangman Game – Python Terminal Edition
This is a simple and fun Hangman game made with Python for the terminal. Guess the hidden word one letter at a time before you run out of attempts!

🎯 Features
Randomly selected words

Input validation with repeat-guess detection

Color-coded terminal output using ANSI escape codes

Emoji feedback for extra fun

Easy-to-read word display

📜 How to Play
Run the game:


python hangman.py
You'll see blanks representing the letters in a randomly selected word.

Type one letter per turn to guess the word.

You have 6 chances to guess wrong before the game ends.

🎨 Terminal Colors

Color	Meaning
🟣 Purple	Welcome message
🔵 Blue	Input prompt
🟢 Green	Correct guess / Win
🔴 Red	Wrong guess / Game Over
🟡 Yellow	Already guessed warning
🔷 Cyan	Word display
💻 Requirements
Python 3.x

Terminal that supports ANSI colors (most modern terminals do)

🗂 File Structure

hangman/
│
├── hangman.py    # Main game code
└── README.md     # Game description
🧪 Sample Output

🎩 Welcome to Hangman! 💀

Word: _ _ _ _ _ _
Guess a letter: p
✅ Correct guess!

Word: p _ _ _ _ _
Guess a letter: z
❌ Wrong guess! 5 attempts left.

...

🎉 Congratulations! You guessed the word: python