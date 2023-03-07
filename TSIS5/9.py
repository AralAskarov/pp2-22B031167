import re

s = input("Enter ")
res = re.findall(r"[A-Z][^A-Z]*", s)
print(*res)


