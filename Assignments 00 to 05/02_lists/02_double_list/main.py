def double_numbers(numbers: list[int]) -> list[int]:
    """
    Function to double each number in the input list.
    Uses list comprehension for efficiency.
    """
    return [num * 2 for num in numbers]


def main():
    numbers = [1, 2, 3, 4]
    doubled_numbers = double_numbers(numbers)  # Get the doubled list
    print(doubled_numbers)  # Output the result


if __name__ == '__main__':
    main()
