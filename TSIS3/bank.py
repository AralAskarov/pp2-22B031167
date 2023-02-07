class bank: 
    def __init__(self, owner, balance = 0): 
        self.owner = owner 
        self.balance = balance    
    def __str__(self): 
        return f"{self.owner} have: {self.balance}"
    def deposit(self, deposit): 
        a=int(self.balance)
        d=int(deposit)
        a = int(a + d)
        print("Your current balance is ")
        print(a) 
    
p = bank("Aral") 
print(p) 
print("внесите депозит")
s=input()
p.deposit(s) 
