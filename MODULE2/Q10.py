#Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5

def num(x,y):
    x= int(input("enter the num: "))
    y =int(input("enter the num: "))
    if x==y or (x-y)==5 or (x+y)==5:
        return True
    else:
        return False
res = num(10,10)
print(res)