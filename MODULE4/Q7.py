#Write a python program to find the longest words.

sample = open("new_file","r")

words = sample.read().split()
sample.close()

long,max = [],[]

for i in words:
    max.append(i)
    long.append(len(i))

sample=long.index(max(long))
print(max[sample])