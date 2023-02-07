#Write a Python program to convert a list of tuples into a dictionary
ls = [("Name", "Ram"), ("Name", "Pooja"), ("Name", "Sara"), ("Age", 21), ("Gender", "Male")]
dict = {}
for i,j in ls:
    dict.setdefault(i,[]).append(j)
print(dict)