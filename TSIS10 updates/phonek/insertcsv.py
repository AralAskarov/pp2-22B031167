import psycopg2
import csv

conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")
cur=conn.cursor()

with open("data2.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('username','phone','address')
    )
    
user_data=[
    ['daniaal33','333','323232'],
    ['ddaan23','23','3232'],
    ['kaif33','1','23']
]

for user in user_data:
    with open('data2.csv','a') as file: #  flag a - append
        writer = csv.writer(file)
        writer.writerow(
        # [name1,name2]
        
        user
        )

fille=open('data2.csv','r')
for line in fille:
    user_data = line
    # for i in user_data:
    #      if i==',':
    #           user_data[i]=' '
    print(user_data)
    # print(type(user_data))
    # user_data = tuple(user_data.split(","))
    user_data = tuple(user_data.split(','))
    print(user_data)
    if user_data!=('\n',) and user_data!=('username', 'phone', 'address\n'):
        sql = """INSERT INTO PhoneBook(username, phone, address) VALUES(%s, %s, %s)"""
        cur.execute(sql, user_data)






conn.commit()

cur.close()
conn.close()