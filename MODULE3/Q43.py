#Write  a  Python  function  to  calculate  the  factorial  of  a  number  (a nonnegative integer)  

def factorial(n):

    if n == 1:
        return 1
    else:
        return(n*factorial(n-1))

num = int(input('enter the num: '))
res = factorial(num)
print(('factorial of', num , 'is' , res))