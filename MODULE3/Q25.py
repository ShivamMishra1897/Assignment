#Write a Python program to replace last value of tuples in a list.
t = (40,50,60,70,80,90)
l = list(t)
print(type(l))

for i in range(len(l)):
    new_l = list(l[i])
    new_l[-1] = 999
    l[i]=tuple(new_l)
print(t)