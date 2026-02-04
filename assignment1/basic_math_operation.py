"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
    1.  Takes two numbers as input from the user.
    2.  Performs the basic mathematical operations on these two numbers:
        o	Addition
        o	Subtraction
        o	Multiplication
        o	Division
    3.  Displays the results of each operation on the screen.
"""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

#Addition
addition=num1+num2
print(f"Addtion of {num1} and {num2} is: {addition}")

#Subtraction
subtraction=num1-num2
print(f"Subtraction of {num1} and {num2} is: {subtraction}")

#Multiplication
multiplication=num1*num2
print(f"Multiplication of {num1} and {num2} is: {multiplication}")

#Division
division=num1/num2
print(f"Division of {num1} and {num2} is: {division}")
