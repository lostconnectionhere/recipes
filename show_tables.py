import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)"
# val = ('Kurdish Naan Bread', 'Naan', 180, 'Step 1: Mix a little bit of flour with the tsp of sugar, warm water and baking powder. Let this rest for a few minutes. ..', 'Nasrin Faraj')

# 1. Show values of tables
# 1.1 Table ingredients
sql_ingredients = "SELECT * FROM ingredients"
mycursor.execute(sql_ingredients)

result_ingredients = mycursor.fetchall();

for ingredient in result_ingredients: 
    print("Table ingredients consists of: ", ingredient)

# 1.2 Table recipes
sql_recipes = "SELECT * FROM recipes"
mycursor.execute(sql_recipes)

result_recipes = mycursor.fetchall();

for recipe in result_recipes: 
    print("Table recipes consists of: ", recipe)


# 1.3 Table recipe_ingredients
sql_recipe_ingredients = "SELECT * FROM recipe_ingredients"
mycursor.execute(sql_recipe_ingredients)

result_recipe_ingredients = mycursor.fetchall();

for recipe_ingredient in result_recipe_ingredients: 
    print("Table recipe_ingredients consists of: ", recipe_ingredient)

