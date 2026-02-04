"""Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
num=51
num_sum=0
for index in range(1,num):
    num_sum = num_sum+index
    print(index)
print(f"Sum of number in the range from 1 to {num-1} is {num_sum}")