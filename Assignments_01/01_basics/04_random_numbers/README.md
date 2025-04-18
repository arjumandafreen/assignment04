
Random Number Generator
Description
This Python script generates a list of 10 random numbers between 1 and 100. The generated numbers are then displayed in colored text (magenta). This script uses the termcolor library to add color to the output in the terminal.

Features:
Generates 10 random numbers.

Displays each random number in magenta color.

Easy to modify the number of random numbers or the range.

Requirements
Python 3.x

termcolor library for colored text.

You can install the required termcolor library using the following command:


pip install termcolor
Usage
Run the script in your terminal:


python random_number_generator.py
The script will output 10 random numbers between 1 and 100 in magenta color.

Example Output

12 57 93 85 67 45 38 82 100 54
All the numbers will be displayed in magenta.

Code Explanation
random.randint(MIN_VALUE, MAX_VALUE): Generates a random number between the specified minimum and maximum values (1 and 100).

termcolor.colored(): Colors the output text in the terminal (magenta in this case).

List Comprehension: Creates a list of random numbers and colors them using a list comprehension.

License
This project is licensed under the MIT License