import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
ssl_cert = os.path.basename("/Users/rozsabir/Recipe_Management_Application/recipe_app/Flask/DigiCertGlobalRootCA.crt.pem")

# Obtain connection string information from the portal
config = {
  'host': db_host,
  'user': db_user,
  'password': db_password,
  'database': db_name,
  'port': 3306,
  'ssl_ca': ssl_cert,
  'ssl_disabled': "False"
}

# Construct connection string
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS recipes;")
print("Finished dropping table (if existed).")

# Create table
cursor.execute("CREATE TABLE recipes (id serial PRIMARY KEY, recipe_name VARCHAR(255))")
print("Finished creating table.")

# Insert some data into table
cursor.execute("INSERT INTO recipes (recipe_name) VALUES ('Naan')")
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO recipes (recipe_name) VALUES ('Fresh Salad')")
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO recipes (recipe_name) VALUES ('Shifta')")
print("Inserted",cursor.rowcount,"row(s) of data.")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")