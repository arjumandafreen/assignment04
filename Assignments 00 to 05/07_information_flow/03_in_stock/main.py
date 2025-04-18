from termcolor import colored
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0
def main():
    fruit = input(colored("Enter a fruit: ", "cyan"))  # changed from yellow to cyan
    stock = num_in_stock(fruit)
    if stock == 0:
        print(colored("This fruit is not in stock.", "magenta"))  # changed from red to magenta
    else:
        print(colored("This fruit is in stock! Here is how many:", "yellow"))  # changed from green to yellow
        print(colored(stock, "green"))  # changed from blue to green
if __name__ == '__main__':
    main()
