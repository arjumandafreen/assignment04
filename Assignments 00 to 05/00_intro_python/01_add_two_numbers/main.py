from termcolor import colored

def sum():
    # 🌟 Welcome Title
    print(colored("\n" + "="*60, "light_magenta"))
    print(colored("🔢  SUM OF TWO NUMBERS  🔢".center(60), "light_magenta"))
    print(colored("="*60 + "\n", "light_magenta"))

    # 🔽 First Number Input
    while True:
        try:
            value1 = int(input(colored("👉 Enter the first number: ", "light_cyan")))
            break
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.\n", "red"))

    # 🔽 Second Number Input
    while True:
        try:
            value2 = int(input(colored("👉 Enter the second number: ", "light_cyan")))
            break
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.\n", "red"))

    # ✅ Display Result
    total = value1 + value2
    print(colored("\n🎉 The total sum is: ", "green") + colored(f"{total}\n", "yellow", attrs=["bold"]))

    # 🛑 End Message
    print(colored("="*60, "light_magenta"))
    print(colored("🔚  END OF PROGRAM  🔚".center(60), "light_magenta"))
    print(colored("="*60 + "\n", "light_magenta"))

# 🔁 Run Program
if __name__ == '__main__':
    sum()
