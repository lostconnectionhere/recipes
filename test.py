import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

sugar = 0
baking_powder = 0
salt = 0
egg = 0
sunflower_oil =0
water =0
ap_flower = 0
sugar = 0 


mycursor = mydb.cursor()

# 1. Show values of tables
# 1.1 Table recipes
sql_recipes = "SELECT ingredient_id FROM ingredients WHERE ingredient_name = 'sugar'"
mycursor.execute(sql_recipes)

result_recipes = mycursor.fetchall();

print("Table recipes consists of: ")
for recipe in result_recipes: 
    print(recipe)
