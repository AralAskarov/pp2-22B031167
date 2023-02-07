thistuple = ("apple",)
print(type(thistuple))


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))\


# <class 'tuple'>
# <class 'str'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)