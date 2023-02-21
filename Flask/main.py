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

# /main_menu/recipe_menu <-- geen .html
@app.route('/main_menu/recipe_menu') 
def recipe_menu():
    return render_template('recipe_menu.html')

@app.route('/main_menu/ingredient_menu')
def ingredient_menu():
    return render_template('ingredient_menu.html')

@app.route('/update_ingredient')
def update_ingredient(old_ing_name, ingredient_id):
    # old_ing_id = input("Which ingredient do you want to update? ")
    # new_ing_name = input("Sure, to what ingredient do you want to update it to? ")

    mycursor.execute("UPDATE ingredients SET ingredient_name = %s WHERE ingredient_id = %s" % (old_ing_name, ingredient_id))
    mydb.commit()

    return render_template('add_ingredient.html')

@app.route('/list_ingredients')
def list_ingredients():
    # Probeer de list_ingredients functie te gebruiken die je al had. 
    # laat die result_ing die je nu hier hebt staan return'en. e.g.:
    # result = list_ingredients()
    # render_template(..., value = result);  
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()
    # for ingredient in result_ing:
    #     print(ingredient)
    return render_template("list_ingredients.html", value = result_ing)

@app.route('/delete_ingredient')
def delete_ing_screen():
    return render_template('delete_ingredient.html')

@app.route('/delete_ingredient/<int:ingredient_id>')
def delete_ingredient(ingredient_id):
    mycursor.execute("DELETE FROM ingredients WHERE ingredient_id = %s" % (ingredient_id,))
    mydb.commit()
    return redirect(url_for('list_ingredients'))


@app.route('/add_ingredient')
def add_ing_screen():
    return render_template('add_ingredient.html')

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    data = request.get_json
    insert_query = ("INSERT INTO ingredients (ingredient_name) VALUES (?)")
    value = (data['ingredient_name'])
    mycursor.execute(insert_query, value)
    # ingredient_name = request.json
    mydb.commit()
    return jsonify({'message': 'Ingredient added successfuly.'})
    # return redirect(url_for('list_ingredients'))



app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
