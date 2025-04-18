from termcolor import colored

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(colored(f'{i} odd', 'magenta', attrs=['bold']))
        else:
            print(colored(f'{i} even', 'cyan', attrs=['bold']))

def is_odd(value: int):
    remainder = value % 2
    return remainder == 1

if __name__ == '__main__':
    main()
