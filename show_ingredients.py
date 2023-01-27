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

sql = "SELECT * FROM ingredients"

mycursor.execute(sql)

result = mycursor.fetchall();

for x in result: 
    print(x)

