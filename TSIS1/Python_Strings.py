# Строки в Python заключаются либо в одинарные, либо в двойные кавычки.
print("Hello")
print('Hello')


# Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



# Strings are Arrays
# Однако в Python нет символьного типа данных, один символ — это просто строка длиной 1.
# Квадратные скобки можно использовать для доступа к элементам строки.
a = "Hello, World!"
print(a[1])


# Looping Through a String  Перебор строки
for x in "banana":
  print(x)


# String Length
a = "Hello, World!"
print(len(a))


# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")