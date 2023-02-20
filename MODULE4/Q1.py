# Write a Python program to read an entire text file.

new_file = open("new_file","w")
new_file.write("hello world")
new_file.close()

new_file = open("new_file","r")
print(new_file.read())
new_file.close()