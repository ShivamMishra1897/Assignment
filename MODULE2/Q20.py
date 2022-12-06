#Write a Python function that takes a list of words and returns the length 
#of the longest one. 

def string(word):
    wordlen = []
    for n in word:
        wordlen.append((len(n),n))
    wordlen.sort()
    return wordlen[-1][0], wordlen[-1][1]
result = string(["Python", "apple", "lemonade"])
print("\n Longest word: ",result[1])
print("Length of the longest word: ",result[0])
