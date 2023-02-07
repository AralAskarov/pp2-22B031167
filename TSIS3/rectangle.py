class Shape:
    def __init__(self):
        self.area = 0
    
    
    def __str__(self):
        return f"{self.area}"


class Rectangle(Shape):
    def __init__(self,lengtht,width):
        self.lengtht=lengtht
        self.width=width
    def area(self):
        return int(self.lengtht*self.width)

a = int(input()) 
b = int(input()) 
sus=Rectangle(a,b)
print(sus.area())
