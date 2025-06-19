"List exercises"
numbers_list = []


for i in range(5):
    number = int(input("Number: "))
    numbers_list.append(number)

average = sum(numbers_list) / len(numbers_list)

print(f"The first number is {numbers_list[0]}")
print(f"The last number is {numbers_list[-1]}")
print(f"The smallest is {min(numbers_list)}")
print(f"The largest number is {max(numbers_list)}")
print(f'The average of the numbers is {average}')




usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter user name: ")

if name in usernames:
    print("Access granted")
else:
    print("Access denied")