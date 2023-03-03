import mysql.connector
# from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')

mydb = mysql.connector.connect(
  host = db_host,
  user = db_user,
  password = db_password,
  database= db_name,
  port= 3306,
  ssl_ca="/Users/rozsabir/Recipe_Management_Application/recipe_app/DigiCertGlobalRootCA.crt.pem",
  ssl_disabled= "False"
)

mycursor = mydb.cursor()

# print(db_username, db_password, db_host, db_name)
# Obtain connection string information from the portal
# config = {
#   'host': db_host,
#   'user': db_user,
#   'password': db_password,
#   'database': db_name,
#   'port': 3306,
#   'ssl_ca':"/Users/rozsabir/Recipe_Management_Application/recipe_app/DigiCertGlobalRootCA.crt.pem",
#   'ssl_disabled': "False"
# }

# Construct connection string
# conn = mysql.connector.connect(**config)
# cursor = conn.cursor()
 
# try:
#    conn = mysql.connector.connect(**config)
#    print("Connection established")
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with the user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cursor = conn.cursor()

# Drop previous table of same name if one exists
mycursor.execute("DROP TABLE IF EXISTS recipes;")
print("Finished dropping table (if existed).")

# Create table
mycursor.execute("CREATE TABLE recipes (id serial PRIMARY KEY, recipe_name VARCHAR(255);")
print("Finished creating table.")

# Insert some data into table
mycursor.execute("INSERT INTO recipes (name) VALUES (%s);", ("Naan"))
print("Inserted",mycursor.rowcount,"row(s) of data.")
mycursor.execute("INSERT INTO recipes (name) VALUES (%s);", ("Fresh Salad"))
print("Inserted",mycursor.rowcount,"row(s) of data.")
mycursor.execute("INSERT INTO recipes (name) VALUES (%s);", ("Shifta"))
print("Inserted",mycursor.rowcount,"row(s) of data.")

# Cleanup
mydb.commit()
mycursor.close()
mydb.close()
print("Done.")