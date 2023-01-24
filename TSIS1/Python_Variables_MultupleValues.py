# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Red"
print(x)
print(y)
print(z)
# Python позволяет вам присваивать значения нескольким переменным в одной строке


# One Value to Multiple Variables
x = y = z = 'Banana'
print(x, y, z)


# Unpack a Collection
# Если у вас есть набор значений в виде спискa
# Python позволяет извлекать значения в переменные. Это называется распаковкой.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)