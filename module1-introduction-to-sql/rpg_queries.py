import sqlite3 as sql3

conn = sql3.connect('rpg_db.sqlite3')

def get_scalar_result(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()[0]

mage = 'SELECT COUNT (DISTINCT character_ptr_id) AS Mage FROM charactercreator_mage;'
theif = 'SELECT COUNT (DISTINCT character_ptr_id) AS Thief FROM charactercreator_thief;'
cleric = 'SELECT COUNT (DISTINCT character_ptr_id) AS Cleric FROM charactercreator_cleric;'
fighter = 'SELECT COUNT (DISTINCT character_ptr_id) AS Fighter FROM charactercreator_fighter;'
items = 'SELECT count (DISTINCT item_id) FROM charactercreator_character_inventory;'
weapons = 'SELECT count (DISTINCT item_ptr_id) FROM armory_weapon;'

ncharaid = 'SELECT COUNT (DISTINCT character_id) FROM charactercreator_character;'


#test
import pandas as pd

charaitems = 'SELECT character_id AS CharacherID, COUNT(item_id) AS Num_Of_Items FROM charactercreator_character_inventory  GROUP BY character_id;'
SQL_Query = pd.read_sql_query(charaitems, conn)
df = pd.DataFrame(SQL_Query, columns=['CharacherID', 'Num_Of_Items'])

charaweapon = 'WITH weapon_data AS (SELECT armory_weapon.item_ptr_id, charactercreator_character_inventory.character_id FROM armory_weapon INNER JOIN charactercreator_character_inventory ON armory_weapon.item_ptr_id=charactercreator_character_inventory.item_id) SELECT character_id, COUNT (item_ptr_id) AS weapon_count FROM weapon_data GROUP BY character_id;'
SQL_Query2 = pd.read_sql_query(charaweapon, conn)
df2 = pd.DataFrame(SQL_Query2, columns=['character_id', 'weapon_count'])



ncharaid = get_scalar_result(conn, ncharaid)
nchara = get_scalar_result(conn,'SELECT COUNT (DISTINCT name) FROM charactercreator_character;')
mage = get_scalar_result(conn, mage)
theif = get_scalar_result(conn, theif)
cleric = get_scalar_result(conn, cleric)
fighter = get_scalar_result(conn, fighter)
items = get_scalar_result(conn, items)
weapons = get_scalar_result(conn, weapons)

print(f'\nThere are a total of {nchara} unique character names \nand {ncharaid} unique characters\n')
print('The subclasses are divied as follows:\n')
print(f'Theifs: {theif} \nMages: {mage} \nCleric: {cleric}\nFighter: {fighter}')
print(f'For a total of {mage + theif + cleric + fighter} \n')

print(f'There are a total of {items} items.')
print(f'Amongst the items, {weapons} are weapons and {items - weapons} are not.')

print(df.head(20))
print(df2.head(20))
print('')
print(f"The avg num of items each character has is {df.Num_Of_Items.mean()}")
print(f'The ave num of weapons each charachter has is {df2.weapon_count.mean()}')
