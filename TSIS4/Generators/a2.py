def producer():
    for i in range(100):
        yield i

def proccesing(seq):
    for i in seq:
        yield i**2

def consumer(seq):
    for i in seq:
        print(f"proccesed item --{i}")
prod=producer()
proc=proccesing(prod)
consumer(seq=proc)