#Write a Python program to get unique values from a list
list = [78,4,10,4,34,5,10,9]

unique_list=[]
[unique_list.append(x) for x in list if x not in unique_list]

print(unique_list)
