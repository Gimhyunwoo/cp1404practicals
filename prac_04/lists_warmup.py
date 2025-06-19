numbers = [3, 1, 4, 1, 5, 9, 2]


# Change the first element of numbers to "ten" (the string, not the number 10).

numbers[0] = "ten"


# Change the last element of numbers to 1
numbers[-1] = 1


#Print all the elements from numbers except the first two (slice)

print(numbers[2:])

#Print whether 9 is an element of numbers

print(9 in numbers)