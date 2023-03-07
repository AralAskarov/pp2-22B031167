import re

s = input("Enter the string: ")
res = re.findall(r"[A-Z][^A-Z]*", s)
print(res)