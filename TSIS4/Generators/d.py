a=int(input())
b=int(input())

def producer(a,b):
    for i in range(a,b):
        yield i

def processing(seq,a,b):
    for i in seq:
        yield i**2

def consumer(seq):
    for i in seq:
        print(f"Квадраты чисел от а до б: {i}")

prod=producer(a,b)
proc=processing(prod,a,b)
con=consumer(proc)


print("ответ без генератора: ")
for i in range(a,b):
    print(i**2)