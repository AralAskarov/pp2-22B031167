import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")
cur=conn.cursor()

print("введите количество юзеров,котороых вы хотите добавить")
c=int(input())
l=[]
for i in range(c):
    user_data = input("введите через пробел ' ': username, phone, address")
    
    user_data = tuple(user_data.split()) # ('Aral', '+77054789999', '12mkr')
    l.append(user_data)
    # sql = """INSERT INTO PhoneBook(username, phone, address) VALUES(%s, %s, %s)"""
    # cur.execute(sql, user_data)
for row in l:
    # sql = """INSERT INTO PhoneBook(username, phone, address) VALUES(%s, %s, %s)"""
    cur.execute("""INSERT INTO PhoneBook(username, phone, address) VALUES(%s, %s, %s)""", row)


conn.commit()

cur.close()
conn.close()