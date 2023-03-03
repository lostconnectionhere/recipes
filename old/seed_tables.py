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

# STEP 1. Cleanup tables
# STEP 1.1 Cleanup tables with auto-increment
tablesWithAI = ["ingredients", "recipes"]

for table in tablesWithAI: 
    sql = "DELETE FROM " + table
    cursor.execute(sql)
    conn.commit()

# STEP 1.2 Cleanup tables without auto-increment
tablesWithoutAI = ["recipe_ingredients"]

for table in tablesWithoutAI:
        sql = "ALTER TABLE " + table + " AUTO_INCREMENT = 1;"
        cursor.execute(sql)
        conn.commit() 

# map(lambda t: cleanTable(t, False), ["ingredients", "recipes"])
# map(lambda t: cleanTable(t, True), ["recipe_ingredients"])

print("Cleaned up all tables")

# STEP 2. Insert values in tables
# STEP 2.1 Insert recipes (seed)
sql_recipes = "INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)"
val_recipes = [
     ('Kurdish Naan Bread', 'Naan', 180, 'Mix a little bit of flour with sugar, warm water and baking powder. Let this rest for a few minutes. Then mix the rest of the ingredients and kneed it until it is soft and smooth. Add some sunflower oil to the ball of dough and cover it. Let the dough rise at a warm place, for example underneath a blanket. After 2-3 hours split the dough in smaller pieces, e.g. 8, cover them and let them rise again for at least 10 minutes. Now you can roll out each of the small balls with a rolling pin. Put a skillet on low to medium heat and without and place the dough. hen it puffs up and bubbles and burnt spots appear, flip it over and cook the other side. Repeat the same until all dough are done.', 'Nasrin Faraj'),
     ('Fried Flat Meatballs', 'Shifta', 60, 'Knead the meat with all the chopped vegetables until it is like a dough, add the flour and knead, when you are able to form a patty and it sticks and does not fall apart then you are good to go. Form little patties, usually they are longish and not thick like burgers but flat. Begin frying them in batches flipping in the oil until browned all over and crispy. Enjoy with lots of fresh greens, tomatoes and fresh bread.', 'Amatullah From Adventuressheart.com'),
     ('Red Lentil Soup', 'Niskena', 30, 'Heat some oil in a large pot and add onions, turmeric, cumin and curry powder. Sauté over medium heat until onions turn translucent. Add lentils, rice, veggie stock, salt and pepper. Bring to a boil, then cover and let simmer over medium low heat 30-35 minutes. Stir in the lemon juice (optional). Adjust texture/thickness by adding more stock or water or let more of the liquid evaporate. Blend/mix until smooth (optional).', 'Seiran From Legally Plantbased'),
     ('Okra Stew', 'Bamî', 30, 'If you are using fresh tomatoes, put them in hot or boiling water for 3-5 minues and peel off the skin. Then puree the tomatoes. Sautee in a pot some garlic and tomato paste for a few minutes. Add the okra and tomatoes to the pot. Then add salt and pepper and top it up with some boiling water. When the soup comes to a boil, lower the heat to medium-low for 20-30 minutes or untion your okra becomes tender. Now you can add some citric acid (optional). This dish is best served with fresh Kurdish Naan and rice.', 'Cooking My Roots'),
     ('Classic Kurdish Salad', 'Zalata', 10, 'This classic Kurdish salad is perfect in all its simplicity and is also the base of many other salads. And no Kurdish meal is served without a salad on the side. Slice the tomatoes, cucumbers in small cubes and the onion in thin slices. Add this to bowl with some sliced parseley, lemon juice and salt to taste. To top it off you can add a pinch of tirsh(sumac) for extra tartness.', 'Cooking My Roots')
]

cursor.executemany(sql_recipes, val_recipes)
print(cursor.rowcount, "record(s) inserted for table recipes: ")

# STEP 2.2 Insert ingredients (seed)
sql_ingredients = "INSERT INTO ingredients (ingredient_name) VALUES (%s)"
val_ingredients = [
    ["baking powder"],
    ["salt"],
    ["egg"],
    ["sunflower oil"],
    ["water"],
    ["all purpose flower"],
    ["sugar"],
    ["tomato"],
    ["onion"],
    ["lemon"],
    ["sumac"],
    ["cucumber"],
    ["okra"],
    ["garlic"],
    ["citric acid"],
    ["ground black pepper"],
    ["dry red lentils"],
    ["vegetable broth cubes"],
    ["ground turmeric"],
    ["ground cumin"],
    ["ground yellow curry powder"],
    ["parsley"],
    ["minced chicken"],
    ["selery leaves"],
]

cursor.executemany(sql_ingredients, val_ingredients)
print(cursor.rowcount, "record(s) inserted for table ingredients: ")

conn.commit()

# STEP 3. Show tables
# Step 3.1 Show table recipes
show_recipes = "SELECT * FROM recipes"
cursor.execute(show_recipes)

result_recipes = cursor.fetchall();

for recipe in result_recipes: 
    print(recipe)

# Step 3.2 Show table ingredients
show_ingredients = "SELECT * FROM ingredients"
cursor.execute(show_ingredients)


result_ingredients = cursor.fetchall();

for ingredient in result_ingredients: 
    print(ingredient)
