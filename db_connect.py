import mysql.connector

def connection():
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "my-secret-pw",
        database = "mydb_test"
    )

    mycursor = mydb.cursor()
    return mydb, mycursor