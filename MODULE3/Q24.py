#Write a Python program to reverse a tuple
t = (9, 8, 7, 6, 5)
a = (9,69,78,55,440,34,56)
print(t[::-1])

c = list(a)
c.reverse()
a = tuple(c)
print(a)
