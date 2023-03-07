n=int(input())
def producer(n):
    for i in range(n+1):
        yield i

def processing(seq,n):
    for i in seq:
        if i%2==0:
            yield i

def consumer(seq):
    for i in seq:
        print(i, end=',')


prod=producer(n)
proc=processing(prod,n)
con=consumer(proc)
    
