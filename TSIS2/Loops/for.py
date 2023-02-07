"""
Цикл for используется для перебора последовательности  (that is either a list, a tuple, a dictionary, a set, or a string).

Это меньше похоже на ключевое слово for в других языках программирования и работает больше как метод итератора, 
который можно найти в других объектно-ориентированных языках программирования.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  #Цикл for не требует предварительной установки индексирующей переменной.

"""
Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:

Example
Loop through the letters in the word "banana":

"""
for x in "banana":
  print(x)