n=int(input())

def producer(n):
    for i in range(n):
        yield i

def processing(seq,n):
    for i in seq:
        if(i%12==0):
            yield i

def consumer(seq):
    for i in seq:
        print(f"Делиться на 3 и 4: {i}")

prod=producer(n)
proc=processing(prod,n)
con=consumer(proc)