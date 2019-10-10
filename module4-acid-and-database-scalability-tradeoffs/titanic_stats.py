import psycopg2


dbname = 'cucraurh'
user = 'cucraurh'
password = '4zbpieIX4PQOp632A8t8BM4iaXpaWGH8'
host = 'salt.db.elephantsql.com'

conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
curs = conn.cursor()


def get_data(cursdata,query):
  cursdata.execute(query)
  return(cursdata.fetchall())

query = 'select count(survived) from titanic_all2 group by survived;'
surv = get_data(curs, query)
print('-------------------')
print(f"{surv[0][0]} died and {surv[1][0]} survived \n")

qurclass = 'select distinct(pclass), count(pclass) from titanic_all2 group by pclass;'

classsur = get_data(curs, qurclass)
for i in classsur:
  print(f"in class {i[0]} there were {i[1]} passengers")

print('')
print('-------------------')
pcsq = 'select distinct(pclass), count(pclass) from titanic_all2 where survived = 0 group by pclass;'
pcs = get_data(curs,pcsq)

pcdq = 'select distinct(pclass), count(pclass) from titanic_all2 where survived = 1 group by pclass;'
pcd = get_data(curs, pcdq)

for i in range(len(pcd)):
  print(f"in class {pcd[i][0]}: {pcs[i][1]}  passengers survied and {pcd[i][1]} did not.")

print('')
print('-------------------')
agesq = 'select survived, avg(age) from titanic_all2 group by survived;'
ages = get_data(curs, agesq)
print(f'The average age of survivors was {ages[1][1]} \n and non survivors was {ages[0][1]} \n')

fareq = 'select pclass, avg(fare) from titanic_all2 group by pclass order by pclass;'
fare = get_data(curs, fareq)
for i in fare:
    print(f'IN {i[0]} class the average fare was {i[1]}')
print('')
print('-------------------')
fcsq = 'select pclass, survived, avg(fare) from titanic_all2 group by pclass, survived order by pclass, survived;'
fcs = get_data(curs, fcsq)

for i in fcs:
    if i[1] == 0:
        surv = 'non-survivors'
        print('')
    else:
        surv = 'survivors'
    print(f'For class {i[0]} the average price for {surv} was ${round(i[2],2)}')

fcsq = 'select pclass, survived, avg(fare) from titanic_all2 group by pclass, survived order by pclass, survived;'
fcs = get_data(curs, fcsq)
print('')
print('-------------------')

scsq = 'select pclass, survived, avg(siblings_spouse) from titanic_all2 group by pclass, survived order by pclass, survived;'
scs = get_data(curs,scsq)
for i in scs:
    if i[1] == 0:
        surv = 'non-survivors'
        print('')
    else:
        surv = 'survivors'
    print(f'For class {i[0]} the average number of  siblings or spose for {surv} was {round(i[2],2)}')
print('')
print('-------------------')

ccsq = 'select pclass, survived, avg(parent_child) from titanic_all2 group by pclass, survived order by pclass, survived;'
ccs = get_data(curs,ccsq)
for i in ccs:
    if i[1] == 0:
        surv = 'non-survivors'
        print('')
    else:
        surv = 'survivors'
    print(f'For class {i[0]} the average number of  parents or childern for {surv} was {round(i[2],2)}')
