import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")

cur=conn.cursor()

print("введите первую букву имени")
a=input()
        

sql = cur.mogrify('''SELECT * FROM PhoneBook WHERE starts_with(username, %s);''', (a,))
print(sql)

cur.execute(sql)

print(cur.fetchall())


print("введите первую цифру номера")
n=input()
sql = cur.mogrify('''SELECT * FROM PhoneBook WHERE starts_with(phone, %s);''', (n,))
print(sql)

cur.execute(sql)

print(cur.fetchall())
conn.commit()

cur.close()
conn.close()

