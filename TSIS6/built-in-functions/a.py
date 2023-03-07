n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))


iterator_list = iter(list)  # convert list to iterator
c=int(1)
for i in range(n):
    m=next(iterator_list) # вызывает первый элемент листа
    c=c*m

print(c)
