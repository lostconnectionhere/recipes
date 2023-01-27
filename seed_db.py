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
tablesWithAI = ["ingredients", "recipes"]

for table in tablesWithAI: 
    sql = "DELETE FROM " + table
    mycursor.execute(sql)
    mydb.commit()

# STEP 1.2 Cleanup tables without auto-increment
tablesWithoutAI = ["recipe_ingredients"]

for table in tablesWithoutAI:
        sql = "ALTER TABLE " + table + " AUTO_INCREMENT = 1;"
        mycursor.execute(sql)
        mydb.commit() 

# map(lambda t: cleanTable(t, False), ["ingredients", "recipes"])
# map(lambda t: cleanTable(t, True), ["recipe_ingredients"])

print("CLEANED TABLE ingredients")

# STEP 2. Insert values in tables
# STEP 2.1 Insert recipes (seed)
sql_recipes = "INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)"
val_recipes = ('Kurdish Naan Bread', 'Naan', 180, 'Step 1: Mix a little bit of flour with the tsp of sugar, warm water and baking powder. Let this rest for a few minutes. ..', 'Nasrin Faraj')
mycursor.execute(sql_recipes, val_recipes)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted for table recipes: ")

# STEP 2.2 Insert ingredients (seed)
sql_ingredients = "INSERT INTO ingredients (ingredient_name) VALUES (%s)"
val_ingredients = [
    ["baking powder"],
    ["salt"],
    ["egg"],
    ["sunflower oil"],
    ["water"],
    ["all purpose flower"]
]

mycursor.executemany(sql_ingredients, val_ingredients)

mydb.commit()

print(mycursor.rowcount, "record(s) inserted for table ingredients: ")

# STEP 3. Show tables
# Step 3. Show table recipes
show_recipes = "SELECT * FROM recipes"
mycursor.execute(show_recipes)

result_recipes = mycursor.fetchall();

for recipe in result_recipes: 
    print(recipe)

# Step 3. Show table ingredients
show_ingredients = "SELECT * FROM ingredients"
mycursor.execute(show_ingredients)


result_ingredients = mycursor.fetchall();

for ingredient in result_ingredients: 
    print(ingredient)
