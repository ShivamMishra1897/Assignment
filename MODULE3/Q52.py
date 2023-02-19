#Write a Python program to returns sum of all divisors of a number

num = int(input("enter the number: "))

for i in range(1,num+1):
    if(num%i==0):
        print(i)