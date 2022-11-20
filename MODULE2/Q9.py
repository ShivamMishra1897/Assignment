#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
def sum(x,y,z):
    if x==y or y==z or x==z:
        sum = 0
    else:
        sum =x+y+z
    return sum
print(sum(1,2,3))
print(sum(1,2,1))
print(sum(1,1,1))
print(sum(1,1,3))
