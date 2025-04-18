from termcolor import colored
def get_user_info():
    first_name = input(colored("What is your first name?: ", "green"))         
    last_name = input(colored("What is your last name?: ", "green"))          
    email_address = input(colored("What is your email address?: ", "green"))   
    return first_name, last_name, email_address

def main():
    user_data = get_user_info()
    print(colored(f"Received the following user data: {user_data}", "magenta")) # changed from yellow to magenta

if __name__ == "__main__":
    main()
