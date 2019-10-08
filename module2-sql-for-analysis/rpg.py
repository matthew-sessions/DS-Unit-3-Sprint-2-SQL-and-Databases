import pandas as pd
import psycopg2
import sqlite3

dbname = 'cucraurh'
user = 'cucraurh'
password = 'K9kz5Sa0QRqbSLyu-jwVoHLkyIEKVX0L'
host = 'salt.db.elephantsql.com'

conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
curs = conn.cursor()


sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()


create_character_table = """
  CREATE TABLE character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
"""

curs.execute(create_character_table)
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
    # print(insert_character)
  curs.execute(insert_character)

curs.close()
conn.commit()
