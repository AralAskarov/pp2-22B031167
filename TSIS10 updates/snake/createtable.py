import psycopg2
conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")
cur=conn.cursor()


cur.execute('''CREATE TABLE snake1
(
    username text

);''')
cur.execute('''CREATE TABLE snake_score2
(
    username text,
    score text,
    level text
);''')


cur.execute('''CREATE TABLE snake_pauze
(
    username text,
    blocks text,
    score text,
    speed text,
    level text,
    black text
);''')
conn.commit()
cur.close()
conn.close()

# cur.execute('''CREATE TABLE PhoneBook 
# (
#     username text PRIMARY KEY,
#     phone varchar(12) PRIMARY KEY,
#     address text NOT NULL
# );''')