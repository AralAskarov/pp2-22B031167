import re
s=input()

    
res=re.sub(r"[ .,]" , ":",s)
print(res)

