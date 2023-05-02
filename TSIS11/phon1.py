import psycopg2
import sys

def search_substring(string, substring):
    if substring in string:
        return True
    else:
        return False


    
try:
        
    conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")
    cur = conn.cursor()
    # cur.execute(command)
    print(" введите паттерн ")
    patt = str(input())
    cur.execute('''SELECT * FROM phonklist;''')
    # for row in cur.fetchall():
    #     print(row)
    for row in cur.fetchall():
        for v in row:
            # b=search_substring(patt,v)
            string = v
            substring = patt

            result = search_substring(string, substring)
            
            if result==True:
                print(row)
    
        # close communication with the PostgreSQL database server
    cur.close()
        # commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()