class String:
    def __init__(self):
        self.low=""
        self.up=""
    def printin(self):
        self.low=input()
        # self.up=self.low
    def upper(self):
        x=self.low
        self.up=x.upper()
    
xa=String()
xa.printin()
print(xa.low)
xa.upper()
print(xa.up)