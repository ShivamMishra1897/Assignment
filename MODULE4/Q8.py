#Write a Python program to count the number of lines in a text file.
with open("sample.txt","r") as file:
   count = 0
   for line in file:
      if line != "\n":
         count +=1
print(count)