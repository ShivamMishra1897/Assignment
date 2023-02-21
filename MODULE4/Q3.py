#Write a Python program to read first n lines of a file.  
n = int(input("enter single digits integer:"))
filename = "new_file"

with open(filename) as new_file:
    head = [next(new_file) for x in range(n)]

print(head)