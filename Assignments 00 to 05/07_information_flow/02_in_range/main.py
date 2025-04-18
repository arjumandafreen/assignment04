from termcolor import colored

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    try:
        n = int(input(colored("Enter the number (n): ", "magenta")))           
        low = int(input(colored("Enter the low range: ", "yellow")))         
        high = int(input(colored("Enter the high range: ", "green")))       

        if in_range(n, low, high):
            print(colored(f"{n} is between {low} and {high}.", "magenta")) # changed from green to magenta
        else:
            print(colored(f"{n} is not between {low} and {high}.", "cyan"))# changed from red to cyan
    
    except ValueError:
        print(colored("Please enter valid integers for all inputs.", "yellow")) # changed from red to yellow

if __name__ == '__main__':
    main()
