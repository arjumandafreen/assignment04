def collect_numbers():
    """
    Collects integers from the user until a blank line is entered.
    Returns a list of the entered integers.
    """
    numbers = []
    while True:
        value = input("Enter a number: ")
        if value == "":
            break
        numbers.append(int(value))
    return numbers

def count_frequencies(numbers):
    """
    Returns a dictionary with the frequency count of each number in the list.
    """
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return frequency

def display_frequencies(frequency_dict):
    """
    Displays how many times each number appears, sorted by number.
    """
    for number in sorted(frequency_dict):
        print(f"{number} appears {frequency_dict[number]} times.")

def run():
    """
    Runs the number frequency counter program.
    """
    numbers = collect_numbers()
    frequencies = count_frequencies(numbers)
    display_frequencies(frequencies)

if __name__ == '__main__':
    run()
