import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()


def show_main_menu(): 
    # show main menu
    print("\n\n*********************")
    print("[Main Menu]")
    print("[0] Exit")
    print("[1] Recipe Menu")
    print("[2] Ingredient Menu")
    print("*********************")

    userChoice = int(input("Make a choice: "))

    if userChoice == 0:
        print("Goodbye")
    elif userChoice == 1:
        show_recipe_menu()
    elif userChoice == 2:
        show_ingredient_menu()
    else:
        print("Unrecognized option: " + userChoice + " please make another choice")
        show_main_menu()


def list_recipes(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT recipe_id, recipe_name_EN FROM recipes")
    result_rec = mycursor.fetchall()

    for recipe in result_rec: 
        print("[%d] %s" % recipe)
    
    print (">>> DONE")

def getRecipe(recipeId):
    print("Fetching recipe " + str(recipeId))

def show_ingredient_menu():
    print("\n\*********************")
    print("[INGREDIENT MENU]")
    print("[0] Back to Main Menu")
    print("[1] List ingredients")
    print("[2] Get ingredients")
    print("*********************")

    userChoice = int(input("Make a choice: "))

    if userChoice == 0:
        show_main_menu()
    elif userChoice == 1:
        list_ingredients()
        show_ingredient_menu()
    elif userChoice == 2:
        ingredient_id = int(input("Recipe ID: "))
        getRecipe(ingredient_id)
    else:
        print("Unrecognized option: " + userChoice + " please make another choice")
        show_ingredient_menu()

    show_main_menu()

def list_ingredients(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()


    
    print (">>> DONE")

show_main_menu()