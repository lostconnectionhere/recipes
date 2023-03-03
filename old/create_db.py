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
cursor.execute("DROP TABLE IF EXISTS recipes, ingredients, recipe_ingredients;")
print("Finished dropping the tables recipes, ingredients and recipe_ingredients.")

# Create table recipes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INT AUTO_INCREMENT PRIMARY KEY, 
        recipe_name_EN VARCHAR(255) NOT NULL, 
        recipe_name_KU VARCHAR(255), 
        total_time INT, 
        directions LONGTEXT NOT NULL, 
        author VARCHAR(255)
    )""")

#create table ingredients
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INT AUTO_INCREMENT PRIMARY KEY, 
        ingredient_name VARCHAR(255) NOT NULL
    )""")

#create table recipe_ingredients
cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipe_ingredients (
        recipe_id INT, 
        ingredient_id INT,
        measurement_unit ENUM('g', 'kg', 'tsp', 'tbsp', 'ml', 'l', 'cup', 'piece(s)') NOT NULL,
        amount INT NOT NULL)""")

        # FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id), 
        # FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)