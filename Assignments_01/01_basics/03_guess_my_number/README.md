Number Guessing Game
Description
This is a simple number guessing game where the program picks a secret number between 1 and 99, and you have to guess it! The game will give you hints if your guess is too low or too high, and the font colors will change based on the feedback provided.

Features:
The game will generate a random number between 1 and 99.

It will give feedback about whether your guess is too low or too high.

The game will congratulate you when you guess correctly.

Requirements
Python 3.x

termcolor library for colored text.

You can install the required termcolor library using the following command:


pip install termcolor
Usage
Run the script in your terminal:


python number_guessing_game.py
The game will ask you to input a guess between 1 and 99.

If your guess is too low or too high, the program will display feedback in colored text.

Once you guess the correct number, the game will congratulate you and display the secret number.

Example Output
bash
Copy
Edit
I am thinking of a number between 1 and 99...
Enter a guess: 50
Your guess is too high

Enter a new guess: 30
Your guess is too low

Enter a new guess: 40
Congrats! The number was: 40
Code Explanation
random.randint(1, 99): Generates a random number between 1 and 99.

termcolor.colored(): Adds color to the text output in the terminal.

Exception Handling: If the user inputs an invalid number (non-integer), the program will ask the user to enter a valid integer.

Color Scheme Used
Intro message: Magenta

Input prompts: Cyan

Too low feedback: Light Red

Too high feedback: Light Blue

Success message: Light Green

Error message: Light Red

License
This project is licensed under the MIT License.