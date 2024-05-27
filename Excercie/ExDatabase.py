import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("D:\Anjali\SQLiteStudio\Examples\ExDatabase.db")
#conn = sqlite3.connect("D:\Anjali\SQLiteStudio\Examples\DBEX.db")
cursorcon = conn.cursor()
print("Opened the database")
print("*****************CREATE OPERATION*******************************")
# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
#print("Table created successfully");
#print("\n")
# conn.execute('''CREATE TABLE Employee
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print("Table created successfully")
# print("\n")
#print("*****************INSERT OPERATION*******************************")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Sumit', 32, 'Delhi', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Shweta', 25, 'Mumbai', 15000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Virajas', 23, 'Mumbai', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Veena', 25, 'Kerela ', 65000.00 )");
#
# conn.commit()
# conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (5, 'Arati', 32, 'Delhi', 20000.00 )")
#
# conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (6, 'Mahesh', 25, 'Mumbai', 15000.00 )")
#
# conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (7, 'Virajas', 23, 'Mumbai', 20000.00 )")
#
# conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (8, 'Veena', 25, 'Kerela ', 65000.00 )")
data = [(11,'Shrinivas',25,'Mumbai',45000),(12,'Gautham',35,'Karnataka',60000),(13,'Viajaya',33,'Delhi',50000)]
conn.executemany("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,?,?,?)",data)


print("\n")
print("*****************SELECT OPERATION*******************************")
cursor = conn.execute("SELECT id, name, address, salary from Employee")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")

print("Records created successfully")

print("*****************UPDATE  OPERATION*******************************")
conn.execute("UPDATE Employee set NAME = 'Shweta' where ID = 10")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursorquery = conn.execute("SELECT id, name, address, salary from Employee")
#ans = cursorcon.fetchall()
for row in cursorquery:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")

print("\n")
print("**************************DELETE OPERATION**************************")
conn.execute("DELETE from Employee where ID = 2;")
conn.commit()

conn.close()