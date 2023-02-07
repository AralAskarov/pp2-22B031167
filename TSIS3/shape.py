class Shape:
    def __init__(self):
        self.area = 0
    
    
    def __str__(self):
        return f"{self.area}"

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

da=input()
x=Shape()
print(x)

xa=Square(da)
print(xa.lenght)