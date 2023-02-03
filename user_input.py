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
sql_ing_id = "SELECT ingredient_id FROM ingredients WHERE ingredient_name = 'sugar'"
mycursor.execute(sql_ing_id)

result_ing_id = mycursor.fetchall();

print("Table recipes consists of: ")
for ing_id in result_ing_id: 
    print(ing_id)

recipe = input('Enter the ingredient to retrieve the correct ingredient_id: ')