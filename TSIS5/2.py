import re
s=input()
k=''
list=[]
for i in s+' ':
    if i!=' ':
        k+=i
    else:
        res=re.search(r'a(bb)|(bbb)',k)
        ress=re.search(r'a(bbbb)',k)

        print(res)
        print(type(res))
        if type(res)!= type(None) and type(ress)==type(None):
           list.append(k)
           k=''
        k=''
        res=''
print(list)
