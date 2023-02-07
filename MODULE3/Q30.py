#Write a Python script to sort (ascending and descending) a dictionary by value.  

d = {'shivam':1,'fellblade':5,'mishra':10}

ls = list(d.items())
ls.sort()
print(ls)

ls = list(d.items())
ls.sort(reverse=True)
print(ls)

dic = dict(ls)
print(dic)