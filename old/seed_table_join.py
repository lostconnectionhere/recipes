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

def add_ingredient_to_recipe(recipe_name, ingredient_name, measurement_unit, amount):
    # Step 1: get id from recipe_name
    cursor.execute("SELECT recipe_id FROM recipes WHERE recipe_name_EN = '%s'" % (recipe_name,))
    result = cursor.fetchone()
    # print(result[0])
    recipe_id = result[0]

    # Step 2: get id from ingredient_name
    cursor.execute("SELECT ingredient_id FROM ingredients WHERE ingredient_name = '%s'" % (ingredient_name,))
    result = cursor.fetchone()
    # print(result[0])
    ingredient_id = result[0]

    query = """
        INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_unit, amount) 
        VALUES (%s, %s, %s, %s)
    """
    params = (recipe_id, ingredient_id, measurement_unit, amount)
    cursor.execute(query, params)
    conn.commit()
    print(cursor.rowcount)

# Recipe 1
add_ingredient_to_recipe("Kurdish Naan Bread", "baking powder", "g", 16)
add_ingredient_to_recipe("Kurdish Naan Bread", "all purpose flour", "kg", 1)
add_ingredient_to_recipe("Kurdish Naan Bread", "sugar", "tsp", 1)
add_ingredient_to_recipe("Kurdish Naan Bread", "salt", "tsp", 1)
add_ingredient_to_recipe("Kurdish Naan Bread", "egg", "piece(s)", 1)
add_ingredient_to_recipe("Kurdish Naan Bread", "sunflower oil", "tbsp", 1)
add_ingredient_to_recipe("Kurdish Naan Bread", "water", "ml", 250)

# Recipe 2 source:http://www.adventuressheart.com/2011/08/shfta-kurdish-meat-patties.html 
add_ingredient_to_recipe("Fried Flat Meatballs", "minced chicken", "g", 700)
add_ingredient_to_recipe("Fried Flat Meatballs", "onion", "piece(s)", 1)
add_ingredient_to_recipe("Fried Flat Meatballs", "garlic", "piece(s)", 1)
add_ingredient_to_recipe("Fried Flat Meatballs", "parsley", "piece(s)", 5)
add_ingredient_to_recipe("Fried Flat Meatballs", "all purpose flour", "tbsp", 4)
add_ingredient_to_recipe("Fried Flat Meatballs", "ground cumin", "tsp", 1)
add_ingredient_to_recipe("Fried Flat Meatballs", "salt", "tsp", 0.5)
add_ingredient_to_recipe("Fried Flat Meatballs", "ground black pepper", "tsp", 0.5)

# Recipe 3 source:https://www.instagram.com/p/CKXUG1PhSWy/
add_ingredient_to_recipe("Red Lentil Soup", "dry red lentils", "g", 200)
add_ingredient_to_recipe("Red Lentil Soup", "sunflower oil", "tbsp", 2)
add_ingredient_to_recipe("Red Lentil Soup", "tomato paste", "tbsp", 1)
add_ingredient_to_recipe("Red Lentil Soup", "onion", "piece(s)", 0.5)
add_ingredient_to_recipe("Red Lentil Soup", "ground yellow curry powder", "tsp", 2)
add_ingredient_to_recipe("Red Lentil Soup", "ground turmeric", "tsp", 1)

# Recipe 4 source:https://www.youtube.com/watch?v=aQWoaPpUYhQ 
add_ingredient_to_recipe("Okra Stew", "okra", "g", 400)
add_ingredient_to_recipe("Okra Stew", "tomato paste", "tbsp", 2)
add_ingredient_to_recipe("Okra Stew", "tomato", "piece(s)", 4)
add_ingredient_to_recipe("Okra Stew", "garlic clove", "piece(s)", 3)
add_ingredient_to_recipe("Okra Stew", "ground turmeric", "tsp", 1)
add_ingredient_to_recipe("Okra Stew", "sunflower oil", "tbsp", 2)
add_ingredient_to_recipe("Okra Stew", "citric acid", "tsp", 0.5)

# Recipe 5 source:https://www.youtube.com/watch?v=qlTcZIHa7pI 
add_ingredient_to_recipe("Classic Kurdish Salad", "tomato", "piece(s)", 4)
add_ingredient_to_recipe("Classic Kurdish Salad", "onion", "piece(s)", 1)
add_ingredient_to_recipe("Classic Kurdish Salad", "parsley", "piece(s)", 1)
add_ingredient_to_recipe("Classic Kurdish Salad", "lemon", "piece(s)", 1)
add_ingredient_to_recipe("Classic Kurdish Salad", "citric acid", "tsp", 0.5)

conn.commit()