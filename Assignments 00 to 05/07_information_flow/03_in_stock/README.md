# 🍎 # Fruit Store Inventory Checker 🍏
or Fruit Stock Checker

This Python program allows users to check how many units of a specific fruit are in stock. It uses the `termcolor` library to provide a colorful and user-friendly terminal experience.

## 🚀 Features

- ✅ Check stock levels of fruits: `apple`, `durian`, and `pear`.
- 🎨 Colorized input and output using the `termcolor` library.
- 📦 Returns `0` if the fruit is not in stock.

## 🖥️ How It Works

1. The user is prompted to enter the name of a fruit.
2. The program checks the fruit name against predefined stock values.
3. It displays whether the fruit is in stock and how many are available.

## 📋 Example

```bash
Enter a fruit: pear
This fruit is in stock! Here is how many:
1000

Enter a fruit: banana
This fruit is not in stock.
🎨 Color Coding
Input Prompt: Cyan

In Stock Message: Yellow

Not in Stock Message: Magenta

Stock Number: Green

🛠️ Requirements
Python 3.x

termcolor library

You can install the required library with:


pip install termcolor
📁 File Structure

fruit_stock_checker.py
README.md
📌 Notes
Only apple, durian, and pear have predefined stock values.

Any other fruit will be considered as not in stock.

👩‍💻 Author
Created for educational purposes — feel free to customize it and expand the fruit database!