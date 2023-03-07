import re
s=input()
k=''
list=[]
for i in s+' ':
    if i!=' ':
        k+=i
    else:
        res=re.search(r'a',k)
        print(res)
        print(type(res))
        if type(res)!= type(None):
           list.append(k)
           k=''
        k=''
        res=''
print(list)
