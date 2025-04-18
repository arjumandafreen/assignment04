🔢 Odd or Even Checker (Colorful Edition)
This Python script checks whether numbers from 10 to 19 are odd or even, and prints the result in a colorful format using the termcolor module.

This is a Python program that classifies numbers from 10 to 19 as either **even** or **odd**. The program uses the `termcolor` library to print the results in color for better visual appeal.
🎯 Purpose
A simple program that:

Iterates over a range of numbers

Checks if each number is odd or even

Prints the result using colorful terminal output

🧪 Sample Output
python-repl


10 even
11 odd
12 even
13 odd
...
Output appears in cyan for even numbers and magenta for odd numbers, both in bold for better visibility.

📦 Requirements
Make sure you have termcolor installed:


pip install termcolor
▶️ How to Run
Save the script as odd_even_colored.py and run it using:

bash
Copy
Edit
python odd_even_colored.py
💡 Code Overview
main() function loops from 10 to 19.

is_odd() determines if a number is odd.

termcolor.colored() adds colorful styling to the output.

📁 File Structure
Copy
Edit
odd_even_colored/
├── odd_even_colored.py
└── README.md
✨ Customization
Feel free to:

Change the number range

Switch up the colors

Add emojis for more fun

Enjoy coding with color! 🎨🚀