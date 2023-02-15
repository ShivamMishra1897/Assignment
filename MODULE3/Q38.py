#Write a Python program to print all unique values in a dictionary. 

d1 = {'shivam':1,'kamil':2,'dhruvin':3,'canon':4,'mridul':5,'shivam':25,'kamil':24}

unique_value = set(val for dic in d1 for val in dic.values())
print(unique_value)
