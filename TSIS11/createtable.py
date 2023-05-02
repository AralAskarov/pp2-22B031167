import psycopg2


def create_tables():
    command= (
        """ CREATE TABLE phonklist (
                name text,
                surname text,
                phone text PRIMARY KEY
                )
        """)
    try:
            
        conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")
        cur = conn.cursor()
        # cur.execute(command)

        cur.execute('''INSERT INTO phonklist
        VALUES
        ('Aral', 'Askarov', '+77054781058'),
        ('Danial', 'Ahmet', '+776054545'),
        ('Ramzan', 'Kadirov', '+00000000001'),
        ('German', 'Gesse', '+77054783884');''')
            # close communication with the PostgreSQL database server
        cur.close()
            # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()


    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_tables()