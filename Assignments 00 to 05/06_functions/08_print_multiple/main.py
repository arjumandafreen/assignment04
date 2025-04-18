from termcolor import colored

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(colored(message, 'cyan', 'on_magenta'))  # Text color cyan, background magenta

def main():
    message = input(colored("Please type a message: ", "blue", attrs=["bold"]))  # Blue text, bold
    repeats = int(input(colored("Enter a number of times to repeat your message: ", "green", attrs=["underline"])))  # Green text, underlined
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
