#Write a Python program to copy the contents of a file to another file. 
print("original copy: ")
original_File = input()
print("new copy name: ")
new_File = input()

transfer = open(original_File,"r")
texts = transfer.readlines()
transfer.close()
transfer = open(new_File,"w")
for x in texts:
    transfer.write(x)
transfer.close()

print("!!!!!it got copiied")