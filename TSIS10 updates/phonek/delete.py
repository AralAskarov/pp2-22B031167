import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")
cur=conn.cursor()
print('write username that you want to delete')
y=input()
# cur.execute('''SELECT username from PhoneBook''')
cur.execute("DELETE FROM PhoneBook WHERE username=%s;",(y,))

conn.commit()

cur.close()
conn.close()