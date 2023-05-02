import psycopg2
conn = psycopg2.connect("dbname=suppliers user=postgres password=aral2197")
cur=conn.cursor()

print('write 1 if you want to change username or press 2, if both press 3')
c=input()
if c=='1':
    print('write phone number')
    p=input()
    print('write new username')
    pp=input()
    # UPDATE goods SET price = 150 WHERE num = 2
    sql = """ UPDATE PhoneBook SET username = %s WHERE phone = %s"""
    cur.execute(sql, (pp,p))

if c=='2':
    print('write username ')
    pp=input()
    print('write new phone')
    p=input()
    # UPDATE goods SET price = 150 WHERE num = 2
    sql = """ UPDATE PhoneBook SET phone = %s WHERE username = %s"""
    cur.execute(sql, (p,pp))
if c=='3':
    print('write address')
    add=input()
    print('write new username')
    pnew=input()
    print('write new phone')
    pnewe=input()
    # UPDATE goods SET price = 150 WHERE num = 2
    # sql = """ UPDATE PhoneBook SET username = %s, SET phone = %s WHERE address = %s"""
    sql = """ UPDATE PhoneBook
            SET phone = %s,
            username = %s
            WHERE address = %s """
    cur.execute(sql, (pnewe, pnew, add))
# sql = """ UPDATE PhoneBook
#             SET username = %s
#             WHERE phone = %s"""
# cur.execute(sql, ('asdasdasdas2e21','2'))

# cur.execute(''' UPDATE PhoneBook
#             SET username = 'Arallll'
#             WHERE phone = '242' ''')
conn.commit()

cur.close()
conn.close()