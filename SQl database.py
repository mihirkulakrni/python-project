import psycopg2

try:
    connection = psycopg2.connect(database = "staff",user = "mihirk",password = "python",host = "127.0.0.1", port = "5432")
except psycopg2.Error as err:
    print("An error was genrated!")

else:
    print("Connection to database was succesful!")    
