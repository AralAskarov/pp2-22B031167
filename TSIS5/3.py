import re
s="The_word in snake_case: "

res=re.findall("[a-z]+_[a-z]+", s)
print(res)  
s=input()
res=re.findall("[a-z]+_[a-z]+", s) 
print(res) 
