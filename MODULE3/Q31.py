#Write  a  Python  script  to  concatenate  following  dictionaries  to  create  a new one. 
dict1 = {"name":"Shivam","age":25}
dict2 = {"city":"baroda","gender":"male"}
dict3 = {"castle":45}
dict4 = {}
for i in (dict1,dict2,dict3):dict4.update(i)
print(dict4)
