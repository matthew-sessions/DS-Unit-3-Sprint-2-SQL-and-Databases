import sqlite3 as sql3

conn = sql3.connect('rpg_db1.sqlite3')

def get_scalar_result(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

mage = 'SELECT * FROM char_items;'
mage = get_scalar_result(conn, mage)
print(mage)
