import sqlite3 as sql3

conn = sql3.connect('northwind_small.sqlite3')
curs = conn.cursor()

def get_scalar_result(conn, sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

productprice = 'select ProductName, UnitPrice from Product order by UnitPrice desc limit 10;'
top10 = get_scalar_result(conn, productprice)

print('\nThe top 10 most expensive products are- \n')
for i in top10:
    print(f'{i[0]}: ${i[1]}')

print('\n-------------------\n')

avgage = 'select avg((julianday(HireDate)- julianday(BirthDate))/365) as avgage from Employee;'
age = get_scalar_result(conn, avgage)
print(f'The avage age per hire is {round(age[0][0])}.')
print('\n-------------------\n')


#Stretch Goal!

agebycity = 'select City, avg((julianday(HireDate)- julianday(BirthDate))/365) as avgage from Employee group by City;'
abc = get_scalar_result(conn,agebycity)
print('The average age by City - \n')
for i in abc:
    print(f'{i[0]}: {round(i[1])} years old.')

sup10 = """
    with allitems as (
    SELECT  Supplier.CompanyName, Product.ProductName, Product.UnitPrice from Product
    INNER JOIN Supplier
    on Product.SupplierId = Supplier.Id)
    SELECT * from allitems order by UnitPrice desc limit 10;
"""
sup10r = get_scalar_result(conn, sup10)
print("Top 10 products by Supplier.")
for i in sup10r:
    print(f"Supplier name: {i[0]}\nProduct name: {i[1]}\nItem price: ${i[2]}\n")

print('\n-------------------\n')

cats = """with allitems as (
SELECT  Category.CategoryName as catname, Product.ProductName, Product.Id as pid, Product.UnitPrice from Product
INNER JOIN Category
on Product.CategoryId = Category.Id)
SELECT catname, count (DISTINCT pid) as countnum from allitems group by catname order by countnum desc;"""

catr = get_scalar_result(conn, cats)
print('Here are the size of each Category:')
for i in catr:
    print(f"Category name: {i[0]}  Category size: {i[1]}")

print(f'\nThe largets Category is {catr[0][0]} with {catr[0][1]} items.')
print('\n-------------------\n')

#Stretch Goal

mostt = """with allitems as (
    SELECT  Employee.FirstName firstn, Employee.LastName as lastn,
    EmployeeTerritory.Id as tid
    from Employee
    INNER JOIN EmployeeTerritory
    on EmployeeTerritory.EmployeeId = Employee.Id)
    select firstn, lastn, count(tid) as ctid from allitems group by firstn, lastn
    order by ctid desc;"""
mosttr = get_scalar_result(conn, mostt)
print(f"The Employee with the most territories is {mosttr[0][0]} {mosttr[0][1]} with {mosttr[0][2]} territories!")
