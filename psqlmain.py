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
