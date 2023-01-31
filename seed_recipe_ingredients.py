import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

# STEP 1 Insert recipe_ingredients (seed)
sql_recipe_ingredient = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_unit, amount) VALUES (%s, %s, %s, %s)"
val_recipe_ingredient = [
     (1, 1, 'g', 16), #baking powder
     (1, 6,'kg', 1), #all purpose flower
     (1, 7, 'tsp', 1), #sugar
     (1, 2, 'tsp', 1), #salt
     (1, 3, 'piece(s)', 1), #egg
     (1, 4, 'tbsp', 3), #sunflower oil
     (1, 5, 'ml', 250) #water

]

mycursor.executemany(sql_recipe_ingredient, val_recipe_ingredient)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted for table recipe_ingredients: ")

# Step 2 Show table ingredients
show_recipe_ingredients = "SELECT * FROM recipe_ingredients"
mycursor.execute(show_recipe_ingredients)

result_recipe_ingredients = mycursor.fetchall();

for recipe_ingredient in result_recipe_ingredients: 
    print(recipe_ingredient)