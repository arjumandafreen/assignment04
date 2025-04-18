Average Calculator
This is a basic Python script that calculates the average of two numbers provided by the user.

📌 Features
Takes two numeric inputs from the user.

Calculates the average using a custom function.

Handles invalid input with a helpful error message.

🧠 How It Works
The user is prompted to enter two numbers.

These values are passed to the find_average() function.

The function returns the average of the two numbers.

The result is printed in a readable format.

If the user enters something that isn't a number, a ValueError is caught and an error message is displayed.

🧪 Example

Enter the first number: 8  
Enter the second number: 4

The average of 8.0 and 4.0 is 6.0
🛠️ How to Run
Make sure you have Python installed.

Save the code in a file, for example average_calculator.py.

Open your terminal or command prompt.

Run the script:


python average_calculator.py
📂 File Structure

average_calculator.py     # Main script with logic and input/output
🧾 Function Breakdown
find_average(a: float, b: float) -> float
Takes two float values.

Returns their average.

main()
Handles user input and output.

Calls find_average() and handles errors.