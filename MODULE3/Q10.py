#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

def values():
    ls = list()
    for i in range(1,30):
        ls.append(i**2)
    print(ls[:5])
    print(ls[-5:])
values()