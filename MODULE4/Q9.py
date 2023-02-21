#Write a Python program to count the frequency of words in a file.

word = input("word to be searched:")
x = 0
with open("sample.txt","r") as file:
    for line in file:
        words = line.split()
        for i in words:
            if(i==word):
                x=x+1
print(x)