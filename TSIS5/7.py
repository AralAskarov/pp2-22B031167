import re


s = input()

def lovv66(s):
    pattern = re.findall("[a-z]+",s)
    k = ""
    for i in pattern:
        k+=i[0].upper()+i[1:len(i)]
    return k
print(lovv66(s))