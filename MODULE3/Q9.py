#Write a Python function that takes two lists and returns true if they have at least one common member

list1 = []
list2 = []

res = False
def common(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                res = True
                return res
print(common([1,3,3,7],[9,8,8,7]))
print(common([7,8,2,6],[1,5,3,4]))