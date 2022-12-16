#Write a Python function to get the largest number, smallest num and sum of all from a list.
#create empty list 

mylist = []

number = int(input('How many numbers: '))

for n in range(number):

    element = int(input('Enter element '))
    mylist.append(element)

print("Largest element in the list is :", max(mylist))

print("Smallest element in the list is :", min(mylist))
