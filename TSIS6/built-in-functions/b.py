s=input()
cntlow=int(0)
cntupp=int(0)

for i in s:
    if bool('a'<= i and i <='z')==1:
        cntlow+=1
    else:
        cntupp+=1
print(cntlow,cntupp,sep="\n")

# bool() and len() are built in functions