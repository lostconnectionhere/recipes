from flask import Flask, render_template
import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def main_menu():
    return render_template('main_menu.html')

# /main_menu/recipe_menu <-- geen .html
@app.route('/main_menu/recipe_menu') 
def recipe_menu():
    return render_template('recipe_menu.html')

@app.route('/main_menu/ingredient_menu')
def ingredient_menu():
    return render_template('ingredient_menu.html')

@app.route('/add_ingredient')
def add_data():
    return render_template('add_ingredient.html')

@app.route('/list_ingredients')
def list_ingredients():
    # Probeer de list_ingredients functie te gebruiken die je al had. 
    # laat die result_ing die je nu hier hebt staan return'en. e.g.:
    # result = list_ingredients()
    # render_template(..., value = result); 
    print("Here you can see all the ingredients: ")
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()
    # for ingredient in result_ing:
    #     print(ingredient)
    return render_template("list_ingredients.html", value = result_ing)

@app.route('/delete_ingredient')
def delete_ingredient():
    del_ingredient = input("What ingredient do you want to delete? ")
    sql_del_ing = "DELETE FROM ingredients WHERE ingredient_id = " + del_ingredient
    mycursor.execute(sql_del_ing)
    mydb.commit()
        
    delete_ingredient()


# @app.route('/recipe/<recipe_name>') #test
# def get_recipe(recipe):
#     return "The recipe is " +str(recipe)

app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
