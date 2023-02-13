#Write a Python program to get the Fibonacci series of given range.
#F(n) = F(n-1) + F(n-2), where n > 1  for nth number
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, 10):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()
