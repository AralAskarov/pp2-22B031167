import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")

cur=conn.cursor()

print("print what you have username,phone or address(1,2,3)")
y=input()
if y=='1':
    i=input()
    

    cur.execute('''SELECT * FROM PhoneBook WHERE username=%s; ''', (i,))
# for row in cur.fetchall():
#     print(row)
if y=='2':
    i=input()
    

    cur.execute('''SELECT * FROM PhoneBook WHERE phone=%s; ''', (i,))
if y=='3':
    i=input()
    

    cur.execute('''SELECT * FROM PhoneBook WHERE address=%s; ''', (i,))

# sql = cur.mogrify('''SELECT * FROM book2 WHERE starts_with(title, %s) AND index= %s;''', ("k", 'KZ'))
# print(sql)

# cur.execute(sql)

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()

