from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_menu():
    return render_template('main_menu.html')

# /main_menu/recipe_menu <-- geen .html
@app.route('/main_menu/recipe_menu') # denk ja 
def recipe_menu():
    return render_template('recipe_menu.html')

@app.route('/main_menu/ingredient_menu')
def ingredient_menu():
    return render_template('ingredient_menu.html')

@app.route('/recipe/<recipe_name>') #test
def get_recipe(recipe):
    return "The recipe is " +str(recipe)

app.run(host='0.0.0.0',port=8001)


# https://pythonbasics.org/flask-tutorial-routes/
# http://localhost:8001/main_menu/recipe_menu <-- geen .html...     
    