#write a python a program to calculate the length of a string 
def length(str):
    count = 0
    for char in str:
        count += 1
    return count
print(length('pythoncode'))