# 1st Video

"""
1. random.randint
--> "random" is module and "randint" is as function
--> "random" is like a python file that has random numbers in it.
    "randint" is a function that pulls out specific(integers) numbers out of module called "random"

ex:
1. import math
   math.pi
   --> everthing in math is accessible
2. from math import pi
   pi
   --> only pi is accessible
3. from math import *
   pi
   --> everything in math is accessible and module name is not needed.
"""

# Do this now

""" 
Write a program that asks the user for a length, then generates a random
width between 1 and the length, and prints this and the are of a rectangle of length x width.
Don't forget the import. 

Ex) Length: 12 
    Area of 12 X 4 is 48
"""

# import random
#
# length = int(input("What is your length? "))
# width = random.randint(1,length) # 기억하기!! random.randint 뒤에 괄호 안에 argument 들어갈 수 있음
# area = length * width
#
# print (f"length: {length}")
# print (f"Area of {length} X {width} is {area} ")

# Key Take Out
# random.randint 뒤에 argument 최소값 최대값 넣는 방법
# f string 사용법
# input 함수에 int 먼저옴

# 2nd video

"""
"Parameter" is what we call the variable inside the function that is 
assigned the value of an "argument" when the function is called. 

ex: 
def print_line(length):
    print ("-" * length)
    
print_line (10)
"""

# Do This Now

"""def print_grid(number_of_rows, number_of_columns):

# complete this function to print a grid of *s, like:

print_grid(3, 7)
*******
*******
*******
"""

# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_rows):
#         print("*" * number_of_columns)

# print_grid(3,7)

# Key Take Out
# for 변수 in 반복 가능한 객체:
#   반복할 코드

# 3rd Video

# def get_limits():
#     low = int(input("Low: "))
#     high = int(input("High: "))
#     return low, high
#
# def run_test():
#     low, high = get_limits()
#     print(low,high)
#     print(type(low))

# def main ():
#     print("Menu: ")
#     choice = input(">").upper()
#     while choice != "Q":
#         if choice == "p":
#             pass
#         elif choice == "G":
#             pass
#         elif choice == "S":
#             pass
#         else:
#             print("Invalid Input")
#         print("Menu: ")
#         choice = input(">").upper()
#     print("Farewell")

# def print_line(length=20, pen ='*'):
#     print(pen*length)
#
# print_line(10,'!')
# print_line(5)
# print_line()

