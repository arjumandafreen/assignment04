# 📅 Leap Year Checker

def main():
    print("🔍 Leap Year Checker")
    print("-" * 25)

    # Prompt user for the year
    try:
        year = int(input("Please enter a year: "))
    except ValueError:
        print("❌ Invalid input. Please enter a valid year (numbers only).")
        return

    # Determine if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"✅ {year} is a leap year!")
    else:
        print(f"❌ {year} is not a leap year.")

# Run the program
if __name__ == '__main__':
    main()
