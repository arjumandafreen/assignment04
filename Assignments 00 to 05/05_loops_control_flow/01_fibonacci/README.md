Fibonacci Sequence Generator
This Python script generates and prints Fibonacci numbers starting from 0 and 1 until the value exceeds a maximum limit (MAX_TERM_VALUE), which is set to 10,000 by default.

Requirements
Python 3.x

How It Works
The script defines two initial terms of the Fibonacci sequence:

curr_term = 0 (The 0th Fibonacci number)

next_term = 1 (The 1st Fibonacci number)

The script then iterates, calculating the next Fibonacci number by adding the previous two terms, and continues this process until the curr_term exceeds the defined maximum value (MAX_TERM_VALUE).

Usage
Clone or download the repository to your local machine.

Run the script:

python fibonacci.py

The script will output Fibonacci numbers, starting from 0, one by one, until the value exceeds the MAX_TERM_VALUE.

Customization
You can change the MAX_TERM_VALUE in the script to any other integer value if you want to adjust the range of Fibonacci numbers generated.

Example Output

0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
License
This project is licensed under the MIT License - see the LICENSE file for details.