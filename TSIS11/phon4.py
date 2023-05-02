import psycopg2
import sys

def gran(val1,val2):
    a=0
    for row in cur.fetchall():
        
        a+=1
        # print('a')
        if a>=val1 and a<=val2:
            print(row)


a=0
try:
        
    conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")
    cur = conn.cursor()
    # cur.execute(command)
    cur.execute('''SELECT * FROM phonklist;''')
    for row in cur.fetchall():
        a+=1
        # print (row)
    print( ' выберите два числа от 1 до', a)
    val1=int(input())
    val2=int(input())
    a=0
    cur.execute('''SELECT * FROM phonklist;''')
    gran(val1,val2)
   
    cur.close()
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()





