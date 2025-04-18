📘 Colorful Divisors Finder
This Python script allows users to input a number and displays all its divisors with colorful output in the terminal using the termcolor library.

🎯 Purpose
A simple terminal-based program that:

Asks the user to enter a number

Finds all divisors of the entered number

Displays the divisors in a colorful, easy-to-read format

🧪 Sample Output
yaml
Copy
Edit
Enter a number: 12

Here are the divisors of 12:
1
2
3
4
6
12
The prompt appears in red, the header in blue, and each divisor in green for better visual clarity.

🛠️ Requirements
You need to install the termcolor module before running the script:

bash
Copy
Edit
pip install termcolor
▶️ How to Run
Save the code in a file (e.g., divisors_colored.py) and run it via terminal:

bash
Copy
Edit
python divisors_colored.py
💡 Code Overview
main() function: Prompts the user for a number.

print_divisors(num): Finds and prints all divisors of num.

Colors:

User input prompt → Red

Output header → Blue

Divisors → Green

📁 Project Structure
Copy
Edit
colorful_divisors/
├── divisors_colored.py
└── README.md
✨ Customization Ideas
Try using different colors for even and odd divisors.

Highlight the number itself differently if it’s a prime.

Add emoji for a more playful feel (e.g., ✅ for each divisor).