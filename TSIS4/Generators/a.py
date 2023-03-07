n=int(input())
def producer():
    for i in range(n):
        yield i

def proccesing(seq,n):
    for i in seq:
        if i**2<n:
            yield i**2

def consumer(seq):
    for i in seq:
        print(f"proccesed item --{i}")

prod=producer()
proc=proccesing(prod,n)
# for i in prod:
#     print(i)

# for i in proc:
#     print(i)
consumer(proc)