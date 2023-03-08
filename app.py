from flask import Flask, render_template, redirect, url_for, jsonify, request
import mysql.connector
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
ssl_cert = os.path.basename("/Users/rozsabir/Recipe_Management_Application/recipe_app/DigiCertGlobalRootCA.crt.pem") 

# Obtain connection string information from the portal
config = {
  'host': db_host,
  'user': db_user,
  'password': db_password,
  'database': db_name,
  'port': 3306,
  'ssl_ca': ssl_cert,
  'ssl_disabled': "False"
}

# Construct connection string
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

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
    cursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = cursor.fetchall()
    return render_template("list_ingredients.html", value = result_ing)

# 1.2 Add Ingredient 
@app.route('/add_ingredient')
def add_ing_screen():
    return render_template('add_ingredient.html')

@app.route('/add_ingredient/add', methods=['POST']) 
def add_ingredient():
    ingredient_name = request.form['ingredient_name']
    cursor.execute("INSERT INTO ingredients (ingredient_name) VALUES (%s)", (ingredient_name,))
    conn.commit()
    return redirect(url_for('list_ingredients'))

# 1.3 Delete Ingredient
@app.route('/delete_ingredient')
def delete_ing_screen():
    return render_template('delete_ingredient.html')

@app.route('/delete_ingredient/<int:ingredient_id>')
def delete_ingredient(ingredient_id):
    cursor.execute("DELETE FROM ingredients WHERE ingredient_id = %s" , (ingredient_id,))
    conn.commit()
    return redirect(url_for('list_ingredients'))

# 1.4 Update Ingredient
@app.route('/update_ingredient')
def update_ing_screen():
    return render_template('update_ingredient.html')

@app.route('/update_ingredient/update', methods=['POST'])
def update_ingredient():

    ingredient_id = request.form['ingredient_id']
    ingredient_name = request.form['ingredient_name']
    cursor.execute("UPDATE ingredients SET ingredient_name = %s WHERE ingredient_id = %s" , (ingredient_name, ingredient_id))
    conn.commit()
    return redirect(url_for('list_ingredients'))

# 2. Recipe Menu CRUD
@app.route('/main_menu/recipe_menu') 
def recipe_menu():
    return render_template('recipe_menu.html')

# 2.1 Show Recipe List
@app.route('/list_recipes')
def list_recipes():
    cursor.execute("SELECT recipe_id, recipe_name_EN, recipe_name_KU, total_time, directions, author FROM recipes")
    result_rec = cursor.fetchall()
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
    cursor.execute("INSERT INTO recipes (recipe_name_EN, recipe_name_KU, total_time, directions, author) VALUES (%s, %s, %s, %s, %s)", (recipe_name_EN, recipe_name_KU, total_time, directions, author))
    conn.commit()
    return redirect(url_for('list_recipes'))

# 2.3 Delete Recipe
@app.route('/delete_recipe')
def delete_rec_screen():
    return render_template('delete_recipe.html')

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    cursor.execute("DELETE FROM recipes WHERE recipe_id = %s" , (recipe_id,))
    conn.commit()
    return redirect(url_for('list_recipes'))

# 2.4 Update Recipe
@app.route('/update_recipe')
def update_rec_screen():
    return render_template('update_recipe.html')

@app.route('/update_recipe/update', methods=['POST'])
def update_recipe():
    recipe_id = request.form['recipe_id']
    recipe_name_EN = request.form['recipe_name']
    cursor.execute("UPDATE recipes SET recipe_name_EN = %s WHERE recipe_id = %s" , (recipe_name_EN, recipe_id))
    conn.commit()
    return redirect(url_for('list_recipes'))

@app.route('/main_menu/list_complete_recipe')
def list_complete_recipes():
    cursor.execute("""SELECT 
                    recipes.recipe_name_EN, 
                    recipes.recipe_name_KU,
                    recipes.total_time, 
                    ingredients.ingredient_name,
                    recipe_ingredients.amount, 
                    recipe_ingredients.measurement_unit,
                    recipes.directions,
                    recipes.author
                    FROM recipe_ingredients 
                    INNER JOIN recipes ON recipe_ingredients.recipe_id = recipes.recipe_id 
                    INNER JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.ingredient_id""")
    result = cursor.fetchall()
    return render_template("list_complete_recipe.html", value = result)

@app.route('/list_complete_recipe/<int:recipe_id>')
def list_per_recipe(recipe_id):
    cursor.execute("""SELECT 
                        recipes.recipe_name_EN, 
                        recipes.recipe_name_KU,
                        recipes.total_time, 
                        ingredients.ingredient_name,
                        recipe_ingredients.amount, 
                        recipe_ingredients.measurement_unit,
                        recipes.directions,
                        recipes.author
                    FROM recipe_ingredients 
                    INNER JOIN recipes ON recipe_ingredients.recipe_id = recipes.recipe_id 
                    INNER JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.ingredient_id
                    WHERE recipe_ingredients.recipe_id = %s """ , (recipe_id,))
    result = cursor.fetchall()
    return render_template("list_complete_recipe.html", value = result)

@app.route('/home')
def home_screen():
    # return("hi")
    cursor.execute("SELECT recipe_id, recipe_name_EN FROM recipes")
    result_rec = cursor.fetchall()
    
    title_list = []
    for recipe in result_rec:
        id = recipe[0] 
        naam = recipe[1]
        tuple = (id, naam)
        title_list.append(tuple)

    return render_template("home.html", title_list=title_list)

@app.route('/show_recipe_screen')
def show_screen():
    return render_template("show_recipe_screen.html")

@app.route('/show_recipe_screen/<int:recipe_id>')
def per_recipe(recipe_id):
    cursor.execute("""SELECT 
                    recipes.recipe_id,
                    recipes.recipe_name_EN, 
                    ingredients.ingredient_name,
                    recipe_ingredients.amount, 
                    recipe_ingredients.measurement_unit,
                    recipes.directions,
                    recipes.author,
                    recipes.total_time
                    FROM recipe_ingredients 
                    INNER JOIN recipes ON recipe_ingredients.recipe_id = recipes.recipe_id 
                    INNER JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.ingredient_id
                    WHERE recipe_ingredients.recipe_id = %s """ , (recipe_id,))
    result = cursor.fetchall()
    
    recipe_name: str = result[0][1]
    directions: str = result[0][5]
    author: str = result[0][6]
    total_time: int = result[0][7] / 60

    html_text = ""
    for item in result:
        ingredient_name = item[2]
        ingredient_amount = item[3]
        measurement_unit = item[4]
        html_text += "<li> %s %s %s </li>" % (ingredient_amount, measurement_unit, ingredient_name)
    
    return render_template("show_recipe_screen.html", recipe_name=recipe_name, directions=directions, author=author, total_time=total_time, ingredients=html_text)

app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
