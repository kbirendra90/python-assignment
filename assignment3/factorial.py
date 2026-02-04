from math import factorial
"""
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""
n = int(input("Enter a number: "))
def num_fact(num):
    # with recursion
    if num == 1:
        return 1
    else:
        num_factor = num * num_fact(num-1)
        return num_factor

    # with loop
    """    
    for index in range(1, num + 1):
        print(index)
        factorial *= index
    while num > 1:
        factorial *= num
        num -= 1
    """
print(num_fact(n))