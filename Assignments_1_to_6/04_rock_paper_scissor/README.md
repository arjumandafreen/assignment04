Rock, Paper, Scissors - Python Terminal Game
This is a simple and fun Rock, Paper, Scissors game created in Python. The user plays against the computer in the terminal. The game uses random choices for the computer and supports colorful output for a better experience.

🚀 Features
User-friendly prompts

Case-insensitive input

Input validation

Colorful terminal output (using ANSI escape sequences)

Emojis for extra fun

📋 How to Play
Run the Python file:

nginx
Copy
Edit
python rock_paper_scissors.py
When prompted, enter your choice:

nginx
Copy
Edit
rock
paper
scissors
The computer will randomly choose one of the options.

The winner is displayed with color-coded results:

🟢 Green: You win

🔴 Red: Computer wins

🟡 Yellow: Tie

🧠 Game Logic
Rock beats Scissors

Scissors beats Paper

Paper beats Rock

If both choose the same, it's a tie.

🖥️ Requirements
Python 3.x

Terminal or command line that supports ANSI escape sequences (most do, including VS Code, macOS/Linux terminal, and modern Windows)

📦 File Structure

rock_paper_scissors/
│
├── rock_paper_scissors.py   # Main game file
└── README.md                # Project information
📌 Example Output

Choose rock, paper, or scissors: rock
You chose: rock
Computer chose: scissors
You win! 🎉 