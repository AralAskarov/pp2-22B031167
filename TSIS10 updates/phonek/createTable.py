import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")

cur=conn.cursor()

cur.execute('''CREATE TABLE PhoneBook 
(
    username text PRIMARY KEY,
    phone varchar(12) PRIMARY KEY,
    address text NOT NULL
);''')


conn.commit()

cur.close()
conn.close()