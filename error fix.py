Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import psycopg2
try:
    connection = psycopg2.connect(database = "staff",user = "mihirk",password = "python",host = "127.0.0.1", port = "5432")
except psycopg2.Error as err:
    print("An error was genrated!")
else:
    print("Connection to database was succesful!")

    
Connection to database was succesful!

cursor = connection.cursor()
connection.rollback()
cursor.execute('''create table mystaff.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cursor.execute('''create table mystaff.employees
psycopg2.errors.DuplicateTable: relation "employees" already exists

cursor = connection.cursor()
connection.rollback()
cursor.execute('''create table mystaff.employees1
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')
SyntaxError: multiple statements found while compiling a single statement
cursor = connection.cursor()

connection.rollback()
cursor.execute('''create table mystaff.employees1
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')

connection.commit()
connection.close()


cursor = connection.cursor()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    cursor = connection.cursor()
psycopg2.InterfaceError: connection already closed
cursor = connection.sursor()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cursor = connection.sursor()
AttributeError: 'psycopg2.extensions.connection' object has no attribute 'sursor'. Did you mean: 'cursor'?
cursor = connection.cursor()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    cursor = connection.cursor()
psycopg2.InterfaceError: connection already closed
