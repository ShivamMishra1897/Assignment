#Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string. 

str1 = 'apple'
str2 = 'lemon'

str1_new =str2[:2] + str1[2:]
str2_new =str1[:2] + str2[2:]

print('new string is:', str1_new," ",str2_new)