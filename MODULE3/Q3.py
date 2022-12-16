#Differentiate between append() and extend () methods

ls1 = ['name','age','gender']
ls1.append('salary')

#print (ls1)
#above the append just enters the specifies element at the last postion

ls2 = ['cars','bikes','food']
ls1.extend(ls2)
print(ls1)