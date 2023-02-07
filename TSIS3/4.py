import math

class Point():
    def __init__(self,x,x1):
        self.x=x
        self.x1=x1
        self.final=x
    def show(self):
        print("you are here", self.final)
    def move(self):
        self.final=int(self.x1)
    def dist(self):
        p=self.x
        w=self.x1
        print(w-p)


print("first write initial coor x ")
x=int(input())
print(" write distance to move")
x2=int(input())
aral=Point(x,x2)
aral.show()
print("moving...")
aral.move()
aral.show()
print("dist between 2 points:")
aral.dist()