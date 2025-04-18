ADULT_AGE = 18  # Minimum adult age in the U.S.

def is_adult(age: int) -> bool:
    return age >= ADULT_AGE

def main():
    try:
        age = int(input("\nHow old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("\nInvalid input! Please enter a valid number for age.\n")

if __name__ == '__main__':
    main()
