#Write a Python program to calculate the area of a trapezoid  
#formula - [a+b]*h/2 where a,b are the base and h is distance bet two parallel

a = float(input("enter the 1st base of a trapezoid: "))
b = float(input("enter the 2nd base of a trapezoid "))

h = float(input("enter the hieght: "))
area = (a+b)*(h/2)
print(area)