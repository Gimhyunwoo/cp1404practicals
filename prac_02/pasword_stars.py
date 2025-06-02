"""
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.
"""

MIN_LENGTH = 8

def main ():
    password = get_password()
    while len(password) < MIN_LENGTH:
       print("Invalid length of password. Try again ")
       password = get_password()

    print_asterisk(password)


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("What is your password?")
    return password


main()

