

# 🔢 Sum of Two Numbers (Colorful CLI App)📁 

This is a simple, beginner-friendly Python program that allows users to **enter two numbers** and view their **sum** in a beautifully styled command-line interface using colors and emojis. It uses the `termcolor` module for colorful output and includes **input validation**, stylish headers/footers, and user-friendly prompts.

---

## ✨ Features

- 🎨 Colorful terminal interface
- 👨‍💻 Input validation with error handling
- ✅ Shows sum with bold styling
- 📦 Lightweight and easy to run
- 🤖 Emojis for a fun experience

---

## 📸 Preview

```bash
============================================================
             🔢  SUM OF TWO NUMBERS  🔢              
============================================================

👉 Enter the first number: 10
👉 Enter the second number: 25

🎉 The total sum is: 35

============================================================
             🔚  END OF PROGRAM  🔚               
============================================================
📦 Requirements
This program only requires:

Python 3.x

termcolor library

🔧 Installation
Clone this repository or download the .py file.

Install the required library using pip:

bash
Copy
Edit
pip install termcolor
🚀 Running the Program
You can run the script using any terminal:

bash
Copy
Edit
python sum_colored.py
Replace sum_colored.py with the actual filename you saved.

🧠 How It Works
Prompts the user to input two numbers.

Validates the input to make sure it's an integer.

Adds the numbers and displays the result in a colorful format.

Uses the termcolor module to make CLI interaction more attractive and readable.

🧪 Sample Code Snippet
python
Copy
Edit
value1 = int(input(colored("👉 Enter the first number: ", "light_cyan")))
value2 = int(input(colored("👉 Enter the second number: ", "light_cyan")))
total = value1 + value2
print(colored("🎉 The total sum is: ", "green") + colored(f"{total}", "yellow", attrs=["bold"]))
🤝 Contributing
Pull requests are welcome! If you have a cool idea like adding more operations (subtraction, multiplication, etc.) or making a menu system, feel free to fork and improve it!

📝 License
This project is open source and free to use under the MIT License.

🙋‍♂️ Author
Developed by: [Arjumand Afreen Tabinda]