import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

# 1. Show values of tables
# 1.1 Table recipes
sql_recipes = "SELECT * FROM recipes"
mycursor.execute(sql_recipes)

result_recipes = mycursor.fetchall();

print("Table recipes consists of: ")
for recipe in result_recipes: 
    print(recipe)

# 1.2 Table ingredients
sql_ingredients = "SELECT * FROM ingredients"
mycursor.execute(sql_ingredients)

result_ingredients = mycursor.fetchall();

print("Table ingredients consists of: ")
for ingredient in result_ingredients: 
    print(ingredient)

# 1.3 Table recipe_ingredients
sql_recipe_ingredients = "SELECT * FROM recipe_ingredients"
mycursor.execute(sql_recipe_ingredients)

result_recipe_ingredients = mycursor.fetchall();

print("Table recipe_ingredients consists of: ")
for recipe_ingredient in result_recipe_ingredients: 
    print(recipe_ingredient)

join_query = """SELECT recipes.recipe_name_EN, 
            recipes.total_time, 
            recipe_ingredients.amount, 
            recipe_ingredients.measurement_unit,
            ingredients.ingredient_name
            FROM recipes 
            INNER JOIN recipe_ingredients ON recipes.recipe_id = recipe_ingredients.recipe_id
            INNER JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.ingredient_id"""

mycursor.execute(join_query)

result_join = mycursor.fetchall()

for x in result_join:
   print(x)