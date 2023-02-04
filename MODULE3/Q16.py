#Write a Python program to check whether a list contains a sub list
ls = [78,10,4,34,5,10,9]

sub_list = [78,34,99]

if (set(sub_list).issubset(set(ls))):
    print("it is a sub list of original list")
else:
    print("not the sublist")

