import psycopg2

def create_db():
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="aral2197",
        host="localhost",
        port="5432"
    )
    con.autocommit = True
    cur = con.cursor()
    cur = con.cursor()
    cur.execute("CREATE database firstdb")
    con.close()
create_db()
table = (
    """
    CREATE TABLE profil (
        id SERIAL PRIMARY KEY,
        name text,
        phone text
    )
    """)
connection = psycopg2.connect(    
    database="firstdb",
    user="postgres",
    password="aral2197",
    host="localhost",
    port="5432")
connection.autocommit = True
cur = connection.cursor()
def check(cur,tablename):
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (tablename,))
    return bool(cur.fetchone()[0])
if not check(cur,"profil"):
    cur.execute(table)

connection.close()