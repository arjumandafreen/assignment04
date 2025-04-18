from typing import List

def add_many_numbers(numbers: List[int]) -> int:
    """
    Returns the sum of a list of integers.
    
    Parameters:
    numbers (List[int]): A list of integers to sum.

    Returns:
    int: The total sum of the numbers.
    """
    return sum(numbers)

def main():
    # Define a sample list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # Calculate the sum using the defined function
    total = add_many_numbers(numbers)

    # Print the result with a stylish message
    print("=" * 40)
    print("🔢  Summing Numbers Program  🔢")
    print("=" * 40)
    print(f"📋 Numbers: {numbers}")
    print(f"✅ Sum of numbers: {total}")
    print("=" * 40)

if __name__ == '__main__':
    main()
