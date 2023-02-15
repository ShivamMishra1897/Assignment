# Write  a  Python  script  to  check  if  a  given  key  already  exists  in  a dictionary.

dict = {'physics':1,'maths':2,'python':3,'biology':4,'astrophysics':5}

print("dictionary:", dict)

check="english"
if check in dict:
    print(check,"present")
else:
    print(check,"absent")