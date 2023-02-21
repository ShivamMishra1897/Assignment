#Write a Python program to append text to a file and display the text
new_file = open("new_file","a")
new_file.write("new line")
new_file.close()

new_file = open("new_file","r")
print(new_file.read())
new_file.close()