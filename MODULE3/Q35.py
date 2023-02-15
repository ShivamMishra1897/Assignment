#Write a Python script to merge two Python dictionaries 

dict_1 = {'name':'shivam','age':'25','salary':500000}
dict_2 = {'name':'ria','age':'25','salary':600000}

dict_3={k:v for i in (dict_1,dict_2) for k,v in i.items()}
print(dict_3)