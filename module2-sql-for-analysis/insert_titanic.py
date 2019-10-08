import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')

dbname = 'cucraurh'
user = 'cucraurh'
password = 'K9kz5Sa0QRqbSLyu-jwVoHLkyIEKVX0L'
host = 'salt.db.elephantsql.com'

conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
curs = conn.cursor()

create_table = """
    CREATE TABLE titanic_all (
    survived INT,
    pclass INT,
    name VARCHAR,
    sex VARCHAR(6),
    age FLOAT,
    siblings_spouse INT,
    parent_child INT,
    fare FLOAT
    );
"""

curs.execute(create_table)

for i in df.values:
    if "'" in i[2]:
        i[2] = i[2].replace("'","*")
    titanic_insert = """
        INSERT INTO titanic_all
        (survived, pclass, name, sex, age, siblings_spouse, parent_child, fare)
        VALUES """ + str(tuple(i.tolist())) + ";"
    curs.execute(titanic_insert)

curs.close()
conn.commit()
