from termcolor import colored

def print_divisors(num: int):
    print(colored(f"Here are the divisors of {num}:", "blue"))
    for i in range(1, num + 1):
        if num % i == 0:
            print(colored(i, "green"))

def main():
    num = int(input(colored("Enter a number: ", "red")))
    print_divisors(num)

if __name__ == '__main__':
    main()
