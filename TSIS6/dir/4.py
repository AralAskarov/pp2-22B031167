import os
f=open("demofilee.txt")
text=f.read()
cnt = 0
text1=text.split("\n") #стринг в лист
for i in text1:
        cnt += 1   
print(cnt) 