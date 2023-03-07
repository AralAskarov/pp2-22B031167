import re
s=input()

res=re.search(r'a\w*',s)
if type(res)!=type(None):
    print("string has matches")
    print(res)
else:
    print("0 matches")

