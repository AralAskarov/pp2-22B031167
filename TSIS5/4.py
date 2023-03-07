import re
s="The_word in snake_case: "

res=re.findall("[A-Z]+[a-z]\w+", s)
print(*res)  
s=input()
res=re.findall("[A-Z]+[a-z]\w+", s)
print(*res)  
