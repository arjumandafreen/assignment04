def generate_even_numbers(count: int) -> list[int]:
    """Generate a list of even numbers up to the given count."""
    return [i * 2 for i in range(count)]

def display_even_numbers(even_numbers: list[int]) -> None:
    """Display even numbers with a neat format."""
    print("Even Numbers:")
    print("-" * 20)
    for num in even_numbers:
        print(f"{num:>2}")  # Right-aligned for a cleaner look

def main() -> None:
    count = 20
    even_numbers = generate_even_numbers(count)
    display_even_numbers(even_numbers)

if __name__ == "__main__":
    main()
