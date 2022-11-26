Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import psycopg2


try:
    connrction = psycopg2.connect(database = "staff",user = "mihirk",password = "python",host = "127.0.0.1",port = "5432")
expect pyscopg2.Error as err:
    
SyntaxError: expected 'except' or 'finally' block
except pyscopg2.Error as err:
    
SyntaxError: invalid syntax





































import psycopg2

try:
    connection = psycopg2.connect(database="staff", user = "mihirk", password = "python", host = "127.0.0.1", port = "5432")
except sycopg2.Error as err:
    print("An error was generated!")
else:
    print("Connection to database was successful!")

    
Connection to database was successful!
