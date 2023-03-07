import os
l = ['calc','pp','global','stat']
with open("newfile.txt", "w+") as fff:
    for i in l:
        fff.write(f'{i}\n')
fff = open("newfile.txt", "r")
print(fff.read())