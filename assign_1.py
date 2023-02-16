# What would you like to do:
# [1]: list recipes
# [2]: list ingredients
# [3]: add ingredient
# ```

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

task1_user_input = input("""
    What would you like to do:
    [1]: list all recipes
    [2]: list all ingredients
    [3]: add ingredient""")

if task1_user_input == 1:
    mycursor.execute("SELECT * FROM recipes")

    result_recipes = mycursor.fetchall()

    print("Table recipes consists of: ")
    for recipe in result_recipes: 
        print(recipe)
else:
    print("I can only perform [1]")