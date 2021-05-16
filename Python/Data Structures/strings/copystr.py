str = 'akhil'
copiedstr = str

print(copiedstr)
print(id(str))
print(id(copiedstr))



#DIFF BETWEEN COPY AND CLONE

import copy


a = 'level'
b = copy.copy(a)
   
print(id(a))
print(id(b))
