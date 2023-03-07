import math
a=int(input("write number of sides: "))
b=int(input("write a "))

t = math.tan(math.radians(180/a))
area = (math.pow(b,2)*a*0.25)/t
print(area)