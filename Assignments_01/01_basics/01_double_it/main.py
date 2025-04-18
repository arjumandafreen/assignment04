from termcolor import colored

def main():
    try:
        num = int(input(colored("Enter a number: ", "magenta")))
        curr_value = num
        while curr_value < 100:
            curr_value = curr_value * 2
            print(colored(curr_value, "green"))
    except ValueError:
        print(colored("Invalid input! Please enter a valid integer.", "magenta"))

if __name__ == '__main__':
    main()
