#Write a Python program to get the Factorial number of given number.
#n! = (n)*(n-1)*(n-2)*...*3*2*1
print("Enter the Number: ")
num = int(input())
fact = 1
i = 1
while i<=num:
    fact = fact*i
    i = i+1
print('\nfactorial = ', fact)