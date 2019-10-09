"""
I think it is easier to insert new data into mongo.
I think that mongo makes it more difficult to organize the data,
but it is more forgiving when it comes to creating data. As long as
the insert is a dict it will work.

I think it is easier to sort through the data with SQL becuase
it is tabular.
"""

import sqlite3 as sq
import pymongo

conn = sq.connect('rpg_db.sqlite3')
curs = conn.cursor()

q = 'select * from charactercreator_character'
chara = curs.execute(q)
charali = chara.fetchall()

doc_append = []
for i in charali:
    doc = {'id': i[0]}
    doc['name'] = i[1]
    doc['level'] = i[2]
    doc['exp'] = i[3]
    doc['hp'] = i[4]
    doc['strength'] = i[5]
    doc['intelligence'] = i[6]
    doc['dexterity'] = i[7]
    doc['wisdom'] = i[8]
    doc_append.append(doc)

client = pymongo.MongoClient("mongodb://admin:8Ncg3goAG9vVLA3r@cluster0-shard-00-00-xibmg.mongodb.net:27017,cluster0-shard-00-01-xibmg.mongodb.net:27017,cluster0-shard-00-02-xibmg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db.test.insert_many(doc_append)
