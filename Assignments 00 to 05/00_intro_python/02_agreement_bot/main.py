from termcolor import colored

def main():
    # 🌟 Stylish header
    print(colored("\n" + "="*60, "light_magenta"))
    print(colored("🐶  What's Your Favorite Animal?  🐱".center(60), "light_magenta", attrs=["bold"]))
    print(colored("="*60 + "\n", "light_magenta"))

    # 🎤 User input
    user_input = input(colored("👉 Enter your favorite animal: ", "light_cyan")).strip().lower()

    # 🎉 Fun response
    print(colored(f"\n💬 My favorite animal is also ", "green") + 
          colored(f"{user_input}!", "yellow", attrs=["bold"]))

    # 🛑 Footer
    print(colored("\n" + "="*60, "light_magenta"))
    print(colored("💖  Thanks for sharing!  💖".center(60), "light_magenta"))
    print(colored("="*60 + "\n", "light_magenta"))

# 🏃‍♂️ Run only if this script is executed directly
if __name__ == '__main__':
    main()
