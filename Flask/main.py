from flask import Flask, render_template, redirect, url_for, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

# creates application object
app = Flask(__name__)

@app.route('/')
def main_menu():
    return render_template('main_menu.html')

# 1. Ingredient Menu CRUD
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

# 2. Recipe Menu CRUD
@app.route('/main_menu/recipe_menu') 
def recipe_menu():
    return render_template('recipe_menu.html')

# 2.1 Show Recipe List
@app.route('/list_recipes')
def list_recipes():
    mycursor.execute("SELECT recipe_id, recipe_name_EN, recipe_name_KU, total_time, directions, author FROM recipes")
    result_rec = mycursor.fetchall()
    return render_template("list_recipes.html", value = result_rec)

# 2.2 Add Recipe 
@app.route('/add_recipe')
def add_rec_screen():
    return render_template('add_recipe.html')

@app.route('/add_recipe/add', methods=['POST']) 
def add_recipes():
    recipe_name_EN = request.form['recipe_name_EN']
    recipe_name_KU = request.form['recipe_name_KU']
    total_time = request.form['total_time']
    directions = request.form['directions']    
    author = request.form['author']
    mycursor.execute("INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)", (recipe_name_EN, recipe_name_KU, total_time, directions, author))
    mydb.commit()
    return redirect(url_for('list_recipes'))

# 2.3 Delete Recipe
@app.route('/delete_recipe')
def delete_rec_screen():
    return render_template('delete_recipe.html')

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    mycursor.execute("DELETE FROM recipes WHERE recipe_id = %s" , (recipe_id,))
    mydb.commit()
    return redirect(url_for('list_recipes'))

# 2.4 Update Recipe
@app.route('/update_recipe')
def update_rec_screen():
    return render_template('update_recipe.html')

@app.route('/update_recipe/update', methods=['POST'])
def update_recipe():

    recipe_id = request.form['recipe_id']
    recipe_name_EN = request.form['recipe_name']
    mycursor.execute("UPDATE recipes SET recipe_name_EN = %s WHERE recipe_id = %s" , (recipe_name_EN, recipe_id))
    mydb.commit()
    return redirect(url_for('list_recipes'))

@app.route('/show_complete_recipes')
def show_recipe_screen():
    return render_template('show_complete_recipes.html')


app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
