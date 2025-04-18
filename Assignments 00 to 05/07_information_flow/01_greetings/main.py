from termcolor import colored

def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input(colored("What's your name? ", "green"))  
    print(colored(greet(name), "magenta"))                

if __name__ == '__main__':
    main()
