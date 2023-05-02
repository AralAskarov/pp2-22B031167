import psycopg2


conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")


cur = conn.cursor()

cur.execute("""
    CREATE OR REPLACE FUNCTION insert_user(vname text, vphone text) RETURNS void AS $$
    BEGIN
        IF EXISTS (SELECT * FROM  phonklist WHERE name = vname) THEN
            UPDATE phonklist SET phone = vphone WHERE name = vname;
        ELSE
            INSERT INTO  phonklist (name, phone) VALUES (vname, vphone);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
""")
print('введите имя юзера и номер')
a=input()
b=input()
cur.callproc('insert_user', (a,b))

conn.commit()

cur.close()
conn.close()