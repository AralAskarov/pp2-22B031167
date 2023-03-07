import re
s = input()
res= re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
print(re.sub('([a-z])([A-Z])', r'\1_\2', res).lower()) #1 и 2 это первая и вторая группа