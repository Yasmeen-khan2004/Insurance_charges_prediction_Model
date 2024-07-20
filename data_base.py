import sqlite3
# to import a database
connection = sqlite3.connect('insurance.db')

query = """create table project
(age integer , bmi integer, region varchar(5), children integer , 
smoker integer , heath integer , sex integer , prediction varchar(10))"""


cur = connection.cursor()
cur.execute(query)
print("Your database and your table is created")

cur.close()
connection.close()


