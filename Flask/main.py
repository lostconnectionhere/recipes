from flask import Flask, render_template, redirect, url_for, jsonify, request
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

@app.route('/main_menu/recipe_menu') 
def recipe_menu():
    return render_template('recipe_menu.html')

# Ingredient Menu CRUD
@app.route('/main_menu/ingredient_menu')
def ingredient_menu():
    return render_template('ingredient_menu.html')

# 1.1 Show Ingredients List
@app.route('/list_ingredients')
def list_ingredients():
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()
    return render_template("list_ingredients.html", value = result_ing)

# 1.2 Add Ingredient 
@app.route('/add_ingredient')
def add_ing_screen():
    return render_template('add_ingredient.html')

@app.route('/add_ingredient/add', methods=['POST']) 
def add_ingredient():
    ingredient_name = request.form['ingredient_name']
    mycursor.execute("INSERT INTO ingredients (ingredient_name) VALUES (%s)", (ingredient_name,))
    mydb.commit()
    return redirect(url_for('list_ingredients'))

# 1.3 Delete Ingredient
@app.route('/delete_ingredient')
def delete_ing_screen():
    return render_template('delete_ingredient.html')

@app.route('/delete_ingredient/<int:ingredient_id>')
def delete_ingredient(ingredient_id):
    mycursor.execute("DELETE FROM ingredients WHERE ingredient_id = %s" , (ingredient_id,))
    mydb.commit()
    return redirect(url_for('list_ingredients'))

# 1.4 Update Ingredient
@app.route('/update_ingredient')
def update_ing_screen():
    return render_template('update_ingredient.html')

@app.route('/update_ingredient/update', methods=['POST'])
def update_ingredient():

    ingredient_id = request.form['ingredient_id']
    ingredient_name = request.form['ingredient_name']
    mycursor.execute("UPDATE ingredients SET ingredient_name = %s WHERE ingredient_id = %s" , (ingredient_name, ingredient_id))
    mydb.commit()
    return redirect(url_for('list_ingredients'))


app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
