"""
CP1404/CP5632 - Practical
Answer the following questions

1. When will a ValueError occur?

Value Error occurs when the user enters an item that cannot be converted to an integer.

2. When will a ZeroDivisionError occur?

When a user enters 0 as the denominator, a zero division error occurs.
A value divided by zero is not mathematically defined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes, modify the code to explicitly check if the denominator is 0 before attempting the division.
This would prevent the possibility of a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")