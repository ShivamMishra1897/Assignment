#Write a Python program to count the occurrences of each word in a given sentence 

str = 'going for a morning run because todays weather is very pleasent for a run'
word ='run'

count = 0
a=str.split(' ')
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print('count is:')
print(count)