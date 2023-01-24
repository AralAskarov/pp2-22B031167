# Переменные, созданные вне функции, называются глобальными переменными
x = 'krutoi'

def myfun():
    print('python ' + x)

myfun()
print('\n')


# example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print('\n')

"""
Обычно, когда вы создаете переменную внутри функции, 
эта переменная является локальной и может использоваться только внутри этой функции.

Чтобы создать глобальную переменную внутри функции, вы можете использовать ключевое слово global.
"""

def myfunction():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
