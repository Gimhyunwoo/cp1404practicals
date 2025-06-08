" name.txt "
name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name = file.read().strip()
file.close()


print(f"Hi {name}!")

"numbers.txt."

with open("numbers.txt",'r') as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())

    result = number1 + number2

    print(f'Sum of the first two numbers is {result}.')

with open("numbers.txt",'r') as file:

    total = 0

    for line in file:
        total += int(line.strip())

    print(f'The total of all numbers is: {total}')

