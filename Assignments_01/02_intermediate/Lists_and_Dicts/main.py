from termcolor import colored

def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(colored(f"Length of the list: {len(fruit_list)}", 'blue', attrs=['underline']))
    fruit_list.append('mango')
    print(colored(f"Updated list: {fruit_list}", 'green', attrs=['underline']))

def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return colored("Index is out of range", 'red', attrs=['underline'])
    return colored(f"Element at index {index}: {lst[index]}", 'white', attrs=['underline'])

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return colored("Index is out of range", 'red', attrs=['underline'])
    lst[index] = new_value
    return colored(f"Updated list: {lst}", 'green', attrs=['underline'])

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return colored("Invalid range", 'red', attrs=['underline'])
    return colored(f"Sliced list: {lst[start:end]}", 'white', attrs=['underline'])

def game():
    lst = ['dog', 'cat', 'bird', 'fish', 'horse']
    while True:
        print(colored("Select operation (access, modify, slice, exit): ", 'blue', attrs=['underline']))
        operation = input().strip().lower()
        if operation == 'access':
            print(colored("Enter index: ", 'blue', attrs=['underline']))
            try:
                index = int(input())
                print(access_element(lst, index))
            except ValueError:
                print(colored("Please enter a valid number", 'red', attrs=['underline']))

        elif operation == 'modify':
            print(colored("Enter index: ", 'blue', attrs=['underline']))
            try:
                index = int(input())
                print(colored("Enter new value: ", 'blue', attrs=['underline']))
                new_value = input().strip()
                print(modify_element(lst, index, new_value))
            except ValueError:
                print(colored("Please enter a valid number", 'red', attrs=['underline']))
        
        elif operation == 'slice':
            print(colored("Enter start index: ", 'blue', attrs=['underline']))
            try:
                start = int(input())
                print(colored("Enter end index: ", 'blue', attrs=['underline']))
                end = int(input())
                print(slice_list(lst, start, end))
            except ValueError:
                print(colored("Please enter a valid number", 'red', attrs=['underline']))
        
        elif operation == 'exit':
            break
        else:
            print(colored("Invalid operation. Please choose again.", 'red', attrs=['underline']))

if __name__ == '__main__':
    main()
    game()
