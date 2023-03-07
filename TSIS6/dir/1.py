import os
f=r'C:\Users\Admin\Desktop\STATA'

fname=os.listdir(f)
for i in fname:
    c=os.path.join(f,i) # соединяет пути
    if os.path.isdir(c): # является ли путь директорией.
        print(f'DIR: {i}') 
    if os.path.isfile(c): # является ли путь файлом.
        print(f'file: {i}')