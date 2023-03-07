import re
# s="The_word in snake_case arab: "

# res=re.findall(r'a.+b$', s)
# print(*res)  
# # s=input()
# # res=re.findall("a+b\bw+", s)
# # print(*res)  
import re
import re
s=input()

k=''
list=[]
for i in s+' ':
    if i!=' ':
        k+=i
    else:
        res=re.search(r"a+b$", k)

        print(res)
        print(type(res))
        if type(res)!= type(None):
           list.append(k)
           k=''
        k=''
        res=''
print(list)