# Write a Python program to find the highest 3 values in a dictionary  
from collections import Counter
dict = {'a': 7, 'e': 4, 'i': 6, 'o': 5, 'u': 25}

k = Counter(dict)

highest  = k.most_common(3)

print("K:V")
for i in highest:
    print(i[0],":",i[1])
