# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s=input()
list=[]
for i in s:
    list.append(i)
list2=reversed(list)
iterator_list = iter(list)
flag='true'
for i in list:
    c=next(iterator_list)
    if(c!=i):
        flag='false'
if flag=="false":
    print('ne palindrom')
else:
    print("palindrom") 