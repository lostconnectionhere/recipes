import mysql.connector
from tabulate import tabulate


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
    [3]: add an ingredient
    Type in the number """)

# print(type(task1_user_input))

if int(task1_user_input) == 1:

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

    for name in result_join:
        print("recipe: " + str(result_join[0]))
        # print("total time: " + str(row[1]))
        # print("amount: " + str(row[2]))
        # print("measurement unit: " + str(row[3]))
        # print("ingredient: " + str(row[4]))
    # print(tabulate(result_join, headers=["English name","total time", "amount", "measurement_unit", "ingredient"], tablefmt="fancy_grid"))

    # mycursor.execute("SELECT * FROM recipes")
    # result_recipes = mycursor.fetchall()

    # print("Table recipes consists of: ")
    # for recipe in result_recipes: 
    #     print(recipe)
elif int(task1_user_input) == 2:
    mycursor.execute("SELECT * FROM ingredients")
    result_ingredients = mycursor.fetchall()

    print("Table ingredients consists of: ")
    for ingredient in result_ingredients:
        print(ingredient)
elif int(task1_user_input) == 3:
    user_added_ingredient = input("So which ingredient do you want to add? ")
    # print(user_added_ingredient)
    # print("INSERT INTO ingredients (ingredient_name) VALUES (" + user_added_ingredient + ")")
    sql = "INSERT INTO ingredients (ingredient_name) VALUES (%s)"
    value =[user_added_ingredient]
    mycursor.execute(sql, value)
    mydb.commit()

    print(user_added_ingredient + " is inserted for table ingredients")
else:
    print("I can only do task 1, 2 and 3")

