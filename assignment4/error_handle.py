"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
try:
    fh = open('sampleaa.txt', 'rt')
    line1 = fh.readline()
    line2 = fh.readline()
    line3 = fh.readline()
    print(f"Reading file content:\n Line 1: {line1}\n Line 2: {line2}\n Line 3: {line3}")
    fh.close()
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' does not exist.")