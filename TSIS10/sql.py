import psycopg2

def check(cur,tablename):
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (tablename,))
    return bool(cur.fetchone()[0])
users_score = (
        """
        CREATE TABLE users_score (
            id SERIAL PRIMARY KEY,
            username text NOT NULL,
            score int,
            level int
        )
        """)
users = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username text NOT NULL
        )
        """
        )
delusers = ("""TRUNCATE TABLE users""")
deluserscore = ("""TRUNCATE TABLE users_score""")      
connection = psycopg2.connect(    
        database="snakescore",
        user="postgres",
        password="aral2196",
        host="localhost",
        port="5432")
cur = connection.cursor()
if not check(cur,"users"):
    cur.execute(users)
if not check(cur,"users_score"):   
    cur.execute(users_score)
cur.execute(delusers)
cur.execute(deluserscore)

connection.commit()
cur.close()
connection.close()