import pandas as pd
import sqlite3 as sql3

df = pd.read_csv('buddymove_holidayiq.csv')
df = df.rename(columns={'User Id': 'User_id'})

conn = sql3.connect('buddymove_holidayiq.sqlite3')
query = 'CREATE TABLE buddy_info (User_Id varchar(12), Sports int, Religious int, Nature int, Theatre int, Shopping int, Picnic int);'

curs = conn.cursor()
curs.execute(query)
curs.close()
conn.commit()

df.to_sql('buddy_info',conn, if_exists='append', index = False)


def get_scalar_result(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def get_scalar_all(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

lenth = 'SELECT COUNT (User_Id) FROM buddy_info;'
lenth = get_scalar_result(conn, lenth)

nature = 'SELECT count(User_Id) FROM buddy_info where Nature >+ 100;'
nature = get_scalar_result(conn, nature)

print(f"The len of the table is {lenth} \n")
print(f"There were {nature} users that had at least 100 for nature. \n")

allavg = 'SELECT avg(Sports), avg(Religious), avg(Nature), avg(Theatre), avg(Shopping), avg(Picnic) FROM buddy_info;'
allavg = get_scalar_all(conn, allavg)

Sports, Religious,Nature, Theatre, Shopping, Picnic = allavg

print(f'Sports has: {Sports}')
print(f'Religious has: {Religious}')
print(f'Nature has: {Nature}')
print(f'Theatre has: {Theatre}')
print(f'Shopping has: {Shopping}')
print(f'Picnic has: {Picnic}')
