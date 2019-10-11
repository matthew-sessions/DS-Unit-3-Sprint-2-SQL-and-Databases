import sqlite3 as sql3

#function for Stretch
def get_scalar_result(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

conn = sql3.connect('demo_data.sqlite3')
curs = conn.cursor()

creatq = 'create table demo (s VARCHAR, x int, y int);'
curs.execute(creatq)


insertli = ["('g', 3, 9);","('v', 5, 7);","('f', 8, 7);"]
for i in insertli:
    query = """
        insert into demo (s, x, y)
        values""" + i
    curs.execute
curs.close()
conn.commit()

count = 'select count(*) from demo;'
countr = get_scalar_result(conn, count)
print(f'There are {countr[0][0]} rows.')

at5 = 'select count(*) from demo where x >= 5 and y >= 5;'
at5r = get_scalar_result(conn, at5)
print(f'There are {at5r[0][0]} rows that x and y are at least 5.')

unique = 'select count(DISTINCT y) from demo;'
uniquer = get_scalar_result(conn, unique)
print(f'There are {uniquer[0][0]} unique values in column y.')
