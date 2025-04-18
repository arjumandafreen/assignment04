def main():
    """
    Prompts the user to enter the quantity of each fruit they want to buy,
    calculates the total cost, and displays it.
    """
    # Price list for available fruits
    fruit_prices = {
        'Apple': 1.5,
        'Durian': 50,
        'Jackfruit': 80,
        'Kiwi': 1,
        'Rambutan': 1.5,
        'Mango': 5
    }

    total_cost = 0.0  # Initialize total cost

    print("Welcome to the Fruit Shop!\n")

    # Ask user for quantity of each fruit
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit}s would you like to buy? ").strip())
                if quantity < 0:
                    print("❗ Please enter a non-negative number.")
                    continue
                total_cost += price * quantity
                break
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number.")

    print("\nThank you for shopping with us!")
    print(f"🛒 Your total bill is: ${total_cost:.2f}")

# Entry point
if __name__ == '__main__':
    main()
