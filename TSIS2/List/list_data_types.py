#List Items - Data Types

#List items can be of any data type:

#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1,list2,list3)



#A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# <class 'list'>

"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.
"""
thislist = list(('apple', "banana", "cherry")) # note the double round-brackets
print(thislist)