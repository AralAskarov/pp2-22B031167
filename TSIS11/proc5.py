
import psycopg2


conn = psycopg2.connect("dbname=aral user=postgres password=aral2197")


cur = conn.cursor()

cur.execute("""
    CREATE OR REPLACE FUNCTION delete_user(vname text, vphone text) RETURNS void AS $$
    BEGIN
        IF vname IS NOT NULL THEN
            DELETE FROM phonklist WHERE name = vname;
        ELSIF vphone IS NOT NULL THEN
            DELETE FROM phonklist WHERE phone = vphone;
        END IF;
    END;
    $$ LANGUAGE plpgsql;
""")

print('введите имя юзера и номер')
a=input()
b=input()
cur.callproc('delete_user', (a,b))

conn.commit()

cur.close()
conn.close()