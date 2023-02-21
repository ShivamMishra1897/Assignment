#Write a Python program to write a list to a file.  
list = ["red","green","blue","yellow"]
f = open("color.txt","w")
f.writelines(list)
f.close()