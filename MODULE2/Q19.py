#Write a Python program to find the first appearance of the substring 
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
#whole 'not'...'poor' substring with 'good'. Return the resulting string. 

def not_poor(str1):
    str_not = str1.find('not')
    str_bad = str1.find('poor')

    if str_bad > str_not:
     str1 = str1.replace(str1[str_not:(str_bad+4)],'good')

    return str1
print(not_poor('The lyrics is not that poor!'))
