# 🎓 Voting Age Checker for Different Countries

# Constants for minimum voting age
VOTING_AGE_PETURKSBOUIPO = 16
VOTING_AGE_STANLAU = 25
VOTING_AGE_MAYENGUA = 48

def main():
    print("🔍 Voting Eligibility Checker")
    print("-" * 35)

    # Get user input
    try:
        user_age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number for age.")
        return

    # Check eligibility for each country
    check_voting_eligibility("Peturksbouipo", user_age, VOTING_AGE_PETURKSBOUIPO)
    check_voting_eligibility("Stanlau", user_age, VOTING_AGE_STANLAU)
    check_voting_eligibility("Mayengua", user_age, VOTING_AGE_MAYENGUA)

def check_voting_eligibility(country: str, age: int, voting_age: int):
    if age >= voting_age:
        print(f"✅ You can vote in {country} (Minimum age: {voting_age}).")
    else:
        print(f"❌ You cannot vote in {country} (Minimum age: {voting_age}).")

if __name__ == "__main__":
    main()
