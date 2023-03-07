import os
f=r'C:\Users\Admin\Desktop\STATA'
def imen(f):
    print(os.path.exists(f))
    print(os.path.dirname(f))
    print(os.path.basename(f))
imen(f)