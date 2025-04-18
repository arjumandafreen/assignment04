from termcolor import colored

def get_name():
    return colored("Arjumand", "magenta", attrs=["bold"])

def main():
    greeting = colored("Howdy", "cyan", attrs=["bold"])
    emoji = colored("😍", "yellow")
    name = get_name()
    border = colored("=" * 30, "green", attrs=["bold"])
    
    print(border)
    print(f"{greeting} {name} {emoji}")
    print(border)

if __name__ == '__main__':
    main()
