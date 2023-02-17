import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

# STEP 1. Cleanup tables
# STEP 1.1 Cleanup tables with auto-increment
# tablesWithAI = ["ingredients", "recipes"]

# for table in tablesWithAI: 
#     sql = "DELETE FROM " + table
#     mycursor.execute(sql)
#     mydb.commit()

# # STEP 1.2 Cleanup tables without auto-increment
# tablesWithoutAI = ["recipe_ingredients"]

# for table in tablesWithoutAI:
#         sql = "ALTER TABLE " + table + " AUTO_INCREMENT = 1;"
#         mycursor.execute(sql)
#         mydb.commit() 

# print("Cleaned up all tables")

# STEP 2. Insert values in tables
# STEP 2.1 Insert recipes (seed)
sql_recipes = "INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)"
val_recipes = [["Kurdish Naan Bread", "Naan", 180, "Step 1: Mix a little bit of flour with the tsp of sugar, warm water and baking powder. Let this rest for a few minutes. ..", "Nasrin Faraj"], 
               ["Minced Meat with Herbs", "Shifta", 60, "Step 1: Get minced meat of your choice (e.g. chicken or lamb), slice fresh parsley, garlic and onion. Step 2: Mix the minced meat with ..", "Roz Sabir"],
               ["Mixed Vegetables in Oven", "Tapsi", 60, "Step 1: Cut your zucchini, eggplant, onions, potatoes and tomatoes in round slices. Step 2: Fry the vegetabels in sunflower oil ..", "Nasrin Faraj"],
               ["Lentil Soup", "Nesqena", 30, "Step 1: Rinse the red lentils under cold running water. Cut the onion and garlic in very small pieces ..", "Nasrin Faraj"],
               ["Easy Fresh Salad", "Zalata", 10, "Step 1: Slice the cucumber and tomato in equal size cubes, the smaller the better. Step 2: Cut the onion is slices", "Roz Sabir"]
               ]
mycursor.executemany(sql_recipes, val_recipes)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted for table recipes")

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
    ["zucchini"],
    ["eggplant"],
    ["tomato"],
    ["garlic"],
    ["onion"],
    ["sumac"],
    ["potatoes"],
    ["cumin powder"]
]

mycursor.executemany(sql_ingredients, val_ingredients)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted for table ingredients: ")

# STEP 2.3 Insert recipe_ingredients (seed)
# sql_recipe_ingredient = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_unit, amount) VALUES (%s, %s, %s, %s)"
# val_recipe_ingredient = [
#      (11, 66, "g", 16),
#      (11, 71,"kg", 1),
#      (11, 67, "tsp", 1),
#      (11, 72, "tsp", 1),
#      (11, 68, "piece(s)", 1),
#      (11, 69, "tbsp", 3),
#      (11, 70, "ml", 250)

# ]

# mycursor.executemany(sql_recipe_ingredient, val_recipe_ingredient)

# mydb.commit()

# print(mycursor.rowcount, "record(s) inserted for table recipe_ingredients: ")

# STEP 3. Show tables
# Step 3.1 Show table recipes
show_recipes = "SELECT * FROM recipes"
mycursor.execute(show_recipes)

result_recipes = mycursor.fetchall()

for recipe in result_recipes: 
    print(recipe)

# Step 3.2 Show table ingredients
show_ingredients = "SELECT * FROM ingredients"
mycursor.execute(show_ingredients)


result_ingredients = mycursor.fetchall()

for ingredient in result_ingredients: 
    print(ingredient)

# Step 3.3 Show table ingredients
# show_recipe_ingredients = "SELECT * FROM recipe_ingredients"
# mycursor.execute(show_recipe_ingredients)

# result_recipe_ingredients = mycursor.fetchall();

# for recipe_ingredient in result_recipe_ingredients: 
#     print(recipe_ingredient)