#Write a Python program to unzip a list of tuples into individual lists
ls = [(1,5), (65,87),(20,39)]
print(list(zip(*ls)))