"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
#write
write_content = str(input("Enter text to write to the file: "))
with open("output.txt", 'w') as fhw:
    fhw.write(write_content)
print(f"Data successfully written to the file {fhw.name}")

#append
append_content = str(input("Enter additional text to append: "))
with open("output.txt",'a') as fha:
    fha.write("\n" + append_content)
print(f"Data successfully appended to the file {fha.name}")

#read
with open("output.txt",'r') as fhr:
    final_content = fhr.read()
print(f"Final content of {fhr.name} : \n {final_content}")
fhr.close()