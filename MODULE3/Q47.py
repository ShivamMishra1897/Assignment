#Write a Python program to read a random line from a file.

file1 = open("MyFile.txt","w")
line_1 =["this is a sample example for python file question \n","multiple line examples \n"]
line_2 =("hello world")

file1.writelines(line_1)
file1.write(line_2)
file1.close()

file1 = open("MyFile.txt","r")
print(file1.read())
file1.close()