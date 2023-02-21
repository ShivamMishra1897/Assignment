#Write a Python program to read a file line by line store it into a variable
file = open("sample.txt","r")
str = ""
for i in range(0,50):
    str = str + file.read(i)

print(str)