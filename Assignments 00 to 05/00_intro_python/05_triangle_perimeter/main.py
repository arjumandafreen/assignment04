from termcolor import colored, cprint
import pyfiglet

def TrianglePerimeter():
    # Beautiful heading
    ascii_banner = pyfiglet.figlet_format("Triangle Perimeter")
    cprint(ascii_banner, "cyan")

    # Function to get side length with colorful prompt and error handling
    def get_side_input(side_number):
        while True:
            try:
                value = float(input(colored(f"🔹 Enter the length of side {side_number}: ", "yellow")))
                return value
            except ValueError:
                cprint("❌ Please enter a valid number!", "red")

    # Collecting the sides
    side1 = get_side_input(1)
    side2 = get_side_input(2)
    side3 = get_side_input(3)

    # Calculating perimeter
    perimeter = side1 + side2 + side3

    # Displaying result
    cprint("\n✅ Calculation complete!", "green")
    cprint(f"The perimeter of the triangle is: {perimeter}", "magenta", attrs=["bold"])

if __name__ == '__main__':
    TrianglePerimeter()
