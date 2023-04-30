import psycopg2
import csv
file = open("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis10\\First\\PhoneList.csv", "r")
bdata = list(csv.reader(file, delimiter=";"))
data = [tuple(row) for row in bdata]
lastnone = len(data) - 1
data.pop(lastnone)
file.close()

def print_table():  
      connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
      with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
      for row in rec:
        print("ID ",row[0])
        print("Name: ",row[1])
        print("Phone: ",row[2])
def lastid():
    l = []
    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        l.append(int(row[0]))
    return max(l,default=0)
def retid(name):

    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        if row[1] == str(name):
            return row[0]
def retidl(namelist):
    ln = []
    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        for name in namelist:
            if row[1] == str(name):
                ln.append(row[0])
    return ln
def deleteData(id):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_delete_query = """Delete from profil where id = %s""" 
        cursor.execute(sql_delete_query, id,)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def bulkInsert(records):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO profil (id, name, phone) VALUES (%s,%s,%s) """

        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into profile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into profil table {}".format(error))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def CheckN(name):
    conn = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT id FROM profil WHERE name = %s", (name,))
    return cur.fetchone() is not None
def Check(ID):
    conn = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT id FROM profil WHERE id = %s", (ID,))
    return cur.fetchone() is not None
def update(records):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_update_query = """ UPDATE profil SET  name = %s, phone = %s WHERE id = %s;
                            """
        result = cursor.executemany(sql_update_query, records)
        connection.commit()
        print(cursor.rowcount, "Record updated successfully into profil table")

    except (Exception, psycopg2.Error) as error:
        print("Failed updateing record into profil table {}".format(error))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

print(" Изначальная таблица : ")
print_table()
print(" Если хотите загрузить через csv напишите 1 или через терминал напишите 2 ,если хотите удалять данные через id пишите 3 через имя 4: ")
re = str(input())
rdata = []

if re == "1":
    bulkInsert(data)
elif re == "2":
    rdata = []
    upd = []
    rdatar = []
    temp = []
    s = ""
    print("введите число строк :")
    n = int(input())
    print("Вводите данные через пробел (без id):")
    for i in range(n):  
        r = str(input()) + " "
        for i in r:
            if i != " ":
                s+=str(i)
            else:
                temp.append(s)
                s = ""
        rdata.append(tuple(temp))
        temp = []
    ID = lastid() + 1
    for i in rdata:
        if CheckN(i[0]):
            upd.append((i[0],i[1],retid(i[0])))
        else :
            rdatar.append((ID,i[0],i[1]))
            ID += 1
    update(upd)
    bulkInsert(rdatar)
    
elif re == "3":
    print("Введите через пробел id шки : ")
    f = str(input())
    nr = f.split() 
    for i in nr:
        deleteData(i)
elif re == "4":
    print("Введите через пробел имена : ")
    x = str(input())
    namelist = x.split()
    lnm = retidl(namelist)
    for i in lnm:
        deleteData(str(i))

    