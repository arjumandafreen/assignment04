from termcolor import colored

def subtract_seven(num):
    num = num - 7
    return num

def main():
    try:
        num = int(input(colored("Enter a number: ", "blue")))  
        num = subtract_seven(num)
        print(colored(f"This should be {num}", "green"))        
    except ValueError:
        print(colored("Invalid input! Please enter a valid integer.", "magenta")) 

if __name__ == '__main__':
    main()
