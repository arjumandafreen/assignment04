from termcolor import colored

def temperature_converter():
    # 🌟 Stylish Header
    print(colored("\n" + "=" * 60, "light_magenta"))
    print(colored("🔥  Temperature Converter  ❄️".center(60), "light_magenta", attrs=["bold"]))
    print(colored("=" * 60 + "\n", "light_magenta"))

    while True:
        try:
            # 🎯 Prompt user input
            degrees_fahrenheit = float(input(
                colored("🌡️ Enter temperature in Fahrenheit: ", "light_cyan")
            ))

            # 🔄 Convert Fahrenheit to Celsius
            degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

            # ✅ Display result
            print(colored("\n✅ Conversion Successful!", "green", attrs=["bold"]))
            print(colored(f"🌡️ {degrees_fahrenheit:.1f}°F = {degrees_celsius:.2f}°C", "yellow", attrs=["bold"]))

            # 🛑 End message 📫
            print(colored("\n" + "=" * 60, "light_magenta"))
            print(colored("🎉  Thank you for using the Temperature Converter!  🎉".center(60), "light_magenta"))
            print(colored("=" * 60 + "\n", "light_magenta"))
            break

        except ValueError:
            # ❌ Error handling
            print(colored("🚫 Invalid input! Please enter a valid number.\n", "red", attrs=["bold"]))

# 🚀 Run only if executed directly
if __name__ == "__main__":
    temperature_converter()
