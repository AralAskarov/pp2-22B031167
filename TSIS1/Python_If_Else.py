a = 33
b = 200
if b > a:
  print("b is greater than a")


# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short Hand If
if a > b: print("a is greater than b") # в одну линию

# Short Hand If ... Else
# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")


# AND 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")



# ничего не произойдет
a = 33
b = 200

if b > a:
  pass