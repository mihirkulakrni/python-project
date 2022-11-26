import psycopg2

f = open("E:\\employees.txt")

records = []


for i in f.readlines():
    records.append(i.split("/ "))
    print(records)

try:
    connection = psycopg2.connect(database="staff", user = "mihirk", password = "python", host = "127.0.0.1", port = "5432")
    
except psycopg2.Error as err:
    print("An error was generated while connecting to the database!")
    
else:
    print("Connection to database was successful!\n")