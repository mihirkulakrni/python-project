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
cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
 values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
        (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
        (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
        (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
        (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")
connection.commit()
connection.close()
