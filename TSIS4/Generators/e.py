n=int(input())
def producer(n):
    for i in reversed(range(0,n+1)):
        yield i

def processing(seq,n):
    for i in seq:
        yield i

def consumer(seq):
    for i in seq:
        print(i)


prod=producer(n)
proc=processing(prod,n)
con=consumer(proc)