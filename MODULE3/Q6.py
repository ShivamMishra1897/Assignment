#Write a Python program to count the number of strings where the string length is 2
#or more and the first and last character are same from a given list of strings. 

def compare(words):
    ctr = 0
    for i in words:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+=1
    return ctr

print(compare(['cars','bike','ctfc',"2213"]))

