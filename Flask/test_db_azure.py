import mysql.connector
from _mysql_connector import errorcode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
# Obtain connection string information from the portal

config = {
  'host':'<mydemoserver>.mysql.database.azure.com',
  'user': db_username,
  'password': db_password,
  'database': db_name
}

# Construct connection string

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()



mydb = mysql.connector.connect(
    host = "localhost",

    database = " "
)

mycursor = mydb.cursor()

# Create table recipes
mycursor.execute("CREATE TABLE recipes (recipe_id INT, recipe_name VARCHAR(255))")

# Insert values 
mycursor.execute("INSERT INTO recipes (recipe_id, recipe_name_EN) VALUES (1, 'Naan')")

mydb.commit()

# Show values of table recipes
mycursor.execute("SELECT * FROM recipes")

# sql = "SELECT * FROM recipes"
# mycursor.execute(sql)

result_recipes = mycursor.fetchall()
