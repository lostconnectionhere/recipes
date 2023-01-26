import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

#create table recipes
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INT AUTO_INCREMENT PRIMARY KEY, 
        recipe_name_EN VARCHAR(255), 
        recipe_name_KU VARCHAR(255), 
        total_time VARCHAR(255), 
        directions VARCHAR(255), 
        author VARCHAR(255)
    )""")

#create table ingredients
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INT PRIMARY KEY, 
        ingredient_name VARCHAR(255)
    )""")

#create table recipe_ingredients
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS recipe_ingredients (
        recipe_id INT, 
        ingredient_id INT,
        measurement_unit ENUM('g', 'kg', 'tsp'. 'tbsp' ),
        amount INT
        FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id), 
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)

    )""")

# mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT * FROM measurement_qty")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

