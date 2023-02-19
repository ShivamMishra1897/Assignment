# Write  a  Python  function  that  checks  whether  a  passed  string  is palindrome or not 

def check_pal(s):
    if(s==s[::-1]):
        print((s), "is a palindrome")
    else:
        print("it is not a palindrome")
s = input("enter the string: ")

print(check_pal(s))