#Write a Python program to read a file line by line and store it into a list
with open("sample.txt") as file:
    list = file.readlines()

print(list)
list = [i.strip() for i in list]
print(list)